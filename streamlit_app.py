import streamlit as st

def welcome_screen():
    st.title("Welcome to Lung Assist Respiratory Survey")
    st.write("This survey is designed to gather information about your respiratory health.")
    next_button = st.button("Next")
    st.empty()

    if next_button:
        st.empty()  # Clear the entire screen
        survey_page()

def survey_page():
    st.title("Respiratory Health Survey")

    # Your survey questions and form go here...

    if st.button("Submit Survey"):
        st.success("Your respiratory survey has been successfully submitted. Thank you!")
        st.empty()  # Clear the entire screen
        
    #st.success("Your respiratory survey has been successfully submitted. Thank you!")

def main():
    welcome_screen()

if __name__ == "__main__":
    main()
