import pytest
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities import Excel_Utils
from Utilities.Logger import log_generator_class
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from Utilities.Read_Config import ReadConfigClass

@pytest.mark.usefixtures("browser_setup") #new
class Test_User_Login_002:
    driver = None #new
    home_page_url = ReadConfigClass.get_home_url()
    login_url = ReadConfigClass.get_login_url()
    registration_url = ReadConfigClass.get_registration_url()
    log = log_generator_class.loggen_method()

    @pytest.mark.regression
    @pytest.mark.user_profile
  #  @pytest.mark.dependency(depends=["test_Credkart_URL_001"])
    def test_Credkart_Login_Params_004(self, credkart_login_data):
        self.log.info("Testcase test_Credkart_URL_004 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening Browser and Landing on {self.login_url}")
        self.lp = Login_Page_Class(self.driver) #object

        self.email = credkart_login_data[0]
        self.password = credkart_login_data[1]
        self.expected_result = credkart_login_data[2]

        #Enter Email
        self.log.info(f"Entering Email --> {self.email}")
        self.lp.enter_email(self.email)

        #Enter password
        self.log.info(f"Entering password --> {self.password}")
        self.lp.enter_password(self.password)

        #Clip on login button
        self.log.info(f"Clicking on Login Button")
        self.lp.click_submit()

        self.log.info(f"Checking Login status")
        if self.lp.verify_menu() == "Pass":
            self.log.info(f"lOGIN PASS")
            self.log.info(f"Click on MENU Button")
            self.lp.click_menu()
            self.log.info(f"Click on Logout Button")
            self.lp.click_logout()
            self.log.info("Taking screenshot for Login Pass")
            self.driver.save_screenshot(f".\\Screenshots\\User_Login_Pass_{self.email}.png")
            self.log.info("Testcase test_Credkart_Login_Params_004 is Pass")
            actual_result = "lOGIN PASS"
        else:
            self.log.info(f"lOGIN FAIL")
            self.log.info("Taking screenshot for Login Fail")
            self.driver.save_screenshot(f".\\Screenshots\\User_Login_Fail.png")
            self.log.info("Testcase test_Credkart_Login_Params_004 is Fail")
            actual_result = "lOGIN FAIL"

        assert actual_result == self.expected_result, f"{actual_result} != {self.expected_result}"
        self.log.info("Testcase test_Credkart_Login_Params_004 is Completed")

    @pytest.mark.regression
    @pytest.mark.user_profile
  #  @pytest.mark.dependency(depends=["test_Credkart_URL_001"])
    def test_Credkart_Login_excel_005(self):
        excel_path = ".\\TestData\\Test_Data.xlsx"
        sheet_name = "Login_Data"
        self.log.info("Testcase test_Credkart_URL_005 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening Browser and Landing on {self.login_url}")
        self.lp = Login_Page_Class(self.driver)  # object
        self.rows = Excel_Utils.get_row_count(excel_path, sheet_name)
        print(f"Number of rows in excel sheet: {self.rows}")
        result_list = []

        for i in range(2, self.rows+1):
            self.email = Excel_Utils.read_data(excel_path, sheet_name, i, 2)
            self.password = Excel_Utils.read_data(excel_path, sheet_name, i, 3)
            self.expected_result = Excel_Utils.read_data(excel_path, sheet_name, i, 4)
            print(f"email : {self.email}")
            print(f"password : {self.password}")
            print(f"expected_result : {self.expected_result}")



            # Enter Email
            self.log.info(f"Entering Email --> {self.email}")
            self.lp.enter_email(self.email)

            # Enter password
            self.log.info(f"Entering password --> {self.password}")
            self.lp.enter_password(self.password)

            # Clip on login button
            self.log.info(f"Clicking on Login Button")
            self.lp.click_submit()

            self.log.info(f"Checking Login status")
            if self.lp.verify_menu() == "Pass":
                self.log.info(f"lOGIN PASS")
                self.log.info(f"Click on MENU Button")
                self.lp.click_menu()
                self.log.info(f"Click on Logout Button")
                self.lp.click_logout()
                self.log.info("Taking screenshot for Login Pass")
                self.driver.save_screenshot(f".\\Screenshots\\User_Login_Pass_{self.email}.png")
                actual_result = "lOGIN PASS"
            else:
                self.log.info(f"lOGIN FAIL")
                self.log.info("Taking screenshot for Login Fail")
                self.driver.save_screenshot(f".\\Screenshots\\User_Login_Fail.png")
                actual_result = "lOGIN FAIL"

            self.log.info(f"Writing data into excel file")
            Excel_Utils.write_data(excel_path, sheet_name, i, 5, actual_result)

            if self.expected_result == actual_result:
                test_case_status = 'Pass'
            else:
                test_case_status = 'Fail'
            result_list.append(test_case_status)
            Excel_Utils.write_data(excel_path, sheet_name, i, 6, test_case_status)

        if "Fail" not in result_list:
            self.log.info(f"All test cases are Passed")
            self.log.info("Testcase test_Credkart_Login_excel_005 is Pass")
            assert True

        else:
            self.log.info(f"All test cases are Failed")
            self.log.info("Testcase test_Credkart_Login_excel_005 is Fail")
            assert False

        self.log.info("Testcase test_Credkart_Login_excel_005 is Completed")
