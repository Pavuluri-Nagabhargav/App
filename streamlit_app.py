import streamlit as st
from PIL import Image

def welcome_screen():
    try:
        image_url = "https://raw.githubusercontent.com/Pavuluri-Nagabhargav/App/main/image_720.png"
        st.image(image, caption='Your image caption', use_column_width=True)
    except Exception as e:
        st.error(f"Error opening the image: {e}")
        return
    #image = Image.open(r'C:\Users\nagab\Downloads\image_720.png')

    #st.image(image, caption='Your image caption', use_column_width=True)
    st.title("Welcome to Lung Assist Respiratory Survey")
    st.write(
"""This survey is designed to gather information about your respiratory health.
        Your participation is important for research and to enhance respiratory care.
        Please click the "Next" button to proceed to the survey.""")

    if "next_button_clicked" not in st.session_state:
        st.session_state.next_button_clicked = False

    next_button = st.button("Next")

    if next_button:
        st.session_state.next_button_clicked = True

    if st.session_state.next_button_clicked:
        st.empty()  # Clear the entire screen
        survey_page()

def survey_page():
    st.title("Respiratory Health Survey")
    # Full Name and Phone Number
    st.header("Personal Information")
    full_name = st.text_input("Full Name:")
    phone_number = st.text_input("Phone Number:")
  # Symptom-Related Questions
    st.header("Symptom-Related Questions")
    shortness_of_breath = st.checkbox("Have you been experiencing shortness of breath?")
    physical_activity = False  # Initialize to False
    if shortness_of_breath:
        physical_activity = st.checkbox("Does it occur or worsen with physical activity?")
    persistent_cough = st.checkbox("Do you have a persistent cough?")
    cough_type = ""  # Initialize to an empty string
    mucus_production = False  # Initialize to False
    mucus_color = ""  # Initialize to an empty string
    mucus_consistency = ""  # Initialize to an empty string
    if persistent_cough:
        cough_type = st.radio("Is it dry or productive (producing mucus)?", ["Dry", "Productive"])
        if cough_type == "Productive":
          mucus_production = st.checkbox("Have you noticed an increase in mucus production?")
          if mucus_production:
            mucus_color = st.text_input("What is the color of the mucus?")
            mucus_consistency = st.text_input("What is the consistency of the mucus?")
    respiratory_infections = st.checkbox("Are you experiencing frequent respiratory infections?")
    chest_symptoms = st.checkbox("Do you have wheezing or chest tightness?")
    st.header("History of Smoking")
    smoked_before = st.checkbox("Have you ever smoked?")
    smoking_duration = 0  # Initialize to 0
    cigarettes_per_day = 0  # Initialize to 0
    former_smoker = False  # Initialize to False
    quit_date = ""  # Initialize to an empty string
    secondhand_smoke = False  # Initialize to False
    if smoked_before:
        smoking_duration = st.number_input("For how long did you smoke? (in years)")
        cigarettes_per_day = st.number_input("How many cigarettes per day did you smoke?")
        former_smoker = st.checkbox("Are you a former smoker?")
        if former_smoker:
            quit_date = st.date_input("When did you quit smoking?")
        secondhand_smoke = st.checkbox("Are you exposed to secondhand smoke?")
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

    # Your survey questions and form go here...

    if st.button("Submit Survey"):
        st.session_state.next_button_clicked = False  # Reset the button state
        st.empty()  # Clear the entire screen
        st.success("""
        Your respiratory survey has been successfully submitted. Thank you!""")
        

def main():
    welcome_screen()

if __name__ == "__main__":
    main()
