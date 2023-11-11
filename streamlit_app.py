import streamlit as st

def main():
    st.title("Screen Clearing Example")

    # User selects an action
    action = st.radio("Select an action:", ["Show Content 1", "Show Content 2"])

    # Display content based on user selection
    if action == "Show Content 1":
        show_content_1()
    elif action == "Show Content 2":
        show_content_2()

def show_content_1():
    st.header("Content 1")
    st.write("This is the first content.")

def show_content_2():
    st.header("Content 2")
    st.write("This is the second content.")

if __name__ == "__main__":
    main()
