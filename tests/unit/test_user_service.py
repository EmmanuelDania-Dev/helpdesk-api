import pytest

from app.schemas.user import UserCreate
from app.services.user_service import authenticate_user, create_user


def test_create_user(db_session):
    user_data = UserCreate(
        name="Test User",
        email="service@example.com",
        password="password123"
    )

    user = create_user(db_session, user_data)

    assert user.email == "service@example.com"
    assert user.name == "Test User"
    assert user.hashed_password != "password123"

def test_create_user_duplicate_email(db_session):
    user_data = UserCreate(
        name="Test User",
        email="service@example.com",
        password="password123"
    )

    create_user(db_session, user_data)

    with pytest.raises(ValueError, match="Email already registered"):
        create_user(db_session, user_data)

def test_authenticate_user_success(db_session):
    user_data = UserCreate(
        name="Test User",
        email="auth@example.com",
        password="password123"
    )

    create_user(db_session, user_data)

    user = authenticate_user(
        db_session,
        "auth@example.com",
        "password123"
    )

    assert user is not None
    assert user.email == "auth@example.com"

def test_authenticate_user_wrong_password(db_session):
    user_data = UserCreate(
        name="Test User",
        email="auth@example.com",
        password="password123"
    )

    create_user(db_session, user_data)

    user = authenticate_user(
        db_session,
        "auth@example.com",
        "wrongpassword"
    )

    assert user is None

def test_non_existent_email(db_session):

    user = authenticate_user(
        db_session,
        "notexist@example.com",
        "password123"
    )

    assert user is None