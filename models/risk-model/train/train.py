import os
import sys
import argparse

import dotenv
import joblib
import pandas as pd
from azureml.core import Run
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import StandardScaler

from azureml.core import Dataset

def main():

    model_name, dataset_name = getRuntimeArgs()
    dotenv.load_dotenv()

    run = Run.get_context()

    if run._run_id.startswith("_OfflineRun"):
        run = None

    credit_data_df = None

    #Load data from Dataset or from local file(for offline runs)
    if run is None:
        dataset_filename = os.environ.get("DATASET_FILE_NAME", )
        credit_data_df = pd.read_csv("dataset/" +dataset_filename)
    else:
        dataset = Dataset.get_by_name(workspace=run.experiment.workspace, name=dataset_name)
        #dataset = run.input_datasets[dataset_name]
        credit_data_df = dataset.to_pandas_dataframe()

    clf = model_train(credit_data_df, run)

    #copying to "outputs" directory, automatically uploads it to azure ml
    output_dir = './outputs/'
    os.makedirs(output_dir, exist_ok=True)
    joblib.dump(value=clf, filename=output_dir+model_name)

    #run.upload_file(name="./outputs/" + model_file_name, path_or_stream=model_file_name)

def model_train(credit_data_df, run):
    #credit_data_df = pd.read_csv("dataset/german_credit_data.csv")  # , nrows=200000, parse_dates=["LEG1_DEP_DATE_GMT", "LEG1_ARR_DATE_GMT","LEG2_DEP_DATE_GMT", "LEG2_ARR_DATE_GMT"])
    credit_data_df.drop("Sno", axis=1, inplace=True)

    y_raw = credit_data_df['Risk']
    X_raw = credit_data_df.drop('Risk', axis=1)
    #del credit_data_df

    categorical_features = X_raw.select_dtypes(include=['object']).columns
    numeric_features = X_raw.select_dtypes(include=['int64', 'float']).columns

    categorical_transformer = Pipeline(steps=[
        ('imputer', SimpleImputer(strategy='constant', fill_value="missing")),
        ('onehotencoder', OneHotEncoder(categories='auto', sparse=False))])

    numeric_transformer = Pipeline(steps=[
        # ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())])

    feature_engineering_pipeline = ColumnTransformer(
        transformers=[
            ('numeric', numeric_transformer, numeric_features),
            ('categorical', categorical_transformer, categorical_features)
        ], remainder="drop")

    #Encode Labels
    le = LabelEncoder()
    encoded_y = le.fit_transform(y_raw)

    #Train test split
    X_train, X_test, y_train, y_test = train_test_split(X_raw, encoded_y, test_size=0.20, stratify=encoded_y, random_state=42)

    #Create sklearn pipeline
    lr_clf = Pipeline(steps=[('preprocessor', feature_engineering_pipeline),
                             ('classifier', LogisticRegression(solver="lbfgs"))])
    #Train the model
    lr_clf.fit(X_train, y_train)

    #Capture metrics
    train_acc = lr_clf.score(X_train, y_train)
    test_acc = lr_clf.score(X_test, y_test)
    print("training accuracy: %.3f" % train_acc)
    print("test data accuracy: %.3f" % test_acc)

    #Log to Azure ML (if not running in local test mode)
    if run is not None:
        run.log('Train accuracy', train_acc)
        run.log('Test accuracy', test_acc)

    return lr_clf

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--MODEL_NAME', type=str)
    parser.add_argument('--DATASET_NAME', type=str)
    args = parser.parse_args()
    return args.MODEL_NAME, args.DATASET_NAME

if __name__ == "__main__":
    main()