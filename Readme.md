1. Создание проекта - django-admin startproject BooksWebApp
2. Создание приложения - python manage.py startapp BooksWeb
3. Добавление приложения в settings.py
4. Подключение БД с помощью выполнения миграции (т.к sqllite3 идет из коробки) - python manage.py migrate
5. Создаем модель и создаем миграцию модели - python manage.py makemigrations (предварительно нужен пакет -m python -m pip install Pillow). И еще раз выолнить миграцию в sqllite3


pip install django-extensions
Запуск сервера - python manage.py runserverэ
Остановить сервер - Ctrl + C