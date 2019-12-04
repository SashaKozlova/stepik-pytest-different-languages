from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_contains_add_button_to_cart(browser):
    browser.get(link)
    WebDriverWait(browser, 10).until(ec.title_contains("Oscar - Sandbox"))
    try:
        language_now = browser.find_element_by_css_selector('option[selected="selected"]')
        print("Current language:" + language_now.text)
    except exceptions.NoSuchElementException:
        print("The specified language cannot be selected. Selected default language English.")
    button_submit = browser.find_element_by_css_selector('button.btn-add-to-basket')
    print("Text on button: " + button_submit.text)
    assert button_submit.is_displayed(), "Button submit isn't present on the page."
