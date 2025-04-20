import requests


class ProjectPage:
    BASE_URL = "https://ru.yougile.com/api-v2/projects"
    def create_project(self, project):
        response = requests.post(f"{self.BASE_URL}/users", json={"project": project})
        return response

    def get_token(user= 'harrypotter', password='expelliarmus'):
        creds = {
        'username': user,
        'password': password
        }
        resp = requests.post(BASE_URL + '/auth/login', json=creds)
        return resp.json()["user_token"]

    def authenticate_project(self, project):
        response = requests.post(f"{self.BASE_URL}/auth", json={"project": project})
        return response

    def get_project_info(self, project_id):
        response = requests.get(f"{self.BASE_URL}/projects/{project_id}")
        return response
