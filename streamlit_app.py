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
        "persistent_cough": data.get("persistent_cough", False),
        "cough_type": data.get("cough_type", ""),
        "mucus_production": data.get("mucus_production", False),
        "mucus_color": data.get("mucus_color", ""),
        "mucus_consistency": data.get("mucus_consistency", ""),
        "respiratory_infections": data.get("respiratory_infections", False),
        "chest_symptoms": data.get("chest_symptoms", False),
        "smoked_before": data.get("smoked_before", False),
        "smoking_duration": data.get("smoking_duration", 0),
        "cigarettes_per_day": data.get("cigarettes_per_day", 0),
        "former_smoker": data.get("former_smoker", False),
        "quit_date": str(data.get("quit_date", "")),
        "secondhand_smoke": data.get("secondhand_smoke", False),
        "workplace_exposure": data.get("workplace_exposure", False),
        "air_pollution": data.get("air_pollution", False),
        "family_history": data.get("family_history", False),
        "daily_activities": data.get("daily_activities", ""),
        "regular_activities": data.get("regular_activities", False),
        "weight_loss_weakness": data.get("weight_loss_weakness", False),
        "lung_problems": data.get("lung_problems", False),
        "other_health_conditions": data.get("other_health_conditions", ""),
        "current_medications": data.get("current_medications", ""),
        "treatments_surgeries": data.get("treatments_surgeries", ""),
        "symptom_onset_date": str(data.get("symptom_onset_date", "")),
        "symptom_progression": data.get("symptom_progression", False),
        "respiratory_allergies": data.get("respiratory_allergies", "")
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
    post_url = "https://lungassist-user.streamlit.app/{patient_id}/submit_surve"
    response = requests.post(post_url, json=relevant_data)

    if response.status_code == 200:
        try:
            response_json = response.json()
            patient_id = response_json.get('patient_id')
            if patient_id is not None:
                st.success(f"Survey submitted successfully! Patient ID: {patient_id}")
            else:
                st.error("Failed to retrieve Patient ID from the response.")
        except ValueError:
            st.error("Error decoding JSON response: The response is not a valid JSON.")
            st.text(response.text)  # Display the raw response for further analysis
    else:
        st.error(f"Failed to submit survey. Status Code: {response.status_code}")
        st.text(response.text)  # Display the raw response for further analysis

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
        response = save_survey_response(locals())
        
        if response.status_code == 200:
            try:
                response_json = response.json()
                patient_id = response_json.get('patient_id')
                if patient_id is not None:
                    st.success(f"Survey submitted successfully! Patient ID: {patient_id}")
                else:
                    st.error("Failed to retrieve Patient ID from the response.")
            except Exception as e:
                st.error(f"Error decoding JSON response: {e}")
                st.text(response.text)  # Display the raw response for further analysis
        else:
            st.error(f"Failed to submit survey. Status Code: {response.status_code}")
            st.text(response.text)  # Display the raw response for further analysis

if __name__ == "__main__":
    main()



