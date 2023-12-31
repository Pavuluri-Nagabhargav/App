import streamlit as st
import pandas as pd
import time

# Mock database to store patient details
patients_db = {
    "0001": {
        "full_name": "Sai",
        "phone_number": "8888888888",
        "shortness_of_breath": True,
        "physical_activity": False,
        "persistent_cough": True,
        "cough_type": "Productive",
        "mucus_production": True,
        "mucus_color": "Yellow",
        "mucus_consistency": "Thick",
        "H_issue": True,
        "Smoke": False,
        # ... (include other survey details)
    },
    "0002": {
        "full_name": "Bhargav",
        "phone_number": "9999999999",
        "shortness_of_breath": False,
        "physical_activity": False,
        "persistent_cough": False,
        "cough_type": "",
        "mucus_production": True,
        "mucus_color": "",
        "mucus_consistency": "",
        "H_issue": False,
        "Smoke": True,
        # ... (include other survey details)
    },
}

def recommendation(patient_data):
    # Your recommendation logic based on survey answers
    # This is a placeholder, adjust it according to your requirements
    yes_count = sum(value for key, value in patient_data.items() if isinstance(value, bool) and value)
    total_questions = sum(isinstance(value, bool) for value in patient_data.values())

    if yes_count / total_questions > 0.5:
        return "Need further respiratory tests"
    else:
        return "Consider for general medication"

def upload_test_results():
    st.header("Upload Test Results")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    upload_status = st.empty()

    if uploaded_file is not None:

        try:
            df = pd.read_csv(uploaded_file)
            st.success("File uploaded successfully!")
            st.write("Please wait until we process the data.........")
            time.sleep(5)  # Simulating processing time

            # Display COPD Status
            st.subheader("COPD Status")
            st.write("Results: **Stage 2**")

            # Display Recommendation Box
            st.subheader("Recommendation Details")
            st.write("Medications:")
            st.write("- **Bronchodilators:**")
            st.write("  - Short-acting (albuterol) for immediate relief.")
            st.write("  - Long-acting (tiotropium, salmeterol) for sustained relief.")
            st.write("- **Inhaled Corticosteroids:**")
            st.write("  - Reduce airway inflammation (fluticasone, budesonide).")

            st.write("Exercise:")
            st.write("- **Pulmonary Rehabilitation:**")
            st.write("  - Supervised program for improved capacity and symptom relief.")
            st.write("- **Aerobic Exercise:**")
            st.write("  - Walking, cycling, swimming for cardiovascular health.")

            st.write("Lifestyle Modifications:")
            st.write("- **Smoking Cessation:**")
            st.write("  - Quit smoking to slow progression.")
            st.write("- **Avoid Irritants:**")
            st.write("  - Minimize exposure to pollutants.")

        except Exception as e:
            st.error(f"Error processing CSV file: {e}")
            upload_status.empty()
    else:
        st.warning("Please choose a CSV file.")

def main():
    st.title("Lung Assist System")

    # Login
    st.sidebar.header("Login")
    username = st.sidebar.text_input("Username")
    password = st.sidebar.text_input("Password", type="password")

    login_button = st.sidebar.button("Login")
    if login_button:
        if username == "admin" and password == "password":
            st.sidebar.success("Logged in successfully!")
            st.session_state.logged_in = True
            st.session_state.current_user = username  # Store the current username in session state
        else:
            st.sidebar.error("Incorrect credentials")

    if not st.session_state.get('logged_in', False):
        st.warning("Please log in to access the patient reports.")
        st.header("Overview")
        st.write("""
        Lung Assist System is committed to transforming respiratory healthcare, In our mission to advance respiratory healthcare, we are developing a product to facilitate early diagnosis of Chronic Obstructive Pulmonary Disease (COPD). 
        Our primary focus is on collaborating with rural clinics, empowering them with a subscription-based service. These clinics, often lacking respiratory specialists, can leverage our KIOSK system to conduct initial patient surveys. The gathered data is securely stored in a dedicated physician's account, provided as part of the subscription.

        The process involves analyzing patient symptoms to offer timely recommendations for advanced tests. This proactive approach enables patients to undergo necessary examinations without enduring prolonged waits for specialty appointments. Once recommended, patients can upload their test reports through our portal. These reports serve as inputs for our advanced machine learning and AI models, predicting the likelihood of COPD and its stages.

        Our ultimate goal is to provide early intervention, saving patients valuable time and ensuring timely treatment before the disease progresses to more severe stages.
        """)

        return

    # Display patient reports folder
    st.header("Patient Reports Folder")
    selected_id = st.selectbox("Please select a patient ID", [""] + list(patients_db.keys()))
    if selected_id and selected_id != "":
        # Retrieve and display detailed survey data based on the selected patient ID
        detailed_data = patients_db[selected_id]
        st.subheader(f"Survey Report for Patient ID: {selected_id}")
        st.write(f"Name: {detailed_data.get('full_name', 'N/A')}")
        st.write(f"Phone Number: {detailed_data.get('phone_number', 'N/A')}")

        # Display other survey details...
        st.header("Symptom-Related Questions:")
        st.write(f"Shortness of Breath: {detailed_data.get('shortness_of_breath', 'N/A')}")
        st.write(f"Physical Activity: {detailed_data.get('physical_activity', 'N/A')}")
        st.write(f"Persistent Cough: {detailed_data.get('persistent_cough', 'N/A')}")
        st.write(f"Cough Type: {detailed_data.get('cough_type', 'N/A')}")
        st.write(f"Mucus Production: {detailed_data.get('mucus_production', 'N/A')}")
        st.write(f"Mucus Color: {detailed_data.get('mucus_color', 'N/A')}")
        st.write(f"Mucus Consistency: {detailed_data.get('mucus_consistency', 'N/A')}")
        st.write(f"Hereditary Issues: {detailed_data.get('H_issue', 'N/A')}")
        st.write(f"Smoking Habit: {detailed_data.get('Smoke', 'N/A')}")

        # Provide recommendation using st.expander
        recommendation_text = recommendation(detailed_data)
        st.subheader("Recommendation Details")
        st.write(recommendation_text)
        if recommendation_text == "Need further respiratory tests":
            upload_test_results()

if __name__ == "__main__":
    main()
