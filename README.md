# Automated Identification of Subarachnoid Hemorrhage in EHR Clinical Notes

This project was completed during my time as a research assistant at Beth Israel Deaconess Medical Center, Harvard Medical School, Department of Neurology under Dr. M. Brandon Westover. It creates a model to automatically identify subarachnoid hemorrhage diagnoses in EHR clinical notes.

## Abstract

**Background/Objectives:** To develop and evaluate a machine learning (ML) approach for automated identification of patients with non-traumatic subarachnoid hemorrhage (SAH) from electronic health records across different hospital systems.

**Methods:** We analyzed electronic health record data from Beth Israel Deaconess Medical Center (BIDMC) and Mass General Brigham (MGB) (2013-2024), creating a cohort of 3,096 patients. We de-veloped logistic regression and random forest models using natural language processing (NLP) and structured data extraction to identify SAH cases. We established ground truth through manual annotation following a standard operating procedure (SOP) and assessed model generalizability by performing cross-hospital validation.

**Results:** The logistic regression model achieved an AUROC of 0.9850 and AUPRC of 0.9540 on the holdout test set. We confirmed generalizability through cross-hospital validation, with models trained on one hospital and tested on another achieving an AUROC of 0.9794 (AUPRC: 0.9603). We estimated the error rate in the general hospital population at 0.11%. Key predictive features included terms like "sah," "subarachnoid," and "nimodipine," while terms such as "trauma" and "fracture" were negatively associated with SAH classification.

**Conclusions:** Our automated electronic health record phenotyping approach accurately identifies patients with non-traumatic SAH across different hospital systems. By integrating structured and unstructured data sources, our model addresses limitations of traditional ICD code-based methods while maintaining high performance and generalizability, enabling efficient large-scale identification of SAH cases without resource-intensive manual chart reviews.

## Reproducing the Project

The data used in this project is not publicly available due to patient privacy concerns. If you are interested in reproducing this project or using the data for your own research, please contact me to discuss potential data access. The data is accessed using Thunderpacks.

## Project Structure

The project is organized into the following directories, representing the data processing pipeline:

*   **cohortExtractionPipeline/ & newFlowCohortExtractionPipeline/**: These directories contain notebooks for extracting patient cohorts from the raw EHR data. They include scripts for filtering notes based on ICD codes, admission dates, and other criteria to create the initial positive and negative cohorts for both BIDMC and MGB.
*   **cleanCohorts/**: This directory contains notebooks for cleaning and standardizing the extracted cohorts. The notebooks merge data from different sources, drop unnecessary columns, and ensure the data is in a consistent format for further processing.
*   **test&trainCohorts/**: This directory contains the notebook for splitting the cleaned cohort into training and testing sets, a crucial step for model development and evaluation.
*   **featureMatrix/**: This directory contains notebooks for creating the feature matrices for the machine learning models. This includes extracting ICD-based features and generating keyword-based features from the clinical note text using techniques like stemming and regex.
*   **trainModels/**: This directory contains the notebooks for training the logistic regression and random forest models. It includes scripts for hyperparameter tuning using Bayesian search and cross-validation.
*   **finalModel/**: This directory contains notebooks for applying the trained models to the holdout test set and performing a final error analysis.
*   **cohortReconstruction/**: This directory contains notebooks for reconstructing the cohorts to estimate the prevalence of SAH and calculate the overall error rate of the model in the general hospital population.
*   **table1InfoExtraction/**: This directory contains notebooks for extracting demographic and clinical information to generate Table 1 for the research paper.
*   **cohortCheck/**: This directory contains notebooks for various checks and validations of the cohorts to ensure data quality.
