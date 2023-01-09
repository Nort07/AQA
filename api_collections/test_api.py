from requests import get
from http import HTTPStatus

from Automation_tests.api_collections.config_file import BASE_URL
from Automation_tests.api_collections.person_collection import Booking


def test_get_status_200():
    response = get(f"{BASE_URL}")
    assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
                                                  f"Expected: {HTTPStatus.OK}"


def test_get_booking():
    response = Booking().booking()
    # response_data = response.json()
    assert response.status_code == HTTPStatus.OK, f"Status code is not as expected\nActual {response.status_code}\n " \
                                                  f"Expected: {HTTPStatus.OK}"
    # assert response_data == [{"firstname": Oleksii}, {"lastname": Fedorchuk}, {"checkin": 2022 - 12 - 11},
    #                          {"checkout": 2023 - 12 - 11}]
