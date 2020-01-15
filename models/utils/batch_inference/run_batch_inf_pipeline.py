import argparse
from azureml.pipeline.core import PublishedPipeline
from azureml.core import Experiment
from dotenv import load_dotenv
import models.utils.AzureMLUtils as AzureMLUtils

def main():
    load_dotenv()
    ws = AzureMLUtils.get_workspace()
    print("got workspace")
    pipeline_id = getRuntimeArgs()
    print("PIPELINE_ID: ", pipeline_id)
    published_pipeline = PublishedPipeline.get(workspace=ws, id=pipeline_id)
    print("published pipeline: ", published_pipeline)
    pipeline_run = Experiment(ws, 'batch-run-code').submit(published_pipeline)
    pipeline_run.wait_for_completion(show_output=True)

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--PIPELINE_ID', type=str)
    args = parser.parse_args()
    return args.PIPELINE_ID

if __name__ == "__main__":
    main()