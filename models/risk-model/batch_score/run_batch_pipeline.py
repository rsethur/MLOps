import dotenv
from azureml.pipeline.core import PublishedPipeline
from azureml.core import Experiment

import models.utils.AzureMLUtils as AzureMLUtils

def main():
    dotenv.load_dotenv()
    ws = AzureMLUtils.get_workspace()
    published_pipeline = PublishedPipeline.get(workspace=ws, id="312d78d5-26d5-4215-95e1-03892402a298")
    pipeline_run = Experiment(ws, 'batch-pipeline-run').submit(published_pipeline)
    pipeline_run.wait_for_completion(show_output=True)

if __name__ == "__main__":
    main()