import requests


class ProjectPage:
    BASE_URL = "http://api-v2/projects"
    def create_project(self, project):
        response = requests.post(f"{self.BASE_URL}/users", json={"project": project})
        return response

    def authenticate_project(self, project):
        response = requests.post(f"{self.BASE_URL}/auth", json={"project": project})
        return response

    def get_project_info(self, project_id):
        response = requests.get(f"{self.BASE_URL}/projects/{project_id}")
        return response
