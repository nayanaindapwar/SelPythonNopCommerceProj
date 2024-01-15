from selenium.webdriver.common.by import By
from pageObjects.SearchCustomerPage import SearchCustomerPage



class DashboardPage:
    def __init__(self, driver):
        self.driver = driver

    customeroption = (By.XPATH, "//a[@href='#']//p[contains(text(),'Customers')]")
    customerlink = (By.XPATH, "// a[ @ href = '/Admin/Customer/List'] // p[contains(text(), 'Customers')]")

    def click_customeroption(self):
        return self.driver.find_element(*DashboardPage.customeroption)

    def click_customerlink(self):
        self.driver.find_element(*DashboardPage.customerlink).click()
        searchcustomerpage = SearchCustomerPage(self.driver)
        return searchcustomerpage

