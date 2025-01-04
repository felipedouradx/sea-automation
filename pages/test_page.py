from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from lib.selenium_helper import Helpers


class TestPage:
    def __init__(self, context):
        self.context = context
        self.helper = Helpers(context)

    def select_search_button(self):
        self.helper.selenium_wait_clickable(2, By.ID, 'APjFqb')
        self.context.browser.find_element(By.ID, 'APjFqb').click()

    def insert_iphone_model(self, iphone_model):
        search_box = self.context.browser.find_element(By.ID, 'APjFqb')
        search_box.send_keys(iphone_model)
        actions = ActionChains(self.context.browser)
        actions.move_to_element(search_box).send_keys(Keys.ENTER).perform()

    def select_shopping_sheet(self):
        self.helper.selenium_wait_clickable(2, By.PARTIAL_LINK_TEXT, 'Shopping')
        shopping_button = self.context.browser.find_element(By.PARTIAL_LINK_TEXT, 'Shopping')
        shopping_button.click()
