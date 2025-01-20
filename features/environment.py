from behave import use_step_matcher
from lib.webdriver_manager import WebdriverManager
from lib.logger import *

use_step_matcher("parse")


def before_scenario(context, scenario):
    context.browser = None
    environment = context.config.userdata.get('base_url', 'apple')
    browser = context.config.userdata.get('browser', 'chrome')
    browsers_list = browser.split(',')
    headless = context.config.userdata.get('headless', 'false').lower() == 'true'
    remote = context.config.userdata.get('remote', 'false').lower() == 'true'
    WebdriverManager.set_driver(browser=browsers_list, headless=headless, remote=remote, context=context)
    WebdriverManager.get_base_url(context=context, base_url=environment)
    logger.info(f"\n\n\tScenario Name - {scenario.name}\n")


def after_scenario(context, scenario):
    if scenario.status == "failed":
        WebdriverManager.screenshot(context, scenario)

    if hasattr(context, 'browser'):
        context.browser.quit()


def after_step(context, step):
    logger.info(f"\n\t\tStep Name - {step.name}")
    logger.info(f"\t\tStatus - {step.status}")
    logger.info(f"\t\tDuration - {step.duration}s")
    browser_error_list = context.browser.get_log(context.browser.log_types[0])
    driver_error_list = context.browser.get_log(context.browser.log_types[1])
    if step.status == 'Status.failed':
        if len(browser_error_list) > 0:
            for err in browser_error_list:
                logger.info(f"\t\tBrowser Error: {err['message']}")
        if len(driver_error_list) > 0:
            for err in driver_error_list:
                logger.info(f"\t\tDriver Error: {err['message']}")

    WebdriverManager.screenshot(context, step)

