from unittest.mock import MagicMock

import pytest

from app.db import session


def test_get_db_closes_session(monkeypatch):
    mock_db = MagicMock()

    monkeypatch.setattr(
        session,
        "SessionLocal",
        lambda: mock_db
    )

    db_generator = session.get_db()

    db = next(db_generator)

    assert db is mock_db

    with pytest.raises(StopIteration):
        next(db_generator)

    mock_db.close.assert_called_once()

def test_get_db_closes_session_on_exception(monkeypatch):
    mock_db = MagicMock()

    monkeypatch.setattr(
        session,
        "SessionLocal",
        lambda: mock_db
    )

    db_generator = session.get_db()

    db = next(db_generator)

    assert db is mock_db

    with pytest.raises(RuntimeError):
        db_generator.throw(RuntimeError("Database error"))

    mock_db.close.assert_called_once()