import pytest
import requests


@pytest.fixture(scope="session", autouse=True)
def teardown_session():
    print("Start testing")
    yield
    print("Testing completed")


@pytest.fixture(autouse=True)
def teardown_test():
    print("before test")
    yield
    print("after test")


def new_obj(payload):
    response = requests.post("https://api.restful-api.dev/objects", json=payload).json()
    return response['id']


@pytest.mark.parametrize("payload", [
    {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    },
    {
        "name": "Dell XPS 13",
        "data": {
            "year": 2020,
            "price": 999.99,
            "CPU model": "Intel Core i7",
            "Hard disk size": "512 GB"
        }
    },
    {
        "name": "HP Spectre x360",
        "data": {
            "year": 2021,
            "price": 1249.99,
            "CPU model": "Intel Core i5",
            "Hard disk size": "256 GB"
        }
    }
])
def test_post_obj(payload):
    response = requests.post("https://api.restful-api.dev/objects", json=payload).json()
    assert response['name'] == payload['name']


@pytest.mark.critical
def test_get_obj_by_id():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    obj_id = new_obj(payload)
    response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}").json()
    assert response['id'] == obj_id


@pytest.mark.medium
def test_put_obj():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    obj_id = new_obj(payload)
    updated_payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}", json=updated_payload).json()
    assert response['name'] == updated_payload['name']
    requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")


def test_patch_obj():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    obj_id = new_obj(payload)
    patch_payload = {
        "name": "Apple MacBook Pro 25 (Updated Name)"
    }
    response = requests.patch(f"https://api.restful-api.dev/objects/{obj_id}", json=patch_payload).json()
    assert response['name'] == patch_payload['name']
    requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")


def test_delete_obj():
    payload = {
        "name": "Apple MacBook Pro 16",
        "data": {
            "year": 2019,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "1 TB"
        }
    }
    obj_id = new_obj(payload)
    response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
    assert response.status_code == 200
    response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
    assert response.status_code == 404
