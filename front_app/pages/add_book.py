import requests
import streamlit as st

st.set_page_config(page_title="LibraryWorm", page_icon=":notebook_with_decorative_cover:",
                   layout="wide", initial_sidebar_state="auto")

st.header('The project is still :violet[in progress]', divider='violet')

with st.form("my_form"):
    st.write("Add book")
    lib_id = st.text_input('ID')
    name = st.text_input('Title')
    author_surname = st.text_input('Author surname')
    author = st.text_input('Author name')
    description = st.text_area('Description (optional)')
    col1, col2 = st.columns(2)
    with col1:
        lang = st.radio(
            "Language",
            ["Russian", "English", "Other"],
        )
    with col2:
        school = st.radio(
            "School",
            ["Primary", "Secondary"],
        )

    submitted = st.form_submit_button("Submit")
    if submitted:
        if (name == '') or (author_surname == '') or (author == '') or (lib_id == ''):
            st.warning('Not all mandatory fields are filled in', icon="⚠️")
        else:
            package = {
                "book_name": name,
                "book_author_surname": author_surname,
                "book_author": author,
                "book_description": description,
                "school": school,
                "library_id": lib_id,
                "language": lang
            }
            response = requests.post(url='http://127.0.0.1:8000/books/create_book', json=package)
            st.success('Done!', icon="✅")

with st.sidebar:
    st.title(':violet[Library]Worm')
    st.page_link("front_main.py", label="Main page")

    st.header(':violet[Changes] in the book catolog', divider='violet')
    st.page_link("pages/add_book.py", label="Add new book")
    st.page_link("pages/change_book_inf.py", label="Edit the book's inf")
    st.page_link("pages/remove_book.py", label="Remove book")

    st.header(':violet[Interactions] with students', divider='violet')
    st.page_link("pages/add_student.py", label="Add new student")
    st.page_link("pages/bind_student_to_book.py", label="Bind the student to the book")
    st.page_link("pages/unbind_student_to_book.py", label="Unbind the student to the book")
    st.page_link("pages/remove_student.py", label="Remove student")