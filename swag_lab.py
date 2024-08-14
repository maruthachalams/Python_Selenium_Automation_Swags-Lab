import time
import requests
import re
from selenium import webdriver
from selenium.webdriver.common.by import By

main_output = "Sl.No"+'\t'+"Login_ID"+'\t'+"Password"+'\t'+"Login_Test_Status"+'\t'+"Order_Status"+'\n'
with open("MainOutput.txt",'w') as SL:
    SL.write(main_output)

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")
driver.maximize_window()
time.sleep(5)

user_names = driver.find_element(By.XPATH, '//*[@id="login_credentials"]')
user_names_text = user_names.text

usernames_list = user_names_text.split("\n")
usernames_list.pop(0)

print(usernames_list)
password = "secret_sauce"

sln = 0

for user_name in usernames_list:
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="user-name"]').send_keys(user_name)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password)
    time.sleep(3)
    driver.find_element(By.XPATH, '//*[@id="login-button"]').click()
    time.sleep(3)
    ProductPageContent = driver.page_source
    try:
        product_key = re.findall(r'title\">\s*([^<]*?)\s*</span>',str(ProductPageContent))[0]
        if (product_key == 'Products'):
            print("Login test passed")
            test1 = "login_test_passed"
            product_item_click = driver.find_element(By.XPATH,'//*[@id="item_4_title_link"]/div').click()
            time.sleep(3)
            add_to_cart_click = driver.find_element(By.XPATH,'//*[@id="add-to-cart"]').click()
            time.sleep(3)
            back_to_products = driver.find_element(By.XPATH,'//*[@id="back-to-products"]').click()
            time.sleep(3)
            product_item_click_2 = driver.find_element(By.XPATH,'//*[@id="item_5_title_link"]/div').click()
            time.sleep(3)
            add_to_cart_click_2 = driver.find_element(By.XPATH,'//*[@id="add-to-cart"]').click()
            time.sleep(3)
            back_to_products_2 = driver.find_element(By.XPATH,'//*[@id="back-to-products"]').click()
            time.sleep(3)
            direct_add_to_cart_click = driver.find_element(By.XPATH,'//*[@id="add-to-cart-test.allthethings()-t-shirt-(red)"]').click()
            time.sleep(3)
            shopping_cart_click = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
            time.sleep(3)
            continue_shopping = driver.find_element(By.XPATH,'//*[@id="continue-shopping"]').click()
            time.sleep(3)
            remove_cart_item = driver.find_element(By.XPATH,'//*[@id="remove-sauce-labs-fleece-jacket"]').click()
            time.sleep(3)
            add_to_cart_click_3 = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-bolt-t-shirt"]').click()
            time.sleep(3)
            shopping_cart_click = driver.find_element(By.XPATH,'//*[@id="shopping_cart_container"]/a').click()
            time.sleep(3)
            checkout = driver.find_element(By.XPATH,'//*[@id="checkout"]').click()
            time.sleep(3)
            checkout_first_name_click = driver.find_element(By.XPATH, '//*[@id="first-name"]').click()
            time.sleep(5)
            checkout_first_name = driver.find_element(By.XPATH, '//*[@id="first-name"]').send_keys("mahas")
            time.sleep(3)
            checkout_last_name_click = driver.find_element(By.XPATH, '//*[@id="last-name"]').click()
            time.sleep(5)
            checkout_last_name = driver.find_element(By.XPATH, '//*[@id="last-name"]').send_keys("pillai")
            time.sleep(3)
            postal_code_click = driver.find_element(By.XPATH, '//*[@id="postal-code"]').click()
            time.sleep(5)
            postal_code = driver.find_element(By.XPATH, '//*[@id="postal-code"]').send_keys("642001")
            time.sleep(3)
            continue_click = driver.find_element(By.XPATH,'//*[@id="continue"]').click()
            time.sleep(3)
            finish_click = driver.find_element(By.XPATH,'//*[@id="finish"]').click() 
            time.sleep(3)
            element = driver.find_element(By.XPATH,'//*[@id="checkout_complete_container"]/h2').text
            print(element)
            assert element == 'Thank you for your order!', "Expected 'Thank you for your order!' but found: {}".format(element)
            print("Order Completed")
            test2 = "Order_completed"
            time.sleep(3)
            back_home_click = driver.find_element(By.XPATH,'//*[@id="back-to-products"]').click()
            sln += 1
            main_output = str(sln)+'\t'+str(user_name)+'\t'+str(password)+'\t'+str(test1)+'\t'+str(test2)+'\n' 
            with open("MainOutput.txt",'a') as SL:
                SL.write(main_output)
        else:
            test1 = "Login_test_faild"
            test2 = "Login_failed"
            print("Login test failed")
            sln += 1
            main_output = str(sln)+'\t'+str(user_name)+'\t'+str(password)+'\t'+str(test1)+'\t'+str(test2)+'\n' 
            with open("MainOutput.txt",'a') as SL:
                SL.write(main_output)
    except:
        test1 = "Login_failed"
        test2 = "Login_failed"
        print("Log in failed")
        sln += 1
        main_output = str(sln)+'\t'+str(user_name)+'\t'+str(password)+'\t'+str(test1)+'\t'+str(test2)+'\n' 
        with open("MainOutput.txt",'a') as SL:
            SL.write(main_output)














