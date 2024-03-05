import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://www.amazon.com/gp/video/storefront/?ie=UTF8&pd_rd_w=SLGDg&content-id=amzn1.sym.bdc477ed-05db-4852-a6b9-774ab16b3ebb&pf_rd_p=bdc477ed-05db-4852-a6b9-774ab16b3ebb&pf_rd_r=Y8GWZ9DFBWW0TDN0Q47Z&pd_rd_wg=RP51i&pd_rd_r=10053101-20a0-4a52-9465-faf1daa6535e&ref_=pd_gw_unk")
driver.maximize_window()

company_link = driver.find_element(By.XPATH, '//*[@id="pv-nav-container"]/div/div[1]/div/ol/li[3]/label/a')
ActionChains(driver).move_to_element(company_link).perform()

time.sleep(2)

careers_link = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="pv-nav-container"]/div/div[1]/div/ol/li[3]/div/div[2]/ul/li[1]/a')))
careers_link.click()

if 1 == 1:
    driver.session_id
