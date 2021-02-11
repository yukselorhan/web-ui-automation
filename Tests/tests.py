import unittest
import HtmlTestRunner
from selenium import webdriver
import os, sys, inspect
from Resources.Locators import Locators
from Resources.TestData import TestData
from Resources.PO import Pages
from Resources.PO.Pages import BasePage, HomePage, SignInPage, BoutiqueListPage, ProductDetailsPage


#Base Class for the tests
class Test_Base(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(TestData.BASE_URL)
        #browser should be loaded in maximized window
        self.driver.maximize_window()
    
    def tearDown(self):
        # To do the cleanup after test has executed.
        self.driver.close()
        self.driver.quit()


# Test class containing methods corresponding to testcases.
class Test_Trendyol_Search(Test_Base):
    def setUp(self):
        # to call the setUp() method of base class or super class.
        super().setUp()

    def test_home_page_loaded_successfully(self):
        # instantiate an object of HomePage class. Remember when the constructor of HomePage class is called
        # it opens up the browser and navigates to Home Page of the site under test.
        self.homePage=HomePage(self.driver)
        self.homePage.goSignIn()
        # assert if the title of Home Page contains Trendyol
        self.assertIn(TestData.HOME_PAGE_TITLE, self.homePage.driver.title)
 

    def test_sign_in_successfully(self):
        self.signInPage=SignInPage(self.driver)
        self.signInPage.login()

    def test_boutique_list_successfully(self):
        self.boutiqueListPage=BoutiqueListPage(self.driver)
        self.productListPage=ProductDetailsPage(self.driver)
    
    def test_add_to_basket(self):
        self.productListPage=ProductDetailsPage(self.driver)
        self.productListPage.clickRandomBoutique(self.driver)
        
    def test_all(self):
        self.homePage=HomePage(self.driver)
        self.homePage.goSignIn()
        self.signInPage=SignInPage(self.driver)
        self.signInPage.login()
        self.boutiqueListPage=BoutiqueListPage(self.driver)
        self.boutiqueListPage.controlBoutique(self.driver)
        self.productListPage=ProductDetailsPage(self.driver)
        self.productListPage.clickRandomBoutique(self.driver)
     