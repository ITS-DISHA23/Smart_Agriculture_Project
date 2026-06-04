# Dataset Analysis

## Primary Dataset

### Dataset Information
- Rows: 16,411
- Columns: 7
- Missing Values: None

### Features
- crop ID
- soil_type
- Seedling Stage
- MOI
- temp
- humidity

### Target Variable
- result (Classes: 0, 1, 2)

### Observations
- Contains environmental and agricultural parameters.
- Features closely match available sensors.
- Suitable for irrigation recommendation prediction.
- Achieved 98.72% accuracy using Random Forest.

### Selection Status
✅ Selected as Final Dataset

---

## Backup Dataset

### Dataset Information
- Rows: 10,000
- Columns: 20
- Missing Values: None

### Features
- Soil_Type
- Soil_pH
- Soil_Moisture
- Organic_Carbon
- Electrical_Conductivity
- Temperature_C
- Humidity
- Rainfall_mm
- Sunlight_Hours
- Wind_Speed_kmh
- Crop_Type
- Crop_Growth_Stage
- Season
- Irrigation_Type
- Water_Source
- Field_Area_hectare
- Mulching_Used
- Previous_Irrigation_mm
- Region

### Target Variable
- Irrigation_Need

### Observations
- Contains detailed agricultural and environmental parameters.
- Includes several features not measurable using the available hardware setup.
- More suitable for large-scale agricultural analysis.
- Requires additional sensors and data sources for real-time deployment.

### Selection Status
❌ Not Selected as Final Dataset

### Reason for Rejection
The backup dataset was analyzed as an alternative dataset. However, the primary dataset was selected because its features (MOI, temperature, humidity, crop type, soil type, and growth stage) closely match the sensor data and project requirements. The backup dataset contains several features that cannot be collected using the available Raspberry Pi and sensor setup.