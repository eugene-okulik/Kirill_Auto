import requests
import allure
from endpoints.base_endpoint import Endpoint


class GetObject(Endpoint):

    def get_by_id(self, obj_id):
        self.url = f"https://api.restful-api.dev/objects/{obj_id}"
        self.response = self.get_object()
        self.response_json = self.response.json()

    @allure.step("Send GET request")
    def get_object(self):
        self.response = requests.get(self.url)
        return self.response

    @allure.step("Verify response")
    def check_object_id(self, obj_id):
        response_json = self.response.json()
        assert response_json['id'] == obj_id

    def check_response_is_404(self):
        assert self.response.status_code == 404
