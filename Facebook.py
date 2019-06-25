from selenium import webdriver
import time
def main():
    driver = webdriver.Chrome()
    driver.get('https://www.facebook.com/')
    userid = driver.find_element_by_xpath('//*[@id="email"]')
    userid.send_keys('your facebook email-id')
    password = driver.find_element_by_xpath('//*[@id="pass"]')
    password.send_keys('your fb password')
    submit = driver.find_element_by_xpath('//*[@id="u_0_2"]')
    submit.click()

main()
