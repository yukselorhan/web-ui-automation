#!/usr/bin/env python3
# -*- coding: utf-8 -*-
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
    
    def login(self,driver):
        self.enter_text(Locators.EMAIL_INPUT, TestData.username) 
        self.enter_text(Locators.LOGIN_PASSWORD_INPUT, TestData.password)
        self.click(Locators.LOGIN_BUTTON)

        try:
            driver.find_element_by_xpath(Locators.MY_ACCOUNT_BUTTON)
            
                   
        except NoSuchElementException:
             print("Could not login!")
        


class BoutiqueListPage(BasePage):
    """Boutique List Page of Trendyol"""
    def __init__(self, driver):
        super().__init__(driver)
        
    def controlBoutique(self, driver):
        scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
        screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
        WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, Locators.TAB_CONTROL)))
        self.click(Locators.CLOSE_BUTTON2)
        element=driver.find_elements_by_xpath(Locators.TAB_CONTROL)
        tab_count=len(element)

        for j in range(1,tab_count): 
            i = 1
            WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, Locators.TAB_CONTROL)))

            WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, Locators.BOUTIQUE_TABS+str([j])))).click()
            WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, Locators.TAB_CONTROL)))

            
            while True:
                # scroll one screen height each time
                driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
                i += 1
                time.sleep(scroll_pause_time)
                # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
                scroll_height = driver.execute_script("return document.body.scrollHeight;")  
                # Break the loop when the height we need to scroll to is larger than the total scroll height
                if (screen_height) * i > scroll_height:
                    break
            
            unloaded_boutique = WebDriverWait(driver,delay).until(EC.presence_of_all_elements_located((By.XPATH, "//span[@class='image-container']//img[@src='https://cdn.dsmcdn.com//web/production/small_boutique_placeholder.jpg']")))
            unloaded_boutique_len = len(unloaded_boutique)
            print("unloaded boutique img count: ", unloaded_boutique_len)
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
        i = randint(1,3)

        # Rastgele bir sekmeye gidiyor
        #WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, Locators.BOUTIQUE_TABS + '['+str(i)+']'))).click()
        element = driver.find_element_by_xpath(Locators.BOUTIQUE_TABS + f'[{str(i)}]')
        element.click()
        # Rastgele bir büyük butiğe gidiyor  
        
        self.click(Locators.COMPONENT_BIG_LIST + f'[{str(i)}]') 
        
    
        #Rastgele bir ürün seçiyor
        try:
            driver.find_element_by_xpath(Locators.PRODUCT_ITEM + f'[{str(i)}]').click()
                   
        except NoSuchElementException:
            driver.find_element_by_xpath(Locators.OTHER_PRODUCT_ITEM + f'[{str(i)}]').click()
        
  
        #ürünü sepete ekliyor
        self.click(Locators.ADD_TO_BASKET_BUTTON)
        time.sleep(4)