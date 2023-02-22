from selene.support.shared import browser
from selene import be, have

def test_positive(resolution_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

def test_negative(resolution_browser):
    browser.element('[name="q"]').should(be.blank).type('Nullfindsearchtest').press_enter()
    browser.element('[id="result-stats"]').should(have.text('Результатов: примерно 0'))
