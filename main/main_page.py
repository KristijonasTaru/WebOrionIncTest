from main.base_page import BasePage
from utils.locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        self.locator = MainPageLocators
        BasePage.__init__(self, driver)

    def hover_on_company_link(self):
        self.hover(*self.locator.LANGUAGE_CHANGE)
        self.wait_element(self.locator.COMPANY_LINK)
        self.hover(*self.locator.COMPANY_LINK)

    def click_on_career(self):
        self.wait_element(self.locator.CAREER_LINK)
        career_link = self.find_element(*self.locator.CAREER_LINK)
        career_link.click()

