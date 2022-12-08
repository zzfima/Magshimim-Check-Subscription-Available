from selenium import webdriver
from selenium.webdriver.common.by import By
import ctypes

if __name__ == '__main__':
    driver = webdriver.Edge()

    driver.get('https://www.magshimim.cyber.org.il/')
    elem = driver.find_element(By.PARTIAL_LINK_TEXT, "רוצה להירשם")
    elem.click()

    current_url = driver.current_url
    driver.close()

    if current_url == "https://www.magshimim.cyber.org.il/closedreg":
        ctypes.windll.user32.MessageBoxW(0, "finished registration :-(", "Registration", 1)
    else:
        ctypes.windll.user32.MessageBoxW(0, "registration opened :-)", "Registration", 1)
