from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import pytest
import allure
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import constant


class TestExportData():
    @pytest.fixture()
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.implicitly_wait(15)
        driver.maximize_window
        driver.get("http://localhost:8080")
        driver.get(constant.url)
        yield
        driver.close()
        driver.quit()
    
    @allure.description("Export JSON")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_export_json(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to export"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
            export__btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Export"]')))
            export__btn.click()

   
        with allure.step("Export data as file Json "):
            export_button = driver.find_element(By.XPATH, '//button[contains(@class, "ls-export-page__finish") and text()="Export"]')
            export_button.click()    
            time.sleep(5)
        
        with allure.step("Check reality format like expected format"):
            root_path = os.path.expanduser("~")
            download_dir = os.path.join(root_path, "Downloads")
            all_files  = os.listdir(download_dir)
            sorted_files = sorted(all_files , key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)
            most_recent_file = sorted_files[0]
            format_file = os.path.splitext(most_recent_file)[1]
            assert format_file == '.json', f"File extension {format_file} does not match {'.json'}"
        
    @allure.description("Export JSON_MIN")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_export_json_min(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to export"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
            export__btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Export"]')))
            export__btn.click()
    
   
        with allure.step("Export data as file JSON MIN"):
            export_div = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"ls-formats__name") and text()="JSON-MIN"]')))
            export_div.click()
            export_button = driver.find_element(By.XPATH, '//button[contains(@class, "ls-export-page__finish") and text()="Export"]')
            export_button.click()   
            time.sleep(5)
        
        with allure.step("Check reality format like expected format"):
            root_path = os.path.expanduser("~")
            download_dir = os.path.join(root_path, "Downloads")
            all_files  = os.listdir(download_dir)
            sorted_files = sorted(all_files , key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)
            most_recent_file = sorted_files[0]
            format_file = os.path.splitext(most_recent_file)[1]
            assert format_file == '.json', f"File extension {format_file} does not match {'.json'}"
            
    @allure.description("Export CSV")  
    @allure.severity(severity_level = "CRITICAL") 
    def test_export_csv(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to export"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
            export__btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Export"]')))
            export__btn.click()
    
   
        with allure.step("Export data as file CSV"):
            export_div = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"ls-formats__name") and text()="CSV"]')))
            export_div.click()
            export_button = driver.find_element(By.XPATH, '//button[contains(@class, "ls-export-page__finish") and text()="Export"]')
            export_button.click()   
            time.sleep(5)
        
        with allure.step("Check reality format like expected format"):
            root_path = os.path.expanduser("~")
            download_dir = os.path.join(root_path, "Downloads")
            all_files  = os.listdir(download_dir)
            sorted_files = sorted(all_files , key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)
            most_recent_file = sorted_files[0]
            format_file = os.path.splitext(most_recent_file)[1]
            assert format_file == '.csv', f"File extension {format_file} does not match {'.csv'}"


    @allure.description("Export TSV")  
    @allure.severity(severity_level = "CRITICAL")        
    def test_export_tsv(self, test_setup):
        email_data = "labelstudio09@gmail.com"
        password_data = "1234asdfASDF" 
        with allure.step("Sign in Label Studio"):
            email = driver.find_element(By.ID,'email')
            email.send_keys(email_data)
            password = driver.find_element(By.ID,'password')
            password.send_keys(password_data)                   
            login_button = driver.find_element(By.CLASS_NAME,'ls-button_look_primary')
            login_button.click()
            
        with allure.step("Select project to export"):
            list_project = driver.find_elements(By.CLASS_NAME, "ls-projects-page__link")
            list_project[0].click()
            export__btn = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//button[contains(@class, "dm-button_size_medium") and text()="Export"]')))
            export__btn.click()
    
   
        with allure.step("Export data as file TSV"):
            export_div = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '//div[contains(@class,"ls-formats__name") and text()="TSV"]')))
            export_div.click()
            export_button = driver.find_element(By.XPATH, '//button[contains(@class, "ls-export-page__finish") and text()="Export"]')
            export_button.click()   
            time.sleep(5)
        
        with allure.step("Check reality format like expected format"):
            root_path = os.path.expanduser("~")
            download_dir = os.path.join(root_path, "Downloads")
            all_files  = os.listdir(download_dir)
            sorted_files = sorted(all_files , key=lambda x: os.path.getmtime(os.path.join(download_dir, x)), reverse=True)
            most_recent_file = sorted_files[0]
            format_file = os.path.splitext(most_recent_file)[1]
            assert format_file == '.csv', f"File extension {format_file} does not match {'.csv'}"
    