def test_health_api(client):

    response = client.get(
        "/api/v1/health"
    )

    assert response.status_code == 200


def test_analyze_api(client):

    response = client.post(

        "/api/v1/analyze",

        json={
            "password":
                "Quantum@Shield2048!"
        }
    )

    assert response.status_code == 200

    data = response.get_json()

    assert data["success"] is True


def test_generate_password_api(client):

    response = client.get(
        "/api/v1/generate-password"
    )

    assert response.status_code == 200


def test_invalid_json(client):

    response = client.post(
        "/api/v1/analyze",
        json={}
    )

    assert response.status_code == 400