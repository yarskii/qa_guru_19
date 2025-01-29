import os
from dotenv import load_dotenv

load_dotenv()

bstack_login = os.getenv('BSTACK_LOGIN')
bstack_access_key = os.getenv('BSTACK_ACCESS_KEY')

bstack_app = os.getenv('BSTACK_APP')
bstack_project_name = os.getenv('BSTACK_PROJECT_NAME')
bstack_build_name = os.getenv('BSTACK_BUILD_NAME')
bstack_session_name = os.getenv('BSTACK_SESSION_NAME')

remote_url = os.getenv('LOCAL_URL')
app_wait_activity = os.getenv('APP_WAIT_ACTIVITY')

relative_path_app = os.getenv('APP_PATH')

if relative_path_app and not bstack_app:
    app = os.path.abspath(os.path.join(os.path.dirname(__file__), relative_path_app))
else:
    app = None

runs_on_bstack = bool(bstack_app)

if runs_on_bstack:
    remote_url = os.getenv('BSTACK_URL')


def to_driver_options_local():
    from appium.options.android import UiAutomator2Options
    options = UiAutomator2Options()

    options.set_capability('appWaitActivity', app_wait_activity)
    options.set_capability('app', app)

    return options


def to_driver_options_bstack(platform_version, platform_name, device_name):
    if platform_name == 'ios':
        from appium.options.ios import XCUITestOptions
        options = XCUITestOptions()
        app_value = os.getenv('BSTACK_APP_IOS')
    else:
        from appium.options.android import UiAutomator2Options
        options = UiAutomator2Options()
        app_value = bstack_app

    options.set_capability('app', app_value)
    options.set_capability('platformVersion', platform_version)
    options.set_capability('platformName', platform_name)
    options.set_capability('deviceName', device_name)

    if runs_on_bstack:
        options.set_capability(
            'bstack:options', {
                'projectName': bstack_project_name,
                'buildName': bstack_build_name,
                'sessionName': bstack_session_name,

                'userName': bstack_login,
                'accessKey': bstack_access_key,
            },
        )

    return options
