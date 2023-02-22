import pytest
from selene.support.shared import browser

@pytest.fixture
def resolution_browser():
    browser.config.window_height = 1920
    browser.config.window_width = 420
    browser.open('https://google.com')