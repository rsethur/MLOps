# Prerequisites

1. __Check if ACI(Azure Container Instance) service is registered in your subscription__: Try executing the command from the Cloud Shell in the portal. Instructions [here](https://docs.microsoft.com/en-us/azure/cloud-shell/quickstart).
    If you dont have access, ask your __admin__.

    `az provider show -n Microsoft.ContainerInstance -o table`

    if not registered, run the below command (you need to be the subscription owner in order to execute this command successfully)

    `az provider register -n Microsoft.ContainerInstance`
    
    If you dont have access, ask your __admin__.

3. If you don't have Azure DevOps account, [create](https://dev.azure.com) one

4. If you do not have a github account, [create](https://github.com/) one

5. __[Optional]__ If you need Batch Inference, we need to create Service Principal & look up Subscription id. Instructions [here](CreateServiceIdentity.md)

6. __[Optional]__ If you plan to build your own models using your data, please make them available in blob store and get access to the store (like accountkey/SAS token)