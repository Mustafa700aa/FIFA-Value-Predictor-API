FIFA 21 Player Value Predictor ⚽💰
Project Overview
An end-to-end Machine Learning project that predicts the market value of football players based on their attributes. The project covers the entire pipeline from raw data cleaning to deploying a production-ready API using FastAPI and Docker.

🚀 Key Features
Data Engineering: Advanced cleaning of the FIFA 21 messy dataset (handling currencies, height/weight conversions, and special characters).

Deep Learning Model: Built and trained a Neural Network using TensorFlow/Keras to predict player values with high accuracy.

RESTful API: Developed a fast and lightweight API using FastAPI to serve model predictions.

Containerization: Fully Dockerized application for consistent deployment across any environment.

🛠️ Tech Stack
Language: Python 3.9

Data Analysis: Pandas, NumPy

Machine Learning: Scikit-learn, TensorFlow, Keras

API Framework: FastAPI, Uvicorn

DevOps: Docker

📂 Project Structure
Plaintext

.
├── Main.py              # FastAPI Application
├── model_logic.py       # Machine Learning Inference Logic
├── utils.py             # Data Preprocessing & Cleaning functions
├── requirements.txt      # Python dependencies
├── Dockerfile           # Docker container configuration
└── assets/              # Saved model and scalers
    ├── fifa_model.keras
    ├── fifa_x_scaler.pkl
    └── fifa_y_scaler.pkl
⚙️ Installation & Setup
Prerequisites
Python 3.9+ (if running locally)

Docker (Recommended)

Option 1: Using Docker (Fastest)
Build the image:

Bash

docker build -t fifa-predictor .
Run the container:

Bash

docker run -p 8000:8000 fifa-predictor
Option 2: Local Setup
Install dependencies:

Bash

pip install -r requirements.txt
Run the server:

Bash

uvicorn Main:app --reload
📖 API Usage
Once the server is running, visit http://localhost:8000/docs to access the interactive Swagger UI.

Endpoint: POST /predict Sample Input:

JSON

{
  "features": [85.0, 92.0, 78.5, ...] 
}
💡 Implementation Details
Preprocessing: Applied custom transformations to handle complex string formats in the raw dataset.

Scaling: Used StandardScaler for both features and target variables to ensure optimal neural network convergence.

Deployment: Optimized the container size using a python:3.9-slim base image.

