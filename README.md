# MLOps - Machine Learning Operations
_I would like to thank the pioneers of the [MLOpsPython](https://github.com/microsoft/MLOpsPython/) repo - i have borrowed several aspects including variable groups, pipelines etc. This project would not have been possible without that repo._ 

__Goal__ is to teach the fundamentals of MLOps to practitioners of Machine Learning with a hands-on approach.

__Why should you care?__ To sustain business benefits of Machine learning across your organization, we need to bring in discipline, automation & best practices. Enter MLOps.

__Approach__
1. __Minimalastic__ approach of an end to end MLOps pipeline: Fully CI/CD YAML based pipeline (no proprietary release pipelines in Azure devops), Gated releases (manual approvals) and full CLI based MLOps  
2. Focus is on clean, understandable pipeline & code - goal is to teach
3. Additional scenarios will include Model explanation, Data drift etc

__Technologies__: We will use Azure Machine Learning & Azure Devops to showcase CI/CD pipelines for a Machine Learning project. However the concepts are valid irrespective of vendor platforms.

__Get Started__
1. Understand what we are trying to do (below section - to be updated)
2. [Setup the environment](setup/Setup.md)
3. [Run an end to end MLOps pipeline](setup/StartBaseScenario.md)

_Note: Automated builds based on code/asset changes have been disabled by setting `triggers: none` in the pipelines. The reason is to avoid triggering accidental builds during your learning phase._



_Acknowledgments for the [German Creditcard Dataset](https://archive.ics.uci.edu/ml/datasets/Statlog+(German+Credit+Data)_

`Dua, D. and Graff, C. (2019). UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.`

