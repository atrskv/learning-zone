import pytest
from selene.support.shared import browser

@pytest.fixture(autouse=True)
def url_open():
    browser.open('https://www.google.com/')
    yield
    browser.close()


@pytest.fixture()
def browser_size():
    browser.driver.set_window_size(1080, 720)


