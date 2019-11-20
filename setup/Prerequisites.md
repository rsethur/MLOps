# Prerequisites

1. __Check if ACI(Azure Container Instance) and AKS (Azure Kubernetes Service) are registered in your subscription__: Try executing the command from the Cloud Shell in the portal. Instructions [here](https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart).
    If you dont have access, ask your __admin__.

    `az provider show -n Microsoft.ContainerInstance -o table`
    
    `az provider show -n Microsoft.ContainerService -o table`

    if not registered, run the below command (you need to be the subscription owner in order to execute this command successfully)

    `az provider register -n Microsoft.ContainerInstance`
    
    `az provider register -n Microsoft.ContainerService`
    
    If you dont have access, ask your __admin__.

3. If you don't have Azure DevOps account, [create](https://dev.azure.com) one

4. If you do not have a github account, [create](https://github.com/) one

<!-- Not needed currently. For future reference.
3. Get subscription id (you need this for later part of the workshop):
    1. Navigate to http://portal.azure.com
    2. Navigate to Browse
    3. In the search box being to type subscription
    4. Select Subscription from the search

2. __Create a Service Identity__ - this will be used by our application(AZure Devops) to access resources (like Azure ML workspace):

    To create service principal, register an application entity in Azure Active Directory (Azure AD) and grant it the Contributor or Owner role of the subscription or the resource group where the web service belongs to.
    Instructions are [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).
    __Important__: When you do the app registration, select Type as "Public client/native" instead of the default "Webapp"

    __Please make note of the following values__ after creating a service principal, we will need them in subsequent steps

    * Application (client) ID
    * Directory (tenant) ID
    * Application Secret

   Note: If you don't have permission, ask your admin to create a Service Identity for you
-->