import pytest
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


# @pytest.fixture(params=["chrome", "firefox"])
@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    # browser = request.param
    print(f"Creating {browser} Driver")
    # colocar o nome dentro das chavetas vai mostrar o nome  do borwser onde está
    # a ser executado
    if browser == "chrome":
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrom' or 'firefox', but got {browser}")
    my_driver.implicitly_wait(10)
    yield my_driver
    print(f"Closing {browser} Driver")
    my_driver.quit()


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="browse to execute tests (chrome or firefox)"
    )
