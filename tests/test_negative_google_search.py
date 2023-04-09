from selene.support.shared import browser
from selene import be, have


def test_negative_google_search(open_browser):
    browser.element('[name="q"]').should(be.blank).type('afrgdfvldlrmfkefmnsdnjdf').press_enter()
    browser.element('[id="topstuff"]').should(have.text('ничего не найдено'))
