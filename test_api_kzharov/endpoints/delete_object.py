import requests
import allure
from endpoints.base_endpoint import Endpoint


class DeleteObject(Endpoint):

    @allure.step("Send DELETE request")
    def delete_by_id(self, obj_id):
        self.response = requests.delete(f"https://api.restful-api.dev/objects/{obj_id}")
        self.response_json = self.response.json()

    @allure.step("Send DELETE request again to verify deletion")
    def check_response_is_404(self):
        assert self.response.status_code == 404
