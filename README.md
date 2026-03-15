# DeepCSAT – Customer Satisfaction Score Prediction Using Artificial Neural Networks

## Project Overview

Customer satisfaction is a key indicator of service quality in e-commerce platforms. Companies receive thousands of customer support requests every day related to product issues, delivery delays, payment problems, and order tracking. Predicting customer satisfaction helps organizations understand service performance and improve customer experience.

This project focuses on predicting **Customer Satisfaction Scores (CSAT)** using customer support interaction data. A **Deep Learning model based on Artificial Neural Networks (ANN)** was developed to learn patterns from customer support interactions and estimate satisfaction levels.

The project also includes a **Streamlit-based web application** that allows users to input interaction details and obtain predicted CSAT scores in real time.

---

## Objectives

* Analyze customer support interaction data.
* Identify key factors influencing customer satisfaction.
* Develop a deep learning model for CSAT prediction.
* Evaluate the model using appropriate performance metrics.
* Deploy the trained model using a Streamlit web application.

---

## Dataset

The dataset used in this project contains customer support interaction records from an e-commerce platform.

Each record represents a customer support interaction and includes features such as:

* Channel Name
* Category
* Sub-category
* Agent Name
* Supervisor
* Manager
* Tenure Bucket
* Agent Shift
* Customer Satisfaction Score (CSAT)

Dataset location in repository:

```
data/eCommerce_Customer_support_data.csv
```

The notebook automatically detects the dataset path if the file is placed in the `data/` directory or the project root.

---

## Project Workflow

### 1. Data Exploration

Initial data analysis was performed to understand the dataset structure, including:

* Dataset shape and size
* Column descriptions
* Missing value analysis
* Distribution of CSAT scores

---

### 2. Data Preprocessing

The preprocessing pipeline includes:

* Handling missing values
* Removing irrelevant columns
* Label encoding categorical variables
* Feature scaling using **StandardScaler**

---

### 3. Model Development

An **Artificial Neural Network (ANN)** was implemented using TensorFlow/Keras.

Model Architecture:

```
Input Layer
Dense Layer (64 neurons, ReLU)
Dense Layer (32 neurons, ReLU)
Dense Layer (16 neurons, ReLU)
Output Layer (1 neuron)
```

This architecture allows the model to capture nonlinear relationships between interaction features and customer satisfaction scores.

---

### 4. Model Training

The model was trained using:

* Optimizer: Adam
* Loss Function: Mean Squared Error (MSE)
* Evaluation Metric: Mean Absolute Error (MAE)
* Epochs: 20
* Batch Size: 32
* Validation Split: 0.2

---

### 5. Model Evaluation

Model performance on the test dataset:

```
Test Loss (MSE): ~1.84
Test MAE: ~0.99
```

This indicates that the predicted CSAT scores differ from the actual scores by approximately **one point on average** on a scale of **1–5**, which represents good predictive performance.

---

### 6. Visualization

Training and validation loss curves were plotted to analyze the learning behavior of the neural network and ensure stable training without significant overfitting.

---

### 7. Model Deployment

The trained model was saved using the native **Keras (.keras)** format and deployed locally using **Streamlit**.

The web application allows users to input customer support interaction details and obtain predicted CSAT scores instantly.

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
CSAT-Prediction
│
├── Notebook
│   └── CSAT_Prediction_Project.ipynb
│
├── Deployment
│   ├── app.py
│   ├── csat_ann_model.keras
│   ├── scaler.pkl
│
├── Dataset
│   └── eCommerce_Customer_support_data.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

### Folder Description

**Notebook/**
Contains the Jupyter notebook used for data exploration, preprocessing, model training, and evaluation.

**Deployment/**
Contains files required to run the Streamlit application for CSAT prediction.

**Dataset/**
Contains the dataset used for model training.

**requirements.txt**
Lists all required Python libraries.

**README.md**
Provides project documentation.

---

## How to Run the Project

### 1. Clone the Repository

```
git clone https://github.com/hubsukalp/CSAT-Prediction.git
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

---

### 3. Run the Streamlit Application

```
streamlit run deployment/app.py
```

---

### 4. Open the Web Application

After running the command above, open the following URL in your browser:

```
http://localhost:8501
```

You will see the **CSAT Prediction Interface**, where you can input interaction details and receive predicted satisfaction scores.

---

## Results

The deployed application demonstrates how machine learning can assist organizations in predicting customer satisfaction levels based on operational support data.

The model successfully learns patterns from historical support interactions and provides real-time predictions through the Streamlit interface.

---

## Conclusion

This project demonstrates the practical application of deep learning techniques for predicting customer satisfaction in e-commerce customer support systems. By analyzing operational parameters such as communication channels, issue categories, and agent information, the ANN model can provide valuable insights into customer satisfaction trends.

The deployed Streamlit application enables real-time prediction of CSAT scores, showcasing how machine learning can be integrated into customer support analytics to improve decision-making and service quality.

---
