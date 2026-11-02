def create_user_and_get_token(client):
    client.post(
        "/users/register",
        json={
            "name": "Ticket User",
            "email": "ticket@example.com",
            "password": "password123"
        }
    )

    response = client.post(
        "/users/login",
        json={
            "email": "ticket@example.com",
            "password": "password123"
        }
    )

    token = response.json()["access_token"]

    return {"Authorization": f"Bearer {token}"}


def test_create_ticket(client):
    headers = create_user_and_get_token(client)

    response = client.post(
        "/tickets/",
        headers=headers,
        json={
            "title": "Login problem",
            "description": "Unable to log into my account."
        }
    )

    assert response.status_code == 201
    assert response.json()["title"] == "Login problem"
    assert response.json()["status"] == "open"


def test_get_my_tickets(client):
    headers = create_user_and_get_token(client)

    client.post(
        "/tickets/",
        headers=headers,
        json={
            "title": "Payment issue",
            "description": "Payment was not processed."
        }
    )

    response = client.get("/tickets/", headers=headers)

    assert response.status_code == 200
    assert len(response.json()) == 1


def test_update_ticket(client):
    headers = create_user_and_get_token(client)

    created = client.post(
        "/tickets/",
        headers=headers,
        json={
            "title": "Old title",
            "description": "Ticket description"
        }
    )

    ticket_id = created.json()["id"]

    response = client.patch(
        f"/tickets/{ticket_id}",
        headers=headers,
        json={"title": "Updated title"}
    )

    assert response.status_code == 200
    assert response.json()["title"] == "Updated title"


def test_delete_ticket(client):
    headers = create_user_and_get_token(client)

    created = client.post(
        "/tickets/",
        headers=headers,
        json={
            "title": "Ticket to delete",
            "description": "This ticket will be deleted."
        }
    )

    ticket_id = created.json()["id"]

    response = client.delete(
        f"/tickets/{ticket_id}",
        headers=headers
    )

    assert response.status_code == 204

    check = client.get(
        f"/tickets/{ticket_id}",
        headers=headers
    )

    assert check.status_code == 404


def test_unauthorized_ticket_access(client):
    response = client.get("/tickets/")

    assert response.status_code in (401, 403)