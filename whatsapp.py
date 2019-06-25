from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def main():
    driver = webdriver.Chrome()
    driver.get('https://web.whatsapp.com/')
    wait = WebDriverWait(driver,10)

    target = 'Name whom you want to send message'
    string = "Message"
    x_arg = '//span[contains(@title,' + target + ')]'
    group_title = wait.until(EC.element_to_be_clickable((By.XPATH, x_arg)))
    group_title.click()
    inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
    input_box = wait.until(EC.element_to_be_clickable((By.XPATH, inp_xpath)))
    for i in range(30):
        input_box.send_keys(string + Keys.ENTER)
        



if __name__ == '__main__':
    main()
