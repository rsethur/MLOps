# Setup Devops Project
#### Part 1 - Configuration
1. Login to Azure Devops -> Enable preview feature called `Multi Stage Pipeline`. Instructions [here](https://docs.microsoft.com/en-us/azure/devops/project/navigation/preview-features?view=azure-devops).
2. Create a project from the devops portal (top right of the portal). If you have trouble then refer to [docs](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
3. Create Azure Resource Manager Service connection. This is needed for azure devops to connect to your subscription and create/manage resources.

    Go to `project settings` in bottom left of devops portal & select `Service Connections` and setup a Resource Manager connection at subsciption level (leave resource group as blank).
    Name of this Connection should be `AzureResourceManagerConnection`. Leave this checked `Allow all pipelines to use this connection`.

#### Part 2 - Setup Variables in Azure Devops
We use [variable groups](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops&tabs=designer#create-a-variable-group) inside Azure DevOps to leverage them across pipelines.
Azure keyvault could be used to store values of confidential variables.

1. Click on **Library** under the Pipelines in the left navigation bar
2. Create new Variable Group
3. Add the following Variables and Values

Please name your variable group **``mlops-aml-vg``** as we are using this name within our build yaml file.

The variable group should contain the following variables:

| Variable Name               | Suggested Value               |
| --------------------------- | ----------------------------  |
| BASE_NAME                   | globally unique name e.g. `xxxxml` <BR>__important__: no underscore, max 10 chars & all lower case|
| AML_COMPUTE_CLUSTER               | amlcompute                  |
| AML_COMPUTE_SKU           | STANDARD_DS4_V2               |
| AKS_CLUSTER         | akscluster                    |
| DATASET_FILE_NAME           | german_credit_data.csv        |
| DATASET_NAME                | credit_dataset                |
| LOCATION                    | eastus2                       |
| MODEL_NAME                  | creditcard-risk-model         |
| RM_SERVICE_CONNECTION       | AzureResourceManagerConnection|
| SP_APP_ID                   | [from above section]          |
| SP_APP_SECRET               | [from above section]         |
| TENANT_ID                   | [from above section]          |

Mark **SP_APP_SECRET** variable as a secret one.

**Note:** The BASE_NAME parameter is used throughout the solution for naming Azure resources (for e.g. resource group will be create with name of BASE_NAME_aml_rg)

Make sure to select the **Allow access to all pipelines** checkbox in the variable group configuration.

