from endpoints.create_object import CreatePost
from endpoints.get_object import GetObject
from endpoints.put_object import PutObject
from endpoints.delete_object import DeleteObject
from endpoints.patch_object import PatchObject

import pytest
import requests
from endpoints.test_data import payload, updated_payload, patch_payload, headers


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


@pytest.fixture
def new_obj():
    # Создаем объект
    response = requests.post("https://api.restful-api.dev/objects", json=payload()).json()
    obj_id = response['id']

    # Возвращаем ID объекта для использования в тестах
    yield obj_id

    # Удаляем объект после завершения теста
    requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")


@pytest.fixture
def updated_payload_fixture():
    return updated_payload()


@pytest.fixture()
def patch_payload_fixture():
    return patch_payload()


@pytest.fixture
def headers_fixture():
    return headers()
