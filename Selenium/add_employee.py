from selenium import webdriver

from selenium.webdriver.chrome.options import Options

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--window-size-=1920,1080")
driver = webdriver.Chrome(options=options)

username = 'orange'
password = 'orangepassword123'

driver.get("http://alchemy.hguy.co/orangehrm")


driver.find_element("xpath", "//*[@id='txtUsername']").send_keys(username)


driver.find_element("xpath", "//*[@id='txtPassword']").send_keys(password)

driver.find_element("xpath", "//*[@id='btnLogin']").click()

driver.find_element("xpath", "//*[@id='menu_pim_viewPimModule']").click()

driver.find_element("xpath", "//*[@id='btnAdd']").click()

firstname = 'Manish'
lastname = 'Sharma'

driver.find_element("xpath", "//*[@id='firstName']").send_keys(firstname)
driver.find_element("xpath", "//*[@id='lastName']").send_keys(lastname)


driver.find_element("xpath", "//*[@id = 'btnSave']").click()

driver.back()

driver.find_element("xpath", "//*[@id='menu_pim_viewPimModule']").click()

driver.find_element(
    "xpath", "//*[@id='empsearch_employee_name_empName']").send_keys(username+lastname)

print('employee search success')
driver.quit()
