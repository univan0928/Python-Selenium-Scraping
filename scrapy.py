from selenium import webdriver
from selenium.webdriver.chrome.options import Options
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

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
for i in range(0,totalCount):
    for j in range(0, 20):
        # driver.find_elements_by_css_selector(".main-col.v_middle.peopleNameTD")[j].find_elements_by_xpath("//strong").text
        userName = driver.find_element_by_css_selector('td.main-col.v_middle.peopleNameTD')[j].find_element_by_css_selector('strong')[0].text
        print(userName)
        # userEmail = driver.find_element_by_xpath('//td[@class="main-col v_middle peopleNameTD"].eq(j).find("small")').text
        # $("td.main-col.v_middle.peopleNameTD").eq(0).find("strong").text()
        # $("td.main-col.v_middle.peopleNameTD").eq(1).find("small").text()
driver.save_screenshot('screenshot.png')
driver.quit()
