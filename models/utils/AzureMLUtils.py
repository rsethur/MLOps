import os
import sys
import dotenv
from azureml.core import Workspace
from azureml.core.authentication import ServicePrincipalAuthentication

def get_workspace():
    dotenv.load_dotenv()
    workspace_name = os.environ.get("WORKSPACE")
    resource_group = os.environ.get("RESOURCE_GROUP")
    subscription_id = os.environ.get("SUBSCRIPTION_ID")
    tenant_id = os.environ.get("TENANT_ID")
    app_id = os.environ.get("SP_APP_ID")
    app_secret = os.environ.get("SP_APP_SECRET")

    service_principal = ServicePrincipalAuthentication(
        tenant_id=tenant_id,
        service_principal_id=app_id,
        service_principal_password=app_secret)

    try:
        aml_workspace = Workspace.get(
            name=workspace_name,
            subscription_id=subscription_id,
            resource_group=resource_group,
            auth=service_principal)

        return aml_workspace
    except Exception as caught_exception:
        print("Error while retrieving Workspace...")
        print(str(caught_exception))
        sys.exit(1)
