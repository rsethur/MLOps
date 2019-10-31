# Setup  Local Dev Environment
 This can be your local machine or Datascience VM in Azure:

1. Fork the MLOps project: visit the MLOps [github project](https://github.com/rsethur/MLOps) and click `Fork` on top right.

    Now you can save your changes to your github.This step is optional but recommended. 

2. Clone the project to your local directory: Click on the "Clone" button in github and copy the https url (like https://github.com/rsethur/MLOps.git)

3. If you have [Git](https://git-scm.com/downloads) installed in your machine, go to command prompt to a project directory and execute
`git clone <URL>`

    Optionally you click the "Clone or Download" button in github to download zip file & extract it.

4. Create conda environment: Via command prompt, navigate to project root folder and execute:
`conda env create -f "code/train/conda_dependencies.yml"`

5. (Optional) Install [postman](https://www.getpostman.com/downloads/) tool. This will give an easy way to inspect the deployed ML service