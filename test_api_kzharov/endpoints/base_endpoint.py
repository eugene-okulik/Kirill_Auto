import allure


class Endpoint:
    response = None
    response_json = None

    @allure.step("Verify response")
    def check_response_is_200(self):
        assert self.response.status_code == 200
