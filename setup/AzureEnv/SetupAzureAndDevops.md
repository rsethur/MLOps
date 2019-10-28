# Setup Azure and Devops

#### Part 1 - Check if you have the right required resources and permissions

1. Check if ACI(Azure Container Instance) is registered in your subscription. Try executing the command from the Cloud Shell in the portal (or ask your admin). Instructions [here](https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart)

    `az provider show -n Microsoft.ContainerInstance -o table`

2. if ACI is not registered, run this command.
note: you need to be the subscription owner in order to execute this command successfully.

    `az provider register -n Microsoft.ContainerInstance`

3. Check if you have access to create Resource Groups. Execute from cloud shell:

    Note: replace `YourUniqueName` with your own (e.g. your user id) - otherwise there will be erroers when multiple people in the subscription try creating with same name

    `az group create --name "YourUniqueName-AML-RG" --location eastus2`

    you can delete it by running:

    `az group delete --name "YourUniqueName-AML-RG"`

    **If you don't have access** to create resource group, ask your admin to give you access (or alteast create the group `YourUniqueName-AML-RG` with reuqired permissions)

3. Get subscription id (you need this for later part of the workshop):
    1. Navigate to http://portal.azure.com
    2. Navigate to Browse
    3. In the search box being to type subscription
    4. Select Subscription from the search

#### Part 2 - Setup Azure Devops

1. If you don't have Azure DevOps account, [create](https://docs.microsoft.com/en-us/azure/devops/organizations/accounts/create-organization?view=azure-devops) one
2. Create a project from the devops portal (top right of the portal). If you have trouble then refer to [docs](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
3. Create a Service Identity. This will be used by our application to access resources (like Azure ML workspace).portal

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

#### Part 3 - Setup Variables in Azure Devops
We use [variable groups](https://docs.microsoft.com/en-us/azure/devops/pipelines/library/variable-groups?view=azure-devops&tabs=designer#create-a-variable-group) inside Azure DevOps to leverage them across pipelines.
Azure keyvault could be used to store values of confidential variables.

1. Click on **Library** under the Pipelines in the left navigation bar
2. Create new Variable Group
3. Add the following Variables and Values

Please name your variable group **``mlops-aml-vg``** as we are using this name within our build yaml file.

The variable group should contain the following variables:

| Variable Name               | Suggested Value              |
| --------------------------- | ---------------------------- |
| COMPUTE_CLUSTER_SKU         | STANDARD_DS2_V2              |
| COMPUTE_CLUSTER_NAME        | traincluster                 |
| BASE_NAME                   | [unique base name]           |
| LOCATION                    | eastus2                      |
| MODEL_NAME                  | creditcard-risk-model.pkl    |
| SP_APP_ID                   |                              |
| SP_APP_SECRET               |                              |
| SUBSCRIPTION_ID             |                              |
| TENANT_ID                   |                              |

Mark **SP_APP_SECRET** variable as a secret one.

**Note:** The BASE_NAME parameter is used throughout the solution for naming Azure resources. There can be naming collisions with resources that require unique names like azure blob storage and registry DNS naming. Make sure to give a unique value to the BASE_NAME variable (e.g. MyUniqueML), so that the created resources will have unique names (e.g. MyUniqueML-AML-RG, MyUniqueML-AML-WS, etc.). The length of the BASE_NAME value should not exceed 10 characters.

Make sure to select the **Allow access to all pipelines** checkbox in the variable group configuration.

