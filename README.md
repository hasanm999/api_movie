# 🎬 Movie API

A beginner-friendly REST API project built with **Python, Django, and Django REST Framework** to practice API development and understand the fundamentals of RESTful web services.

The main goal of this project is **learning by building** — practicing API endpoints, handling HTTP requests, and implementing CRUD operations using Django REST Framework's generic views.

## 🎯 Project Goals

- Understand the fundamentals of REST APIs.
- Learn how to build APIs using Django REST Framework.
- Practice handling HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`.
- Work with serializers to convert model data into API responses.
- Learn how to use generic views to reduce repetitive code.
- Understand URL routing and connect endpoints to their corresponding views.

## 🛠️ Tech Stack

- **Python** — Programming language
- **Django** — Web framework
- **Django REST Framework** — API development
- **SQLite** — Database (Django's default database, unless configured otherwise)

## ✨ Features

- Retrieve a list of movies.
- Retrieve details of a single movie.
- Create new movie records.
- Update existing movie records.
- Delete movie records.
- Use Django REST Framework generic views to implement API endpoints.

## 🔗 API Endpoints

The project includes the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/list/` | Retrieve all movies |
| `GET` | `/<int:pk>/` | Retrieve a movie by ID |
| `POST` | `/create/` | Create a new movie |
| `PUT` | `/update/<int:pk>/` | Update a movie |
| `DELETE` | `/delete/<int:pk>/` | Delete a movie |

> **Note:** These paths are relative to the URL configuration that includes the movie app. The final URLs may have an additional prefix configured in the main project.

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/hasanm999/api_movie.git
cd api_movie
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

### 3. Activate the virtual environment

**Windows:**

```bash
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install django djangorestframework
```

If the repository includes a `requirements.txt` file, you can install its dependencies instead:

```bash
pip install -r requirements.txt
```

### 5. Apply database migrations

```bash
python manage.py migrate
```

### 6. Start the development server

```bash
python manage.py runserver
```

The development server will be available at:

http://127.0.0.1:8000/

## 🧠 What I Learned

This project is part of my journey to improve my backend development skills and understand how APIs work in practice.

Through this project, I am practicing:

- Django REST Framework fundamentals.
- Serializers and model data handling.
- Generic API views.
- CRUD operations.
- URL configuration and endpoint design.
- HTTP methods and client-server communication.

## 📚 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework Documentation](https://www.django-rest-framework.org/)
- [Django REST Framework — Generic Views](https://www.django-rest-framework.org/api-guide/generic-views/)

## 👨‍💻 Author

**Hasan Mirzaie**

GitHub: [@hasanm999](https://github.com/hasanm999)

---

⭐ This is a learning project focused on practicing API development with Django REST Framework. More features and improvements may be added as I continue learning.
