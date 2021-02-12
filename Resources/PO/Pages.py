import sys
import time
from random import randint
import datetime as dt
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver import ChromeOptions, Chrome
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementNotInteractableException
import os, sys, inspect


import os, sys, inspect
# fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
# extract the path to parent directory
parentdir = os.path.dirname(currentdir)
# insert path to the folder from parent directory from which the python module/ file is to be imported
sys.path.insert(0, parentdir)



from Resources.Locators import Locators
from Resources.TestData import TestData

delay=10

class BasePage():
    """This class is the parent class for all the pages in our application."""
    """It contains all common elements and functionalities available to all pages."""

    # this function is called every time a new object of the base class is created.
    def __init__(self, driver):
        self.driver=driver

    # this function performs click on web element whose locator is passed to it.
    def click(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
    
    # this function asserts comparison of a web element's text with passed in text.
    def assert_element_text(self, by_locator, element_text):
        web_element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        assert web_element.text == element_text

    # this function performs text entry of the passed in text, in a web element whose locator is passed to it.
    def enter_text(self, by_locator, text):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    # this function checks if the web element whose locator has been passed to it, is enabled or not and returns
    # web element if it is enabled.
    def is_enabled(self, by_locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))

    # this function checks if the web element whose locator has been passed to it, is visible or not and returns
    # true or false depending upon its visibility.
    def is_visible(self,by_locator):
        element=WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)
    
    # this function moves the mouse pointer over a web element whose locator has been passed to it.
    def hover_to(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        ActionChains(self.driver).move_to_element(element).perform()
        
class HomePage(BasePage):
    """Home Page of Trendyol"""
    def __init__(self, driver):
        super().__init__(driver)


    def goSignIn(self):
        self.click(Locators.CLOSE_BUTTON)
        self.click(Locators.LOGIN_DROPDOWN)


class SignInPage(BasePage):
    """SignIn Page of Trendyol"""
    def __init__(self, driver):
        super().__init__(driver)
    

    def login(self):
        self.enter_text(Locators.EMAIL_INPUT, TestData.username) 
        self.enter_text(Locators.LOGIN_PASSWORD_INPUT, TestData.password)
        self.click(Locators.LOGIN_BUTTON)
        if not Locators.MY_ACCOUNT_BUTTON: 
           print("Could not login!")

class BoutiqueListPage(BasePage):
    """Boutique List Page of Trendyol"""
    def __init__(self, driver):
        super().__init__(driver)
        

    def controlBoutique(self, driver):

        time.sleep(2)
        self.click(Locators.CLOSE_BUTTON2)

        for i in range(1,10):            
            WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, Locators.BOUTIQUE_TABS+str([i])))).click()

            time.sleep(5)
            for k in range(1,70): 
                webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
                time.sleep(0.8)
        
        unloaded_imgs = driver.find_elements_by_xpath(Locators.UNLOADED_BOUTIQUE) 
        unloaded_boutique_len = len(unloaded_imgs)
        print("unloaded boutique img", unloaded_boutique_len)

        boutique_class = driver.find_elements_by_class_name(Locators.COMPONENT_ITEM)
        boutique_len = len(boutique_class)
        print("boutique count: ",boutique_len)
        
        self.click(Locators.SCROLLUP_BUTTON) 

class ProductDetailsPage(BasePage):
    """Product Details Page for the clicked product on Trendyol"""
    def __init__(self,driver):
        super().__init__(driver)

    def clickRandomBoutique(self, driver):
        time.sleep(2)
        i = randint(1,10)

        # Rastgele bir sekmeye gidiyor
        WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, Locators.BOUTIQUE_TABS+str([i])))).click()
    
        # Rastgele bir butiğe gidiyor
        self.click(Locators.COMPONENT_ITEM)
    
        #Rastgele bir ürün seçiyor
        element_list = driver.find_elements_by_class_name(Locators.PRODUCT_ITEM)
        #j = randint(1,len(element_list))  
        time.sleep(1)
        j = randint(1,3)
        element = driver.find_element_by_xpath('//*[@id="search-app"]/div/div/div[2]/div[2]/div/div['+str(j)+']/div[1]/a/div[1]/div/img')
        element.click()

        #ürünü sepete ekliyor
        self.click(Locators.ADD_TO_BASKET_BUTTON)
