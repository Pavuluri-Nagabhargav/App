import streamlit as st

def welcome_screen(container):
    st.title("Welcome to Lung Assist Respiratory Survey")
    st.write("This survey is designed to gather information about your respiratory health.")

    if st.button("Next"):
        container.empty()  # Clear the container
        survey_container = st.empty()
        survey_page(survey_container)
    container.empty()

def survey_page(container):
    container.empty()
    st.title("Respiratory Health Survey")
    #container.empty()  
    # Your survey questions and form go here...

    if st.button("Submit Survey"):
        container.empty()  # Clear the container
        st.success("Your respiratory survey has been successfully submitted. Thank you!")

def main():
    container = st.empty()
    welcome_screen(container)

if __name__ == "__main__":
    main()
