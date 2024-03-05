from selenium.webdriver import Keys
from main.base_page import BasePage
from utils.locators import JobOfferLocators, CommonLocators


class JobOfferPage(BasePage):
    def __init__(self, driver):
        self.locator = JobOfferLocators
        BasePage.__init__(self, driver)

    def move_to_first_offer(self):
        self.wait_element(self.locator.FIRST_JOB_OFFER)
        first_offer = self.find_element(*self.locator.FIRST_JOB_OFFER)
        first_offer.click()

    def apply_iframe_info(self):
        iframe_locator = self.locator.IFRAME
        self.wait_element(self.locator.IFRAME)

        self.switch_to_iframe(iframe_locator)

        first_name = self.find_element(*self.locator.FIRST_NAME)
        first_name.send_keys("name")

        last_name = self.find_element(*self.locator.LAST_NAME)
        last_name.send_keys("lastname")

        # Switch back to default content
        self.switch_to_default_content()

    # html = self.find_element(*self.locator.HTML)
    # html.send_keys(Keys.PAGE_DOWN)