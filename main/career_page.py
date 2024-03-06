from main.base_page import BasePage
from utils.locators import CareerPageLocators


class CareerPage(BasePage):
    def __init__(self, driver):
        self.locator = CareerPageLocators
        BasePage.__init__(self, driver)

    def open_dropdown(self):
        self.wait_element(self.locator.DROPDOWN_LOCATIONS)
        dropdown = self.find_element(*self.locator.DROPDOWN_LOCATIONS)
        dropdown.click()
        self.wait_element(self.locator.DROPDOWN_MENU)

    def pick_vilnius_location(self):
        dropdown_menu = self.find_element(*self.locator.DROPDOWN_MENU)
        vilnius_location = dropdown_menu.find_element(*self.locator.VILNIUS_LOCATION)
        self.hover(*self.locator.VILNIUS_LOCATION)
        vilnius_location.click()

    def press_search_button(self):
        search_button = self.find_element(*self.locator.SEARCH_BUTTON_CAREER)
        search_button.click()
