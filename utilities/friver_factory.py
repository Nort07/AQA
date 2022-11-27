from selenium.webdriver import Chrome, Firefox, Safari
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


class DriverFactory:
    CHROME = 1
    FIREFOX = 2
    EDGE = 3

    @staticmethod
    def create_driver(driver_id: int):
        if int(driver_id) == 1:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        elif int(driver_id) == 2:
            driver = Firefox(service=Service(GeckoDriverManager().install()))
        elif int(driver_id) == 3:
            driver = Edge(service=Service(EdgeChromiumDriverManager().install()))
        else:
            driver = Chrome(service=Service(ChromeDriverManager().install()))
        return driver