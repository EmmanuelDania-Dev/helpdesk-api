import pytest
from fastapi import HTTPException
from fastapi.security import HTTPAuthorizationCredentials

from app.core.security import create_access_token, hash_password
from app.dependencies.auth import get_current_user
from app.models.user import User


def test_get_current_user_returns_user(db_session):
    user = User(
        name="Test User",
        email="test@example.com",
        hashed_password=hash_password("password123")
    )

    db_session.add(user)
    db_session.commit()
    db_session.refresh(user)

    token = create_access_token({"sub": str(user.id)})

    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials=token
    )

    current_user = get_current_user(
        credentials=credentials,
        db=db_session
    )

    assert current_user.id == user.id
    assert current_user.email == user.email

def test_get_current_user_invalid_token(db_session):
    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials="invalid-token"
    )

    with pytest.raises(HTTPException) as exc:
        get_current_user(
            credentials=credentials,
            db=db_session
        )

    assert exc.value.status_code == 401
    assert exc.value.detail == "Could not validate credentials"

def test_get_current_user_invalid_user_id(db_session):
    token = create_access_token({"sub": "abc"})

    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials=token
    )

    with pytest.raises(HTTPException) as exc:
        get_current_user(
            credentials=credentials,
            db=db_session
        )

    assert exc.value.status_code == 401

def test_get_current_user_nonexistent_user(db_session):
    token = create_access_token({"sub": "9999"})

    credentials = HTTPAuthorizationCredentials(
        scheme="Bearer",
        credentials=token
    )

    with pytest.raises(HTTPException) as exc:
        get_current_user(
            credentials=credentials,
            db=db_session
        )

    assert exc.value.status_code == 401
    assert exc.value.detail == "Could not validate credentials"