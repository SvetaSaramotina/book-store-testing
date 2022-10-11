###### Shop: отображение страницы товара
import time

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("SvetaTester92@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Saramotina")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
# shop_btn.click()
# book_HTML5 = driver.find_element(By.CSS_SELECTOR, '[alt="Mastering HTML5 Forms"]')
# book_HTML5.click()
# header_book = driver.find_element_by_class_name('product_title.entry-title')
# header_book_text = header_book.text
# assert header_book_text == "HTML5 Forms"
# driver.quit()



######### Shop: количество товаров в категории

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("SvetaTester92@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Saramotina")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
# shop_btn.click()
# HTML_btn = shop_btn = driver.find_element(By.LINK_TEXT, "HTML")
# HTML_btn.click()
# products = driver.find_elements(By.CSS_SELECTOR, "[id = 'content'] > ul > Li")
# assert len(products) == 3
# driver.quit()



######### Shop: сортировка товаров

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# from selenium.webdriver.support.select import Select
# driver.get("https://practice.automationtesting.in/")
# my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("SvetaTester92@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Saramotina")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
# shop_btn.click()
# element = driver.find_element(By.CLASS_NAME, "orderby")
# element_select = driver.find_element_by_css_selector('[value="menu_order"]')
# element_select_selected = element_select.get_attribute("selected")
# assert element_select_selected is not None
# element = driver.find_element(By.CLASS_NAME, "orderby")
# select = Select(element)
# select.select_by_index(4)
# element = driver.find_element(By.CLASS_NAME, "orderby")
# element_select = driver.find_element_by_css_selector('[value="price"]')
# element_select_selected = element_select.get_attribute("selected")
# assert element_select_selected is not None
# driver.quit()


###### Shop: отображение, скидка товара

# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver.get("https://practice.automationtesting.in/")
# wait = WebDriverWait(driver, 20)
# my_account_btn = driver.find_element(By.LINK_TEXT, "My Account")
# my_account_btn.click()
# username = driver.find_element_by_id("username")
# username.send_keys("SvetaTester92@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("Saramotina")
# login_btn = driver.find_element_by_css_selector('[value="Login"]')
# login_btn.click()
# shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
# shop_btn.click()
# book_android_quick_star_guide = driver.find_element_by_css_selector('img[title="Android Quick Start Guide"]')
# book_android_quick_star_guide.click()
# old_price = driver.find_element_by_css_selector(".price > del > span")
# old_price_text = old_price.text
# new_price = driver.find_element_by_css_selector(".price > ins > span")
# new_price_text = new_price.text
# assert old_price_text == "₹600.00"
# assert new_price_text  == "₹450.00"
# book_cover = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'img[title="Android Quick Start Guide"]')))
# book_cover.click()
# book_cover_close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.pp_close')))
# book_cover_close.click()
# driver.quit()


###### Shop: проверка цены в корзине

# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver.implicitly_wait(15)
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# wait = WebDriverWait(driver, 20)
# shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
# shop_btn.click()
# book_HTML5_WebApp_Development_basket_btn = driver.find_element_by_css_selector('[href="/shop/?add-to-cart=182"]')
# book_HTML5_WebApp_Development_basket_btn.click()
# time.sleep(3)
# products = driver.find_element(By.CLASS_NAME, 'cartcontents')
# products_text = products.text
# assert products_text == "1 Item"
# time.sleep(3)
# price = driver.find_element(By.CSS_SELECTOR, '.wpmenucart-contents > .amount')
# price_text = price.text
# assert price_text == "₹180.00"
# basket_btn = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
# basket_btn.click()
# time.sleep(3)
# subtotal = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '[data-title="Subtotal"]'), ""))
# total_price = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'tbody  > .order-total .woocommerce-Price-currencySymbol'), ""))
# driver.quit()



####Shop: работа в корзине

# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# wait = WebDriverWait(driver, 10)
# shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_HTML5_WebApp_Development_basket_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
# book_HTML5_WebApp_Development_basket_btn.click()
# time.sleep(3)
# book_JS_Data_Structures_basket_btn = driver.find_element_by_css_selector('[data-product_id="180"]')
# book_JS_Data_Structures_basket_btn.click()
# basket_btn = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
# basket_btn.click()
# time.sleep(3)
# delete_first_book = driver.find_element_by_css_selector('[data-product_id="182"]')
# delete_first_book.click()
# time.sleep(3)
# undo = driver.find_element(By.LINK_TEXT, "Undo?")
# undo.click()
# Quantity_books = driver.find_element_by_css_selector('[name="cart[045117b0e0a11a242b9765e79cbf113f][qty]"]')
# Quantity_books.clear()
# Quantity_books.send_keys("3")
# UPDATE_BASKET_btn = driver.find_element_by_css_selector('[name="update_cart"]')
# UPDATE_BASKET_btn.click()
# Quantity_books_value = Quantity_books.get_attribute('value')
# assert Quantity_books_value == "3"
# time.sleep(3)
# APPLY_COUPON_btn = driver.find_element_by_css_selector('[name="apply_coupon"]')
# APPLY_COUPON_btn.click()
# wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-error"), "Please enter a coupon code."))
# driver.quit()


####### Shop: покупка товара

# import time
# from selenium.webdriver.common.by import By
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# driver.maximize_window()
# driver.get("https://practice.automationtesting.in/")
# wait = WebDriverWait(driver, 10)
# shop_btn = driver.find_element(By.LINK_TEXT, "Shop")
# shop_btn.click()
# driver.execute_script("window.scrollBy(0, 300);")
# book_HTML5_WebApp_Development_basket_btn = driver.find_element_by_css_selector('[data-product_id="182"]')
# book_HTML5_WebApp_Development_basket_btn.click()
# time.sleep(3)
# basket_btn = driver.find_element_by_class_name('wpmenucart-icon-shopping-cart-0')
# basket_btn.click()
# PROCEED_TO_CHECKOUT_btn = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "checkout-button")))
# PROCEED_TO_CHECKOUT_btn.click()
# first_name = wait.until(EC.element_to_be_clickable((By.ID, "billing_first_name")))
# first_name.send_keys('Sveta')
# last_name = driver.find_element_by_id('billing_last_name')
# last_name.send_keys('Saramotina')
# email = driver.find_element_by_id('billing_email')
# email.send_keys('SvetaTester92@yandex.ru')
# phone = driver.find_element_by_id('billing_phone')
# phone.send_keys('89111111111')
# country_select = driver.find_element_by_id('s2id_billing_country')
# country_select.click()
# country_text = driver.find_element_by_id('s2id_autogen1_search')
# country_text.send_keys("Russia")
# element_country = driver.find_element_by_id('select2-results-1')
# element_country.click()
# street = driver.find_element_by_id('billing_address_1')
# street.send_keys('Lenina')
# city = driver.find_element_by_id('billing_city')
# city.send_keys('Kemerovo')
# state_country = driver.find_element_by_id('billing_state')
# state_country.send_keys('Kemerovskay oblast')
# postcode = driver.find_element_by_id('billing_postcode')
# postcode.send_keys('650904')
# driver.execute_script("window.scrollBy(0, 600);")
# time.sleep(3)
# Check_Payments_radio = driver.find_element_by_id('payment_method_cheque')
# Check_Payments_radio.click()
# PLACE_ORDER_btn = driver.find_element_by_id('place_order')
# PLACE_ORDER_btn.click()
# wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
# wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".shop_table :nth-child(3) :nth-child(3)"), "Check Payments"))
# driver.quit()