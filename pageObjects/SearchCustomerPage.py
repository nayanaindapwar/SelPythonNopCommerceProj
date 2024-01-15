from selenium.webdriver.common.by import By
from pageObjects.AddCustomerPage import AddCustomerPage
from pageObjects.EditCustomerPage import EditCustomerPage


class SearchCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    search_email = (By.ID, "SearchEmail")
    search_firstname = (By.ID, "SearchFirstName")
    search_lastname = (By.ID, "SearchLastName")
    search_company = (By.ID, "SearchCompany")
    search_customer_button = (By.ID, "search-customers")
    add_button = (By.XPATH, "//a[normalize-space()='Add new']")
    edit_button = (By.XPATH, "//a[normalize-space()='Edit']")

    def enterSearchEmail(self):
        return self.driver.find_element(*SearchCustomerPage.search_email)

    def enterSearchFirstName(self):
        return self.driver.find_element(*SearchCustomerPage.search_firstname)

    def enterSearchLastName(self):
        return self.driver.find_element(*SearchCustomerPage.search_lastname)

    def enterSearchCompany(self):
        return self.driver.find_element(*SearchCustomerPage.search_company)

   # def clickSearchCustomerButton(self):
    #    return self.driver.find_element(*SearchCustomerPage.search_customer_button)

    def clickSearchCustomerButton(self):
        search_cust_button = self.driver.find_element(*SearchCustomerPage.search_customer_button)
        # Use JavaScript to click the button
        return self.driver.execute_script("arguments[0].click();", search_cust_button)

    def clickAddButton(self):
        self.driver.find_element(*SearchCustomerPage.add_button).click()
        addcustomerpage = AddCustomerPage(self.driver)
        return addcustomerpage

    def clickEditButton(self):
        self.driver.find_element(*SearchCustomerPage.edit_button).click()
        editcustomerpage = EditCustomerPage(self.driver)
        return editcustomerpage


