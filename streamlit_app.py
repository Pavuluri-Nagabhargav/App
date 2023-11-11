import streamlit as st
import requests
import hashlib

# Dictionary to store the mapping between phone numbers and patient IDs
phone_number_to_patient_id = {}

def generate_patient_id(phone_number):
    # Use a hash function to generate a unique patient ID based on the phone number
    hash_object = hashlib.md5(phone_number.encode())
    return hash_object.hexdigest()

def save_survey_response(data):
    relevant_data = {
        "full_name": data["full_name"],
        "phone_number": data["phone_number"],
        "shortness_of_breath": data.get("shortness_of_breath", False),
        "physical_activity": data.get("physical_activity", False),
        # ... (rest of your data)
    }

    phone_number = data["phone_number"]
    if phone_number not in phone_number_to_patient_id:
        # If the phone number is not in the dictionary, generate a new patient ID
        patient_id = generate_patient_id(phone_number)
        phone_number_to_patient_id[phone_number] = patient_id
    else:
        # If the phone number is already in the dictionary, retrieve the existing patient ID
        patient_id = phone_number_to_patient_id[phone_number]

    relevant_data["patient_id"] = patient_id

    # Assuming you have a URL where you want to send the survey responses
    post_url = f"https://lungassist-user.streamlit.app/{patient_id}/submit_survey"
    response = requests.post(post_url, json=relevant_data)

    if response.status_code == 200:
        try:
            response_json = response.json()
            if isinstance(response_json, dict):  # Check if the response is a JSON object
                patient_id = response_json.get('patient_id')
                if patient_id is not None:
                    st.success(f"Survey submitted successfully! Patient ID: {patient_id}")
                else:
                    st.error("Failed to retrieve Patient ID from the response.")
            else:
                st.error("Invalid JSON response: The response is not a JSON object.")
                st.text(response.text)  # Display the raw response for further analysis
        except ValueError as e:
            st.error(f"Error decoding JSON response: {e}")
            st.text(response.text)  # Display the raw response for further analysis
    else:
        st.error(f"Failed to submit survey. Status Code: {response.status_code}")
        st.text(response.text)  # Display the raw response for further analysis

def welcome_screen():
    st.title("Welcome to Lung Assist Respiratory Survey")
    
    st.markdown("""
        This survey is designed to gather information about your respiratory health.
        Your participation is important for research and to enhance respiratory care.
        Please click the "Next" button to proceed to the survey.
    """)
    
    if st.button("Next"):
        st.empty()  # Clear the screen
        main()

def main():
    st.title("Respiratory Health Survey")

    # Full Name and Phone Number
    full_name = st.text_input("Full Name:")
    phone_number = st.text_input("Phone Number:")

    # Save Survey Response
    if st.button("Submit Survey"):
        survey_data = {
            "full_name": full_name,
            "phone_number": phone_number,
            # ... (add more survey questions)
        }

        save_survey_response(survey_data)

        # Clear the screen and show success message
        st.success("Your respiratory survey has been successfully updated. Thank you!")

def run_survey():
    welcome_screen()

if __name__ == "__main__":
    run_survey()
