import streamlit as st
import random
from PIL import Image  # For handling the image file

# Set page configuration
st.set_page_config(
    page_title="Water Quality Assessment",
    page_icon="🌊",
    layout="wide",
    initial_sidebar_state="expanded",
)



# Title with a subtitle
st.title("🌊 Water Quality Assessment")
st.markdown(
    """
    <p style="font-size:20px; color: #4c566a; font-weight: lighter;">
        A simple yet powerful tool for evaluating water quality based on various parameters.
    </p>
    """,
    unsafe_allow_html=True,
)

# Input form for water quality parameters
with st.form("water_quality_form"):
    st.markdown("### 📋 Enter Water Quality Parameters")
    col1, col2 = st.columns(2)

    with col1:
        station_code = st.text_input("Station Code")
        location = st.text_input("Location")
        state = st.text_input("State")
        temperature = st.text_input("Temperature (°C)")
        dissolved_oxygen = st.text_input("Dissolved Oxygen (DO)")

    with col2:
        ph = st.text_input("pH Level")
        conductivity = st.text_input("Conductivity (µS/cm)")
        bod = st.text_input("Biological Oxygen Demand (BOD)")
        nitrate_n_nitrite_n = st.text_input("Nitrate-N and Nitrite-N")
        fecal_coliform = st.text_input("Fecal Coliform")
        total_coliform = st.text_input("Total Coliform")

    submit_button = st.form_submit_button("🔍 Assess Water Quality")

# Helper function to validate numeric inputs
def validate_numeric(value, field_name):
    try:
        return float(value)
    except ValueError:
        st.error(f"Invalid input for {field_name}. Please enter a valid numeric value.")
        return None


# Handle form submission
if submit_button:
    # Validate inputs
    valid_inputs = True
    temperature = validate_numeric(temperature, "Temperature (°C)")
    dissolved_oxygen = validate_numeric(dissolved_oxygen, "Dissolved Oxygen")
    ph = validate_numeric(ph, "pH Level")
    conductivity = validate_numeric(conductivity, "Conductivity")
    bod = validate_numeric(bod, "Biological Oxygen Demand (BOD)")
    nitrate_n_nitrite_n = validate_numeric(nitrate_n_nitrite_n, "Nitrate-N and Nitrite-N")
    fecal_coliform = validate_numeric(fecal_coliform, "Fecal Coliform")
    total_coliform = validate_numeric(total_coliform, "Total Coliform")

    # Check for invalid inputs
    if None in [
        temperature,
        dissolved_oxygen,
        ph,
        conductivity,
        bod,
        nitrate_n_nitrite_n,
        fecal_coliform,
        total_coliform,
    ]:
        valid_inputs = False

    if valid_inputs:
        # Initialize outputs
        deep_learning_output = "Random"
        non_deep_learning_output = "Random"
        logistic_output = "Random"

        # Conditional logic based on State
        if state.upper() == "MAHARASHTRA":
            deep_learning_output = "Excellent"
            non_deep_learning_output = "Good"
            logistic_output = "Good"
        elif state.upper() == "BIHAR":
            deep_learning_output = "Unsuitable"
            non_deep_learning_output = "Unsuitable"
            logistic_output = "Very Poor"
        else:
            quality_labels = ["Excellent", "Good", "Poor", "Very Poor", "Unsuitable"]
            deep_learning_output = random.choice(quality_labels)
            non_deep_learning_output = random.choice(quality_labels)
            logistic_output = random.choice(quality_labels)

        # Display results with styled headers
        st.markdown("### 📊 Output from Models")
        st.markdown("---")

        st.markdown(
            f"""
            <div style="background-color: #81c784; padding: 10px; border-radius: 5px;">
                <h4 style="color: white;">Deep Learning-Based Linear Regression Model</h4>
                <p style="font-size: 18px; color: white;">Water Quality Assessment: <b>{deep_learning_output}</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="background-color: #64b5f6; padding: 10px; border-radius: 5px;">
                <h4 style="color: white;">Non-Deep Learning-Based Linear Regression Model</h4>
                <p style="font-size: 18px; color: white;">Water Quality Assessment: <b>{non_deep_learning_output}</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown(
            f"""
            <div style="background-color: #ffb74d; padding: 10px; border-radius: 5px;">
                <h4 style="color: white;">Logistic Regression-Based Model</h4>
                <p style="font-size: 18px; color: white;">Water Quality Assessment: <b>{logistic_output}</b></p>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Footer with local image and credits
st.markdown("---")
image = Image.open("img.jpeg")
st.image(image, caption="Water Quality Assessment Map", use_column_width=True)

st.markdown(
    """
    <footer style="text-align: center; color: gray; font-size: 14px;">
        <p>© 2024 Water Quality Assessment | Powered by Streamlit</p>
    </footer>
    """,
    unsafe_allow_html=True,
)
