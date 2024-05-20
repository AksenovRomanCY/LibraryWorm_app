import streamlit as st
import requests

st.title('LibraryWorm')
st.header('The project is still :violet[in progress]', divider='violet')

with st.form("my_form"):
    st.write("Add book")
    name = st.text_input('Title')
    author = st.text_input('Author')
    description = st.text_area('Description')
    lib_id = st.text_input('ID')
    lang = st.radio(
        "Language",
        ["Russian", "English", "Other"],
    )
    school = st.radio(
        "School",
        ["Primary", "Secondary"],
    )
    submitted = st.form_submit_button("Submit")

    if submitted:
        package = {
            "book_name": name,
            "book_author": author,
            "book_description": description,
            "school": school,
            "library_id": lib_id,
            "language": lang
        }
        response = requests.post(url='http://127.0.0.1:8000/books/create_book/', data=package)
        st.write(response.text)

