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

driver.find_element("xpath", "//*[@id = 'btnSave']").click()

firstname1 = 'Manishh'
lastname2 = 'Mandall'

driver.find_element(
    "xpath", "//*[@id = 'personal_txtEmpFirstName']").clear()
driver.find_element(
    "xpath", "//*[@id = 'personal_txtEmpFirstName']").send_keys(firstname1)

driver.find_element(
    "xpath", "//*[@id='personal_txtEmpLastName']").clear()

driver.find_element(
    "xpath", "//*[@id='personal_txtEmpLastName']").send_keys(lastname2)


driver.find_element("xpath", "//*[@id='personal_optGender_1']").click()
print('male selected')


driver.find_element(
    "xpath", "//*[@id='personal_cmbNation']/option[83]").click()
print('indian selected')


date = '1998-08-18'

driver.find_element("xpath", "//*[@id='personal_DOB']").clear()

driver.find_element("xpath", "//*[@id='personal_DOB']").send_keys(date)

print('dob submitted')

driver.quit()
