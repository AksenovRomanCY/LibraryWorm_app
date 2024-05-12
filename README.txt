## Установка (mac)
1. Клонирование репозитория

```git clone https://github.com/AksenovRomanCY/LibraryWorm_app.git```

2. Переход в директорию Oxygen

```cd sql_app```

3. Создание виртуального окружения

```python3 -m venv venv```

4. Активация виртуального окружения

```source venv/bin/activate```

5. Установка зависимостей

```pip3 install -r requirements.txt```

6. Запуск скрипта

```uvicorn main:app --reload```
```streamlit run front_main.py```

7. Вручную создать в таблице базе данных "students" строку с uuid "00000000000000000000000000000000",
   и оставить осталные значения пустыми


## Зависимости
Эта программа зависит от интепретатора Python версии 3.12 или выше


## Для разработки
При обновлении библтотек, обновлять requirements командой:
pip freeze > requirements.txt