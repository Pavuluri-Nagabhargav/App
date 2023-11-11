import streamlit as st
from typing import Dict, Any

# Mock database to store patient details
patients_db: Dict[str, Dict[str, Any]] = {
    "patient1": {
        "full_name": "Sai",
        "phone_number": "8888888888",
        "shortness_of_breath": True,
        "physical_activity": True,
        # ... (include other survey details)
    },
    "patient2": {
        "full_name": "Bhargav",
        "phone_number": "9999999999",
        "shortness_of_breath": False,
        "physical_activity": False,
        # ... (include other survey details)
    },
}

def recommendation(patient_data: Dict[str, Any]) -> str:
    # Your recommendation logic based on survey answers
    # This is a placeholder, adjust it according to your requirements
    true_count = sum(value for key, value in patient_data.items() if isinstance(value, bool) and value)
    if true_count >= 10:
        return "Need further respiratory tests."
    else:
        return "Consider for general medication."

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
        return

    # View Patient Reports
    st.sidebar.subheader("Patient Reports")
    selected_patient_id = st.sidebar.selectbox("Select Patient ID", list(patients_db.keys()))
    if selected_patient_id:
        # Retrieve and display detailed survey data based on the selected patient ID
        detailed_data = patients_db[selected_patient_id]
        st.subheader(f"Patient Report for Patient ID: {selected_patient_id}")
        st.write(f"Name: {detailed_data.get('full_name', 'N/A')}")
        st.write(f"Phone Number: {detailed_data.get('phone_number', 'N/A')}")

        # Display other survey details...
        st.header("Symptom-Related Questions:")
        st.write(f"Shortness of Breath: {detailed_data.get('shortness_of_breath', 'N/A')}")
        st.write(f"Physical Activity: {detailed_data.get('physical_activity', 'N/A')}")
        # ... (include other survey details)

        # Provide recommendation
        st.header("Recommendation")
        st.write(recommendation(detailed_data))

if __name__ == "__main__":
    main()
