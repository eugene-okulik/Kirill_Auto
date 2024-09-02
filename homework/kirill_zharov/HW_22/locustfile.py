import requests
from datetime import datetime
from locust import task, HttpUser
import random


# start = datetime.now()
# response = requests.get('https://restful-booker.herokuapp.com', headers={'Authorization': 'd2038db4811dbe6'})
# print(response)
# end = datetime.now()
# print(end - start)

class Booker(HttpUser):
    token = None

    def on_start(self):
        response = self.client.post(
            'authorize',
            json={"username": "admin", "password": "password123"}
        )
        self.token = response.json()['token']

    @task(3)
    def get_all_books(self):
        self.client.get(
            '/booking',
            headers={'Authorization': self.token}
        )

    @task(1)
    def get_one_book(self):
        self.client.get(
            f'/booking/{random.choice([128, 224, 140, 282])}',
            headers={'Authorization': self.token}
        )
