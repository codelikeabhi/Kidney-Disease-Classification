# Kidney Disease Prediction Using CT Scan Images

# How to run?

### Steps:

Clone the Repo

```bash
https://github.com/codelikeabhi/Kidney-Disease-Classification
```

### Step 1: Create a Conda Env after opening the Repo

```bash
conda create -n kidney python==3.8 -y
```

```bash
conda activate kidney
```

### Step 2: Install the requirements package

```bash
pip install -r requirements.txt
```

## Workflow

1. Update Config.yaml
2. Update params.yaml
3. Update the Entity
4. Update the Configuration Manager in /src/KidneyDiseaseClassifier/config
5. Update the Components
6. Update the Pipeline
7. Update the main.py
8. Update the dvc.yaml
9. Update app.py

### MLFlow
[Documentation](https://mlflow.org/docs/latest/index.html)

###### cmd
- mlflow ui

### DagsHub
[DagsHub](https://dagshub.com)

#### Run the following commands to export as env variables:
```bash
export MLFLOW_TRACKING_URI = https://dagshub.com/codelikeabhi/Kidney-Disease-Classification.mlflow

export MLFLOW_TRACKING_USERNAME= codelikeabhi

export MLFLOW_TRACKING_PASSWORD= replace_with_your_tracking_password
```