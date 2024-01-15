
from selenium.webdriver.common.by import By
from pageObjects.DashboardPage import DashboardPage

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    user_email = (By.ID, "Email")
    user_password = (By.ID, "Password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")

    def enterEmail(self):
        return self.driver.find_element(*LoginPage.user_email)

    def enterPassword(self):
        return self.driver.find_element(*LoginPage.user_password)

    def clickLoginButton(self):
        loginbutton = self.driver.find_element(*LoginPage.login_button)
        # Use JavaScript to click the button
        self.driver.execute_script("arguments[0].click();", loginbutton)
        dashboardPage = DashboardPage(self.driver)
        return dashboardPage


