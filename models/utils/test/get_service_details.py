import argparse
from models.utils import AzureMLUtils
from azureml.core.webservice import Webservice

def main():
    ws = AzureMLUtils.get_workspace()
    print("Workspace lookup successful")
    # read command line parameters
    service_name = getRuntimeArgs()

    #look up service
    service = Webservice(ws, service_name)

    # look up scoring uri
    scoring_uri = service.scoring_uri

    #Get the first api key
    if service.compute_type == "AKS":
        api_key = service.get_keys()[0]
    elif service.compute_type == "ACI":
        api_key = "dummy"
    else:
        raise Exception("Unknown compute type")

    # This line is needed to for Azure Devops to set api key and scoring uri as environment variable.
    print("##vso[task.setvariable variable=TMP_SCORING_URI]", scoring_uri)
    print("##vso[task.setvariable variable=TMP_API_KEY]", api_key)

def getRuntimeArgs():
    parser = argparse.ArgumentParser()
    parser.add_argument('--SERVICE_NAME', type=str)
    args = parser.parse_args()
    return args.SERVICE_NAME

if __name__ == "__main__":
    main()