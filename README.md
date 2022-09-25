# проект yamdb_final

![example workflow](https://github.com/vladtut/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

## Описание проекта:

Этот проект предоставляет доступ к api проекта api_yamdb, который позволяет оставлять отзывы и оценки к произведениям мирового искусства.

## использованные технологии:
 * Python3
 * DRF (Django REST framework)
 * Django ORM
 * Docker
 * Gunicorn
 * nginx
 * Яндекс Облако(Ubuntu 18.04)
 * PostgreSQL

## Примеры работы с API:

### Работа с моделью AUTH:

Регистрация нового пользователя

```
POST http://api.example.org/api//v1/auth/signup/
```

Получение JWT-токена

```
GET http://api.example.org/api/v1/auth/token/
```

### Работа с моделью CATEGORIES:

Получение списка всех категорий

```
GET http://api.example.org/api//v1/categories/
```

Добавление новой категории

```
POST http://api.example.org/api/v1/categories/
```

Удаление категории

```
POST http://api.example.org/api/v1/categories/{slug}/
```

### Работа с моделью GENRES:

Получение списка всех жанров

```
GET http://api.example.org/api//v1/genres/
```

Добавление жанра

```
POST http://api.example.org/api/v1/genres/
```

Удаление жанра

```
DEL http://api.example.org/api/v1/genres/{slug}/
```

### Работа с моделью TITLES:

Получение списка всех жанров

```
GET http://api.example.org/api//v1/genres/
```

Добавление жанра

```
POST http://api.example.org/api/v1/genres/
```

Удаление жанра

```
DEL http://api.example.org/api/v1/genres/{slug}/
```

### Работа с моделью TITLES:

Получение списка всех произведений

```
GET http://api.example.org/api//v1/titles/
```

Добавление произведения

```
POST http://api.example.org/api/v1/titles/
```

Получение информации о произведении

```
PATCH http://api.example.org/api/v1/titles/{titles_id}/
```

Частичное обновление информации о произведении

```
DEL http://api.example.org/api//v1/titles/{titles_id}/
```

Удаление произведения

```
POST http://api.example.org/api/v1/titles/{titles_id}/
```

### Работа с моделью REVIEWS:

Получение списка всех отзывов

```
GET http://api.example.org/api//v1/titles/{title_id}/reviews/
```

Добавление нового отзыва

```
POST http://api.example.org/api/v1/titles/{title_id}/reviews/
```

Полуение отзыва по id

```
GET http://api.example.org/api/v1/titles/{title_id}/reviews/{review_id}/
```

Частичное обновление отзыва по id

```
PATCH http://api.example.org/api//v1/titles/{title_id}/reviews/{review_id}/
```

Удаление отзыва по id

```
DEL http://api.example.org/api/v1/titles/{title_id}/reviews/{review_id}/
```

### Работа с моделью COMMENTS:

Получение списка всех комментариев к отзыву

```
GET http://api.example.org/api//v1/titles/{title_id}/reviews/{review_id}/comments/
```

Добавление комментария к отзыву

```
POST http://api.example.org/api/v1/titles/{title_id}/reviews/{review_id}/comments/
```

Получение комментария к отзыву

```
DEL http://api.example.org/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

Частичное обновление комментария к отзывуv

```
PATCH http://api.example.org/api//v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

Удаление комментария к отзыву

```
DEL http://api.example.org/api/v1/titles/{title_id}/reviews/{review_id}/comments/{comment_id}/
```

### Работа с моделью USERS:

Получение списка всех пользователей

```
GET http://api.example.org/api//v1/users/
```

Добавление пользователя

```
POST http://api.example.org/api/v1/users/
```

Получение пользователя по username

```
GET http://api.example.org/api/v1/users/{username}/
```

# АВТОРЫ:
работы выыполнял vlad, а его тимлидом был anton
