import pytest
from selene import browser
import os
from dotenv import load_dotenv
from utils import config
from appium import webdriver
import allure

load_dotenv()


@pytest.fixture(scope='session',
                params=[('11.0', 'android', 'Samsung Galaxy S21')],
                ids=['base'],
                autouse=True)
def mobile_management(request):
    env = os.getenv('ENVIRONMENT')
    with allure.step('init app session'):
        if env == 'local':
            browser.config.driver = webdriver.Remote(
                config.remote_url,
                options=config.to_driver_options_local()
            )
        else:
            platform_version, platform_name, device_name = request.param
            browser.config.driver = webdriver.Remote(
                config.remote_url,
                options=config.to_driver_options_bstack(platform_version, platform_name, device_name)
            )

    browser.config.timeout = float(os.getenv('timeout', '30.0'))

    yield

    browser.quit()
