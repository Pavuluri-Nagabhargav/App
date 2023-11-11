import streamlit as st

def main():
    st.title("Respiratory Health Survey")

    # Add background image
    background_image_url = "https://images.theconversation.com/files/485402/original/file-20220919-12-mtp5y0.jpg?ixlib=rb-1.1.0&rect=0%2C0%2C2944%2C2036&q=45&auto=format&w=926&fit=clip"
    st.markdown(
        f'<style>body{{background-image: url("{background_image_url}");background-size: cover;}}</style>',
        unsafe_allow_html=True
    )

    # Full Name and Phone Number
    st.header("Personal Information")
    full_name = st.text_input("Full Name:")
    phone_number = st.text_input("Phone Number:")

    # Symptom-Related Questions
    st.header("Symptom-Related Questions")
    shortness_of_breath = st.checkbox("Have you been experiencing shortness of breath?")
    if shortness_of_breath:
        physical_activity = st.checkbox("Does it occur or worsen with physical activity?")

    persistent_cough = st.checkbox("Do you have a persistent cough?")
    if persistent_cough:
        cough_type = st.radio("Is it dry or productive (producing mucus)?", ["Dry", "Productive"])
        if cough_type == "Productive":
            mucus_production = st.checkbox("Have you noticed an increase in mucus production?")
            if mucus_production:
                mucus_color = st.text_input("What is the color of the mucus?")
                mucus_consistency = st.text_input("What is the consistency of the mucus?")

    respiratory_infections = st.checkbox("Are you experiencing frequent respiratory infections?")
    chest_symptoms = st.checkbox("Do you have wheezing or chest tightness?")

    # History of Smoking
    st.header("History of Smoking")
    smoked_before = st.checkbox("Have you ever smoked?")
    if smoked_before:
        smoking_duration = st.number_input("For how long did you smoke? (in years)")
        cigarettes_per_day = st.number_input("How many cigarettes per day did you smoke?")
        former_smoker = st.checkbox("Are you a former smoker?")
        if former_smoker:
            quit_date = st.date_input("When did you quit smoking?")

        secondhand_smoke = st.checkbox("Are you exposed to secondhand smoke?")

    # Occupational and Environmental Exposure
    st.header("Occupational and Environmental Exposure")
    workplace_exposure = st.checkbox("Are you exposed to dust, chemicals, fumes, or other irritants at your workplace?")
    air_pollution = st.checkbox("Do you live in an area with high air pollution?")

    # Family History
    st.header("Family History")
    family_history = st.checkbox("Is there a history of COPD or other chronic respiratory diseases in your family?")

    # Lifestyle and Daily Impact
    st.header("Lifestyle and Daily Impact")
    daily_activities = st.text_area("How do your symptoms affect your daily activities and quality of life?")
    regular_activities = st.checkbox("Are you able to perform regular activities without becoming short of breath?")
    weight_loss_weakness = st.checkbox("Have you noticed any weight loss or muscle weakness?")

    # Previous Health Issues
    st.header("Previous Health Issues")
    lung_problems = st.checkbox("Have you had any previous lung problems, such as asthma, bronchitis, or pneumonia?")
    other_health_conditions = st.text_area("Do you have any other health conditions, especially heart disease or hypertension?")

    # Medication and Treatment History
    st.header("Medication and Treatment History")
    current_medications = st.text_area("Are you currently taking any medications, including inhalers or other treatments for breathing problems?")
    treatments_surgeries = st.text_area("Have you undergone any treatments or surgeries that might affect your lungs?")

    # Symptom Onset and Progression
    st.header("Symptom Onset and Progression")
    symptom_onset_date = st.date_input("When did you first notice your symptoms?")
    symptom_progression = st.checkbox("Have your symptoms been getting worse over time?")

    # Allergies
    st.header("Allergies")
    respiratory_allergies = st.text_area("Do you have any allergies that might affect your respiratory system?")

    # Save Survey Response
    if st.button("Submit Survey"):
        save_survey_response(locals())

if __name__ == "__main__":
    main()
