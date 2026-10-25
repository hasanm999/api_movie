# 🎬 Movie API

A RESTful API for managing movie data, built with **Django** and **Django REST Framework**.

This project was developed as a learning exercise to practice REST API development, generic views, serializers, JWT authentication, filtering, searching, ordering, and API documentation.

## ✨ Features

- 🎥 List and retrieve movies
- ➕ Create new movies
- ✏️ Update existing movies
- 🗑️ Delete movies
- 🔐 JWT authentication
- 🔎 Filter movies by name, description, and year
- 🔍 Search movies by supported fields
- ↕️ Order movies by year
- 📚 Interactive API documentation with Swagger
- 🛡️ Permissions for authenticated and anonymous users

## 🛠️ Tech Stack

- Python
- Django
- Django REST Framework
- Simple JWT
- django-filter
- drf-yasg
- SQLite

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hasanm999/api_movie.git
cd api_movie
```

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

**Windows (Git Bash):**

```bash
source venv/Scripts/activate
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

**Linux / macOS:**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Apply Database Migrations

```bash
python manage.py migrate
```

### 6. Create a Superuser (Optional)

```bash
python manage.py createsuperuser
```

### 7. Run the Development Server

```bash
python manage.py runserver
```

The API will be available at:

`http://127.0.0.1:8000/`

## 🔑 Authentication

The API uses JSON Web Tokens (JWT) for authentication.

### Obtain a Token

**Endpoint:** `POST /api/token/`

Example request body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

Example response:

```json
{
  "refresh": "your_refresh_token",
  "access": "your_access_token"
}
```

### Refresh an Access Token

**Endpoint:** `POST /api/token/refresh/`

Request body:

```json
{
  "refresh": "your_refresh_token"
}
```

Use the access token in the `Authorization` header for protected endpoints:

```http
Authorization: Bearer your_access_token
```

## 📡 API Endpoints

Base URL:

`http://127.0.0.1:8000`

| Method | Endpoint | Description |
|---|---|---|
| GET | `/movies/api/list/` | List movies |
| POST | `/movies/api/list/` | Create a movie |
| GET | `/movies/api/<id>/` | Retrieve a movie |
| PUT | `/movies/api/<id>/` | Update a movie |
| PATCH | `/movies/api/<id>/` | Partially update a movie |
| DELETE | `/movies/api/<id>/` | Delete a movie |
| POST | `/api/token/` | Obtain JWT tokens |
| POST | `/api/token/refresh/` | Refresh an access token |

Replace `<id>` with the movie's integer ID.

### Movie Data Format

Example JSON body for creating a movie:

```json
{
  "name": "Inception",
  "description": "A thief enters people's dreams to steal secrets.",
  "year": 2010,
  "is_active": true
}
```

The `name` field must contain more than two characters.

## 🔎 Filtering, Searching, and Ordering

The movie list endpoint supports filtering, searching, and ordering.

### Filtering

Filter movies by name, description, or year:

```http
GET /movies/api/list/?name=Inception
GET /movies/api/list/?year=2010
GET /movies/api/list/?description=dreams
```

### Searching

Use the `search` query parameter:

```http
GET /movies/api/list/?search=Inception
```

Supported search fields include `name`, `description`, and `year`.

### Ordering

Order movies by year:

```http
GET /movies/api/list/?ordering=year
```

For descending order:

```http
GET /movies/api/list/?ordering=-year
```

## 🔐 Permissions

- **Movie list and create:** Authentication is required.
- **Movie detail:** Anonymous users can retrieve movie details. Authentication is required for updates and deletion.
- **JWT endpoints:** Obtain or refresh tokens using the configured authentication endpoints.

Inactive movies (`is_active=False`) are excluded from the API querysets.

## 📚 API Documentation

Interactive Swagger documentation is available at:

`http://127.0.0.1:8000/swagger/`

You can explore the API endpoints and test requests from your browser.

## 📖 Resources

- [Django Documentation](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Simple JWT Documentation](https://django-rest-framework-simplejwt.readthedocs.io/)
- [django-filter Documentation](https://django-filter.readthedocs.io/)
- [drf-yasg Documentation](https://drf-yasg.readthedocs.io/)

## 👨‍💻 Author

**Hasan Mirzaie**

- GitHub: [@hasanm999](https://github.com/hasanm999)
- Repository: [api_movie](https://github.com/hasanm999/api_movie)

---

⭐ This project is part of my journey in learning backend development and REST API design.
