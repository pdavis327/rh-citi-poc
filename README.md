# Citi - Policy Aggregation Assistant

## Introduction

Citi POC - InstructLab fine-tuning

Background and justification can be found [here](https://docs.google.com/document/d/1DkU8inHNn_OyC5YbcQcdmt0v361lhOblPS9usdJjQ3I/edit?tab=t.0).

## Prerequisites
To set up a new Conda environment, run the following commands:

```zsh
conda create --name my_project_env
conda activate my_project_env
pip install -r requirements.txt
```

To add pre-commit hooks, run the following command:
```zsh
`pre-commit install`
```

## Repository structure
The following are files and folders in the repository:

* `requirements.txt`: This file contains python dependencies.
* `util/`: This folder contains some utility modules.
* `assets/inputs`: This folder should contain the input pdfs. 
* `assets/outputs`: This is where the processed documents will land. 

### Running from your local python environment

```console
python convert_pdf.py
```

## Feedback and tips

* PoCs should start with evaluating existing foundation models to ensure they can’t already answer questions the customer is interested in.
* Also, you need success criteria in the form of an evaluation
* Check your Docling versions. Install from 2.25.2, 2.8.3 (installed last week) vs 2.26.0 (installed yesterday) gave wildly different results on tables
* The current version is unable to keep track of section headers (most are just labeled “##” even when that’s not the case)
* The native parser in Docling does a surprisingly good job, even on complicated PDFs.
* The word “context” in the Q&A files is misleading
“questions_and_answers” is also overloaded with the filename.
* Long-term: Focus on the value-added parts of the work and get rid of the rest
* Preparing the YAML, taxonomy, tarballs, and checks is tedious.
* Replace with a UI or other mechanism to provide a friendly interface to automate away non-value-added tasks.
