from selenium.webdriver.common.by import By


class CommonLocators(object):
    ACCEPT_COOKIES = (By.XPATH, '//*[@id="hs-eu-confirmation-button"]')
    INDUSTRIES_LINK = (By.XPATH, '/html[1]/body[1]/header[1]/div[1]/nav[1]/div[2]/ul[1]/li[1]/a[1]/span[1]')
class MainPageLocators(object):
    LANGUAGE_CHANGE = (By.XPATH, '/html[1]/body[1]/header[1]/div[1]/nav[1]/div[3]/ul[1]')
    COMPANY_LINK = (By.XPATH, '//*[@id="primaryMenu"]/ul/li[5]')
    CAREER_LINK = (By.XPATH, "/html/body/header/div/nav/div[2]/ul/li[5]/div/div/div/div[1]/a[1]")


class CareerPageLocators(object):
    HTML = (By.TAG_NAME, 'html')
    DROPDOWN_LOCATIONS = (By.XPATH, "(//b[@class='button'])[1]")
    DROPDOWN_MENU = (By.XPATH, "(//div[@class='selectric-items'])[1]")
    VILNIUS_LOCATION = (By.XPATH, "/html[1]/body[1]/main[1]/article[1]/div[1]"
                                  "/div[1]/div[2]/div[1]/div[1]/div[1]/div[3]"
                                  "/div[1]/ul[1]/li[12]")
    SEARCH_BUTTON_CAREER = (By.XPATH, "//button[normalize-space()='Search']")


class JobOfferLocators(object):
    FIRST_JOB_OFFER = (By.XPATH, "//div[@class='row ajax-target']/*[1]")
    IFRAME = (By.XPATH, "//iframe[@id='grnhse_iframe']")
    APPLY_HEADING = (By.XPATH, "//h2[@class='heading']")
    FIRST_NAME = (By.XPATH, '//*[@id="first_name"]')
    LAST_NAME = (By.XPATH, "//input[@id='last_name']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PHONE = (By.XPATH, "//input[@id='phone']")
    ATTACH_CV = (By.XPATH, "//button[@aria-describedby='resume-allowable-file-types']")
    ATTACH_COVER_LETTER = (By.XPATH, "//button[@aria-describedby='resume-allowable-file-types']")
    LINKED_IN_PROFILE = (By.XPATH, "//input[@id='job_application_answers_attributes_0_text_value']")
    AGREE_CHECKBOX = (By.XPATH, "//input[@id='job_application_data_compliance_gdpr_processing_consent_given']")

