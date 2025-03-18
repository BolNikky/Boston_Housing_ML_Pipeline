# Boston_Housing_ML_Pipeline

**Project Overview**

This project involves building a predictive model using the Random Forest Regressor to estimate the median value of owner-occupied homes (MEDV) based on the Boston Housing dataset. The model is deployed as a FastAPI application, allowing users to input feature values and receive predictions via an API endpoint. The project includes data preprocessing, model evaluation, and API deployment.

**Files in This Repository**

app.py: The main FastAPI application file containing the API endpoints and prediction logic.

test.py: The script used for testing the model and generating predictions.

model.pkl: The trained Random Forest Regressor model saved as a pickle file.

boston.csv: The dataset used for training and testing the model.

Boston_housing_ML_Pipeline.ipynb: A Jupyter Notebook containing the exploratory data analysis, model training, and evaluation steps.

**How to Run This Project**

**Clone the repository:**

git clone https://github.com/yourusername/boston-housing-ml-pipeline.git
cd boston-housing-ml-pipeline

**Install the required dependencies:**

pip install fastapi uvicorn pydantic numpy pandas scikit-learn

**Run the FastAPI application:**

uvicorn app:app --host 0.0.0.0 --port 8000 --reload

**Access the API:**

The API will be available at http://127.0.0.1:8000.

Use the /predict endpoint to make predictions by sending a POST request with the required features.

**Evaluation Metrics and Model Performance**

The model's performance was evaluated using the following metrics:

**Mean Squared Error (MSE):** 24.00

**R² Score:** -0.009

**Mean Absolute Error (MAE):** 3.69

These metrics indicate that the model's performance is suboptimal, suggesting a need for further feature engineering or alternative modeling approaches.

**Challenges Faced and Solutions**

**Handling Missing Values:**

**Challenge:** Missing values in the training and validation sets.

**Solution: **Implemented strategies to identify and handle missing values, ensuring complete datasets for training and validation.

**Model Performance:**

**Challenge:** Suboptimal performance indicated by R² score and error metrics.

**Solution:** Conducted hyperparameter tuning and considered additional feature engineering techniques.

**API Deployment:**

**Challenge:** Deploying the model as a FastAPI endpoint.

**Solution:** Successfully implemented a FastAPI endpoint that accepts JSON input and returns predictions.

**Conclusion**
This project demonstrates the process of building and deploying a predictive model using the Random Forest Regressor. Despite the challenges faced, valuable insights were gained into data preprocessing, model evaluation, and API deployment. Future work should focus on improving model performance through advanced feature engineering and exploring alternative algorithms.
