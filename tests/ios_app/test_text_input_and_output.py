from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step
import pytest


@pytest.mark.parametrize('mobile_management',
                         [('12', 'ios', 'iPhone XS')],
                         ids=['ios'],
                         indirect=True)
def test_text_input_and_output(mobile_management):
    with step('Ввод текста'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Button')).click()

        input_text = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Input'))
        input_text.type('hello@browserstack.com').press_enter()

    with step('Проверка содержимого'):
        text_output = browser.element((AppiumBy.ACCESSIBILITY_ID, 'Text Output'))
        text_output.should(have.text('hello@browserstack.com'))
