from jose import jwt

from app.core.config import settings
from app.core.security import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)


def test_hash_password():
    password = "password123"

    hashed = hash_password(password)

    assert hashed != password
    assert isinstance(hashed, str)

def test_verify_password():
    password = "password123"

    hashed = hash_password(password)

    verify = verify_password(
        password,
        hashed
    )

    assert verify is True

def test_verify_wrong_password():
    password = "password123"
    wrong_password = "wrongpassword"

    hashed = hash_password(password)

    verify = verify_password(
        wrong_password,
        hashed
    )

    assert verify is False

def test_create_access_token():
    data = {"sub": "1"}

    token = create_access_token(data)

    assert isinstance(token, str)
    assert len(token) > 0

def test_decode_access_token():
    data = {"sub": "1"}

    token = create_access_token(data)

    decoded = decode_access_token(token)

    assert decoded == "1"

def test_decode_invalid_token():
    token = "this-is-not-a-valid-jwt"

    decoded = decode_access_token(token)

    assert decoded is None

def test_decode_token_without_subject():
    token = jwt.encode(
        {"role": "user"},
        settings.secret_key,
        algorithm= settings.algorithm
    )

    decoded = decode_access_token(token)

    assert decoded is None