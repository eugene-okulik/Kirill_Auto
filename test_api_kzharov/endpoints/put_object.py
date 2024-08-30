import requests
import allure
from endpoints.base_endpoint import Endpoint


class PutObject(Endpoint):

    @allure.step("Send PUT request")
    def put_by_id(self, obj_id, updated_payload):
        self.response = requests.put(f"https://api.restful-api.dev/objects/{obj_id}", json=updated_payload)
        self.response_json = self.response.json()

    @allure.step("Verify response")
    def check_response_title_is_correct(self, updated_payload):
        assert self.response_json['name'] == updated_payload['name']
