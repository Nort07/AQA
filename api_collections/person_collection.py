from Automation_tests.api_collections.base_api import BaseAPI
from Automation_tests.api_collections.config_file import BASE_URL, USERNAME, PASSWORD


class Booking(BaseAPI):
    def get_token(self):
        response = self.post(f"{BASE_URL}auth", {"username": USERNAME, "password": PASSWORD})
        return response

    def booking(self):
        response = self.get(f"{BASE_URL}booking",
                            {"firstname": Oleksii, "lastname": Fedorchuk, "checkin": 2022 - 12 - 11,
                             "checkout": 2023 - 12 - 11})

        return response

