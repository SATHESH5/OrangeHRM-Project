from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_03
import pytest
import time

class Test_Delete_Existing_Employee_Details:
    
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox()
        yield
        self.driver.close()
        
    def test_PIM(self, booting_function):
        self.driver.get(self.url)
        self.driver.maximize_window()
        time.sleep(4)
        # Login Functionality
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_03.PIM_Selectors.input_box_username).send_keys(TC_PIMdata_03.PIM_Data.username)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_03.PIM_Selectors.input_box_password).send_keys(TC_PIMdata_03.PIM_Data.password)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.PIM_Selectors.login_xpath).click() 
        time.sleep(3)
        
        # To delete an existing Employee
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.PIM_Selectors.PIM_xpath).click()
        time.sleep(4)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.PIM_Selectors.delete_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_03.PIM_Selectors.delete_1_xpath).click()
        time.sleep(8)
        print("Employee details successfully Deleted")
        
        
        
       