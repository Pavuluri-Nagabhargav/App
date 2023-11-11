import streamlit as st
import pandas as pd

# Create a DataFrame to store survey responses
survey_data = pd.DataFrame(columns=["Question", "Response"])

# Symptom-Related Questions
st.header("Symptom-Related Questions")

# Function to add responses to the DataFrame
def add_response(question, response):
    survey_data.loc[len(survey_data)] = [question, response]

# Question 1
shortness_of_breath = st.checkbox("Have you been experiencing shortness of breath?")
if shortness_of_breath:
    physical_activity = st.checkbox("Does it occur or worsen with physical activity?")
    add_response("Shortness of Breath", f"Yes ({'with physical activity' if physical_activity else 'without physical activity'})")
else:
    add_response("Shortness of Breath", "No")

# Question 2
persistent_cough = st.checkbox("Do you have a persistent cough?")
if persistent_cough:
    cough_type = st.radio("Is it dry or productive (producing mucus)?", ("Dry", "Productive"))
    add_response("Persistent Cough", f"Yes ({cough_type} cough)")
else:
    add_response("Persistent Cough", "No")

# ... Continue with the rest of the questions in a similar manner

# Display the survey responses
st.header("Survey Responses")
st.write(survey_data)

