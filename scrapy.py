from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
driver.get("https://plateforme-audienceformations.com/")

title = driver.find_element_by_xpath('//input[@type="text"]')
login = driver.find_element_by_xpath('//input[@type="text"]').send_keys("contact@alabs.io")
password = driver.find_element_by_xpath("//input[@type='password']").send_keys("frel7haup6senk_SHOX")
submit = driver.find_element_by_xpath("//input[@value='Sign In']").click()

try:
    element = WebDriverWait(driver, 10000000).until(
        EC.presence_of_element_located((By.ID, "totalCoursesMetric"))
    )
    print('Successfully logged in')
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")
peopleButton = driver.find_element_by_id("people_navitem").click()
word = driver.find_element_by_xpath('//span[@class="badge coursefilter-total"]').text
totalNumber = word.split(' ', 1)
totalCount = int(totalNumber[0])//20
print(totalCount)
driver.save_screenshot("screenshot.png")

for i in range(0,totalCount):
    for j in range(0, 20):
        userName = driver.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[1].find_element_by_tag_name("strong")
        userEmail = driver.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[1].find_element_by_tag_name("small")
        status = driver.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[3].find_element_by_tag_name("small")
        last = driver.find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[4].find_element_by_tag_name("small")
        print(userName.text)
        print(userEmail.text)
        print(status.text)
        print(last.text)
    peopleButton = driver.find_element_by_xpath('//a[@title="Page Suivant"]').click()
    driver.save_screenshot("screenshot1.png")
    time.sleep(3)
driver.quit()