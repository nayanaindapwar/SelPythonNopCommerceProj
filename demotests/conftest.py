import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(autouse=True)
def setup(request):
    browser_name=request.config.getoption("browser_name")
    if browser_name == "chrome":

        # Chrome Driver - Chrome browser
        service_obj = Service()
        driver = webdriver.Chrome(service=service_obj)
    elif browser_name == "firefox":
        # Firefox driver - Firefox browser
        service_obj = Service()
        driver = webdriver.Firefox(service=service_obj)
    elif browser_name == "edge":
        service_obj = Service()
        driver = webdriver.Edge(service=service_obj)

    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://admin-demo.nopcommerce.com")

    request.cls.driver = driver
    yield
    driver.quit()