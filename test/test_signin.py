from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest

class TestSingIn():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        driver.maximize_window
        yield
        driver.close()
        driver.quit()
        
    def test_login_by_valid_user(self, test_setup):
        driver.get("http://localhost:8080")
        email = driver.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = driver.find_element(By.ID,'password')
        # Send your password
        password.send_keys("1234asdfASDF")
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
    
    def test_login_by_incorrect_password(self, test_setup):
        driver.get("http://localhost:8080")
        email = driver.find_element(By.ID,'email')
        # Send your email
        email.send_keys("labelstudio09@gmail.com")
        password = driver.find_element(By.ID,'password')
        # Send your incorrect password
        password.send_keys("incorrectpassword")
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")
            
    def test_login_by_incorrect_email(self, test_setup):
        driver.get("http://localhost:8080")
        email = driver.find_element(By.ID,'email')
        # Send your incorrect email
        email.send_keys("incorrectemail")
        password = driver.find_element(By.ID,'password')
        # Send your incorrect password
        password.send_keys("1234asdfASDF")
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")
        
    def test_login_by_invalid_email(self, test_setup):
        driver.get("http://localhost:8080")
        email = driver.find_element(By.ID,'email')
        # Send your invalid email
        email.send_keys("invalidemail@gmail.com")
        password = driver.find_element(By.ID,'password')
        # Send your invalid password
        password .send_keys("1234")
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")
    
    def test_not_fill_field_login(self, test_setup):
        driver.get("http://localhost:8080")
        email = driver.find_element(By.ID,'email')
        # Send your invalid email
        email.send_keys("")
        password = driver.find_element(By.ID,'password')
        # Send your invalid password
        password.send_keys("")
        login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
        login_button.click()
        error = driver.find_element(By.CLASS_NAME,"error")
        text = error.text
        if text == "The email and password you entered don't match.":
            print("Pass")
        

 