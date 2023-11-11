import streamlit as st

def welcome_screen():
    st.title("Welcome to Lung Assist Respiratory Survey")
    st.write("This survey is designed to gather information about your respiratory health, lets get started.")

    if "next_button_clicked" not in st.session_state:
        st.session_state.next_button_clicked = False

    next_button = st.button("Next")

    if next_button:
        st.session_state.next_button_clicked = True

    if st.session_state.next_button_clicked:
        st.empty()  # Clear the entire screen
        survey_page()

def survey_page():
    st.title("Respiratory Health Survey")

    # Your survey questions and form go here...

    if st.button("Submit Survey"):
        st.session_state.next_button_clicked = False  # Reset the button state
        st.empty()  # Clear the entire screen
        st.success("Your respiratory survey has been successfully submitted. Thank you!")

def main():
    welcome_screen()

if __name__ == "__main__":
    main()
