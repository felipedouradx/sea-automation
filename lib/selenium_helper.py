from selenium.common import TimeoutException
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class Helpers:

    def __init__(self, context):
        self.context = context

    """
        SELENIUM-WAIT(EXPECT CONDITIONS)

        Here are some other commonly used conditions provided by the expected_conditions module:
        title_is: Wait for the title of the page to be a certain string.
        title_contains: Wait for the page title to contain a certain string.
        presence_of_element_located: Wait for an element to be present in the DOM.
        visibility_of_element_located: Wait for an element to not only be present in the DOM but also be visible.
        invisibility_of_element_located: Wait for an element to either be absent from the DOM or not visible.
        text_to_be_present_in_element: Wait for a specific text to be present in a certain element.
        text_to_be_present_in_element_value: Similar to the above, but checks the element's value attribute.
        frame_to_be_available_and_switch_to_it: Wait for a frame to be available and switch to it.
        alert_is_present: Wait for an alert dialog to be present.
        element_to_be_selected: Wait for an element to be selected. This is typically used with <input> elements like checkboxes or radio buttons.
        element_located_to_be_selected: Similar to element_to_be_selected, but uses locator strategy.
        element_selection_state_to_be: Wait for the selection state of an element to be a certain value.
        element_located_selection_state_to_be: Similar to element_selection_state_to_be, but uses locator strategy.
        staleness_of: Wait for an element to no longer be attached to the DOM.
        element_to_be_clickable: Wait for an element to be clickable.
        visibility_of: Wait for a certain WebElement to be visible.
        presence_of_all_elements_located: Wait for all elements matching a locator to be present in the DOM.
    """

    def selenium_wait(self, timeout, expected_conditions):
        try:
            return WebDriverWait(self.context.browser, timeout).until(expected_conditions)
        except TimeoutException:
            pass

    def selenium_wait_presence(self, timeout, search_type, web_element):
        try:
            expected_conditions = ec.presence_of_element_located((search_type, web_element))
            self.selenium_wait(timeout, expected_conditions)

        except TimeoutException:
            pass

    def selenium_wait_clickable(self, timeout, search_type, web_element):
        try:
            expected_conditions = ec.element_to_be_clickable((search_type, web_element))
            self.selenium_wait(timeout, expected_conditions)

        except TimeoutException:
            pass

