import pytest
import requests
import allure

# Фикстура для инициализации и завершения сессии тестов
@pytest.fixture(scope="session", autouse=True)
def teardown_session():
    print("Start testing")
    yield
    print("Testing completed")

# Фикстура для инициализации и завершения каждого теста
@pytest.fixture(autouse=True)
def teardown_test():
    print("before test")
    yield
    print("after test")

# Фикстура для создания нового объекта перед тестом и удаления его после теста
@pytest.fixture
def new_obj():
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
    yield obj_id
    requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")

# Тесты для различных API операций
@allure.feature("API Testing")
@allure.story("Create objects")
@allure.title("Test POST request with different payloads")
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
    with allure.step("Send POST request"):
        response = requests.post("https://api.restful-api.dev/objects", json=payload).json()
    with allure.step("Verify response"):
        assert response['name'] == payload['name']

@allure.feature("API Testing")
@allure.story("Retrieve objects")
@allure.title("Test GET request by ID")
@pytest.mark.critical
def test_get_obj_by_id(new_obj):
    obj_id = new_obj
    with allure.step("Send GET request"):
        response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}").json()
    with allure.step("Verify response"):
        assert response['id'] == obj_id

@allure.feature("API Testing")
@allure.story("Update objects")
@allure.title("Test PUT request")
@pytest.mark.medium
def test_put_obj(new_obj):
    obj_id = new_obj
    updated_payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    with allure.step("Send PUT request"):
        response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}", json=updated_payload).json()
    with allure.step("Verify response"):
        assert response['name'] == updated_payload['name']

@allure.feature("API Testing")
@allure.story("Partial update objects")
@allure.title("Test PATCH request")
def test_patch_obj(new_obj):
    obj_id = new_obj
    patch_payload = {
        "name": "Apple MacBook Pro 25 (Updated Name)"
    }
    with allure.step("Send PATCH request"):
        response = requests.patch(f"https://api.restful-api.dev/objects/{obj_id}", json=patch_payload).json()
    with allure.step("Verify response"):
        assert response['name'] == patch_payload['name']

@allure.feature("API Testing")
@allure.story("Delete objects")
@allure.title("Test DELETE request")
def test_delete_obj(new_obj):
    obj_id = new_obj
    with allure.step("Send DELETE request"):
        response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
    with allure.step("Verify response status"):
        assert response.status_code == 200
    with allure.step("Send DELETE request again to verify deletion"):
        response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
        assert response.status_code == 404
