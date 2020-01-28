## Model Registration, Deployment & Batch Inference for Pretrained Image Classification Model

1. Setup your [local dev environment](/docs/SetupLocalDevEnvironment.md). However use this for `Step 5` instead:
<BR> `conda env create -f "models/img-model/batch_score/env/conda_dependencies.yml"`

2. Create a GPU cluster from [Azure ML Studio](https://ml.azure.com) with NC6 compute type & 2 nodes. Name it `gpuc`

3. CLI for pointing to the right subscription
<BR>
`az account set --subscription <your subscription id>`
4. CLI for model registration
<BR>`az ml model register --workspace-name <your workspace name> --resource-group <your resource group> -n img-model -p models/imgclassification/model`

5. CLI for deploying model (realtime scoring)
<BR>`az ml model deploy -n img-aci --model img-model:1 --ic   models/imgclassification/score/inference_config.yml --dc  models/imgclassification/score/aci_deployment_config.yml --overwrite --workspace-name <your workspace name> --resource-group <your resource group>`

6. Batch inference
    1. Publish Batch Inference Pipeline
        <BR> `python -m models.utils.batch_inference.publish_batch_inf_pipeline --AML_PIPELINE_YML_PATH models/imgclassification/batch_score/pipeline/AMLBatchPipeline.yml --AML_PIPELINE_NAME imgbatch`

    2. Run the pipeline 
    <BR>`az ml run submit-pipeline --pipeline-id <pipeline id from above command> --workspace-name <your workspace name> --resource-group <your resource grouo> --experiment-name img-batch-exp-gpu`