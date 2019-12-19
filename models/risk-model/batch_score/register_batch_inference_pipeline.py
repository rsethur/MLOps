import os

import dotenv
from azureml.contrib.pipeline.steps import ParallelRunStep, ParallelRunConfig
from azureml.core import Dataset, Model
from azureml.core import Environment
from azureml.pipeline.core import Pipeline, PipelineData
import models.utils.AzureMLUtils as AzureMLUtils

BATCH_PIPELINE_NAME = "risk-scoring-batch-pipeline"
# Params: batch_pipeline_name, aml_compute_cluster, scoring_dataset, model_name + version
def main():
    dotenv.load_dotenv()
    ws = AzureMLUtils.get_workspace()
    print("got workspace")

    build_src_dir = os.environ.get("Build.SourcesDirectory")
    aml_compute_name = os.environ.get("AML_COMPUTE_CLUSTER")
    compute_target = ws.compute_targets[aml_compute_name]
    scoring_dataset = Dataset.get_by_name(ws, "credit_dataset")
    model = Model(ws, "risk-model")
    score_env = Environment.from_conda_specification("scoring_env", os.path.join(build_src_dir, "models/risk-model/batch_score/conda_dependencies.yml"))
    datastore = ws.get_default_datastore()
    output_folder = PipelineData(name='inferences', datastore=datastore)
    parallel_run_config = ParallelRunConfig(
        source_directory=os.path.join(build_src_dir, "models/risk-model/batch_score"),
        entry_script="batch_score.py",  # the user script to run against each input
        mini_batch_size='200',
        error_threshold=5,
        output_action='append_row',
        environment=score_env,
        compute_target=compute_target,
        node_count=2,
        run_invocation_timeout=600)
    distributed_inference_step = ParallelRunStep(
        name='credit-risk-inference-step',
        inputs=[scoring_dataset.as_named_input("credit_dataset")],
        output=output_folder,
        parallel_run_config=parallel_run_config,
        models=[model],
        arguments=['--model_name', 'risk-model'],
        allow_reuse=True
    )

    pipeline = Pipeline(workspace=ws, steps=[distributed_inference_step])
    pipeline.publish(BATCH_PIPELINE_NAME)

    #pipeline_run = Experiment(ws, 'batchinfer').submit(pipeline)
    #pipeline_run.wait_for_completion(show_output=True)


if __name__ == "__main__":
    main()