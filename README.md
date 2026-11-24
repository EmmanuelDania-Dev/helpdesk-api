# HelpDesk API

A RESTful HelpDesk API built with **FastAPI, Python, SQLAlchemy, and SQLite**. It allows users to create accounts, authenticate securely, and manage support tickets through a set of protected API endpoints.

The project focuses on backend engineering concepts such as authentication, database relationships, data validation, authorization, pagination, filtering, automated testing, and continuous integration.

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
- **Automated Testing:** Test application behavior and API endpoints using Pytest.
- **Test Coverage:** Measure code coverage using pytest-cov.
- **Code Quality:** Enforce code-quality standards using Ruff.
- **Continuous Integration:** Automatically run linting and tests through GitHub Actions.

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
| pytest-cov | Test coverage reporting |
| HTTPX | API testing client |
| Ruff | Linting and code quality |
| GitHub Actions | Continuous integration |

## Project Structure

```text
helpdesk-api/
│
├── .github/
│   └── workflows/
│       └── ci.yml
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
│   ├── unit/
│   │   ├── test_security.py
│   │   ├── test_user_service.py
│   │   ├── test_db_session.py
│   │   └── test_auth_dependency.py
│   │
│   ├── conftest.py
│   ├── test_main.py
│   ├── test_tickets.py
│   └── test_users.py
│
├── .env.example
├── .gitignore
├── alembic.ini
├── pyproject.toml
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

The project includes unit tests and API integration tests written with Pytest.

Run the complete test suite from the project root:

```bash
pytest -v
```

The test suite covers:

- Root endpoint responses.
- User registration.
- Duplicate registration.
- Successful and unsuccessful login.
- Password hashing and verification.
- Authentication dependencies.
- Database session behavior.
- Ticket creation and retrieval.
- Ticket updates and deletion.
- Authentication requirements.
- Handling of nonexistent tickets.

Tests use an isolated SQLite database so they do not modify the application's development database.

### Test Coverage

The project uses `pytest-cov` to measure how much of the application code is exercised by the test suite.

Run:

```bash
pytest --cov=app --cov-report=term-missing --cov-report=html
```

This generates:

- A terminal coverage report showing covered and uncovered lines.
- An HTML coverage report in the `htmlcov/` directory.

The current test suite achieves **99% overall code coverage**.

## Code Quality with Ruff

Ruff is used to identify linting issues and maintain consistent code quality.

Run the checks using:

```bash
ruff check app tests
```

The command checks the application and test code for linting issues.

## Continuous Integration with GitHub Actions

The project includes a GitHub Actions workflow located at:

```text
.github/workflows/ci.yml
```

The workflow automatically runs when code is pushed to the `main` branch or when a pull request targets `main`.

The CI pipeline performs the following steps:

1. Checks out the repository.
2. Sets up the configured Python environment.
3. Installs project dependencies.
4. Runs Ruff to check code quality.
5. Runs the Pytest suite with coverage reporting.

This helps identify linting issues and test failures automatically before changes are merged.

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
- Writing unit and integration tests.
- Using fixtures and isolated test databases.
- Measuring test coverage.
- Applying automated linting and code-quality checks.
- Setting up continuous integration with GitHub Actions.

## Demo Recordings

### API Demonstration

A demonstration of the HelpDesk API running and its main functionality:

https://drive.google.com/file/d/177E89HTxR5yFg8Oeh4MTfdB9xTdDzGpw/view?usp=sharing

### Testing and Code Quality Demonstration

A demonstration of the project's automated tests, coverage, and Ruff checks:

https://drive.google.com/file/d/1k-ce1Q749y3xDVBsVyn2ixX1Ycyq_89e/view?usp=sharing

## Author

**Emmanuel Dania**

- GitHub: [EmmanuelDania-Dev](https://github.com/EmmanuelDania-Dev)

---

*Built with Python and FastAPI.*
