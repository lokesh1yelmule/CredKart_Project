#python ki file jisme save hogi usme python packge folder create krna
from logging import info

import pytest
from faker import Faker
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.Logger import log_generator_class
from pageObjects.Login_Page import Login_Page_Class
from pageObjects.Registration_Page import Registration_Page_Class
from Utilities.Read_Config import ReadConfigClass

@pytest.mark.usefixtures("browser_setup") #new
class Test_User_Profile:
    driver = None # new #initialize driver on class level as define kia #warnings hide krne ke liye otherwise warnings dikhegi anyway test cases run honge hi
    email = ReadConfigClass.get_data_for_email()
    password = ReadConfigClass.get_data_for_password()
    home_page_url = ReadConfigClass.get_home_url()
    login_url = ReadConfigClass.get_login_url()
    registration_url = ReadConfigClass.get_registration_url()
    log = log_generator_class.loggen_method()

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.flaky(reruns = 1, reruns_delay = 1) #rerun krne ke liye if fails
    @pytest.mark.dependency(name="test_Credkart_URL_001")
    def test_Credkart_URL_001(self):
        # self.log.info("This is Info")
        # self.log.warning("This is Warning")
        self.log.info("Testcase test_Credkart_URL_001 is started")
        self.driver.get(self.home_page_url)
        self.log.info(f"Opening Browser and Landing on {self.home_page_url}")
        self.log.info(f"Checking Page Title")
        if self.driver.title == "CredKart":
            self.log.info(f"Page Title is correct and landed on correct url --> {self.driver.title}")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_pass.png")
            self.log.info("Testcase test_Credkart_URL_001 is Pass")
        else:
            self.log.info(f"Page Title is incorrect and landed on url --> {self.driver.title}")
            self.log.info("Taking Screenshot")
            self.driver.save_screenshot(".\\Screenshots\\CredKart_Home_Page_fail.png")
            self.log.info("Testcase test_Credkart_URL_001 is Fail")
            assert False

        self.log.info("Testcase test_Credkart_URL_001 is Completed")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.user_profile
    @pytest.mark.flaky(reruns=1, reruns_delay=1)  # rerun krne ke liye if fails
    @pytest.mark.dependency(depends=["test_Credkart_URL_001"])
    def test_Credkart_Login_002(self):
        self.log.info("Testcase test_Credkart_URL_002 is started")
        self.driver.get(self.login_url)
        self.log.info(f"Opening Browser and Landing on {self.login_url}")
        self.lp = Login_Page_Class(self.driver) #object
        self.log.info(f"Entering Email --> {self.email}")

        # Enter Email
        # email = self.driver.find_element(By.ID, "email")
        # email.send_keys("CredenceTest_5005@credence.in")
        self.lp.enter_email(self.email)

        # Enter Password
        # password = self.driver.find_element(By.ID, "password")
        # password.send_keys("Password@123")
        self.log.info(f"Entering password --> {self.password}")
        self.lp.enter_password(self.password)

        # Click on login button
        # login_button = self.driver.find_element(By.CLASS_NAME, "btn-primary")
        # login_button.click()
        self.log.info(f"Clicking on Login Button")
        self.lp.click_submit()

        # Verify Login
        # try:
        #     # time.sleep(5)
        #     # Wait to load menu button
        #     WebDriverWait(self.driver, 5).until(
        #         expected_conditions.visibility_of_element_located((By.XPATH, "//a[@role='button']"))
        #     )
        #     self.driver.save_screenshot(".\\Screenshots\\Login_success_screenshot.png")
        #     # Click on menu Button
        #     self.driver.find_element(By.XPATH, "//a[@role='button']").click()
        #     # Click on Logout link
        #     self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
        #     print("Login Success")
        # except:
        #     self.driver.save_screenshot(".\\Screenshots\\Login_failure_screenshot.png")
        #     print("Login Failure")
        #     assert False
        self.log.info(f"Checking Login status")
        if self.lp.verify_menu() == "Pass":
            self.log.info(f"lOGIN PASS")
            self.log.info(f"Click on MENU Button")
            self.lp.click_menu()
            self.log.info(f"Click on Logout Button")
            self.lp.click_logout()
            self.log.info("Taking screenshot for Login Pass")
            self.driver.save_screenshot(".\\Screenshots\\User_Login_Pass.png")
            self.log.info("Testcase test_Credkart_URL_002 is Pass")
        else:
            self.log.info(f"lOGIN FAIL")
            self.log.info("Taking screenshot for Login Fail")
            self.driver.save_screenshot(".\\Screenshots\\User_Login_Fail.png")
            self.log.info("Testcase test_Credkart_URL_002 is Fail")
            assert False

        self.log.info("Testcase test_Credkart_URL_002 is Completed")

    @pytest.mark.smoke
    @pytest.mark.regression
    @pytest.mark.user_profile
    def test_Credkart_Registration_003(self):
        self.log.info("Testcase test_Credkart_URL_003 is started")
        self.driver.get(self.registration_url)
        self.log.info(f"Opening Browser and Landing on {self.registration_url}")

        # Click on Register link
        # self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[4]/a").click()

        name_data = Faker().name()
        print(f"name_data -> {name_data}")

        email_data = Faker().email()
        print(f"email_data --> {email_data}")

        self.rp = Registration_Page_Class(self.driver)
        self.lp = Login_Page_Class(self.driver)

        # Enter Name
        # self.driver.find_element(By.ID, "name").send_keys(name_data)
        self.log.info(f"Entering Name --> {name_data}")
        self.rp.enter_name(name_data)

        # Enter Email
        # self.driver.find_element(By.ID, "email").send_keys(email_data)
        self.log.info(f"Entering Email --> {email_data}")
        self.lp.enter_email(email_data)

        # Enter Password
        # self.driver.find_element(By.ID, "password").send_keys("Password@123")
        self.log.info(f"Entering Password")
        self.lp.enter_password("Password@123")

        # Enter Confirm Password
        # self.driver.find_element(By.ID, "password-confirm").send_keys("Password@123")
        self.log.info(f"Entering confirm Password")
        self.rp.enter_confirm_password("Password@123")

        # Click Register Button
        # self.driver.find_element(By.CLASS_NAME, "btn-primary").click()
        self.log.info(f"Click on Register Button")
        self.lp.click_submit()

        # Verify Registration

        # try:
        #     self.driver.save_screenshot(".\\Screenshots\\Registration_success_screenshot3.png")
        #     # Click on menu Button
        #     self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/a").click()
        #     # Click on Logout link
        #     self.driver.find_element(By.XPATH, "/html/body/header/nav/div/div[2]/ul[2]/li[3]/ul/li/a").click()
        #     print("Registration Success")
        # except:
        #     self.driver.save_screenshot(".\\Screenshots\\Registration_failure_screenshot4.png")
        #     print("Registration Failure")
        #     assert False
        self.log.info(f"Checking Registration Status")
        if self.lp.verify_menu() == "Pass":
            self.log.info(f"Registration Pass")
            self.log.info(f"Click on Menu Button")
            self.lp.click_menu()
            self.log.info(f"Click on Logout Button")
            self.lp.click_logout()
            self.log.info(f"Taking SCreenshot for registration Pass")
            self.driver.save_screenshot(".\\Screenshots\\User_registration_pass.png")
            self.log.info("Testcase test_Credkart_URL_003 is Pass")
        else:
            self.log.info(f"Registration Fail")
            self.log.info(f"Taking SCreenshot for registration Fail")
            self.driver.save_screenshot(".\\Screenshots\\User_registration_fail.png")
            self.log.info("Testcase test_Credkart_URL_003 is Fail")
            assert False

        self.log.info("Testcase test_Credkart_URL_003 is Completed")


# pytest -v -s -n auto --html=HTMLReports/my_reports.html --browser chrome

#pytest -v -s -n auto --alluredir="AllureReports" --browser chrome
# allure serve "AllureReports"