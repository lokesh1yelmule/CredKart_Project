import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser")

# Here we are going to add - - browser is a command line argument which is user define or custom argument you can say.

@pytest.fixture(scope="class") #new
def browser_setup(request):
    browser = request.config.getoption("--browser") # we are going to share --browser value at the time of execution(pytest command)
    if browser == "chrome":
        print("Launching Chrome browser")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    elif browser == "edge":
        print("Launching Edge browser")
        driver = webdriver.Edge()
    elif browser == "headless":
        print("Launching chrome headless browser")
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(options=chrome_options)
    else:
        print("Launching Firefox browser")
        driver = webdriver.Firefox()
    driver.maximize_window()
    driver.implicitly_wait(5)
    #attaching driver to class
    request.cls.driver = driver #new
    yield driver
    driver.quit()

# compatibility testing here we can do non-functional type , browser comp

# Use Name --> CredenceTest_5005@credence.in
# Password --> Password@123

@pytest.fixture(params=[
    ('CredenceTest_5000002334@credence.in', 'Password@123', 'login-pass'),
    ('CredenceTest_500000@credence.in','Password@123', 'login-fail'),
    ('CredenceTest_5000002334@credence.in', 'Password@1234', 'login-pass'),
    ('CredenceTest_50009@credence.in', 'Password@13', 'login-fail')
])

def credkart_login_data(request):
    return request.param

def pytest_metadata(metadata):
    #to add metadata
    metadata["Project Name"] = "Credkart"
    metadata["Module Name"] = "Login"
    metadata["Tester Name"] = "Credence"
    metadata["URL"] = "https://apps.credence.in/"
    #TO REMOVE METADATA
    del metadata["Platform"]



# 3-4-5- 10 data h to ye fixture use krenge agr jyada h to excel use krenge