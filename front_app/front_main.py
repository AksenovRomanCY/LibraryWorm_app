import streamlit as st
import requests

st.title('LibraryWorm')
st.header('The project is still :violet[in progress]', divider='violet')

with st.sidebar:
    st.header(':violet[Changes] in the book catolog', divider='violet')
    st.page_link("pages/add_book.py", label="Add new book")
    st.page_link("pages/change_book_inf.py", label="Edit the book's inf")

    st.header(':violet[Interactions] with students', divider='violet')
    st.page_link("pages/add_student.py", label="Add new student")
    st.page_link("pages/bind_student_to_book.py", label="Bind the student to the book")
    st.page_link("pages/unbind_student_to_book.py", label="Unbind the student to the book")

with st.container():
    st.subheader('Catalog')

    response = requests.get(url='http://127.0.0.1:8000/books/get_book_list/')
    response_dict = response.json()
    st.dataframe(data=response_dict, column_config={
        "library_id": "ID",
        "book_name": "Title",
        "book_author": "book_author",
        "book_description": "Description",
        "language": "Language",
        "school": "School",
        "available": "Available",
        "student_name": "Borrower name",
        "student_class": "Borrower class",
    })

st.divider()

with st.container():
    st.subheader('About us')
    st.caption('We are the CyberJerboa team and we are extremely excited to develop a website for'
               ' the Trinity School Library. The website is still under development and offers little functionality.')
