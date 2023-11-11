import streamlit as st
import requests
import hashlib

# Dictionary to store user credentials
user_credentials = {}

# Dictionary to store the mapping between phone numbers and patient IDs
phone_number_to_patient_id = {}

def generate_patient_id(phone_number):
    # Use a hash function to generate a unique patient ID based on the phone number
    hash_object = hashlib.md5(phone_number.encode())
    return hash_object.hexdigest()

def create_account(username, password):
    # Store user credentials in the dictionary
    user_credentials[username] = {'password': password}

def authenticate(username, password):
    # Authenticate user credentials
    user_info = user_credentials.get(username)
    return user_info and user_info['password'] == password

def fetch_survey_data(patient_id):
    # Placeholder for fetching detailed survey data based on patient ID
    # You need to implement this method to fetch data from your server
    api_url = f"https://lungassist.streamlit.app/api/patient/{patient_id}"  # Replace with the actual API endpoint
    response = requests.get(api_url)
    detailed_data = response.json() if response.status_code == 200 else {}
    return detailed_data

def main():
    st.title("Respiratory Health Survey")

    # Account creation
    st.sidebar.header("Create Account")
    new_username = st.sidebar.text_input("New Username")
    new_password = st.sidebar.text_input("New Password", type="password", key="new_password")

    if st.sidebar.button("Create Account"):
        create_account(new_username, new_password)
        st.sidebar.success("Account created successfully! You can now log in.")

    # Login
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    login_attempted = st.sidebar.button("Login")
    if login_attempted:
        if authenticate(username, password):
            st.sidebar.success("Logged in successfully!")
            st.session_state.logged_in = True
            st.session_state.current_user = username  # Store the current username in session state
        else:
            st.sidebar.error("Incorrect credentials")

    if not st.session_state.get('logged_in', False):
        st.warning("Please log in to access the survey reports.")
        return

    # Survey form goes here...
    # ...

    # View Survey Reports
    st.sidebar.subheader("Survey Reports")
    selected_id = st.sidebar.selectbox("Select Patient ID", list(phone_number_to_patient_id.values()))
    if selected_id:
        # Retrieve and display detailed survey data based on the selected patient ID
        detailed_data = fetch_survey_data(selected_id)
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
