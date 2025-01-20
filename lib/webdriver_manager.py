from datetime import datetime
import allure
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium_stealth import stealth


class WebdriverManager:

    @staticmethod
    def set_driver(browser='chrome', headless=False, remote=False, context=None):
        if context.browser is None:
            if 'chrome' in browser:
                options = ChromeOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--ignore-certificate-errors")
                if headless:
                    options.add_argument("--headless")
                    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
                    options.add_argument(f'user-agent={user_agent}')
                    options.add_argument('--window-size=1920,1080')
                    options.add_argument('--allow-running-insecure-content')

                if remote:
                    context.browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
                else:
                    context.browser = webdriver.Chrome(options=options)

                stealth(
                    context.browser,
                    languages=["en-US", "en"],
                    vendor="Google Inc.",
                    platform="Win32",
                    webgl_vendor="Intel Inc.",
                    renderer="Intel Iris OpenGL Engine",
                    fix_hairline=True,
                )

            if 'edge' in browser:
                options = EdgeOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--ignore-certificate-errors")
                if headless:
                    options.add_argument("--headless")
                    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
                    options.add_argument(f'user-agent={user_agent}')
                    options.add_argument('--window-size=1920,1080')
                    options.add_argument('--allow-running-insecure-content')
                if remote:
                    context.browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
                else:
                    context.browser = webdriver.Edge(options=options)

            if 'firefox' in browser:
                options = FirefoxOptions()
                options.add_argument("--no-sandbox")
                options.add_argument("--disable-dev-shm-usage")
                options.add_argument("--ignore-certificate-errors")
                if headless:
                    options.add_argument("--headless")
                    user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'
                    options.add_argument(f'user-agent={user_agent}')
                    options.add_argument('--window-size=1920,1080')
                    options.add_argument('--allow-running-insecure-content')
                if remote:
                    context.browser = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=options)
                else:
                    context.browser = webdriver.Firefox(options=options)

    @staticmethod
    def get_base_url(context, base_url='google'):
        if 'sea' in base_url:
            context.browser.get('https://analista-teste.seatecnologia.com.br/')

    @staticmethod
    def take_screenshot(driver, scenario_name):
        screenshots_directory = "screenshots"
        if not os.path.exists(screenshots_directory):
            os.makedirs(screenshots_directory)

        file_name = f"{scenario_name}_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.png"
        screenshot_path = os.path.join(screenshots_directory, file_name)
        driver.save_screenshot(screenshot_path)
        return screenshot_path

    @staticmethod
    def screenshot(context, scenario):
        screenshot_path = WebdriverManager.take_screenshot(context.browser, scenario.name)
        WebdriverManager.attach_screenshot_to_allure(screenshot_path)

    @staticmethod
    def attach_screenshot_to_allure(report_path):
        with open(report_path, "rb") as image_file:
            file_content = bytearray(image_file.read())
            allure.attach(file_content, name="Screenshot", attachment_type=allure.attachment_type.PNG)
