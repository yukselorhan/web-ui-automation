from selenium.webdriver.common.by import By


class Locators():
    # --- Home Page Locators ---
    CLOSE_BUTTON=(By.CSS_SELECTOR,"body > div.fancybox-overlay.fancybox-overlay-fixed > div > div > a")
    LOGIN_DROPDOWN=(By.XPATH, "//*[@id='account-navigation-container']/div/div[1]/div[1]/p")
    LOGIN_BUTTON=(By.CSS_SELECTOR,'#account-navigation-container > div > div.account-nav-item.user-login-container > div.link.account-user > p')

    # --- SignIn Page Locators ---
    EMAIL_INPUT=(By.ID,"login-email")
    LOGIN_PASSWORD_INPUT=(By.ID,"login-password-input")
    LOGIN_BUTTON=(By.CSS_SELECTOR,'#login-register > div.lr-container > div.q-layout.login > form > button > span')
    MY_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Hesabım']")


    # --- Boutique List Page Locators ---
    CLOSE_BUTTON2=(By.CSS_SELECTOR,'#modal-root > div > div > div.modal-close')
    SCROLLUP_BUTTON=(By.CSS_SELECTOR,'#scrollToUp > div > div')
    BOUTIQUE_TABS="//*[@id='navigation-wrapper']/nav/ul/li"
    COMPONENT_ITEM='component-item'
    UNLOADED_BOUTIQUE=(By.XPATH, "//span[@class='image-container']//img[@alt='']")


    # --- Product Details Page Locators ---
    PRODUCT_ITEM='p-card-img'
    ADD_TO_BASKET_BUTTON=(By.CSS_SELECTOR, "#product-detail-app > div > div.pr-cn > div.pr-cn-in > div.pr-in-at > div.prc-inf-wrp > div > button")
    
    
    
    

    