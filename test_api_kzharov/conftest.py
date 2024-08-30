from endpoints.create_object import CreatePost
from endpoints.get_object import GetObject
from endpoints.put_object import PutObject
from endpoints.delete_object import DeleteObject
from endpoints.patch_object import PatchObject

import pytest
import requests


@pytest.fixture
def new_obj():
    # Создаем объект
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    response = requests.post("https://api.restful-api.dev/objects", json=payload).json()
    obj_id = response['id']

    # Возвращаем ID объекта для использования в тестах
    yield obj_id

    # Удаляем объект после завершения теста
    requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")


@pytest.fixture
def payload():
    return {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }


@pytest.fixture
def updated_payload():
    return {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }


@pytest.fixture()
def patch_payload():
    return {
        "name": "Apple MacBook Pro 25 (Updated Name)"
    }


@pytest.fixture
def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_token_here"
    }


@pytest.fixture()
def create_post_endpoint():
    return CreatePost()


@pytest.fixture()
def get_object_endpoint():
    return GetObject()


@pytest.fixture()
def put_object_endpoint():
    return PutObject()


@pytest.fixture()
def patch_object_endpoint():
    return PatchObject()


@pytest.fixture()
def delete_object_endpoint():
    return DeleteObject()
