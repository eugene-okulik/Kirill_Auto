import requests


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
    return response['id']


def post_obj():
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
    assert response['name'] == payload['name']


def get_obj_by_id():
    obj_id = new_obj()
    response = requests.get(f"https://api.restful-api.dev/objects/{obj_id}").json()
    assert response['id'] == obj_id


def put_obj():
    obj_id = new_obj()
    payload = {
        "name": "Apple MacBook Pro 20",
        "data": {
            "year": 2020,
            "price": 1849.99,
            "CPU model": "Intel Core i9",
            "Hard disk size": "2 TB"
        }
    }
    response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}", json=payload).json()
    assert response['name'] == payload['name']


def patch_obj():
    obj_id = new_obj()
    payload = {
        "name": "Apple MacBook Pro 25 (Updated Name)"
    }
    response = requests.patch(f"https://api.restful-api.dev/objects/{obj_id}", json=payload).json()
    assert response['name'] == payload['name']


def delete_obj():
    obj_id = new_obj()
    response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
    assert response.status_code == 200
    response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
    assert response.status_code == 404
