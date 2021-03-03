from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://gist.github.com")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[1]/div/div[5]/a[1]").click()
time.sleep(1)
driver.find_element_by_id("login_field").send_keys("@gmail.com")
time.sleep(1)
driver.find_element_by_id("password").send_keys("pass")
time.sleep(1)
driver.find_element_by_xpath("/html/body/div[3]/main/div/div[3]/form/input[14]").click()
time.sleep(1)

driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/details/summary").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[1]/div/div[6]/details/details-menu/form/button").click()
time.sleep(3)
driver.find_element_by_xpath("/html/body/div[4]/main/div/form/input[2]").click()

time.sleep(2)
driver.close()
print ("success running robot program")
