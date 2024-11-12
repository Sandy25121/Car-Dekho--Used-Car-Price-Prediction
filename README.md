Car Dheko - Used Car Price Prediction
Project Overview
This project, Car Dheko - Used Car Price Prediction, leverages machine learning to predict the prices of used cars based on various attributes such as make, model, year, fuel type, and transmission. The goal is to create a tool that enhances customer experience by providing a reliable, real-time price prediction tool accessible to both customers and sales representatives. This model is deployed in an interactive Streamlit app for ease of use.

Key Skills and Concepts
Data Cleaning and Preprocessing
Exploratory Data Analysis (EDA)
Machine Learning Model Development
Price Prediction Techniques
Model Evaluation and Optimization
Streamlit App Development
Documentation and Reporting
Domain
Industries: Automotive, Data Science, Machine Learning
Problem Statement
Objective: As a data scientist at Car Dheko, your goal is to develop a predictive model to estimate used car prices. This model should be accurate and user-friendly, with deployment in a Streamlit app that allows users to input car features and receive real-time price predictions.

Project Scope
This project uses historical car price data across various cities, featuring attributes such as make, model, year, and fuel type. The project steps include:

Data Processing: Consolidating, cleaning, and standardizing the dataset.
Model Development: Selecting, training, and optimizing machine learning models for price prediction.
Deployment: Creating an interactive Streamlit application to deliver real-time predictions based on user input.
Project Workflow
1. Data Processing
Data Import and Consolidation: Import datasets from multiple cities, assign city tags, and merge into a single structured dataset.
Handling Missing Values: Impute missing values using statistical methods (mean, median) or assign default categories.
Data Formatting: Standardize units and formats, e.g., convert "70 kms" to integers.
Encoding Categorical Variables: Use one-hot and label encoding as needed.
Normalization: Scale numerical features for consistency, using Min-Max or Standard scaling.
Outlier Removal: Identify and handle outliers using IQR or Z-score.
2. Exploratory Data Analysis (EDA)
Descriptive Statistics: Calculate summary statistics to understand data distribution.
Visualization: Use scatter plots, box plots, and heatmaps to explore relationships.
Feature Selection: Use correlation analysis and feature importance to identify key predictors.
3. Model Development
Train-Test Split: Split data for training and evaluation (e.g., 80-20).
Model Selection: Experiment with models such as Linear Regression, Decision Trees, and Random Forests.
Hyperparameter Tuning: Optimize model parameters using Grid or Random Search.
4. Model Evaluation
Metrics: Evaluate models using MAE, MSE, and R-squared.
Model Comparison: Select the best model based on performance metrics.
5. Deployment
Streamlit App: Build and deploy the app, allowing users to enter car details for instant predictions.
UI Design: Ensure a clear, user-friendly interface.
Results
A robust machine learning model for accurate car price prediction.
Comprehensive dataset analysis and visualizations.
Detailed documentation explaining the methodology, models, and results.
An interactive Streamlit application for real-time predictions.
Project Evaluation Metrics
Model Performance: Mean Absolute Error (MAE), Mean Squared Error (MSE), R-squared.
Data Quality: Completeness and accuracy of preprocessed data.
Application Usability: User satisfaction and ease of use.
Documentation Quality: Clarity and thoroughness.
Technical Tags
Data Preprocessing, Machine Learning, Price Prediction, Regression, Python, Pandas, Scikit-Learn, EDA, Streamlit, Model Deployment
Dataset Details
Dataset: Multiple Excel files for different cities, each providing car specifications and features.
Source: CarDekho
Project Deliverables
Source Code: Scripts for data preprocessing, model development, and deployment.
Documentation: Comprehensive explanations of methodology, model selection, and evaluation.
Visualizations: Reports and charts generated during EDA.
Predictive Model: Finalized, optimized model.
Streamlit App: Fully functional web application for car price predictions.
