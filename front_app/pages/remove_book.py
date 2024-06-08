import requests
import streamlit as st

st.set_page_config(page_title="LibraryWorm", page_icon=":notebook_with_decorative_cover:",
                   layout="wide", initial_sidebar_state="auto")

st.header('The project is still :violet[in progress]', divider='violet')

with st.form("my_form"):
    library_id = st.text_input('Remove by ID')
    remove = st.form_submit_button("Remove")
    if remove:
        if library_id == '':
            st.warning('Not all mandatory fields are filled in', icon="⚠️")
        else:
            response = requests.get(
                url='http://127.0.0.1:8000/books/remove_book/{str(library_id)}', params={"library_id": str(library_id)})
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
