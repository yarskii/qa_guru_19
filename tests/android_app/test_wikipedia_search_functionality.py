from appium.webdriver.common.appiumby import AppiumBy
from selene import have, be
from selene.support.shared import browser
from allure import step


def test_wikipedia_search_functionality():
    with step('Skip wellcome screen'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).should(
            be.visible).click()

    with step('Type "Selene" in the search field'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Selene')

    with step('Verify that articles related to "Selene" are found'):
        articles = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        articles.should(have.size_greater_than(0))

    with step('Click on the first article'):
        first_article = articles.first
        first_article.click()

    with step('Verify that the article about "Selene" is displayed'):
        browser.element((AppiumBy.FLUTTER_INTEGRATION_TEXT, 'new UiSelector().text("Selene").instance(0)'))

    with step('Search for "Appium" in the search field'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/page_toolbar_button_search')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with step('Click on the first article'):
        first_article = articles.first
        first_article.click()

    with step('Verify that the article about "Automation for Apps" is displayed'):
        browser.element((AppiumBy.FLUTTER_INTEGRATION_TEXT, 'new UiSelector().text("Automation for Apps")'))

    with step('Open a new tab in the browser'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/tabsCountText')).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'New tab')).click()

    with step('Verify that the new tab displays the welcome message'):
        browser.element((AppiumBy.FLUTTER_INTEGRATION_TEXT, 'new UiSelector().text("Welcome to ")'))
