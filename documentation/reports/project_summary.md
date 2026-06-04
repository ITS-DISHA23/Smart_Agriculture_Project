# Smart Agriculture Monitoring System

## Problem Statement

Efficient water management is a major challenge in agriculture. Farmers often rely on manual observation to determine irrigation requirements, which can lead to over-irrigation or under-irrigation, resulting in water wastage and reduced crop productivity. The objective of this project is to develop an IoT-enabled smart agriculture system that uses sensor data and machine learning to predict irrigation requirements and assist farmers in making informed irrigation decisions.

---

## Objectives

- Monitor environmental conditions using IoT sensors.
- Collect soil moisture, temperature, humidity, and rainfall data.
- Develop a machine learning model for irrigation prediction.
- Provide irrigation recommendations based on real-time sensor readings.
- Reduce water wastage and improve irrigation efficiency.
- Create a dashboard for monitoring sensor data and predictions.

---

## Dataset Selection

Two datasets were analyzed during the project.

### Primary Dataset
- Rows: 16,411
- Columns: 7
- Features:
  - Crop Type
  - Soil Type
  - Seedling Stage
  - Moisture Index (MOI)
  - Temperature
  - Humidity
- Target Variable:
  - Result (0, 1, 2)

### Backup Dataset
- Rows: 10,000
- Columns: 20
- Included additional agricultural parameters such as soil pH, organic carbon, electrical conductivity, rainfall, wind speed, and irrigation history.

### Final Dataset Selection

The primary dataset was selected because its features closely matched the data that could be collected using the available hardware setup (DHT11 sensor, soil moisture sensor, and rain sensor). This made it more suitable for real-time IoT deployment.

---

## Model Training Process

The dataset was first analyzed for missing values and data quality issues. No missing values were found. Since machine learning algorithms cannot directly process categorical values, the Crop Type, Soil Type, and Seedling Stage features were converted into numerical form using Label Encoding.

The dataset was then divided into input features and target labels. An 80:20 train-test split was performed, where 80% of the data was used for training and 20% was used for testing.

A Random Forest Classifier was selected for prediction because it provides high accuracy, handles mixed feature types effectively, and reduces overfitting through ensemble learning. The model was trained using the encoded features and evaluated on unseen test data.

Feature importance analysis revealed that Moisture Index (MOI), Temperature, and Humidity were the most influential factors affecting irrigation decisions.

---

## Results

### Model Performance

- Algorithm: Random Forest Classifier
- Training/Test Split: 80:20
- Accuracy Achieved: **98.72%**

### Feature Importance

| Feature | Importance |
|----------|----------|
| MOI | 36.1% |
| Temperature | 28.3% |
| Humidity | 21.7% |
| Seedling Stage | 7.9% |
| Crop Type | 3.4% |
| Soil Type | 2.6% |

### Comparative Model Analysis

Two machine learning models were evaluated during the project.

| Model | Features Used | Accuracy |
|---------|---------|---------|
| Full Model | Crop Type, Soil Type, Seedling Stage, MOI, Temperature, Humidity | 98.72% |
| Sensor-Only Model | MOI, Temperature, Humidity | 87.79% |

The sensor-only model was developed to evaluate the feasibility of a fully automated IoT-based irrigation prediction system using only live sensor readings. While the model achieved a reasonable accuracy of 87.79%, its performance was lower than the full-feature model, particularly for one of the irrigation classes.

The comparison indicates that crop type, soil type, and growth stage contribute significant information for accurate irrigation prediction. Therefore, the final system adopts a hybrid approach that combines live sensor readings with user-provided agricultural information to achieve higher prediction accuracy.

### Interpretation

The model successfully learned the relationship between crop conditions and irrigation requirements. The highest impact on prediction came from moisture level, temperature, and humidity, which align with the sensor data available in the proposed IoT system.

---

## Conclusion

A Smart Agriculture Monitoring System was successfully developed using Machine Learning and IoT technologies to provide intelligent irrigation recommendations. The primary dataset was selected because its features closely matched the data that could be collected using the available hardware setup, including the Raspberry Pi, DHT11 sensor, soil moisture sensor, and rain sensor. A Random Forest Classifier was trained and evaluated, achieving an accuracy of 98.72% when using all available features. To assess the feasibility of a fully automated IoT-based solution, a sensor-only model using MOI, temperature, and humidity was also developed, achieving an accuracy of 87.79%. The comparison demonstrated that while environmental sensor data alone can provide useful irrigation recommendations, incorporating crop-specific, soil-specific, and growth-stage information significantly improves prediction performance. Therefore, the final proposed system adopts a hybrid architecture that combines live IoT sensor readings with agricultural inputs to deliver highly accurate irrigation recommendations. The developed system has the potential to optimize water usage, improve crop health, and support sustainable agricultural practices through data-driven decision-making.