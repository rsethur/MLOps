import os
import AMLUtils
from azureml.core import Experiment
from azureml.train.estimator import Estimator
from azureml.core import Dataset
from azureml.core import Environment
from azureml.core.compute import AmlCompute
from azureml.core.conda_dependencies import CondaDependencies
from dotenv import load_dotenv

TRAIN_SCRIPT_FOLDER = "code/train"

def main():
    load_dotenv()
    compute_cluster_name = os.environ.get("COMPUTE_CLUSTER_NAME")
    model_name = os.environ.get("MODEL_NAME")
    experiment_name = model_name+"-experiment"
    dataset_name = os.environ.get("DATASET_NAME")

    ws = AMLUtils.get_workspace()
    exp = Experiment(workspace=ws, name=experiment_name)

    compute_target = getComputeCluster(ws, compute_cluster_name)

    dataset = Dataset.get_by_name(ws, dataset_name, version='latest')

    environment_variables = {"MODEL_NAME":model_name, "DATASET_NAME":dataset_name}

    est = Estimator(source_directory=TRAIN_SCRIPT_FOLDER,
                    entry_script='train1.py',
                    # pass dataset object as an input
                    inputs=[dataset.as_named_input(dataset_name)],
                    compute_target=compute_target,
                    environment_variables=environment_variables,
                    conda_dependencies_file="train_conda_env.yml")

    run = exp.submit(est)
    run.wait_for_completion(show_output=True)

    # Write the run id to file. This is needed for future stages in the build pipeline (to register the model)
    run_id = run.get_details()["runId"]
    print("Writing Run id to run_id.txt: "+run_id)
    with open("run_id.txt", "w") as text_file:
        print(run_id, file=text_file, end="")


def getComputeCluster(ws, compute_cluster_name):
    if compute_cluster_name in ws.compute_targets:
        compute_target = ws.compute_targets[compute_cluster_name]
        if compute_target and type(compute_target) is AmlCompute:
            print('Found compute target ' + compute_cluster_name)
    else:
        raise Exception('ERROR: compute not found')
    return compute_target


if __name__ == "__main__":
    main()