# Setup Devops Project

1. Login to Azure Devops -> Enable preview feature called `Multi Stage Pipeline`. Instructions [here](https://docs.microsoft.com/en-us/azure/devops/project/navigation/preview-features?view=azure-devops).
2. Create a project from the devops portal (top right of the portal). If you have trouble then refer to [docs](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
3. Create Azure Resource Manager Service connection. This is needed for azure devops to connect to your subscription and create/manage resources.

    Go to `project settings` in bottom left of devops portal & select `Service Connections` and setup a Resource Manager connection. You have few options:
    * __Option 1:__ If you have `Contributor` or `Owner` access to the `Subscription` or a `Resource Group`
        * Select `Service Principal (Automatic)`
        * Select the scope of your choice (ideally select `Subscription` as scope and specific `Resource group`) 
        * Name of this Connection should be `AzureResourceManagerConnection`. Leave this checked `Allow all pipelines to use this connection`.
    * __Option 2:__ If you would like to restrict access to a ML workspace level OR if you are in a tighter access control environment:
        * Create Service Principal & look up Subscription id. Instructions [here](CreateServiceIdentity.md). If you already created one part of prerequisites, you can skip this.
        * Select `Service Principal (Manual)`
        * Select the scope of your choice (in this case select `Machine Learning Workspace`)
        * Fill in all the values 
        * Name of this Connection should be `AzureResourceManagerConnection`. Leave this checked `Allow all pipelines to use this connection`.

4. The following step is needed for additional security for the prediction service that we will deploy. Inorder to treat the service endpoint URI and API key as `secret` in the devops pipeline, create a variable group:
    1. In Azure Devops leftnav, navigate to `Pipeline` -> `Library`. Create a new `Variable group` by clicking `+ Variable`. Name it `MLOPSVG`
    2. Open the group and select `Allow access to all pipelines`
    3. Add two new variables `TMP_API_KEY` and `TMP_SCORING_URI`. For the values enter any value e.g. `dummy`. Click the `Lock` icon in the value to mark it `Secret`.
    <BR>`Save` the changes to the Variable group
    
5. [Optional] For Batch Inference you need to add the following variables using the values you got in the [prerequsite step](Prerequisites.md):
    1. WORKSPACE
    2. RESOURCE_GROUP
    3. SP_APP_ID
    4. SP_APP_SECRET
    5. SUBSCRIPTION_ID
    6. TENANT_ID
    <BR>`Save` the changes to the Variable group



