## Установка (mac)
1. Клонирование репозитория

```git clone https://github.com/AksenovRomanCY/LibraryWorm_app.git```

2. Переход в директорию

```cd sql_app```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip3 install -r requirements.txt```

6. Запуск скрипта(В разных терминалах)

```uvicorn main:app --reload``` (в папке sql_app)
```streamlit run front_main.py```(в папке sql_app/front_app)

7. После первого запуска сервера в таблице "students" базы данных вручную создать строку с
   uuid "00000000000000000000000000000000", и "-" в полях "student_surname", "student_name", "student_class"


## Зависимости
Эта программа зависит от интепретатора Python версии 3.12 или выше


## Для разработки
При обновлении библиотек, обновлять requirements командой:
pip freeze > requirements.txt