from selene import be, have
from selene.support.shared import browser


def test_search(browser_size):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_search_negative(browser_size):
    browser.element('[name="q"]').should(be.blank).type('''1231231242""!"%!"!"%!"((((""!!"№"№)))''').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено'))
