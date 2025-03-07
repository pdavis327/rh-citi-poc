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
