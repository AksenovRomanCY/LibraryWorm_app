import requests
import streamlit as st

st.header('The project is still :violet[in progress]', divider='violet')

with st.form("my_form"):
    st.write("Add student")
    surname = st.text_input('Surname')
    name = st.text_input('Name')
    st_class = st.text_input('Class')
    submitted = st.form_submit_button("Submit")
    if submitted:
        if (name or st_class or surname) == '':
            st.warning('Not all mandatory fields are filled in', icon="⚠️")
        else:
            package = {
                "student_surname": surname,
                "student_name": name,
                "student_class": st_class,
            }
            response = requests.post(url='http://127.0.0.1:8000/students/create_student/', json=package)
            st.success('Done!', icon="✅")

with st.sidebar:
    st.title('LibraryWorm')
    st.page_link("front_main.py", label="Catalog")

    st.header(':violet[Changes] in the book catolog', divider='violet')
    st.page_link("pages/add_book.py", label="Add new book")
    st.page_link("pages/change_book_inf.py", label="Edit the book's inf")

    st.header(':violet[Interactions] with students', divider='violet')
    st.page_link("pages/add_student.py", label="Add new student")
    st.page_link("pages/bind_student_to_book.py", label="Bind the student to the book")
    st.page_link("pages/unbind_student_to_book.py", label="Unbind the student to the book")
