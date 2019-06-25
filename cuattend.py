from selenium import webdriver
import time
def main():
    driver = webdriver.Chrome()
    driver.get('https://uims.cuchd.in/uims/')
    userid = driver.find_element_by_xpath('//*[@id="txtUserId"]')
    userid.send_keys('your UID')
    submit = driver.find_element_by_xpath('//*[@id="btnNext"]')
    submit.click()
    password = driver.find_element_by_xpath('//*[@id="txtLoginPassword"]')
    password.send_keys('Your password')
    submit = driver.find_element_by_xpath('//*[@id="btnLogin"]')
    submit.click()
    '''
    dropdown = driver.find_element_by_xpath('//*[@id="slide-toggle1"]/a')
    dropdown.click()
    dropdown = driver.find_element_by_xpath('//*[@id="menu-content"]/li[4]/a')
    dropdown.click()
    '''
    

main()
