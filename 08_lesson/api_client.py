import requests
from config import BASE_URL, API_TOKEN


class YougileClient:

    def __init__(self):
        self.base_url = BASE_URL
        self.headers = {
            'Authorization': f'Bearer {API_TOKEN}',
            'Content-Type': 'application/json'
        }

    def create_project(self, title):
        """Создаёт проект с заданным названием."""
        url = (
            f"{self.base_url}"
            "/api-v2/projects"
        )
        data = {"title": title}
        response = requests.post(url, json=data, headers=self.headers)
        return response

    def get_project(self, project_id):
        """Получает проект по ID."""
        url = (
            f"{self.base_url}"
            f"/api-v2/projects/{project_id}"
        )
        response = requests.get(url, headers=self.headers)
        return response

    def update_project(self, project_id, new_title):
        """Обновляет название проекта."""
        url = (
            f"{self.base_url}"
            f"/api-v2/projects/{project_id}"
        )
        data = {"title": new_title}
        response = requests.put(url, json=data, headers=self.headers)
        return response
