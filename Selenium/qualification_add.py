from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.select import Select

options = Options()
options.add_argument("--window-size-=1920,1080")
driver = webdriver.Chrome(options=options)

username = 'orange'
password = 'orangepassword123'

driver.get("http://alchemy.hguy.co/orangehrm")


driver.find_element("xpath", "//*[@id='txtUsername']").send_keys(username)

driver.find_element("xpath", "//*[@id='txtPassword']").send_keys(password)

driver.find_element("xpath", "//*[@id='btnLogin']").click()

driver.find_element("xpath", "//*[@id='menu_pim_viewMyDetails']").click()

driver.find_element("xpath", "//*[@id='sidenav']/li[9]/a").click()

driver.find_element("xpath", "//*[@id='addWorkExperience']").click()

company = 'IBM'
title = 'Test Specialist Automation'

datefrom = '2021-05-24'
to = '2022-06-16'

driver.find_element(
    "xpath", "//*[@id='experience_employer']").send_keys(company)
driver.find_element("xpath", "//*[@id='experience_jobtitle']").send_keys(title)

driver.find_element(
    "xpath", "//*[@id='experience_from_date']").send_keys(datefrom)
driver.find_element("xpath", "//*[@id='experience_to_date']").send_keys(to)

driver.find_element("xpath", "//*[@id='btnWorkExpSave']").click()

print('record submitted')

driver.quit()
