import requests
import streamlit as st

if 'book_name' not in st.session_state:
    st.session_state['book_name'] = ''
if 'book_author_surname' not in st.session_state:
    st.session_state['book_author_surname'] = ''
if 'book_author' not in st.session_state:
    st.session_state['book_author'] = ''
if 'book_description' not in st.session_state:
    st.session_state['book_description'] = ''
if 'school' not in st.session_state:
    st.session_state['school'] = ''


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
                "Borrower name": [response_dict.get("student_name")],
                "Borrower class": [response_dict.get("student_class")],
                "Data of issue": [response_dict.get("date_of_issue")]
            }, hide_index=True)
            st.session_state['book_name'] = response_dict.get("book_name")
            st.session_state['book_author_surname'] = response_dict.get("book_author_surname")
            st.session_state['book_author'] = response_dict.get("book_author")
            st.session_state['book_description'] = response_dict.get("book_description")
            st.session_state['school'] = response_dict.get("school")


with st.form("my_form2"):
    st.write("Add book")
    name = st.text_input('Title', st.session_state['book_name'])
    author_surname = st.text_input('Author surname', st.session_state['book_author_surname'])
    author = st.text_input('Author name', st.session_state['book_author'])
    description = st.text_area('Description (optional)', st.session_state['book_description'])
    if st.session_state['book_description'] == "Primary":
        sch_point = 0
    else:
        sch_point = 1
    school = st.radio(
        "School",
        ["Primary", "Secondary"],
        index=sch_point
    )
    submitted = st.form_submit_button("Submit")
    if submitted:
        if (name or author) == '':
            st.warning('Not all mandatory fields are filled in', icon="⚠️")
        else:
            package = {
                "book_name": name,
                "book_author_surname": author_surname,
                "book_author": author,
                "book_description": description,
                "school": school,
            }
            response = requests.put(
                url='http://127.0.0.1:8000/books/update/{str(library_id)}', params={"library_id": str(library_id)},
                json=package
            )
            st.success('Done!', icon="✅")
            st.session_state['book_name'] = ''
            st.session_state['book_author_surname'] = ''
            st.session_state['book_author'] = ''
            st.session_state['book_description'] = ''
            st.session_state['school'] = ''


with st.sidebar:
    st.title(':violet[Library]Worm')
    st.page_link("front_main.py", label="Main page")

    st.header(':violet[Changes] in the book catolog', divider='violet')
    st.page_link("pages/add_book.py", label="Add new book")
    st.page_link("pages/change_book_inf.py", label="Edit the book's inf")

    st.header(':violet[Interactions] with students', divider='violet')
    st.page_link("pages/add_student.py", label="Add new student")
    st.page_link("pages/bind_student_to_book.py", label="Bind the student to the book")
    st.page_link("pages/unbind_student_to_book.py", label="Unbind the student to the book")
