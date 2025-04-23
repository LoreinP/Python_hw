import pytest
from Project_Page import ProjectPage

project_page = ProjectPage()

@pytest.fixture(scope="module")
def setup_project():
    project_name= "test_project"
    password = "secure_password"
    ProjectPage.create_project(project_name, password)
    yield ProjectPage, password
    ProjectPage.authenticate_project(ProjectPage, password)

def test_create_project_positive(setup_project):
    username, password = setup_project
    response = project_page.create_project(ProjectPage)
    assert response.status_code == 201

def test_create_project_negative():
    response = project_page.create_project("")
    assert response.status_code == 401

def test_authenticate_project_positive(setup_project):
    project, password = setup_project
    response = project_page.authenticate_project(project)
    assert response.status_code == 200

def test_authenticate_project_negative():
    response = project_page.authenticate_project("invalid_project")
    assert response.status_code == 400

def test_get_project_info_positive(setup_project):
    project, password = setup_project
    auth_response = project_page.authenticate_project(project)
    project_id = auth_response.json().get("id")
    response = project_page.get_project_info(project_id)
    assert response.status_code == 200

def test_get_project_info_negative():
    response = project_page.get_project_info(11111)
    assert response.status_code == 404
