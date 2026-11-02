# HelpDesk API

A RESTful HelpDesk API built with **FastAPI, Python, SQLAlchemy, and SQLite**. It allows users to create accounts, authenticate securely, and manage support tickets through a set of protected API endpoints.

The project focuses on backend engineering concepts such as authentication, database relationships, data validation, authorization, pagination, filtering, and automated testing.

## Features

- **User Registration:** Create user accounts with email and password validation.
- **Password Hashing:** Secure password storage using Argon2.
- **JWT Authentication:** Authenticate users and generate access tokens.
- **Protected Routes:** Restrict access to authenticated users.
- **Ticket Management:** Create, retrieve, update, and delete support tickets.
- **User Authorization:** Users can only access and manage their own tickets.
- **Pagination:** Retrieve tickets in smaller batches using `skip` and `limit`.
- **Filtering:** Filter tickets by status (`open`, `in_progress`, or `closed`).
- **Data Validation:** Validate incoming requests using Pydantic.
- **Database Migrations:** Manage database schema changes using Alembic.
- **Automated Testing:** Test API endpoints and application behavior using Pytest.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Backend programming language |
| FastAPI | REST API framework |
| Pydantic | Request validation and response schemas |
| SQLAlchemy | ORM and database operations |
| SQLite | Relational database |
| Alembic | Database migrations |
| Argon2 / pwdlib | Password hashing |
| JWT / python-jose | Token-based authentication |
| Pytest | Automated testing |
| HTTPX | API testing client |

## Project Structure

```text
helpdesk-api/
│
├── app/
│   ├── api/
│   │   └── routes/
│   │       ├── users.py
│   │       └── tickets.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── db/
│   │   ├── base.py
│   │   └── session.py
│   │
│   ├── dependencies/
│   │   └── auth.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── ticket.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── ticket.py
│   │
│   ├── services/
│   │   └── user_service.py
│   │
│   └── main.py
│
├── alembic/
│
├── tests/
│   ├── conftest.py
│   ├── test_main.py
│   ├── test_users.py
│   └── test_tickets.py
│
├── .env.example
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/EmmanuelDania-Dev/helpdesk-api.git
```

### 2. Navigate to the project root

```bash
cd helpdesk-api
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

**Windows:**

```powershell
.venv\Scripts\activate
```

**Linux / macOS:**

```bash
source .venv/bin/activate
```

### 5. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root.

Add the following configuration:

```env
APP_NAME=HelpDesk API
ENVIRONMENT=development
DEBUG=true
SECRET_KEY=replace_with_your_own_secret_key
```

Generate a secure secret key using:

```bash
python -c "import secrets; print(secrets.token_urlsafe(32))"
```

Copy the generated value into your `.env` file.

**Important:** Never commit your actual `.env` file or secret key to GitHub.

### 7. Apply database migrations

```bash
python -m alembic upgrade head
```

### 8. Start the development server

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## API Documentation

FastAPI automatically generates interactive API documentation.

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to explore endpoints, authenticate, submit requests, and inspect responses.

## Main API Endpoints

### Users

| Method | Endpoint | Description |
|---|---|---|
| POST | `/users/register` | Register a new user |
| POST | `/users/login` | Authenticate and receive an access token |

### Tickets

| Method | Endpoint | Description |
|---|---|---|
| POST | `/tickets/` | Create a support ticket |
| GET | `/tickets/` | Retrieve the authenticated user's tickets |
| GET | `/tickets/{ticket_id}` | Retrieve a specific ticket |
| PATCH | `/tickets/{ticket_id}` | Update a ticket |
| DELETE | `/tickets/{ticket_id}` | Delete a ticket |

### Pagination and Filtering

The ticket listing endpoint supports pagination and status filtering.

Example requests:

```text
GET /tickets/?skip=0&limit=10
GET /tickets/?status=open
GET /tickets/?status=closed
GET /tickets/?skip=0&limit=5&status=in_progress
```

Available ticket statuses:

- `open`
- `in_progress`
- `closed`

## Authentication

The API uses JSON Web Tokens (JWT) for authentication.

To access protected endpoints:

1. Register an account.
2. Log in using your email and password.
3. Copy the returned access token.
4. Authorize your requests using the Bearer token.

Example:

```text
Authorization: Bearer YOUR_ACCESS_TOKEN
```

Passwords are hashed before storage and are never returned in API responses.

## Running Tests

The project includes automated tests written with Pytest and FastAPI TestClient.

Run the complete test suite from the project root:

```bash
python -m pytest -v
```

The tests cover:

- Root endpoint responses.
- User registration.
- Duplicate registration.
- Successful and unsuccessful login.
- Ticket creation and retrieval.
- Ticket updates and deletion.
- Authentication requirements.

Tests use an isolated SQLite database so they do not modify the application's development database.

## Database Migrations

Alembic is used to manage database schema changes.

Generate a migration:

```bash
python -m alembic revision --autogenerate -m "describe your changes"
```

Apply migrations:

```bash
python -m alembic upgrade head
```

## Learning Objectives

This project was developed to strengthen practical backend engineering skills, including:

- Building RESTful APIs.
- Structuring a Python backend application.
- Working with relational databases and ORM relationships.
- Implementing authentication and authorization.
- Managing configuration and environment variables.
- Handling database migrations.
- Implementing pagination and filtering.
- Writing automated API tests.

## Demo

This is a demo recording of the API running successfully:

https://drive.google.com/file/d/14gnXMmgbd91rPMvb-s0jgAnIQm8nBk2c/view?usp=sharing

## Author

**Emmanuel Dania**

- GitHub: [EmmanuelDania-Dev](https://github.com/EmmanuelDania-Dev)

---

*Built with Python and FastAPI.*