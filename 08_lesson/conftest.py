import pytest
import requests
from api_client import YougileClient


@pytest.fixture
def yougile_client():
    return YougileClient()


@pytest.fixture
def existing_project_id():
    # Используем ID существующего проекта
    return "0056de80-156a-4320-9fdc-65dc172f658c"


@pytest.fixture
def created_project(yougile_client):
    title = "Test Project for Positive Tests"
    response = yougile_client.create_project(title)
    assert response.status_code == 201
    project_id = response.json()['id']
    yield project_id
    requests.delete(
        (
            f"{yougile_client.base_url}"
            f"/api-v2/projects/{project_id}"
        ),
        headers=yougile_client.headers
    )
