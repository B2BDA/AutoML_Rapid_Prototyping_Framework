# AutoML_Rapid_Prototyping_Framework

## Objective
The main objective of this framework is to have an automated data science and machine learning pipeline for rapid prototyping and inferecing.
## Summary
> Sometimes we just want to understand if the data given to us is at all feasible for ML. So we can just pass the data as is through the pipeline and we should be able to get some results in form on models, performance metrics, EDA e.t.c and this will help us understand feasibility with regards to applying ML to the data given. 
> This framework is built on Orchest - https://www.orchest.io/
> This might be a direct replacement of Papermill/Parameterized notebooks and AirFlow.
> From the below diagram, we see that we are using various libraries for Data Cleaning, EDA, ML e.t.c
> The main objective is to have a low code ML pipeline which takes care of dirty data, performs necessary EDA and finally gives us a best performing model.
> Now after the pipeline gets completed, we should be able to have a fair idea regarding the data, the type of data cleaning which was performed, data transformations and also which modelling approach works best.
> **This is best for rapid prototying and winning client deals.**
> As we can see from concept to quick productionisation is possible with this approach.
> Highly intuitive. Basic knowledge of Python/ML is required for execution and interpretation.
> Plus this architecture can easily be scaled up and hosted on prem.

Planned Workflow on Miro Board
![image](https://user-images.githubusercontent.com/48247827/136177439-c76b2190-228d-415c-9a0b-50a4eec70ac3.png)
Ready Prototype on Orchest
![image](https://user-images.githubusercontent.com/48247827/136177036-679524e2-bc58-46aa-9f48-5c9ce7f70eee.png)
## Libraries used
1. autoviml
2. dataprep
3. datacleaner
5. pycaret
6. tpot
7. klib

*** will be updated as I explore more
# Next Steps
1. Add pyspark support for large df
2. Add new auto eda - edatk
3. Add model explainer - shap
4. Add model monitor - evidently
