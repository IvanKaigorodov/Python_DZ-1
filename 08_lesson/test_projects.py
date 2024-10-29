import requests
import pytest

base_url = "https://ru.yougile.com/api-v2/"


def auth():
    return {
        "Authorization": "Bearer 7PQctA0q5RNNIMhcltR58nm"
        "GZi58MzSCEwoJEd28vnnqujlrBNg4lLjoRGt1bc-u",
        "Content-Type": "application/json"
    }


# Добавить проект (позитивная проверка)
def test_create_project():
    my_headers = auth()
    payload = {
        "title": "Python-8.3",
        "users": {
            "df9bcca1-2bdf-4722-b105-f09631290479": "admin"}
    }

    response = requests.post(
        base_url+'projects', headers=my_headers, json=payload)
    assert response.status_code == 201, f"Response Body:{
        response.text}"
    json_response = response.json()
    assert "id" in json_response


# Добавить проект с ошибкой users (негативная проверка)
def test_create_project_error_users():
    my_headers = auth()
    payload = {
        "title": "Python-8.4",
        "users": {"123": "admin"}
    }

    response = requests.post(
        base_url+'projects', headers=my_headers, json=payload)
    assert response.status_code == 400, f"Response Body:{
        response.text}"
    json_response = response.json()
    assert "message" in json_response


# Получить список проектов
def test_get_projects():
    my_headers = auth()

    response = requests.get(
        base_url+'projects', headers=my_headers)
    assert response.status_code == 200, f"Response Body:{
        response.text}"
    json_response = response.json()
    assert isinstance(json_response.get(
        'content'), list), f"Expected list, got:{
            type(json_response.get('content'))}"


# Изменить название проекта (позитивная проверка)
def test_change_project():
    project_id = "1286a020-0502-4e04-8f8f-01b9d4cd257b"
    url = f"{base_url}projects/{project_id}"
    my_headers = auth()
    payload = {
        "title": "Python-8.4",
        "users": {
            "df9bcca1-2bdf-4722-b105-f09631290479": "admin"}
    }

    response = requests.put(
        url, headers=my_headers, json=payload)
    assert response.status_code == 200, f"Response Body:{
        response.text}"


# Изменить название проекта без данных (негативная проверка)
def test_update_project_erroe_data():
    project_id = "1286a020-0502-4e04-8f8f-01b9d4cd257b"
    url = f"{base_url}projects/{project_id}"
    my_headers = auth()
    payload = {
        "title": ""
    }

    response = requests.put(
        url, headers=my_headers, json=payload)
    assert response.status_code == 400, f"Response Body:{
        response.text}"
    json_response = response.json()
    assert "message" in json_response


# Запрос проекта по id
def test_get_project_by_id():
    project_id = "e3d9659f-f70c-412a-8c42-693adc2c8ae7"
    url = f"{base_url}projects/{project_id}"
    my_headers = auth()

    response = requests.get(url, headers=my_headers)
    assert response.status_code == 200, f"Response Body:{
        response.text}"
    json_response = response.json()
    assert "title" in json_response, "Новый проект ДЗ-8"
