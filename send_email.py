from seleniumwire import webdriver
from selenium.webdriver.common.by import By
import time

def send_email(user, password, recivers, subject, body):
    options = webdriver.ChromeOptions()
    options.add_argument('--disable-blink-features=AutomationControlled')
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)

    url_login = 'https://mail.google.com/'
    
    driver.get(url_login)

    login = driver.find_element(By.ID, "identifierId")
    login.send_keys(user)

    Button = driver.find_element(By.ID, "identifierNext")
    time.sleep(10)
    Button.click()
    time.sleep(10)

    Button_pass = driver.find_element(By.ID, "passwordNext")

    key = driver.find_element(By.CSS_SELECTOR, 'input[type="password"]')
    key.send_keys(password)
    time.sleep(10)
    Button_pass.click()
    time.sleep(20)

    for reciver in recivers:
        button_email = driver.find_element(By.CSS_SELECTOR, 'div.T-I.T-I-KE.L3')
        button_email.click()
        time.sleep(3)

        recipient_email = driver.find_element(By.CSS_SELECTOR, 'input[aria-label="Destinatários"]')
        recipient_email.send_keys(reciver)
        time.sleep(3)

        subject_email = driver.find_element(By.NAME, 'subjectbox')
        subject_email.send_keys(subject)
        time.sleep(3)

        body_email = driver.find_element(By.CSS_SELECTOR, "div[aria-label='Corpo da mensagem']")
        body_email.send_keys(body)
        time.sleep(3)

        send_button = driver.find_element(By.CSS_SELECTOR, ".T-I.J-J5-Ji.aoO.v7.T-I-atl.L3")
        time.sleep(3)
        send_button.click()
        time.sleep(5)

def main():
    user = 'email@gmail.com'
    password = 'password'
    recivers = ['email1@gmail.com', 'email2@gmail.com']
    subject = 'teste envio'
    body = 'Envio de email teste via RPA'
    send_email(user, password, recivers, subject, body)

if __name__ == "__main__":
    main()