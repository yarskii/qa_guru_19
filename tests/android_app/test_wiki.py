from appium.webdriver.common.appiumby import AppiumBy
from selene import have
from selene.support.shared import browser
from allure import step
import pytest


@pytest.mark.parametrize('mobile_management',
                         [('9.0', 'android', 'Google Pixel 3')],
                         ids=['android'],
                         indirect=True)
def test_search(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Selene')

    with step('Verify content found'):
        articles = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        articles.should(have.size_greater_than(0))

    with step('Click on the first article'):
        first_article = articles.first
        first_article.click()
