import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Smart Agriculture Monitoring System",
    page_icon="🌱",
    layout="wide"
)
# -----------------------------
# Sidebar
# -----------------------------
with st.sidebar:

    st.title("🌱 Smart Agriculture")

    st.markdown("---")

    st.subheader("Project Details")

    st.write("NIT Rourkela Internship Project")

    st.write("Model: Random Forest")

    st.write("Full Model Accuracy: 98.72%")

    st.write("Sensor-Only Model Accuracy: 87.79%")

    st.markdown("---")

    st.subheader("Technologies")

    st.write("• Raspberry Pi")
    st.write("• DHT11 Sensor")
    st.write("• Soil Moisture Sensor")
    st.write("• Rain Sensor")
    st.write("• Streamlit")
    st.write("• Scikit-Learn")
# -----------------------------
# Load Model and Encoders
# -----------------------------
try:
    model = joblib.load("ml_model/irrigation_model.pkl")

    crop_encoder = joblib.load("ml_model/crop_encoder.pkl")
    soil_encoder = joblib.load("ml_model/soil_encoder.pkl")
    stage_encoder = joblib.load("ml_model/stage_encoder.pkl")

    model_loaded = True

except Exception as e:
    model_loaded = False
    st.error(f"Error loading model files: {e}")
if model_loaded:
    st.success("✅ Model Loaded Successfully")

else:
    st.error("❌ Model Not Loaded")
# -----------------------------
# Header
# -----------------------------
st.title("🌱 Smart Agriculture Monitoring System")
st.markdown("### AI + IoT Based Irrigation Recommendation System")

st.divider()

# -----------------------------
# Sensor Section
# -----------------------------
st.header("📡 Live Sensor Data")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Temperature", "30°C")

with col2:
    st.metric("Humidity", "65%")

with col3:
    st.metric("Soil Status", "Dry")

with col4:
    st.metric("Rain Status", "No Rain")

st.divider()

# -----------------------------
# Crop Information
# -----------------------------
st.header("🌾 Crop Information")

crop = st.selectbox(
    "Crop Type",
    [
        "Wheat",
        "Potato",
        "Carrot",
        "Tomato",
        "Chilli"
    ]
)

soil = st.selectbox(
    "Soil Type",
    [
        "Black Soil",
        "Alluvial Soil",
        "Sandy Soil",
        "Red Soil",
        "Clay Soil",
        "Loam Soil",
        "Chalky Soil"
    ]
)

stage = st.selectbox(
    "Growth Stage",
    [
        "Germination",
        "Seedling Stage",
        "Vegetative Growth / Root or Tuber Development",
        "Flowering",
        "Pollination",
        "Fruit/Grain/Bulb Formation",
        "Maturation",
        "Harvest"
    ]
)

st.divider()

# -----------------------------
# Environmental Conditions
# -----------------------------
st.header("🌦 Environmental Conditions")

col1, col2, col3 = st.columns(3)

with col1:
    moi = st.number_input(
        "Moisture Index (MOI)",
        min_value=0.0,
        max_value=100.0,
        value=40.0
    )

with col2:
    temperature = st.number_input(
        "Temperature (°C)",
        min_value=0.0,
        max_value=60.0,
        value=30.0
    )

with col3:
    humidity = st.number_input(
        "Humidity (%)",
        min_value=0.0,
        max_value=100.0,
        value=65.0
    )

st.divider()

# -----------------------------
# Prediction Section
# -----------------------------
if st.button("🚀 Predict Irrigation Requirement"):

    if model_loaded:

        try:

            # Encode Inputs
            crop_encoded = crop_encoder.transform([crop])[0]
            soil_encoded = soil_encoder.transform([soil])[0]
            stage_encoded = stage_encoder.transform([stage])[0]

            # Create Input DataFrame
            input_data = pd.DataFrame(
                [[
                    crop_encoded,
                    soil_encoded,
                    stage_encoded,
                    moi,
                    temperature,
                    humidity
                ]],
                columns=[
                    "crop_ID_encoded",
                    "soil_type_encoded",
                    "stage_encoded",
                    "MOI",
                    "temp",
                    "humidity"
                ]
            )

            # Prediction
            prediction = model.predict(input_data)[0]

            # Probability Scores
            probabilities = model.predict_proba(input_data)[0]

            # Raw Prediction (for testing)
            st.write("Raw Prediction:", prediction)

            # Recommendation
            st.subheader("🌱 Irrigation Recommendation")

            if prediction == 0:
                st.success("✅ No Irrigation Required")

            elif prediction == 1:
                st.warning("💧 Irrigation Required")

            elif prediction == 2:
                st.info("🌧 High Moisture Condition")

            # -----------------------------
            # Prediction Confidence
            # -----------------------------
            st.subheader("📊 Prediction Confidence")

            prob_df = pd.DataFrame(
                {
                    "Class": ["Class 0", "Class 1", "Class 2"],
                    "Probability (%)": [
                        round(probabilities[0] * 100, 2),
                        round(probabilities[1] * 100, 2),
                        round(probabilities[2] * 100, 2)
                    ]
                }
            )

            st.dataframe(prob_df, use_container_width=True)

            # -----------------------------
            # Input Summary
            # -----------------------------
            st.subheader("📋 Input Summary")

            summary_df = pd.DataFrame(
                {
                    "Parameter": [
                        "Crop Type",
                        "Soil Type",
                        "Growth Stage",
                        "MOI",
                        "Temperature",
                        "Humidity"
                    ],
                    "Value": [
                        crop,
                        soil,
                        stage,
                        moi,
                        temperature,
                        humidity
                    ]
                }
            )

            st.dataframe(summary_df, use_container_width=True)

        except Exception as e:
            st.error(f"Prediction Error: {e}")

    else:
        st.error("Model files not found. Please check the ml_model folder.")

st.divider()

st.header("📈 Feature Importance")

feature_names = [
    "MOI",
    "Temperature",
    "Humidity",
    "Growth Stage",
    "Crop Type",
    "Soil Type"
]

importance_values = [
    0.361271,
    0.283183,
    0.216885,
    0.078946,
    0.033551,
    0.026165
]

fig, ax = plt.subplots(figsize=(8, 4))

ax.barh(feature_names, importance_values)

ax.set_xlabel("Importance")

st.pyplot(fig)

st.divider()

st.header("🏗 System Architecture")

st.markdown("""
Sensors (DHT11, Soil Moisture, Rain Sensor)

⬇

Raspberry Pi

⬇

Data Processing

⬇

Random Forest Model

⬇

Irrigation Recommendation

⬇

Streamlit Dashboard
""")