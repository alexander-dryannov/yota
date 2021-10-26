import os, sys
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from fake_useragent import UserAgent
from dotenv import load_dotenv, find_dotenv

def create_driver(fua):
    options = webdriver.FirefoxOptions()
    options.set_preference("general.useragent.override", fua.opera)
    return webdriver.Firefox(options=options)

def helper(position):
    time.sleep(10)
    elements_speed = driver.find_elements(By.CLASS_NAME, "tick.ng-star-inserted")
    elements_speed[position].click()
    buttons = driver.find_elements(By.TAG_NAME, "button")
    for button in buttons:
        if button.text == "ПОДКЛЮЧИТЬ": 
            button.click()
        else: 
            pass

def login_yota(driver):
    try:
        driver.get("https://my.yota.ru/login")
        time.sleep(3)
        elements_input = driver.find_elements(By.CSS_SELECTOR, "input")
        elements_input[1].send_keys(os.getenv("password"))
        button = driver.find_elements(By.TAG_NAME, "button")[2]
        button.click()
    except Exception as ex:
        print(ex)
        driver.close()
        driver.quit()

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    fua = UserAgent()
    driver = create_driver(fua)
    login_yota(driver)
    if sys.argv[1] == "up":
        helper(12)
    elif sys.argv[1] == "down":
        helper(1)
    driver.close()
    driver.quit()