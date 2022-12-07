from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()

driver.get('https://www.magshimim.cyber.org.il/')
elem = driver.find_element(By.PARTIAL_LINK_TEXT, "רוצה להירשם")
elem.click()

if driver.current_url == "https://www.magshimim.cyber.org.il/closedreg":
    print("finished registration :-(")
else:
    print("registration opened :-)")

driver.close()
