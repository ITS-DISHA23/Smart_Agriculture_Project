# Smart Agriculture Monitoring System

## Overview

An IoT and Machine Learning based smart agriculture system that monitors environmental conditions and predicts irrigation requirements using sensor data and agricultural parameters.

## Technologies Used

- Raspberry Pi
- DHT11 Temperature and Humidity Sensor
- Soil Moisture Sensor
- Rain Sensor
- Python
- Scikit-learn
- Random Forest Classifier
- Streamlit
- GitHub

## Features

- Real-time sensor monitoring
- Irrigation recommendation system
- Machine learning-based prediction
- Streamlit dashboard visualization
- Raspberry Pi integration
- Data-driven irrigation management

## Model Performance

| Model | Features Used | Accuracy |
|---------|---------|---------|
| Full Model | Crop Type, Soil Type, Growth Stage, MOI, Temperature, Humidity | **98.72%** |
| Sensor-Only Model | MOI, Temperature, Humidity | **87.79%** |

## Key Findings

- Moisture Index (MOI), Temperature, and Humidity were the most influential features.
- The full model achieved the highest prediction accuracy.
- The sensor-only model demonstrated the feasibility of a fully automated IoT solution.
- A hybrid approach combining sensor data and agricultural information provides the best performance.