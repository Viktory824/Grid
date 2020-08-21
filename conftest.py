from pytest import fixture
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox",
                     choices=["chrome", "firefox", "safari"])
    parser.addoption("--executor", action="store", default="10.48.22.83")
    # default = "192.168.0.27"


# @fixture(scope='function', name='driver')
# def get_driver():
#     driver = webdriver.Chrome(executable_path='./drivers/chromedriver')
#     # driver = webdriver.Safari()
#     # driver = webdriver.Firefox(executable_path='../drivers/geckodriver')
#     driver.maximize_window()
#     yield driver
#     driver.quit()

@fixture(name='driver')
def remote(request):
    driver = request.config.getoption("--browser")
    executor = request.config.getoption("--executor")
    driver = webdriver.Remote(command_executor=f"http://{executor}:4444/wd/hub",
                              desired_capabilities={"browserName": driver})
    # "platform": "linux"

    driver.maximize_window()
    request.addfinalizer(driver.quit)
    return driver
