import unittest

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from main.career_page import CareerPage
from main.job_offer_page import JobOfferPage
from main.main_page import MainPage
from test.base_test import BaseTest


class MainTest(BaseTest, unittest.TestCase):
    def test_a_hover_on_company_link_and_click_career_link(self):
        main_page = MainPage(self.driver)
        main_page.open("/")
        main_page.accept_cookies()
        main_page.hover_on_company_link()
        main_page.click_on_career()

        # change expected_result to fail the test
        actual_results = self.driver.find_element(By.XPATH, "//h3[normalize-space()='Find Open Jobs']").text
        expected_result = 'Find Open Jobs'
        self.assertEqual(expected_result, actual_results, "The 'Find Open Jobs' element is not visible")

    def test_b_move_to_job_offers(self):
        career_page = CareerPage(self.driver)
        career_page.open("careers/")
        career_page.accept_cookies()
        career_page.open_dropdown()
        career_page.pick_vilnius_location()
        career_page.press_search_button()

        actual_result = self.driver.find_element(By.XPATH, "//h1[@class='article-title h1']").text
        expected_result = "Careers"
        self.assertEqual(expected_result, actual_result, "The 'Careers' element is not visible")

    def test_c_apply_for_job(self):
        job_offer_page = JobOfferPage(self.driver)
        job_offer_page.open("careers/jobs/?_job_location=lithuania")
        job_offer_page.accept_cookies()
        job_offer_page.move_to_first_offer()
        job_offer_page.apply_iframe_info_and_submit_filled_form()

        # assertFalse to fail test
        WebDriverWait(self.driver, 5).until(EC.frame_to_be_available_and_switch_to_it(
            (By.XPATH, "//iframe[@id='grnhse_iframe']")))
        actual_result = self.driver.find_element(By.XPATH, "//div[@id='validate_resume_error']")
        element_displayed = actual_result.is_displayed()
        self.assertTrue(element_displayed, "The 'Error message' element is not visible")

        self.driver.switch_to.default_content()

