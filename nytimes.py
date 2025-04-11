import requests as r
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from time import sleep

# NYT credentials
EMAIL = ''
PASSWORD = ''

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
wait = WebDriverWait(driver, 10)  # more realistic wait time

# Access Redeem site for NYT access
driver.get('https://www.nytimes.com/subscription/redeem?campaignId=8LRFH&gift_code=eb8412d177990b25')
sleep(2)

# Close popup if it appears
if driver.find_elements(By.CSS_SELECTOR, '.css-hqisq1'):
    driver.find_element(By.CSS_SELECTOR, '.css-17rpywy').click()

# Log in to NYT
email = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#email')))
email.send_keys(EMAIL)

password = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#password')))
password.send_keys(PASSWORD)

login_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-1i3jzoq-buttonBox-buttonBox-primaryButton-primaryButton-Button')))
login_button.click()

continue_button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.css-t0f7tz')))
continue_button.click()

sleep(0.1)
driver.quit()