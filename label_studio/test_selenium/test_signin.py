from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.core.utils import ChromeType
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import pytest
import allure
import constant

class TestSingIn():
    @pytest.fixture()
    def test_setup(self):
        global driver
        chrome_service = Service(ChromeDriverManager(chrome_type=ChromeType.GOOGLE).install())
        chrome_options = Options()
        options = [
        "--headless",
        "--disable-gpu",
        "--window-size=1920,1200",
        "--ignore-certificate-errors",
        "--disable-extensions",
        "--no-sandbox",
        "--disable-dev-shm-usage"
        ]
        for option in options:
            chrome_options.add_argument(option)
        driver = webdriver.Chrome(service=chrome_service, options=chrome_options)
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        # driver.get(constant.url)
        yield
        driver.close()
        driver.quit()
        
    @allure.description("Validate Label Studio with valid login credentials")  
    @allure.severity(severity_level = "CRITICAL")  
    def test_login_by_valid_user(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Entering a valid email " + email_data):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            
        with allure.step("Entering a valid password " + password_data):
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)
            
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        assert "projects" in driver.current_url
        
    
    @allure.description("Validate Label Studio with invalid password")  
    @allure.severity(severity_level = "NORMAL")  
    def test_login_by_incorrect_password(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "incorrectpassword" 
        with allure.step("Entering a valid email " + email_data):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            
        with allure.step("Entering a invalid password " + password_data):
            password = driver.find_element(By.ID,'password')
            password.send_keys( password_data)
            
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text     
        if text == "The email and password you entered don't match.":
                allure.attach(driver.get_screenshot_as_png(),
                              name="Invalid Credentials", attachment_type=allure.attachment_type.PNG)
            
            
    @allure.description("Validate Label Studio with invalid email")  
    @allure.severity(severity_level = "NORMAL")          
    def test_login_by_incorrect_email(self, test_setup):
        email_data = "invalidemail@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Entering a invalid email " + email_data):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
        
        with allure.step("Entering a valid password " + password_data):
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)
            
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
           allure.attach(driver.get_screenshot_as_png(),
                              name="Invalid Credentials", attachment_type=allure.attachment_type.PNG)
            
    @allure.description("Validate Label Studio with invalid login credentials")  
    @allure.severity(severity_level = "NORMAL")      
    def test_login_by_invalid_email(self, test_setup):
        email_data = "invalidemail@gmail.com"
        password_data = "1234" 
        with allure.step("Entering a invalid email " + email_data):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            
        with allure.step("Entering a invalid password " + password_data):
            password = driver.find_element(By.ID,'password')   
            password.send_keys(password_data)
            
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            allure.attach(driver.get_screenshot_as_png(),
                              name="Invalid Credentials", attachment_type=allure.attachment_type.PNG)
    
    @allure.description("Validate Label Studio with not fill field login")  
    @allure.severity(severity_level = "NORMAL")  
    def test_not_fill_field_login(self, test_setup):
        email_data = ""
        password_data = "" 
        with allure.step("Not fill email"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            
        with allure.step("Not fill password"):
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)
            
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
             allure.attach(driver.get_screenshot_as_png(),
                              name="Invalid Credentials", attachment_type=allure.attachment_type.PNG)
    
     
    