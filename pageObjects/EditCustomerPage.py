import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from pageObjects.SearchCustomerPage import SearchCustomerPage


class EditCustomerPage:
    def __init__(self, driver):
        self.driver = driver

    edit_customer_email = (By.ID, "Email")
    edit_customer_password = (By.ID, "Password")
    edit_firstname = (By.ID, "FirstName")
    edit_lastname = (By.ID, "LastName")
    edit_gender_male = (By.ID, "Gender_Male")
    edit_gender_female = (By.ID, "Gender_Female")
    edit_dob = (By.ID, "DateOfBirth")
    edit_company = (By.ID, "Company")
    edit_save_button = (By.NAME, "save")
    delete_customer = (By.ID, "customer-delete")
    del_alert = (By.ID, "customermodel-Delete-delete-confirmation-title")
    confirm_del_message = (By.XPATH, "//div[normalize-space()='Are you sure you want to delete this item?']")
    confirm_delete = (By.XPATH, "//button[normalize-space()='Delete']")
    delete_success_message = (By.XPATH, "//div[@class='alert alert-success alert-dismissable']")

    def updateCustomerEmail(self):
        return self.driver.find_element(*EditCustomerPage.edit_customer_email)

    def updateCustomerPassword(self):
        return self.driver.find_element(*EditCustomerPage.edit_customer_password)

    def updateFirstName(self):
        return self.driver.find_element(*EditCustomerPage.edit_firstname)

    def updateLastName(self):
        return self.driver.find_element(*EditCustomerPage.edit_lastname)

    def updateGenderMale(self):
        return self.driver.find_element(*EditCustomerPage.edit_gender_male)

    def updateGenderFemale(self):
        return self.driver.find_element(*EditCustomerPage.edit_gender_female)

    def updateDob(self):
        return self.driver.find_element(*EditCustomerPage.edit_dob)

    def updateCompany(self):
        return self.driver.find_element(*EditCustomerPage.edit_company)

    def updateSaveButton(self):
        editsavebutton = self.driver.find_element(*EditCustomerPage.edit_save_button)
        # Use JavaScript to click the button
        self.driver.execute_script("arguments[0].click();", editsavebutton)

    def clickDeleteCustomer(self):
        self.driver.find_element(*EditCustomerPage.delete_customer).click()

        # Wait for the modal to be present
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.del_alert))

        # Click the "Delete" button in the modal
        self.driver.find_element(*self.confirm_delete).click()

        # Wait to appear delete success message
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.delete_success_message))

        text_delete_success_message = self.driver.find_element(*EditCustomerPage.delete_success_message).text
        print(text_delete_success_message)
        assert "The customer has been deleted successfully." in text_delete_success_message





