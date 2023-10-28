from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from Test_Data import TC_PIMdata_02
import pytest
import time

class Test_Edit_Existing_Employee_Details:
    
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
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_username).send_keys(TC_PIMdata_02.PIM_Data.username)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_password).send_keys(TC_PIMdata_02.PIM_Data.password)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.login_xpath).click() 
        time.sleep(3)
        
        # To edit the added employee personal details
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.PIM_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.edit_xpath).click()
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_FirstName).send_keys(Keys.CONTROL+"a")
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_FirstName).send_keys(Keys.DELETE)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_FirstName).send_keys(TC_PIMdata_02.PIM_Data.FirstName)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_MiddleName).send_keys(Keys.CONTROL+"a")
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_MiddleName).send_keys(Keys.DELETE)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_MiddleName).send_keys(TC_PIMdata_02.PIM_Data.MiddleName)
        time.sleep(3)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_LastName).send_keys(Keys.CONTROL+"a")
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_LastName).send_keys(Keys.DELETE)
        time.sleep(2)
        self.driver.find_element(by=By.NAME, value=TC_PIMdata_02.PIM_Selectors.input_box_LastName).send_keys(TC_PIMdata_02.PIM_Data.LastName)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.otherID_xpath).send_keys(Keys.CONTROL+"a")
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.otherID_xpath).send_keys(Keys.DELETE)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.otherID_xpath).send_keys(TC_PIMdata_02.PIM_Data.otherID_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.license_xpath).send_keys(TC_PIMdata_02.PIM_Data.license_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.license_date_xpath).send_keys(TC_PIMdata_02.PIM_Data.license_date_data)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.SSN_xpath).send_keys(TC_PIMdata_02.PIM_Data.SSN_data)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.SIN_xpath).send_keys(TC_PIMdata_02.PIM_Data.SIN_data)
        time.sleep(2)
        nationality_box = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.national_xpath).send_keys(Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        marital_box = self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.marital_xpath)
        marital_box.send_keys(Keys.DOWN, Keys.ENTER)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.male_xpath).click()
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.date_xpath).send_keys(TC_PIMdata_02.PIM_Data.birth_data)
        time.sleep(2)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.click_xpath)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.save_xpath_1).click()
        time.sleep(5)
        #Custom fields
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.custom_xpath).send_keys(Keys.DOWN, Keys.DOWN, Keys.DOWN, Keys.ENTER)
        time.sleep(3)
        self.driver.find_element(by=By.XPATH, value=TC_PIMdata_02.PIM_Selectors.save_xpath_2).click()
        time.sleep(6)
        print("Successfull Employee Details Addition")
        
        
            
            
            