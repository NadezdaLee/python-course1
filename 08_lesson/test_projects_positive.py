import pytest
import requests
from api_client import YougileClient


@pytest.fixture
def yougile_client():
    return YougileClient()


@pytest.fixture
def created_project(yougile_client):
    title = "Test Project for Positive Tests"
    response = yougile_client.create_project(title)
    assert response.status_code == 201
    project_id = response.json()['id']
    yield project_id
    # Очистка: удаление проекта после теста
    requests.delete(
        (
            f"{yougile_client.base_url}"
            f"/api-v2/projects/{project_id}"
        ),
        headers=yougile_client.headers
    )


class TestProjectsPositive:

    def test_create_project_success(self, yougile_client):
        """
        Тест создания проекта.
        Что проверяет:
        * статус‑код 201 (ресурс создан);
        * в ответе есть поле `id` (проект создан).
        """
        title = "New Test Project"
        response = yougile_client.create_project(title)
        assert response.status_code == 201
        assert 'id' in response.json()

    def test_get_project_success(self, yougile_client, created_project):
        """
        Тест получения проекта.
        Что проверяет:
        * статус‑код 200;
        * ID в ответе совпадает с запрошенным;
        * есть поле `title` (данные проекта вернулись).
        Использует фикстуру `created_project` для получения валидного ID.
        """
        response = yougile_client.get_project(created_project)
        assert response.status_code == 200
        assert response.json()['id'] == created_project
        assert 'title' in response.json()
        assert response.json()['title'] == "Test Project for Positive Tests"

    def test_update_project_success(self, yougile_client, created_project):
        """
        Тест обновления проекта.
        Что проверяет:
        * статус‑код 200;
        * после обновления можно получить проект с новым названием.
        Использует фикстуру `created_project`
        для получения ID существующего проекта.
        """
        new_title = "Updated Test Project"
        response = yougile_client.update_project(created_project, new_title)
        assert response.status_code == 200
        assert response.json()['id'] == created_project

        # Дополнительная проверка: получаем проект и проверяем новое название
        get_response = yougile_client.get_project(created_project)
        assert get_response.status_code == 200
        assert get_response.json()['title'] == new_title
