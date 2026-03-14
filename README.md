# DeepCSAT – Customer Satisfaction Score Prediction Using Artificial Neural Networks

## Project Overview

Customer satisfaction is a crucial metric for evaluating the quality of customer support services in e-commerce platforms. Organizations handle thousands of customer interactions daily through different communication channels. Understanding and predicting customer satisfaction helps businesses improve service quality and customer experience.

This project focuses on predicting **Customer Satisfaction Scores (CSAT)** using customer support interaction data. The model analyzes various operational parameters such as communication channel, issue category, agent information, and support handling details to estimate customer satisfaction levels.

A **Deep Learning model using Artificial Neural Networks (ANN)** was implemented to learn patterns from historical customer support data and predict CSAT scores.

---

## Objectives

* Analyze customer support interaction data.
* Identify factors influencing customer satisfaction.
* Build a predictive model using Artificial Neural Networks.
* Evaluate model performance using appropriate metrics.
* Deploy the trained model locally using a Streamlit web application.

---

## Dataset Description

The dataset contains customer support interaction records with multiple features such as:

* Communication channel
* Issue category
* Sub-category
* Agent details
* Supervisor and manager information
* Tenure bucket
* Agent shift
* Customer Satisfaction Score (CSAT)

Each record represents a customer support interaction and the satisfaction score provided after the interaction.

---

## Project Workflow

### 1. Data Exploration

Initial data analysis was performed to understand dataset structure, including:

* Dataset shape
* Column information
* Missing value analysis
* Distribution of CSAT scores

### 2. Data Preprocessing

Data preprocessing steps included:

* Handling missing values
* Removing irrelevant columns
* Label encoding categorical features
* Feature scaling using **StandardScaler**

### 3. Model Development

An **Artificial Neural Network (ANN)** model was implemented using TensorFlow/Keras with the following architecture:

* Input Layer
* Dense Layer (64 neurons, ReLU)
* Dense Layer (32 neurons, ReLU)
* Dense Layer (16 neurons, ReLU)
* Output Layer (1 neuron)

### 4. Model Training

The model was trained using:

* Optimizer: Adam
* Loss Function: Mean Squared Error (MSE)
* Evaluation Metric: Mean Absolute Error (MAE)

### 5. Model Evaluation

The model achieved:

* **Test Loss (MSE): ~1.84**
* **Test MAE: ~0.99**

This indicates that the predicted CSAT score differs from the actual value by approximately **1 point on average**, which is reasonable for a CSAT scale ranging from 1 to 5.

### 6. Visualization

Training and validation loss curves were plotted to analyze the learning behavior of the neural network and confirm stable training without significant overfitting.

### 7. Model Deployment

The trained model was saved using the native **Keras (.keras) format** and deployed locally using **Streamlit**.

The web application allows users to input interaction details and receive a predicted CSAT score in real time.

---

## Technologies Used

* Python
* TensorFlow / Keras
* Scikit-learn
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Streamlit

---

## Project Structure

```
CSAT_Prediction_App
│
├── app.py
├── csat_ann_model.keras
├── scaler.pkl
├── requirements.txt
```

---

## How to Run the Project

### Install Dependencies

```
pip install -r requirements.txt
```

### Run the Application

```
streamlit run app.py
```

The application will open in your browser at:

```
http://localhost:8501
```

---

## Results

The deployed application allows users to input encoded interaction parameters and obtain predicted customer satisfaction scores instantly.

This demonstrates how deep learning models can assist organizations in **analyzing customer support performance and improving decision-making**.

---

## Conclusion

This project demonstrates the practical application of deep learning techniques in predicting customer satisfaction for e-commerce support systems. By analyzing operational parameters from customer interactions, the ANN model can provide useful insights into factors affecting customer satisfaction.

The deployed application provides an interactive interface for real-time CSAT prediction, showcasing the potential of machine learning in enhancing customer service analytics.

---


