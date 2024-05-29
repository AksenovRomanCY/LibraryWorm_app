import requests
import streamlit as st

if 'library_id' not in st.session_state:
    st.session_state['library_id'] = ''

st.header('The project is still :violet[in progress]', divider='violet')


library_id = st.text_input('Search by ID')
search = st.button("Search")
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
        st.session_state['library_id'] = response_dict.get("library_id")

st.divider()


unbind = st.button("Unbind")
if unbind:
    response = requests.put(
        url='http://127.0.0.1:8000/books/update_r/{str(library_id)}',
        params={"library_id": str(st.session_state['library_id'])}
    )
    st.success('Done!', icon="✅")
    st.session_state['library_id'] = ''


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
