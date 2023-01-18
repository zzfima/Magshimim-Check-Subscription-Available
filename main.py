from selenium import webdriver
from selenium.webdriver.common.by import By
import ctypes

if __name__ == '__main__':
    driver = webdriver.Edge()

    driver.get('https://www.eventbrite.com/e/24223-registration-518511260137')
    elem = driver.find_element(By.XPATH, "//div[@data-testid='panel-info']")
    if elem.text == "Sold Out":
        ctypes.windll.user32.MessageBoxW(0, "finished registration :-(", "IDPA", 1)
    else:
        ctypes.windll.user32.MessageBoxW(0, "registration opened :-)", "IDPA", 1)

    driver.close()
