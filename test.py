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


delay = 10

# browser ı parametre olarak alıyoruz
def choose_driver():
    # webdriver chrome ise
    if sys.argv[1] == "chrome":
        opts = ChromeOptions()
        opts.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opts)
        return driver
    # webdriver firefox ise
    elif sys.argv[1] == "firefox":
        driver = webdriver.Firefox()
        return driver
    else:
        print("driver ismini doğru giriniz")
        return 0




def login(driver):

    username = "yukselorhaan@gmail.com"
    password = "1q2w3e4r"

    driver.get("https://www.trendyol.com/")
    time.sleep(1)
    #webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH,"/html/body/div[7]/div/div/a"))).click()
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#account-navigation-container > div > div.account-nav-item.user-login-container > div.link.account-user > p'))).click()
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID,"login-email"))).send_keys(username)
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.ID,"login-password-input"))).send_keys(password)
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#login-register > div.lr-container > div.q-layout.login > form > button > span'))).click()
    #webdriver.ActionChains(driver).send_keys(Keys.ESCAPE).perform()
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#modal-root > div > div > div.modal-close'))).click()

   
# tablara tıklıyor ve fotoları kontrol ediyor
def tabs_click(driver):
    boutique_tabs = "//*[@id='navigation-wrapper']/nav/ul/li"
    
   
    # tabların xpathler leri 1 2 3 diye gidiyor. xpathlere lere göre tablarda geziyor range(1,9)
    for i in range(1,10):
        time.sleep(3)
        WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, boutique_tabs+str([i])))).click()
        

        # butiklerin kaç tane olduğunu buluyor
        time.sleep(5)
        for k in range(1,70): 
            webdriver.ActionChains(driver).send_keys(Keys.SPACE).perform()
            time.sleep(0.8)
            
            unloaded_imgs = driver.find_elements_by_css_selector("img[src*='placeholder']") 
            for u in unloaded_imgs:
                print('unloaded butik img:{}' .format(u.get_attribute('alt')))

        boutique_class = driver.find_elements_by_class_name('component-item')
        boutique_len = len(boutique_class)
        print("butik sayısı: ",boutique_len)
        WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR,'#scrollToUp > div > div'))).click()

        
def click_random_boutique(driver):
    time.sleep(2)
    i = randint(1,10)
    boutique_tabs = "//*[@id='navigation-wrapper']/nav/ul/li"
    random_boutique = 'component-item'
    add_to_basket_button = "#product-detail-app > div > div.pr-cn > div.pr-cn-in > div.pr-in-at > div.prc-inf-wrp > div > button"

    # Rastgele bir sekmeye gidiyor
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.XPATH, boutique_tabs+str([i])))).click()
    
    # Rastgele bir butiğe gidiyor
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CLASS_NAME, random_boutique))).click()
    
    
    #Rastgele bir ürün seçiyor
    element_list = driver.find_elements_by_class_name('p-card-img')
    #j = randint(1,len(element_list))  
    time.sleep(1)
    j = randint(1,3)
    element = driver.find_element_by_xpath('//*[@id="search-app"]/div/div/div[2]/div[2]/div/div['+str(j)+']/div[1]/a/div[1]/div/img')
    element.click()

    #ürünü sepete ekliyor
    WebDriverWait(driver,delay).until(EC.element_to_be_clickable((By.CSS_SELECTOR, add_to_basket_button))).click()
    

        
        


browser = choose_driver()
browser.maximize_window()
login(browser)
tabs_click(browser)
click_random_boutique(browser)