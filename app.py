import streamlit as st
import pandas as pd
# Import your classes from your script (assuming it's named prediction_logic.py)
from src.pipeline.predict_pipeline import PredictPipeline, CustomData 

# 1. App Header
st.set_page_config(page_title="Student Performance Predictor")
st.title("🎓 Student Math Score Predictor")
st.markdown("Fill in the student details below to estimate their math score.")

# 2. Input Form
with st.form("student_data_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        gender = st.selectbox("Gender", ["female", "male"])
        race_ethnicity = st.selectbox("Race/Ethnicity", ["group A", "group B", "group C", "group D", "group E"])
        parental_level_of_education = st.selectbox("Parental Education", [
            "some high school", "high school", "some college", 
            "associate's degree", "bachelor's degree", "master's degree"
        ])
        lunch = st.selectbox("Lunch Type", ["standard", "free/reduced"])

    with col2:
        test_preparation_course = st.selectbox("Test Preparation Course", ["none", "completed"])
        reading_score = st.number_input("Reading Score", min_value=0, max_value=100, value=70)
        writing_score = st.number_input("Writing Score", min_value=0, max_value=100, value=70)

    # Submit button
    submitted = st.form_submit_button("Predict Math Score")

# 3. Prediction Logic
if submitted:
    # Initialize CustomData with inputs
    student_data = CustomData(
        gender=gender,
        race_ethnicity=race_ethnicity,
        parental_level_of_education=parental_level_of_education,
        lunch=lunch,
        test_preparation_course=test_preparation_course,
        reading_score=reading_score,
        writing_score=writing_score
    )

    # Convert to DataFrame using your method
    final_df = student_data.get_data_as_data_frame()
    
    # Display the processed input for verification
    st.subheader("Student Profile Data")
    st.dataframe(final_df)

    # Run the Prediction Pipeline
    try:
        pipeline = PredictPipeline()
        prediction = pipeline.predict(final_df)
        
        # Display Results
        st.success(f"### Predicted Math Score: **{prediction[0]:.2f}**")
    except Exception as e:
        st.error(f"Error during prediction: {e}")
