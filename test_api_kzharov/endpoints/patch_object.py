import requests
import allure
from endpoints.base_endpoint import Endpoint


class PatchObject(Endpoint):

    @allure.step("Send PATCH request")
    def patch_by_id(self, patch_payload, obj_id):
        self.response = requests.patch(f"https://api.restful-api.dev/objects/{obj_id}", json=patch_payload)
        self.response_json = self.response.json()

    @allure.step("Verify response")
    def check_response_title_is_correct(self, title):
        assert self.response_json['name'] == title['name']
