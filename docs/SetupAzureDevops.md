# Setup Devops Project

1. Login to Azure Devops -> Enable preview feature called `Multi Stage Pipeline`. Instructions [here](https://docs.microsoft.com/en-us/azure/devops/project/navigation/preview-features?view=azure-devops).
2. Create a project from the devops portal (top right of the portal). If you have trouble then refer to [docs](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
3. Create Azure Resource Manager Service connection. This is needed for azure devops to connect to your subscription and create/manage resources.

    Go to `project settings` in bottom left of devops portal & select `Service Connections` and setup a Resource Manager connection. You have to create at the correct scope:
    * If you would like to create the ML workspace via azure devops subscription, then  select subscription as the scope and leave resource group as blank. Alternatively you can select resoure group as scope (you have to create it before hand)
    * If you would like to use an existing workspace then select Azure ML workspace as the scope - and select the corresponding workspace.
    Name of this Connection should be `AzureResourceManagerConnection`. Leave this checked `Allow all pipelines to use this connection`.

4. Inorder to treat the service endpoint URI and API key as `secret` in the pipeline, create a variable group:
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



