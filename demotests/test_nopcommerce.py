import time

import pytest

from TestData.AddCustomerData import AddCustomerData
from TestData.LoginData import LoginData
from pageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


@pytest.mark.usefixtures("setup")
class TestNopCommerce(BaseClass):
    def test_nopcommerce(self, getData, getAddData):
        loginpage = LoginPage(self.driver)
        loginpage.enterEmail().clear()
        loginpage.enterEmail().send_keys(getData["username"])
        time.sleep(2)
        loginpage.enterPassword().clear()
        loginpage.enterPassword().send_keys(getData["password"])
        time.sleep(2)
        dashboardPage = loginpage.clickLoginButton()
        time.sleep(3)

        dashboardPage.click_customeroption().click()
        time.sleep(2)
        searchcustomerpage = dashboardPage.click_customerlink()

        # For adding new customer
        addcustomerpage = searchcustomerpage.clickAddButton()
        addcustomerpage.enterCustomerEmail().send_keys(getAddData["email"])
        addcustomerpage.enterCustomerPassword().send_keys(getAddData["password"])
        addcustomerpage.enterFirstName().send_keys(getAddData["fname"])
        addcustomerpage.enterLastName().send_keys(getAddData["lname"])
        addcustomerpage.selectGenderFemale().click()
        # addcustomerpage.enterDob().send_keys("25/06/1980")
        addcustomerpage.enterCompany().send_keys(getAddData["company"])
        addcustomerpage.selectTaxCheckbox().click()
        addcustomerpage.enterManageOFVendor()
        # searchcustomerpage = addcustomerpage.addSaveButton()
        addcustomerpage.addSaveButton()
        time.sleep(2)

        searchcustomerpage.enterSearchEmail().send_keys(getAddData["email"])
        time.sleep(2)
        searchcustomerpage.enterSearchFirstName().send_keys(getAddData["fname"])
        time.sleep(3)
        searchcustomerpage.enterSearchLastName().send_keys(getAddData["lname"])
        time.sleep(2)
        searchcustomerpage.clickSearchCustomerButton()
        time.sleep(2)

        # Write a code to confirm that record is present as per search criteria

        editcustomerpage = searchcustomerpage.clickEditButton()
        time.sleep(2)
        editcustomerpage.updateCustomerEmail().clear()
        editcustomerpage.updateCustomerEmail().send_keys(getAddData["update_email"])
        time.sleep(2)
        editcustomerpage.updateCustomerPassword().clear()
        editcustomerpage.updateCustomerPassword().send_keys(getAddData["update_password"])
        time.sleep(2)
        editcustomerpage.updateFirstName().clear()
        editcustomerpage.updateFirstName().send_keys(getAddData["update_fname"])
        time.sleep(2)
        editcustomerpage.updateLastName().clear()
        editcustomerpage.updateLastName().send_keys(getAddData["update_lname"])
        time.sleep(2)
        # searchcustomerpage = editcustomerpage.updateSaveButton()
        editcustomerpage.updateSaveButton()
        time.sleep(2)

        searchcustomerpage.enterSearchEmail().send_keys(getAddData["update_email"])
        time.sleep(2)
        searchcustomerpage.enterSearchFirstName().send_keys(getAddData["update_fname"])
        time.sleep(3)
        searchcustomerpage.enterSearchLastName().send_keys(getAddData["update_lname"])
        time.sleep(2)
        searchcustomerpage.clickSearchCustomerButton()
        time.sleep(2)

        editcustomerpage = searchcustomerpage.clickEditButton()
        editcustomerpage.clickDeleteCustomer()

    @pytest.fixture(params=LoginData.getTestData())
    def getData(self, request):
        return request.param

    @pytest.fixture(params=AddCustomerData.getCustomerData())
    def getAddData(self, request):
        return request.param

