from faker import Faker
from faker.providers import DynamicProvider
from main.base_page import BasePage
from utils.locators import JobOfferLocators

fake_generator = Faker("lt_LT")
emai_domain_provider = DynamicProvider(
    provider_name="email_domain",
    elements=["@gmil.com", "@makl.net", "@yakoo.com", "@esail.com", "@drte.com",
              "@musicianistas.org", "@greeorangenmail.net", "@hometownmail.com",
              "@techietown.com", "@marchoctobermail.com"],
)
fake_generator.add_provider(emai_domain_provider)


class JobOfferPage(BasePage):
    def __init__(self, driver):
        self.locator = JobOfferLocators
        BasePage.__init__(self, driver)

    def move_to_first_offer(self):
        self.wait_element(self.locator.FIRST_JOB_OFFER)
        first_offer = self.find_element(*self.locator.FIRST_JOB_OFFER)
        first_offer.click()

    def apply_iframe_info_and_submit_filled_form(self):

        iframe_locator = self.locator.IFRAME

        try:
            self.switch_to_iframe(iframe_locator)

            self.wait_element(self.locator.SUBMIT_APPLICATION_BUTTON)
            submit_application_button = self.find_element(*self.locator.SUBMIT_APPLICATION_BUTTON)
            submit_application_button.click()

            # generate random inputs
            first_name_input = fake_generator.first_name()
            last_name_input = fake_generator.last_name()
            email_input = first_name_input + last_name_input + fake_generator.email_domain()
            phone_input = fake_generator.phone_number()
            linked_in_input = "//linked/" + first_name_input + last_name_input + email_input + phone_input
            linked_in_input = linked_in_input.replace(" ", "")

            # fill form
            first_name = self.find_element(*self.locator.FIRST_NAME)
            first_name.send_keys(first_name_input)

            last_name = self.find_element(*self.locator.LAST_NAME)
            last_name.send_keys(last_name_input)

            email = self.find_element(*self.locator.EMAIL)
            email.send_keys(email_input)

            phone = self.find_element(*self.locator.PHONE)
            phone.send_keys(phone_input)

            linked_in = self.find_element(*self.locator.LINKED_IN_PROFILE)
            linked_in.send_keys(linked_in_input)

            cv_send_keys = self.find_element(*self.locator.ATTACH_CV)
            cv_send_keys.send_keys(JobOfferLocators.CV_FILE_PATH)

            (self.find_element(*self.locator.ATTACH_COVER_LETTER)
                .send_keys(JobOfferLocators.COVER_LETTER_FILE_PATH))

            accept_terms = self.find_element(*self.locator.AGREE_CHECKBOX)
            accept_terms.click()

        finally:
            self.switch_to_default_content()
