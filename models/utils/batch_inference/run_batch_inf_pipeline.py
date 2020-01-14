from azureml.pipeline.core import PipelineEndpoint

import models.utils.AzureMLUtils as AzureMLUtils

def main():
    ws = AzureMLUtils.get_workspace()
    print("got workspace")
    pipeline_endpoint = PipelineEndpoint.get(workspace=ws, name="parallel-run-step")
    pipeline_run  = pipeline_endpoint.submit("risk-model-batch")
    pipeline_run.wait_for_completion(show_output=True)

if __name__ == "__main__":
    main()