import sys
import os
import time,datetime
from dotenv import load_dotenv
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core.datastore import Datastore
from azureml.core.dataset import Dataset


def get_workspace():
    load_dotenv()
    name = os.environ.get("BASE_NAME")+"-AML-WS"
    resource_group = os.environ.get("BASE_NAME")+"-AML-RG"
    subscription_id = os.environ.get("SUBSCRIPTION_ID")
    tenant_id = os.environ.get("TENANT_ID")
    app_id = os.environ.get("SP_APP_ID")
    app_secret = os.environ.get("SP_APP_SECRET")

    service_principal = ServicePrincipalAuthentication(
        tenant_id=tenant_id,
        service_principal_id=app_id,
        service_principal_password=app_secret)

    try:
        aml_workspace = Workspace.get(
            name=name,
            subscription_id=subscription_id,
            resource_group=resource_group,
            auth=service_principal)

        return aml_workspace
    except Exception as caught_exception:
        print("Error while retrieving Workspace...")
        print(str(caught_exception))
        sys.exit(1)

def upload_and_register_dataset():
    ws = get_workspace()
    datastore = ws.get_default_datastore()
    dataset_name = os.environ.get("MODEL_NAME") + "-DATASET"
    dataset_file_name = os.environ.get("DATASET_FILE")
    print("***CWD***: " + os.getcwd())
    dataset_path_in_src = "./dataset/"+ dataset_file_name

    curr_timestamp = str(int(time.time()))
    dataset_dir_in_datastore = dataset_name + "/" + curr_timestamp

    datastore.upload_files(files=[dataset_path_in_src], target_path=dataset_dir_in_datastore, overwrite=False, show_progress=True)

    dataset_path_in_datastore = [(datastore, dataset_dir_in_datastore+"/"+dataset_file_name)]
    print("dataset_path_in_datastore: "+str(dataset_path_in_datastore))
    dataset = Dataset.Tabular.from_delimited_files(path=dataset_path_in_datastore)
    dataset.register(workspace=ws, name=dataset_name, create_new_version=True)
    print("done")

#upload_and_register_dataset()
