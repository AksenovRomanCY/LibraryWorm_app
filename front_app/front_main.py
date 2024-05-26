import streamlit as st
import requests

st.header('The project is still :violet[in progress]', divider='violet')

tab1, tab2, tab3 = st.tabs(["Catalog", "Borrower list", "Student list"])
with tab1:
    response = requests.get(url='http://127.0.0.1:8000/books/get_book_list/')
    response_dict = response.json()
    st.dataframe(data=response_dict, column_config={
        "library_id": "ID",
        "book_name": "Title",
        "book_author_surname": "Author surname",
        "book_author": "Author name",
        "book_description": "Description",
        "language": "Language",
        "school": "School",
        "available": "Available",
        "student_name": "Borrower name",
        "student_class": "Borrower class",
        "date_of_issue": "Data of issue"
    })

with tab2:
    response = requests.get(url='http://127.0.0.1:8000/students/get_borrowers/')
    response_dict = response.json()
    st.dataframe(data=response_dict, column_config={
        "student_surname": "Surname",
        "student_name": "Name",
        "student_class": "Class",
        "date_of_issue": "Date of issue",
        "school": "School",
        "library_id": "ID",
        "book_name": "Title",
        "book_author_surname": "Author surname",
        "book_author": "Author name"
    })

with tab3:
    response = requests.get(url='http://127.0.0.1:8000/students/get_students_all/')
    response_dict = response.json()
    st.dataframe(data=response_dict, column_config={
        "student_surname": "Surname",
        "student_name": "Name",
        "student_class": "Class"
    })


with st.container():
    st.subheader('About us', divider='violet')
    st.caption('We are the CyberJerboa team and we are extremely excited to develop a website for'
               ' the Trinity School Library. The website is still under development and offers little functionality.')

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
