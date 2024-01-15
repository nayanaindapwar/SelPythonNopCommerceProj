from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# from pageObjects.SearchCustomerPage import SearchCustomerPage


class AddCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    customer_email = (By.ID, "Email")
    customer_password = (By.ID, "Password")
    firstname = (By.ID, "FirstName")
    lastname = (By.ID, "LastName")
    gender_male = (By.ID, "Gender_Male")
    gender_female = (By.ID, "Gender_Female")
    dob = (By.ID, "DateOfBirth")
    company = (By.ID, "Company")
    tax_checkbox = (By.ID, "IsTaxExempt")
    manager_of_vendor = (By.ID, "VendorId")
    save_button = (By.NAME, "save")

    def enterCustomerEmail(self):
        return self.driver.find_element(*AddCustomerPage.customer_email)

    def enterCustomerPassword(self):
        return self.driver.find_element(*AddCustomerPage.customer_password)

    def enterFirstName(self):
        return self.driver.find_element(*AddCustomerPage.firstname)

    def enterLastName(self):
        return self.driver.find_element(*AddCustomerPage.lastname)

    def selectGenderMale(self):
        return self.driver.find_element(*AddCustomerPage.gender_male)

    def selectGenderFemale(self):
        return self.driver.find_element(*AddCustomerPage.gender_female)

    def enterDob(self):
        return self.driver.find_element(*AddCustomerPage.dob)

    def enterCompany(self):
        return self.driver.find_element(*AddCustomerPage.company)

    def selectTaxCheckbox(self):
        return self.driver.find_element(*AddCustomerPage.tax_checkbox)

    def enterManageOFVendor(self):
        mov_dropdown = self.driver.find_element(*AddCustomerPage.manager_of_vendor)
        select = Select(mov_dropdown)
        select.select_by_value("1")

    def addSaveButton(self):
        savebutton = self.driver.find_element(*AddCustomerPage.save_button)
        # Use JavaScript to click the button
        self.driver.execute_script("arguments[0].click();", savebutton)
        # searchcustomerpage = SearchCustomerPage(self.driver)
        # return searchcustomerpage
