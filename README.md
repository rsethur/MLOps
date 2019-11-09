# MLOps - Machine Learning Operations
_We would like to thank the pioneers of the [MLOpsPython](https://github.com/microsoft/MLOpsPython/) repo - We have borrowed several aspects from the repo_ 

__Goal__ is to teach the fundamentals of MLOps to practitioners of Machine Learning with a hands-on approach.

__Why should you care?__ To sustain business benefits of Machine learning across your organization, we need to bring in discipline, automation & best practices. Enter MLOps.

__Approach__
1. __Minimalistic__ approach of an end to end MLOps pipeline: Fully CI/CD YAML based pipeline (no proprietary release pipelines in Azure devops), Gated releases (manual approvals) and full CLI based MLOps  
2. Focus is on clean, understandable pipeline & code - goal is to teach
3. Additional scenarios will include Model explanation, Data drift etc

__Technologies__: We will use Azure Machine Learning & Azure Devops to showcase CI/CD pipelines for a Machine Learning project. However the concepts are valid irrespective of vendor platforms.

__Get Started__
1. Understand what we are trying to do (below section + workshop discussion)
2. [Setup the environment](setup/Setup.md)
3. [Run an end to end MLOps pipeline](setup/StartBaseScenario.md)

_Note: Automated builds based on code/asset changes have been disabled by setting `triggers: none` in the pipelines. The reason is to avoid triggering accidental builds during your learning phase._

__MLOps Flow and Current Setup__
![MLOps Flow](setup/imgs/MLOpsFlow.jpg)

The above diagram illustrates a possible end to end MLOps scenario. Our current Build-Release pipeline has a subset: `Training` :arrow_right: `Approval` :arrow_right: `Model Registration` :arrow_right: `Package` :arrow_right: `Deploy in test`.
<BR><br>__Notes on our Base scenario:__
1. Directory Structure
    1. `mlops_pipelines` contains the devops pipelines
        1. The EnvCreatePipeline.yml is a devops pipeline that will provision all the components in the cloud
        2. The BuildReleasePipeline.yml is a devops pipeline that would perform the subset of steps mentioned above (Training to Deployment in Test)
    2. `code` directory has the source code for training and scoring. This will be used by Azure ML to create docker images to perform training & scoring.
    3. `dataset` directory contains the german credit card dataset
2. Training: For training we use a simple LogisticRegression model on the German Credit card dataset. We build sklearn pipeline that does festure engineering. We export the whole pipeline as a the model binary (pkl file).
3. We use Azure ML CLI as a mechanism for interacting with Azure ML due to simplicity reasons.

>More documentation will follow.

<br>_Acknowledgments for the [German Creditcard Dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+%28German+Credit+Data%29)_

`Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.`

