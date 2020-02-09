# Create Service identity

This is used for either of these cases:
1. Manual Service connection creation for Azure Devops
2. For use in Batch Inference (this will not be needed in future once we get the CLI support for Batch inference from the product)

### Steps
Note: If you don't have required permission, ask your admin to create this for you

1. Get subscription id (you need this for subsequent steps):
    1. Navigate to http://portal.azure.com
    2. Navigate to Browse
    3. In the search box being to type subscription
    4. Select Subscription from the search

2. __Create a Service Identity__ - this will be used by our application(Azure Devops) to access resources (like Azure ML workspace):

    To create service principal, register an application entity in Azure Active Directory (Azure AD) and grant it the Contributor or Owner role to the `Resource group` where your ML workspace will be. Alternatively you can provide access only to the ML workspace. 
    
    <BR>Instructions are [here](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal).
    <BR>__Note:__ The instructions in the link above provides generic steps to provide access to subscription or resource group level. However as indicated above you need to provide access to the resource group where the workspace will be OR provide access at workspace level.

    __Please make note of the following values__ after creating a service principal, we will need them in subsequent steps

    * Application (client) ID
    * Directory (tenant) ID
    * Application Secret

   