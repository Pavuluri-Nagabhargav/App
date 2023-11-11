import streamlit as st
import requests
import hashlib

# Dictionary to store user credentials
user_credentials = {"admin": "password"}  # Add more users if needed

# Dictionary to store the mapping between phone numbers and patient IDs
phone_number_to_patient_id = {}

# Sample survey data for testing
sample_survey_data_yes = {
    "full_name": "Sai",
    "phone_number": "8888888888",
    "shortness_of_breath": True,
    "physical_activity": True,
    "persistent_cough": True,
    "cough_type": "Productive",
    "mucus_production": True,
    "mucus_color": "Yellow",
    "mucus_consistency": "Thick",
    "respiratory_infections": True,
    "chest_symptoms": True,
    "smoked_before": True,
    "smoking_duration": 10,
    "cigarettes_per_day": 5,
    "former_smoker": True,
    "quit_date": "2021-01-01",
    "secondhand_smoke": True,
    "workplace_exposure": True,
    "air_pollution": True,
    "family_history": True,
    "daily_activities": "Shortness of breath affects daily activities.",
    "regular_activities": False,
    "weight_loss_weakness": True,
    "lung_problems": True,
    "other_health_conditions": "Hypertension",
    "current_medications": "Inhaler",
    "treatments_surgeries": "None",
    "symptom_onset_date": "2022-01-15",
    "symptom_progression": True,
    "respiratory_allergies": "Pollen"
}

sample_survey_data_no = {
    "full_name": "Bhargav",
    "phone_number": "9999999999",
    "shortness_of_breath": False,
    "physical_activity": False,
    "persistent_cough": False,
    "cough_type": "",
    "mucus_production": False,
    "mucus_color": "",
    "mucus_consistency": "",
    "respiratory_infections": False,
    "chest_symptoms": False,
    "smoked_before": False,
    "smoking_duration": 0,
    "cigarettes_per_day": 0,
    "former_smoker": False,
    "quit_date": "",
    "secondhand_smoke": False,
    "workplace_exposure": False,
    "air_pollution": False,
    "family_history": False,
    "daily_activities": "",
    "regular_activities": True,
    "weight_loss_weakness": False,
    "lung_problems": False,
    "other_health_conditions": "",
    "current_medications": "",
    "treatments_surgeries": "",
    "symptom_onset_date": "",
    "symptom_progression": False,
    "respiratory_allergies": ""
}

def generate_patient_id(phone_number):
    # Use a hash function to generate a unique patient ID based on the phone number
    hash_object = hashlib.md5(phone_number.encode())
    return hash_object.hexdigest()

def authenticate(username, password):
    # Fixed login credentials (admin/password)
    return user_credentials.get(username) == password

def fetch_survey_data(patient_id):
    # Placeholder for fetching detailed survey data based on patient ID
    # For testing purposes, return sample_survey_data_yes or sample_survey_data_no
    return sample_survey_data_yes if patient_id == phone_number_to_patient_id.get("8888888888") else sample_survey_data_no

def recommendation(survey_data):
    # Placeholder logic for generating a recommendation
    # Customize this based on your actual recommendation criteria
    yes_count = sum(value for key, value in survey_data.items() if isinstance(value, bool) and value)
    total_questions = sum(isinstance(value, bool) for value in survey_data.values())

    if yes_count / total_questions > 0.5:
        return "Need further respiratory tests"
    else:
        return "Consider for general medication"

def main():
    st.title("Lung Assist System")  # Updated title

    # Login
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    login_button = st.sidebar.button("Login")
    if login_button:
        if authenticate(username, password):
            st.sidebar.success("Logged in successfully!")
            st.session_state.logged_in = True
            st.session_state.current_user = username  # Store the current username in session state
        else:
            st.sidebar.error("Incorrect credentials")

    if not st.session_state.get('logged_in', False):
        st.warning("Please log in to access the survey reports.")
        return

    # Display patient reports folder
    st.header("Patient Reports Folder")
    for patient_id, name in phone_number_to_patient_id.items():
        st.write(f"Patient ID: {patient_id}, Name: {name}")

    # View Survey Reports
    st.sidebar.subheader("Survey Reports")
    selected_id = st.sidebar.selectbox("Select Patient ID", list(phone_number_to_patient_id.keys()))
    if selected_id:
        # Retrieve and display detailed survey data based on the selected patient ID
        detailed_data = fetch_survey_data(selected_id)
        st.subheader(f"Survey Report for Patient ID: {selected_id}")
        st.write(f"Name: {detailed_data.get('full_name', 'N/A')}")
                st.write(f"Phone Number: {detailed_data.get('phone_number', 'N/A')}")
        st.write(f"Patient ID: {selected_id}")

        # Display other survey details...
        st.header("Symptom-Related Questions:")
        st.write(f"Have you been experiencing shortness of breath? {'Yes' if detailed_data.get('shortness_of_breath', False) else 'No'}")
        if detailed_data.get('shortness_of_breath', False):
            st.write(f"If yes, does it occur or worsen with physical activity? {'Yes' if detailed_data.get('physical_activity', False) else 'No'}")
        st.write(f"Do you have a persistent cough? {'Yes' if detailed_data.get('persistent_cough', False) else 'No'}")
        if detailed_data.get('persistent_cough', False):
            st.write(f"Is it dry or productive (producing mucus)? {detailed_data.get('cough_type', 'N/A')}")
            if detailed_data.get('cough_type') == "Productive":
                st.write(f"Have you noticed an increase in mucus production? {'Yes' if detailed_data.get('mucus_production', False) else 'No'}")
                if detailed_data.get('mucus_production', False):
                    st.write(f"What is the color of the mucus? {detailed_data.get('mucus_color', 'N/A')}")
                    st.write(f"What is the consistency of the mucus? {detailed_data.get('mucus_consistency', 'N/A')}")
        st.write(f"Are you experiencing frequent respiratory infections? {'Yes' if detailed_data.get('respiratory_infections', False) else 'No'}")
        st.write(f"Do you have wheezing or chest tightness? {'Yes' if detailed_data.get('chest_symptoms', False) else 'No'}")

        st.header("History of Smoking:")
        st.write(f"Have you ever smoked? {'Yes' if detailed_data.get('smoked_before', False) else 'No'}")
        if detailed_data.get('smoked_before', False):
            st.write(f"For how long did you smoke? {detailed_data.get('smoking_duration', 0)} years")
            st.write(f"How many cigarettes per day did you smoke? {detailed_data.get('cigarettes_per_day', 0)}")
            st.write(f"Are you a former smoker? {'Yes' if detailed_data.get('former_smoker', False) else 'No'}")
            if detailed_data.get('former_smoker', False):
                st.write(f"When did you quit smoking? {detailed_data.get('quit_date', 'N/A')}")
            st.write(f"Are you exposed to secondhand smoke? {'Yes' if detailed_data.get('secondhand_smoke', False) else 'No'}")

        # Display other survey details...
        # Include the remaining questions in a similar fashion

        # Provide recommendation
        st.header("Recommendation")
        st.write(recommendation(detailed_data))

if __name__ == "__main__":
    main()
