from selenium import webdriver
from selenium.webdriver.common.by import By
import smtplib
from email.mime.text import MIMEText


def send_email_smtp(msg_text):
    msg = MIMEText(msg_text)
    msg['Subject'] = 'Magshimim subscription'
    msg['From'] = 'Magshimim.subscription@gmail.com'
    msg['To'] = 'zzfima@gmail.com'

    s = smtplib.SMTP('smtp.office365.com', 587)
    s.sendmail('Magshimim.subscription@gmail.com', 'zzfima@gmail.com', msg.as_string())
    s.quit()


if __name__ == '__main__':
    driver = webdriver.Edge()

    driver.get('https://www.magshimim.cyber.org.il/')
    elem = driver.find_element(By.PARTIAL_LINK_TEXT, "רוצה להירשם")
    elem.click()

    if driver.current_url == "https://www.magshimim.cyber.org.il/closedreg":
        send_email_smtp("finished registration :-(")
    else:
        send_email_smtp("registration opened :-)")

    driver.close()
