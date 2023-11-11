import streamlit as st


def welcome_screen():
    st.title("Welcome to Lung Assist Respiratory Survey")
    st.write("This survey is designed to gather information about your respiratory health.")

    if st.button("Next"):
        survey_container = st.empty()
        survey_page(survey_container)

def survey_page(container):
    container.title("Respiratory Health Survey")

    # Your survey questions and form go here...

    if st.button("Submit Survey"):
        container.empty()  # Clear the container
        st.success("Your respiratory survey has been successfully submitted. Thank you!")

def main():
    welcome_screen()

if __name__ == "__main__":
    main()
