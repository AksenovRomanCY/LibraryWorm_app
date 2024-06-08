import requests
import streamlit as st

st.set_page_config(page_title="LibraryWorm", page_icon=":notebook_with_decorative_cover:",
                   layout="wide", initial_sidebar_state="auto")

if 'library_id' not in st.session_state:
    st.session_state['library_id'] = ''
if 'student_name' not in st.session_state:
    st.session_state['student_name'] = ''
if 'student_surname' not in st.session_state:
    st.session_state['student_surname'] = ''

st.header('The project is still :violet[in progress]', divider='violet')

with st.form("my_form"):
    library_id = st.text_input('Search by ID')
    search = st.form_submit_button("Search")
    if search:
        if library_id == '':
            st.warning('Not all mandatory fields are filled in', icon="⚠️")
        else:
            response = requests.get(
                url='http://127.0.0.1:8000/books/get_book_id/{str(library_id)}', params={"library_id": str(library_id)}
            )
            response_dict = response.json()
            st.dataframe({
                "ID": [response_dict.get("library_id")],
                "Title": [response_dict.get("book_name")],
                "Author surname": [response_dict.get("book_author_surname")],
                "Author name": [response_dict.get("book_author")],
                "Description": [response_dict.get("book_description")],
                "Language": [response_dict.get("language")],
                "School": [response_dict.get("school")],
                "Available": [response_dict.get("available")],
                "Student surname": [response_dict.get("student_surname")],
                "Student name": [response_dict.get("student_name")],
                "Student class": [response_dict.get("student_class")],
                "Data of issue": [response_dict.get("date_of_issue")]
            }, hide_index=True)
            st.session_state['library_id'] = response_dict.get("library_id")


student_surname = st.text_input('Add student surname')
st.session_state['student_surname'] = student_surname
student_name = st.text_input('Add student name')
st.session_state['student_name'] = student_name
date_st = st.radio(
    "Date",
    ["Current date", "Custom date"],
    index=0
    )
if date_st == "Current date":
    date = 'current'
else:
    date = st.date_input("Date", format="YYYY-MM-DD", value=None)
st.session_state['date'] = date

bind = st.button("Bind")
if bind:
    if (student_surname == '') or (student_name == '') or (st.session_state['library_id'] == ''):
        st.warning('Not all mandatory fields are filled in', icon="⚠️")
    else:
        response = requests.put(
            url='http://127.0.0.1:8000/books/update_a/{str(library_id)}/{str(student_surname)}/{str(student_name)}/{'
                'str(date)}',
            params={"library_id": str(st.session_state['library_id']),
                    "student_surname": str(st.session_state['student_surname']),
                    "student_name": str(st.session_state['student_name']),
                    "date": str(st.session_state['date'])}
        )
        st.success('Done!', icon="✅")
        st.session_state['library_id'] = ''
        st.session_state['student_surname'] = ''
        st.session_state['student_name'] = ''
        st.session_state['date'] = ''


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
