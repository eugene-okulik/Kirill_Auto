import requests
import allure
from endpoints.base_endpoint import Endpoint


class CreatePost(Endpoint):
    url = "https://api.restful-api.dev/objects"

    @allure.step("Send POST request")
    def new_object(self, payload, headers):
        self.response = requests.post(self.url, json=payload, headers=headers)
        self.response_json = self.response.json()
        return self.response

    @allure.step("Verify response")
    def check_response_title_is_correct(self, payload):
        assert self.response_json['name'] == payload['name']
