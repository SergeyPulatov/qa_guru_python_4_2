import pytest
from selene.support.shared import browser
from selene import browser
from selene import be, have

@pytest.fixture()
def browser_change_size():
    browser.config.window_width = 720
    browser.config.window_height = 1080
    browser.open('https://google.com')

def test_1_positive(browser_change_size):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_2_negative(browser_change_size):
    browser.element('[name="q"]').should(be.blank).type('jkbnvsjsdfdsfdsf').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))



