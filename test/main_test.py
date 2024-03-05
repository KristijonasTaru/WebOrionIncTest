from main.career_page import CareerPage
from main.job_offer_page import JobOfferPage
from main.main_page import MainPage
from test.base_test import BaseTest


class MainTest(BaseTest):
    def test_hover_on_company_link_and_click_career_link(self):
        main_page = MainPage(self.driver)
        main_page.open("/")
        main_page.accept_cookies()
        main_page.hover_on_company_link()
        main_page.click_on_career()

    def test_move_to_job_offers(self):
        career_page = CareerPage(self.driver)
        career_page.open("careers/")
        career_page.accept_cookies()
        career_page.scroll_down_html()
        career_page.open_dropdown()
        career_page.pick_vilnius_location()
        career_page.press_search_button()

    def test_apply_for_job(self):
        job_offer_page = JobOfferPage(self.driver)
        job_offer_page.open("careers/jobs/?_job_location=lithuania")
        job_offer_page.accept_cookies()
        job_offer_page.move_to_first_offer()
        job_offer_page.apply_iframe_info()

        # Assert that career page is loaded
        # You can add assertions here to verify that you are on the expected page
        # For example:
        # self.assertIn("Careers", self.driver.title)
