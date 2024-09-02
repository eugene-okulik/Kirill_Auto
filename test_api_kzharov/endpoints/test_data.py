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


def patch_payload():
    return {
        "name": "Apple MacBook Pro 25 (Updated Name)"
    }


def headers():
    return {
        "Content-Type": "application/json",
        "Authorization": "Bearer your_token_here"
    }
