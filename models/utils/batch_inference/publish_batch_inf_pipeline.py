"""
NOTE: This is a stop gap script until Batch inference supports AZ ML CLI
"""
from dotenv import load_dotenv
import os
from azureml.pipeline.core import Pipeline

import models.utils.AzureMLUtils as AzureMLUtils

#BATCH_PIPELINE_NAME = "risk-scoring-batch-pipeline"

def main():
    load_dotenv()
    ws = AzureMLUtils.get_workspace()
    print("got workspace")
    pipeline_yaml_path = os.environ.get("AML_PIPELINE_YAML_PATH")
    pipeline_name = os.environ.get("AML_PIPELINE_NAME")
    print("pipeline_yaml_path: ",pipeline_yaml_path)
    print("pipeline_name: ",pipeline_name)
    #script_yaml = "models/risk-model/batch_score/pipeline/AMLBatchPipeline.yml"
    pipeline = Pipeline.load_yaml(ws, filename=pipeline_yaml_path)
    pipeline.publish(pipeline_name)

if __name__ == "__main__":
    main()