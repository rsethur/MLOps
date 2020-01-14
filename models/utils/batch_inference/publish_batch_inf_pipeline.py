"""
NOTE: This is a stop gap script until Batch inference supports AZ ML CLI
"""
import os
import argparse
from dotenv import load_dotenv
from azureml.pipeline.core import Pipeline

import models.utils.AzureMLUtils as AzureMLUtils

#BATCH_PIPELINE_NAME = "risk-scoring-batch-pipeline"

def main():
    load_dotenv()
    ws = AzureMLUtils.get_workspace()
    print("got workspace")
    pipeline_yaml_path = os.environ.get("AML_PIPELINE_YML_PATH")
    pipeline_name = os.environ.get("AML_PIPELINE_NAME")
    print("pipeline_yaml_path: ",pipeline_yaml_path)
    print("pipeline_name: ",pipeline_name)
    #script_yaml = "models/risk-model/batch_score/pipeline/AMLBatchPipeline.yml"
    pipeline = Pipeline.load_yaml(ws, filename=pipeline_yaml_path)
    pipeline.publish(pipeline_name)

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--AML_PIPELINE_YML_PATH', type=str)
    parser.add_argument('--AML_PIPELINE_NAME', type=str)
    args = parser.parse_args()
    return args.MODEL_NAME, args.DATASET_NAME

if __name__ == "__main__":
    main()