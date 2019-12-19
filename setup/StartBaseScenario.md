# Run an end-to-end MLOps pipeline

## Section 1: Setup Github & Integration with Devops
1. Perform the initial [setup](Setup.md) if not already done
2. Fork the MLOps repository
    1. Visit the MLOps [github project](https://github.com/rsethur/MLOps) and click `Fork` on top right.
    2. Give a name & let it remain "Public" for course of this workshop
    4. From your github repository, directly edit the file `mlops_pipelines/recipes/common/Variables.yml`: Change the `BASE_NAME` as per the instructions given there.
    3. In your project page copy your clone https url by clicking on the `Clone or Download` button - you will need this for next step
3. Setup integration between Devops & Github
    1. In the Azure Devops project you created earlier goto: Pipelines -> Pipelines
    2. Create new pipeline by clicking "New pipeline" button on top right
    3. To respond to question "Where is your code", click `Github (YAML)`
        1. Authorize the two requests: One for Azure devops to connect to github to load your pipelines & another for integration of triggers from github to Devops
        2. Click `Existing Azure Pipelines YAML file`
        3. Now you will see a list of YML (yaml) files. Follow next step below.

## Section 2: Create the environment 
This step will create the cloud environment and provision all the required services including Resource group & Azure ML Workspace
1. Continuing from the last section: select `mlops_pipelines/EnvCreatePipeline.yml` -> Click Continue -> Click Run
2. You can monitor the status by clicking on the stages. Check if your pipeline ran successfully.

## Section 3: Create a Dataset in Azure ML
1. Login into the [Azure ML portal](https://ml.azure.com/) and switch to the new workspace that was created using the build pipeline:
    1. In the top nav bar, click the Switch Directory icon
    2. Click on the drop down `Machine learning workspace` and select the one that was just created (`BASE_NAME-aml-ws`)
2. In the left panel click `Dataset` -> `Create Dataset` -> `from web files` 
    1. Paste this url `https://raw.githubusercontent.com/rsethur/MLOps/master/dataset/german_credit_data.csv`
    2. __Important__ Change dataset name to `credit_dataset`
    3. If a `CORS error` shows up, open the page and check all boxes in the `Allowed methods` drop down. 
    4. Follow the onscreen instructions by clicking `Next` till completion
    
## Section 4: Run the Build Release pipeline
Now we can run training & automate the deployment by running the build release pipeline.
1. Similar to first pipeline we ran, in the Azure Devops projectgoto: Pipelines -> Pipelines
2. Create new pipeline by clicking "New pipeline" button on top right
3. To respond to question "Where is your code", click `Github (YAML)`
    1. Click `Existing Azure Pipelines YAML file`
    2. Now you will see a list of YML (yaml) files: select `mlops_pipelines/BasicBuildRelease.yml` -> Click Continue -> Click Run

You can monitor the status by clicking on the stages. Check if your pipeline ran successfully.

## Section 5: Test the deployed service
1. Get the service endpoint:
    1. Navigate to the [Azure ML portal](https://ml.azure.com/)
    2. Go to `Endpoints` in the left nav bar -> click on the deployed service
    3. copy the url of the `REST endpoint` from the details
2. Two options for testing the end point
    1. Easy option: 
        1. Go to the prefilled request details in this [page](https://apitester.com/shared/checks/653d9edc6be34516b3998be73af478fd)
        2. Replace the existing URL with the new endpoint url -> click the `Test` button
        3. You should see `[0]` in the response body (The label `0` means bad and `1` means good from this credit risk model's perspective). For this data you will see a `0`.
    2. Another option:
        1. Use your favourite REST endpoint testing tool like Postman or API Tester (online)
        2. Fill the details: 
            1. Your rest endpoint URL
            2. Set content-type to `application/json`
            3. Request type to `POST`
            4. Copy the following post data -> press submit/test
            ```
            {
              'data': {
                "Age": [
                  20
                ],
                "Sex": [
                  "male"
                ],
                "Job": [
                  0
                ],
                "Housing": [
                  "own"
                ],
                "Saving accounts": [
                  "little"
                ],
                "Checking account": [
                  "little"
                ],
                "Credit amount": [
                  100
                ],
                "Duration": [
                  48
                ],
                "Purpose": [
                  "radio/TV"
                ]
              }
            }
           ```
            
## Section 6: Clean up
Once you understand the concepts & ready to delete the resources you can fo the the following:

From Azure Devops run the pipeline `mlops_pipelines/EnvTearDownPipeline.yml`. Alternatively you can login to Azure Portal and delete the resource group that we created (i.e. `your-unique-name-aml-rg`).

Do :star: the repo if you like it.