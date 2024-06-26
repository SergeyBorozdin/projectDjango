# projectDjango

Реальный инструмент для работы. Реестр обрудования был реализован на excel, была задача развернуть в базу данных с отражением через браузер.

Пример реестра в эксель

![picture](https://github.com/SergeyBorozdin/equipmentRegistry/blob/main/registr%20old.png)


Новый реестр

![picture](https://github.com/SergeyBorozdin/equipmentRegistry/blob/main/registr%20new1.png)
![picture1](https://github.com/SergeyBorozdin/equipmentRegistry/blob/main/registr%20new%202.png)
![picture2](https://github.com/SergeyBorozdin/equipmentRegistry/blob/main/registr%20new%203.png)
![picture2](https://github.com/SergeyBorozdin/equipmentRegistry/blob/main/registr%20new%204.png)



- https://www.youtube.com/watch?v=OYeqcxaYUbQ&list=PLDyJYA6aTY1nZ9fSGcsK4wqeu-xaJksQQ&index=5
- в папке проекта устанавливаем джанго
- pip install django
- команды можно посмотреть на сайте https://pypi.org/
- после обращаемся к джанго и создаем проект django-admin startproject progger

- приложение уже готово для запуска нужно только в терминале перейти в папку проекта написать команду python3 manage.py runserver 
- создаем приложение для отражения домашней страницы и страницы about python3 manage.py startapp main 
- from django.http import HttpResponse в views используем как заглушку для проверки работы страниц, после render для отображения шаблонов
- Для отражения разных стилей подключим к проекту https://getbootstrap.com/ https://www.bootstrapcdn.com/
- официальная документация по джанго https://docs.djangoproject.com/en/5.0/howto/static-files/
- иконки для сайта https://fontawesome.com/, для работы нужно подключить в файле html в данном случае layout
- для настройки Datatables  официальная документация + видео 
- https://datatables.net/
- https://www.youtube.com/watch?v=6vVnP02bkQc&t=18s














- Команды 
- включить сетевое на виндовс
- python -m venv venv
-  .\venv\Scripts\activate
- pip install django

- проверка
- python -m django --version

- запуск сервера
- python manage.py runserver
