from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
# options = Options()
# options.headless = True
# options.add_argument("--window-size=1920,1200")

DRIVER_PATH = 'chromedriver.exe'
driver = webdriver.Chrome(
    # options=options, 
    executable_path=DRIVER_PATH)
driver.get("https://plateforme-audienceformations.com/")
delay = 3 # seconds
try:
    myElem = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, 'okta-signin-username')))
    print "Page is ready!"
except TimeoutException:
    print "Loading took too much time!"
login = driver.find_element_by_id("okta-signin-username").send_keys("contact@alabs.io")
password = driver.find_element_by_id("okta-signin-password']").send_keys(frel7haup6senk_SHOX)
submit = driver.find_element_by_id("okta-signin-submit").click()