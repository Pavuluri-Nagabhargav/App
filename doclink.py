
import streamlit as st
import requests
import hashlib

# Dictionary to store the mapping between phone numbers and patient IDs
phone_number_to_patient_id = {}
login_credentials = {'username': 'admin', 'password': 'password'}

def generate_patient_id(phone_number):
    # Use a hash function to generate a unique patient ID based on the phone number
    hash_object = hashlib.md5(phone_number.encode())
    return hash_object.hexdigest()

def save_survey_response(data):
    phone_number = data["phone_number"]
    if phone_number not in phone_number_to_patient_id:
        # If the phone number is not in the dictionary, generate a new patient ID
        patient_id = generate_patient_id(phone_number)
        phone_number_to_patient_id[phone_number] = patient_id
    else:
        # If the phone number is already in the dictionary, retrieve the existing patient ID
        patient_id = phone_number_to_patient_id[phone_number]

    data["patient_id"] = patient_id
    # Assuming you have a URL where you want to send the survey responses
    post_url = "https://lungassist-user.streamlit.app/survey_endpoint"
    response = requests.post(post_url, json=data)
    return response

def authenticate(username, password):
    return username == login_credentials['username'] and password == login_credentials['password']

def main():
    st.title("Respiratory Health Survey")

    # Login
    login_attempted = st.sidebar.button("Login")
    if login_attempted:
        username = st.sidebar.text_input("Username")
        password = st.sidebar.text_input("Password", type="password")
        if authenticate(username, password):
            st.sidebar.success("Logged in successfully!")
            st.experimental_session_state.logged_in = True
        else:
            st.sidebar.error("Invalid credentials")

    if not hasattr(st.experimental_session_state, 'logged_in') or not st.experimental_session_state.logged_in:
        st.warning("Please log in to access the survey reports.")
        return

    # Survey form goes here...
    # ...

    # View Survey Reports
    st.sidebar.subheader("Survey Reports")
    selected_id = st.sidebar.selectbox("Select Patient ID", list(phone_number_to_patient_id.values()))
    if selected_id:
        # Retrieve and display detailed survey data based on the selected patient ID
        # You need to implement a method to fetch the survey data for the selected patient ID from your server
        detailed_data = {}  # Implement a method to fetch data based on patient ID
        st.subheader(f"Survey Report for Patient ID: {selected_id}")
        st.write(f"Name: {detailed_data.get('full_name', 'N/A')}")
        st.write(f"Phone Number: {detailed_data.get('phone_number', 'N/A')}")
        st.write(f"Patient ID: {selected_id}")
        # Display other survey details...

        # Check important questions and provide recommendation
        if detailed_data.get('shortness_of_breath', False) or detailed_data.get('persistent_cough', False):
            st.warning("Patient requires further diagnostic tests.")
        else:
            st.success("Patient might need general medication.")

if __name__ == "__main__":
    main()
