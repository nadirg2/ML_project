# Machine Learning pet-project

The project explores the dataset of students performance. The goal is to develop a system that can predict student's math score.

## Project Highlights

* Data Exploration & Feature Engineering: The project leverages exploratory data analysis (EDA) to uncover insights and identify potential predictors of exam performance. Feature engineering techniques are applied to enhance the dataset for model training.
* Model Training & Optimization: A range of machine learning algorithms are explored, including [specify the algorithms used, e.g., Linear Regression, CatBoost, XGBoost]. The model selection process incorporates GridSearchCV for hyperparameter tuning to achieve optimal performance.
* User-Friendly Web Interface: A Flask-based web application allows users to input student information and receive a predicted exam score. The interface provides a clear and concise presentation of the prediction.

## Project Structure

```
.
├── artifacts/
│   ├── data.csv
│   ├── model.pkl
│   ├── preprocessor.pkl
│   ├── test.csv
│   └── train.csv
├── notebook/
│   ├── eda.ipynb
│   └── model_training.ipynb
├── src/
│   ├── components/
│   │   ├── logs/
│   │   ├── __init__.py
│   │   ├── data_ingestion.py
│   │   ├── data_transformation.py
│   │   └── model_trainer.py
│   ├── pipeline/
│   │   ├── __init__.py
│   │   ├── predict_pipeline.py
│   │   └── train_pipeline.py
│   ├── __init__.py
│   ├── exception.py
│   ├── logger.py
│   └── utils.py
├── templates/
│   └── index.html
├── .gitignore
├── app.py
├── requirements.txt
└── setup.py
```

## Key Components
* data_transformation.py: Handles data loading, cleaning, and feature engineering tasks.
* model_trainer.py: Implements model training, hyperparameter tuning using GridSearchCV, and model saving.
* utils.py: Contains helper functions for data manipulation.
* app.py: Defines the Flask web application for user interaction and prediction generation.
* model.pkl: Stores the trained machine learning model.


The project was created for educational purposes
