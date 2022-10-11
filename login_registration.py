##### Registration_login: регистрация аккаунта

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
# my_account_btn.click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("SvetaTester92@yandex.ru")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Saramotina")
# register_btn = driver.find_element_by_css_selector('[value="Register"]')
# register_btn.click()
# driver.quit()


###### Registration_login: логин в систему

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# driver.implicitly_wait(15)
# my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("SvetaTester92@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Saramotina")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# element = driver.find_element_by_css_selector('.woocommerce-MyAccount-navigation-link.woocommerce-MyAccount-navigation-link--customer-logout a')
# element_get_text = element.text
# assert element_get_text == "Logout"
# driver.quit()