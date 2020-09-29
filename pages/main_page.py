from selenium.webdriver.common.by import By

class MailPage():

    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        loginForm = self.find_element(By.XPATH, "//span[contains(text(),'Sign in')]")
        loginForm.click()

        loginField = self.find_element(By.XPATH, "//input[@name='loginOrEmail']")
        loginField.send_keys('master')

        passwordField = self.driver.find_element(By.ID, "user_password")
        passwordField.send_keys(password)

        loginButton = self.driver.find_element(By.NAME, "commit")
        loginButton.click()








        passwordField = driver.find_element(By.XPATH, "//input[@name='password']")
        passwordField.send_keys('test12345')

        loginButton = driver.find_element(By.XPATH, "//button[@class='new-btn new-btn-variant-contained new-btn-color-accent new-btn-size-100 new-btn-full-width styles-module__btn--1GJI-']")
        loginButton.click()
        time.sleep(5)