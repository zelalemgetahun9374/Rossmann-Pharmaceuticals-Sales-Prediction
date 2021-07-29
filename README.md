# Rossmann-Pharmaceuticals-Sales-Prediction

**Table of Contents**

- [Rossmann-Pharmaceuticals-Sales-Prediction](#rossmann-pharmaceuticals-sales-prediction)
  - [Overview](#overview)
  - [Scenario](#scenario)
  - [Approach](#approach)
  - [Project Structure](#project-structure)
    - [data:](#data)
    - [models:](#models)
    - [notebooks:](#notebooks)
    - [scripts](#scripts)
    - [tests:](#tests)
    - [logs:](#logs)
    - [root folder](#root-folder)
  - [Installation guide](#installation-guide)

## Overview
This repository is used for week 3 challenge of 10Academy. The instructions for this project can be found in the challenge document.

## Scenario
You work at Rossmann Pharmaceuticals as a Machine Learning Engineer. The finance team
wants to forecast sales in all their stores across several cities six weeks ahead of time.
Managers in individual stores rely on their years of experience as well as their personal
judgement to forecast sales.

The data team identified factors such as promotions, competition, school and state holidays,
seasonality, and locality as necessary for predicting the sales across the various stores.

Your job is to build and serve an end-to-end product that delivers this prediction to analysts
in the finance team.

## Approach
The project is divided and implemented by the following phases
- Exploration of customer purchasing behavior
- Prediction of store sales
  - Machine learning approach
  - Deep Learning approach
- Serving predictions on a web interface

## Project Structure
The repository has a number of files including python scripts, jupyter notebooks, pdfs and text files. Here is their structure with a brief explanation.

### data:
- the folder where the dataset csv file is stored

### models:
- the folder where models' pickle files are stored

### notebooks:
- `EDA.ipynb`: a jupyter notebook for exploratory data analysisalgorithms

### scripts
- `app_logger.py`: a python script for logging
- `csv_helper.py`: a python script for handling reading and writing of csv files
- `df_cleaner.py`: a python script for cleaning pandas dataframes
- `df_selector.py`: a python script for selecting data from a pandas dataframe
- `df_visualizer.py`: a python script for plotting selected data
- `df_outlier_handler.py`: a python script for cleaning outliers in  a pandas dataframe

### tests:
- the folder containing unit tests for components in the scripts

### logs:
- the folder containing log files (if it doesn't exist it will be created once logging starts)

### root folder
- `10 Academy Batch 4 - Week 3 Challenge.pdf`: the challenge document
- `requirements.txt`: a text file lsiting the projet's dependancies
- `travis.yml`: a configuration file for Travis CI
- `setup.py`: a configuration file for installing the scripts as a package
- `README.md`: Markdown text with a brief explanation of the project and the repository structure.

## Installation guide
```
git clone https://github.com/zelalemgetahun9374/Rossmann-Pharmaceuticals-Sales-Prediction
cd Rossmann-Pharmaceuticals-Sales-Prediction
pip install -r requirements.txt
```