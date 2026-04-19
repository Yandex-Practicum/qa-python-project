import pytest
from selenium import webdriver
from pages.login_page import LoginPage
from helpers import generate_user, create_user, delete_user


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):

    driver = webdriver.Chrome() if request.param == "chrome" else webdriver.Firefox()
    driver.get("https://stellarburgers.education-services.ru/")
    driver.maximize_window()

    yield driver
    driver.quit()


@pytest.fixture
def user():
    user_data = generate_user()
    response = create_user(user_data)
    token = response.json()["accessToken"]

    yield user_data

    delete_user(token)


@pytest.fixture
def auth_driver(driver, user):

    login = LoginPage(driver)

    login.open_login()
    login.login(user["email"], user["password"])

    login.wait_login_success() 

    return driver
