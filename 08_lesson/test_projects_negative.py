import pytest
import requests  # Важно: добавлен импорт requests
from api_client import YougileClient


@pytest.fixture
def yougile_client():
    return YougileClient()


class TestProjectsNegative:

    def test_create_project_missing_title(self, yougile_client):
        """
        Тест: попытка создать проект без названия.
        Что проверяет:
        * сервер возвращает ошибку (400 или 422);
        * в сообщении об ошибке есть слова "error" или "message".
        Ожидаемое поведение: API отклоняет запрос
        из‑за отсутствия обязательного поля.
        """
        url = f"{yougile_client.base_url}/api-v2/projects"
        response = requests.post(
            url,
            json={},
            headers=yougile_client.headers
        )
        assert response.status_code in [400, 422]
        response_text = response.text.lower()
        assert "error" in response_text or "message" in response_text

    def test_get_project_not_found(self, yougile_client):
        """
        Тест: попытка получить несуществующий проект.
        Что проверяет:
        * статус‑код 404 (не найдено);
        * сервер корректно обрабатывает запрос с несуществующим ID.
        Ожидаемое поведение: API возвращает 404 для несуществующих ресурсов.
        """
        invalid_id = "nonexistent-id-12345"
        response = yougile_client.get_project(invalid_id)
        assert response.status_code == 404

    def test_update_project_invalid_data(
        self, yougile_client, created_project
    ):
        """
        Тест: попытка обновить проект с некорректными данными.
        Что проверяет:
        * сервер возвращает ошибку (400 или 422);
        * API отклоняет поле, которого нет в схеме.
        Использует фикстуру created_project
        для валидного ID, но передаёт некорректные данные.
        Ожидаемое поведение: сервер не применяет изменения и возвращает ошибку.
        """
        url = (
            f"{yougile_client.base_url}"
            f"/api-v2/projects/"
            f"{created_project}"
        )
        payload = {"invalid_field": "value"}
        response = requests.put(
            url,
            json=payload,
            headers=yougile_client.headers
        )
        assert response.status_code in [400, 422]
