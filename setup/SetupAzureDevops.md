# Setup Devops Project

1. Login to Azure Devops -> Enable preview feature called `Multi Stage Pipeline`. Instructions [here](https://docs.microsoft.com/en-us/azure/devops/project/navigation/preview-features?view=azure-devops).
2. Create a project from the devops portal (top right of the portal). If you have trouble then refer to [docs](https://docs.microsoft.com/en-us/azure/devops/organizations/projects/create-project?view=azure-devops)
3. Create Azure Resource Manager Service connection. This is needed for azure devops to connect to your subscription and create/manage resources.

    Go to `project settings` in bottom left of devops portal & select `Service Connections` and setup a Resource Manager connection at subsciption level (leave resource group as blank).
    Name of this Connection should be `AzureResourceManagerConnection`. Leave this checked `Allow all pipelines to use this connection`.


