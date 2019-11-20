# MLOps - Machine Learning Operations

__Goals__  
1. Create a library of modular recipes (parameterized devops pipeline templates) which could then be composed to create custom end to end CI/CD pipelines for Machine Learning
2. To learn & teach fundamentals  

__Why care?__ To sustain business benefits of Machine learning across any organization, we need to bring in discipline, automation & best practices. Enter MLOps.

__Approach__
1. _Minimalistic_: Focus is on clean, understandable pipeline & code  
2. _Modular_: Atomic recipes that could be referred and reused (e.g recipe: Deploy to production after approval)

__Status__: [Project board](https://github.com/rsethur/MLOps/projects/1)

__Technologies__: Azure Machine Learning & Azure Devops

__Technical Aspects__ 
<BR>_It is fine if you do not understand this yet - there will be discussions in the workshop (todo: add detailed notes)_
1. Fully CI/CD YAML based multistage pipeline (does not use classic release pipelines in Azure devops)
2. Use YAML based variables template (no need to configure variable groups through UI)
2. Gated releases (manual approvals)
3. CLI based MLOps: use Azure ML CLI from Devops pipelines as a mechanism for interacting with the ML platform. Simple and clean.

__Get Started__
1. Understand what we are trying to do (below section + workshop discussion)
2. [Setup the environment](setup/Setup.md)
3. [Run an end to end MLOps pipeline](setup/StartBaseScenario.md)

_Note: Automated builds based on code/asset changes have been disabled by setting `triggers: none` in the pipelines. The reason is to avoid triggering accidental builds during your learning phase._

__MLOps Flow and Current Setup__
![MLOps Flow](setup/imgs/MLOpsFlow.jpg)

The above diagram illustrates a possible end to end MLOps scenario. Our current Build-Release pipeline has a subset: `Training` :arrow_right: `Approval` :arrow_right: `Model Registration` :arrow_right: `Package` :arrow_right: `Deploy in test` :arrow_right: `Approval` :arrow_right: `Deploy to Production`
<BR><br>__Notes on our Base scenario:__
1. Directory Structure
    1. `mlops_pipelines` contains the devops pipelines
        1. The EnvCreatePipeline.yml is a devops pipeline that will provision all the components in the cloud
        2. The BasicBuildRelease.yml is a devops pipeline that would perform the subset of steps mentioned above (Training to Deployment in Test)
    2. `code` directory has the source code for training and scoring. This will be used by Azure ML to create docker images to perform training & scoring.
    3. `dataset` directory contains the german credit card dataset
2. Training: For training we use a simple LogisticRegression model on the German Credit card dataset. We build sklearn pipeline that does feature engineering. We export the whole pipeline as a the model binary (pkl file).
3. We use Azure ML CLI as a mechanism for interacting with Azure ML due to simplicity reasons.

>More documentation will follow.

__Acknowledgements__
1. _[MLOpsPython](https://github.com/microsoft/MLOpsPython/) python repo was one of the inspirations for this - thanks to the contributors_
2. _[German Creditcard Dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29)_
<BR>`Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.`

