from selenium import webdriver
import time
wb = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
wb.get("https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title")
k = wb.find_element_by_xpath('//*[@id="wrap"]/div[3]/div/div/div[2]/a[1]')
time.sleep(2)
k.click()

input = wb.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/div[1]/p/input')
time.sleep(2)
input.send_keys("测试")

button = wb.find_element_by_xpath('//*[@id="filter-box"]/div/div[1]/div/form/button')
time.sleep(2)
button.click()
