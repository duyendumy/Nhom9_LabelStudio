from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import TimeoutException, NoSuchElementException
import pytest
import allure
import constant

class TestCloudStorage():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        # driver = webdriver.Chrome(executable_path="D:/Cong cu va Moi truong phat trien phan mem/chromedriver/chromdriver.exe")
        driver.implicitly_wait(15)
        # driver.maximize_window
        driver.get("http://localhost:8080")
        # driver.get(constant.url)
        yield
        driver.close()
        driver.quit()
        
    
    
    
        
    
    