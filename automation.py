from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
from dotenv import load_dotenv
load_dotenv()

# Consts
DRIVER_PATH = os.getenv("DRIVER_PATH")
PDF_PATH = os.getenv("PDF_PATH")
# Private info
FULL_NAME = os.getenv("FULL_NAME")
ID = os.getenv("ID")
EMAIL = os.getenv("EMAIL")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

driver = webdriver.Chrome(DRIVER_PATH)
try:
    # Submitting the standard online form
    driver.get("https://motssl5.mot.gov.il/FORMS/he/request-parking-badge/lang/he-IL")
    name_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "ff_nm_name[]")))
    name_input.send_keys(FULL_NAME)
    driver.find_element_by_name("ff_nm_files_citizen_id[]").send_keys(ID)
    driver.find_element_by_name("ff_nm_email[]").send_keys(EMAIL)
    driver.find_element_by_name("ff_nm_file1[]").send_keys(PDF_PATH)
    driver.find_element_by_id("bfSubmitButton").click()

    # Submitting a different form because the first one isn't working
    driver.get("https://motssl5.mot.gov.il/FORMS/he/parking-badge/lang/he-IL")
    name_input = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.NAME, "ff_nm_full_name[]")))
    name_input.send_keys("יעל נוב")
    driver.find_element_by_name("ff_nm_teudat_zehut_rid[]").send_keys(ID)
    driver.find_element_by_name("ff_nm_phone[]").send_keys(PHONE_NUMBER)
    driver.find_element_by_name("ff_nm_content_ttl[]").send_keys(
        "הגשתי כבר המון פעמים בגשה לקבלת תו נכה בטופס ההגשה המקוון וגם בטופס הזה. בשני המקרים אתם לא מגיבים. אבקש לטפל בבקשה במהרה, אנחנו מחכים כבר מעל חודש וזה חשוב מאוד.")
    driver.find_element_by_name("ff_nm_file[]").send_keys(PDF_PATH)
    driver.find_element_by_name("ff_nm_email[]").send_keys(EMAIL)
    driver.find_element_by_id("bfSubmitButton").click()
finally:
    driver.quit()

