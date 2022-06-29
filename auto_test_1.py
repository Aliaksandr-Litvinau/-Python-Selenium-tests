from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.kufar.by/')
search_box = driver.find_element(By.XPATH, '//*[@id="searchbar-main"]/div/div/input')
search_box.clear()
search_box.send_keys("дача")
search_box.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
