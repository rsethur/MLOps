"""
NOTE: This code is a stop gap script until Batch inference supports AZ ML CLI
"""
import os
import argparse
from dotenv import load_dotenv
from azureml.pipeline.core import Pipeline

import models.utils.AzureMLUtils as AzureMLUtils

def main():
    load_dotenv()
    ws = AzureMLUtils.get_workspace()
    print("Workspace lookup successful")
    # read command line parameters
    pipeline_yaml_path, pipeline_name = getRuntimeArgs()
    # Load the pipeline from YAML file
    pipeline = Pipeline.load_yaml(ws, filename=pipeline_yaml_path)
    # Publish the pipeline
    published_pipeline = pipeline.publish(pipeline_name)
    print("Published pipeline id: ", published_pipeline.id)

    # This line is needed to for Azure Devops to set PIPELINE_ID as environment variable.
    # This is needed in the next step (if there is need to run the pipeline)
    print("##vso[task.setvariable variable=PIPELINE_ID]",published_pipeline.id)

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--AML_PIPELINE_YML_PATH', type=str)
    parser.add_argument('--AML_PIPELINE_NAME', type=str)
    args = parser.parse_args()
    return args.AML_PIPELINE_YML_PATH, args.AML_PIPELINE_NAME

if __name__ == "__main__":
    main()