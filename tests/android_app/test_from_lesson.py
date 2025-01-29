from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure import step


def test_search():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).should(
            be.visible).click()

    with step('Type search'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type(
            'BrowserStack'
        )

    with step('Verify content found'):
        browser.all(
            (AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')
        ).should(have.size_greater_than(0))
