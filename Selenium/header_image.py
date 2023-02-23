from selenium import webdriver

from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size-=1920,1080")
driver = webdriver.Chrome(options=options)


driver.get("http://alchemy.hguy.co/orangehrm")

src = driver.find_element("xpath",
                          "//div[@id='divLogo']/img").get_attribute("src")

print(src)


driver.quit()
