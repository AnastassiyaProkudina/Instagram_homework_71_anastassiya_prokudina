# Введение
### Эта документация поможет вам ознакомиться с ресурсами Instagram API и покажет, как выполнять различные запросы, чтобы вы могли извлечь из этого максимальную пользу.

## Rest
**На данный момент доступны три ресурса:** 
<br>
posts: используется для получения всех проектов.
<br>
likes: используется для получения всех лайков.
<br>
comments: используется для получения всех комментариев.

## Проект
Существует 13 постов

## Схема проекта

| **Ключ**   | **Тип** | **Описание**            |
|------------|---------|-------------------------|
| id         | int     | Идентификатор поста     |     
| text       | string  | Текст поста             |
| image      | image   | Фото                    |
| author     | int     | Идентификатор Автора    |
| created_at | string  | Время создания          |     
| updated_at | string  | Дата и время обновления |


## Получить все посты
Вы можете получить доступ к списку проектов, используя: http://127.0.0.1:8000/api/posts/

## Получить один проект
Вы можете получить один прост, добавив id в качестве параметра: http://127.0.0.1:8000/api/posts/1




## лайки
Существует 7 лайков, отсортированных по идентификатору.

Схема лайкови


| **Ключ** | **Тип** | **Описание**         |
|----------|---------|----------------------|
| id       | int     | Идентификатор лайка  |     
| author   | int     | Идентификатор Автора |
| post     | int     | Идентификатор Поста  |

## Получить все лайки
Вы можете получить доступ к списку проектов, используя: http://127.0.0.1:8000/api/likes/

## Получить одну лайк
Вы можете получить один лайку, добавив id в качестве параметра: http://127.0.0.1:8000/api/likes/1


---
for  superuser admin:
<br>email: admin@admin.com
<br>Password: admin
<hr>
for  all users:
<br>john_doe@mail.com, root@mail.com, lilu_23@mail.com, chris_tacher@mail.com, plavalaguna@mail.com
<br>Password: A123456a
<hr>
