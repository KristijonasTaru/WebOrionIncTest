from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from utils.locators import CommonLocators


class BasePage(object):
    def __init__(self, driver, base_url='https://www.orioninc.com/'):
        self.base_url = base_url
        self.driver = driver
        self.timeout = 3

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def open(self, url):
        url = self.base_url + url
        self.driver.get(url)

    def hover(self,*locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    def wait_element(self, *locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(*locator))
        except TimeoutException:
            print("Element not found ")
            self.driver.quit()

    def accept_cookies(self):
        industries_link_locator = CommonLocators.INDUSTRIES_LINK
        self.hover(*industries_link_locator)
        accept_cookies_locator = CommonLocators.ACCEPT_COOKIES
        accept_cookies = self.driver.find_element(*accept_cookies_locator)
        accept_cookies.click()

    def switch_to_iframe(self, iframe_locator):
        try:
            WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(iframe_locator))
        except TimeoutException:
            print("Iframe not found")
            self.driver.quit()

    def switch_to_default_content(self):
        self.driver.switch_to.default_content()

