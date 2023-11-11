import streamlit as st
import requests
import hashlib

# Dictionary to store user credentials
user_credentials = {"admin": "password"}  # Add more users if needed

# Dictionary to store the mapping between phone numbers and patient IDs
phone_number_to_patient_id = {}

# Sample survey data for testing
sample_survey_data = {
    "full_name": "John Doe",
    "phone_number": "1234567890",
    "shortness_of_breath": True,
    "persistent_cough": False,
    # Add more survey data...
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
    # For testing purposes, return sample_survey_data
    return sample_survey_data

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
    st.title("Respiratory Health Survey")

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
        for key, value in detailed_data.items():
            if isinstance(value, bool):
                st.write(f"{key.replace('_', ' ').title()}: {value}")

        # Recommendation
        st.subheader("Recommendation")
        st.write(recommendation(detailed_data))

if __name__ == "__main__":
    main()
