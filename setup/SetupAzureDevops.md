# Setup Devops Project
#### Part 1 - Configuration
1. Login to Azure Devops
1. Create a project from the devops portal (top right of the portal). Select the project visibility as `Enterprise`. If you have trouble then refer to [docs](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
3. Create a Service Identity - this will be used by our application to access resources (like Azure ML workspace):

    To create service principal, register an application entity in Azure Active Directory (Azure AD) and grant it the Contributor or Owner role of the subscription or the resource group where the web service belongs to.
    Instructions are [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).
    __Important__: When you do the app registration, select Type as "Public client/native" instead of the default "Webapp"

    __Please make note of the following values__ after creating a service principal, we will need them in subsequent steps

    * Application (client) ID
    * Directory (tenant) ID
    * Application Secret

   Note: If you don't have permission, ask your admin to create a Service Identity for you

4. Create Azure Resource Manager Service connection. This is needed for azure devops to connect to your subscription and create/manage resources.

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
| BASE_NAME                   | `your-unique-name` e.g. setu-mlops(max 10 chars & all lower case)|
| COMPUTE_CLUSTER_NAME        | traincluster                  |
| COMPUTE_CLUSTER_SKU         | STANDARD_DS2_V2               |
| DATASET_FILE_NAME           | german_credit_data.csv        |
| DATASET_NAME                | credit_dataset                |
| LOCATION                    | eastus2                       |
| MODEL_NAME                  | creditcard-risk-model         |
| RM_SERVICE_CONNECTION       | AzureResourceManagerConnection|
| SP_APP_ID                   |                               |
| SP_APP_SECRET               |                               |
| TENANT_ID                   |                               |

Mark **SP_APP_SECRET** variable as a secret one.

**Note:** The BASE_NAME parameter is used throughout the solution for naming Azure resources (for e.g. resource group will be create with name of BASE_NAME_aml_rg)

Make sure to select the **Allow access to all pipelines** checkbox in the variable group configuration.

