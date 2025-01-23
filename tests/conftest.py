import pytest
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions
from selene import browser
import os
from dotenv import load_dotenv


@pytest.fixture(scope="session", autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='function',
                params=[('9.0', 'android', 'Google Pixel 3')],
                ids=['base'],
                autouse=True)
def mobile_management(request):
    bstack_login = os.getenv("BSTACK_LOGIN")
    bstack_access_key = os.getenv("BSTACK_ACCESS_KEY")
    bstack_app = os.getenv("BSTACK_APP")
    bstack_project_name = os.getenv("BSTACK_PROJECT_NAME")
    bstack_buld_name = os.getenv("BSTACK_BULD_NAME")
    bstack_session_name = os.getenv("BSTACK_SESSION_NAME")

    platform_version, platform_name, device_name = request.param
    driver_platform = UiAutomator2Options()

    if platform_name == 'ios':
        driver_platform = XCUITestOptions()

    options = driver_platform.load_capabilities({
        "platformVersion": platform_version,
        'platformName': platform_name,
        "deviceName": device_name,

        "app": bstack_app,

        'bstack:options': {
            "projectName": bstack_project_name,
            "buildName": bstack_buld_name,
            "sessionName": bstack_session_name,

            "userName": bstack_login,
            "accessKey": bstack_access_key
        }
    })

    browser.config.driver_remote_url = 'http://hub.browserstack.com/wd/hub'
    browser.config.driver_options = options

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    yield

    browser.quit()
