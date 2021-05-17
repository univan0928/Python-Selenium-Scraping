from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time 
import mysql.connector

# Open the chrome browser
options = Options()
options.headless = True
options.add_argument("--window-size=1920,1200")
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')
driver.get("https://plateforme-audienceformations.com/")

# Log in with userName and password
title = driver.find_element_by_xpath('//input[@type="text"]')
login = driver.find_element_by_xpath('//input[@type="text"]').send_keys("contact@alabs.io")
password = driver.find_element_by_xpath("//input[@type='password']").send_keys("frel7haup6senk_SHOX")
submit = driver.find_element_by_xpath("//input[@value='Sign In']").click()

# Check if enter into main page
try:
    element = WebDriverWait(driver, 10000000).until(
        EC.presence_of_element_located((By.ID, "totalCoursesMetric"))
    )
    print('Successfully logged in')
except TimeoutException:
    print("Timed out waiting for page to load")
finally:
    print("Page loaded")

# Click the report button and then click the history button
reportButton = driver.find_element_by_id("reports_navitem").click()
print("report roaded!")

wait = WebDriverWait(driver, 10)
historyButton = wait.until(EC.element_to_be_clickable((By.XPATH, '//a[text()="Historique des rappels"]')))
historyButton.click()
print("history roaded!")
driver.save_screenshot("screenshot.png")

# Get the counts of page and row
word = driver.find_element_by_xpath('//span[@class="tip"]').text
wordSplit = word.split(' ')
totalCount = wordSplit[2]
print(totalCount)

# Connect the database
mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="zoho_table"
    )
mycursor = mydb.cursor()
mycursor.execute("START TRANSACTION")

for i in range(0,int(totalCount) + 1):
    row = driver.find_element_by_xpath('//table[@class="table table-striped table-rpt"]').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")
    for j in range(0, len(row)):
        dealName = driver.find_element_by_xpath('//table[@class="table table-striped table-rpt"]').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[0]
        userName = driver.find_element_by_xpath('//table[@class="table table-striped table-rpt"]').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[1]
        status = driver.find_element_by_xpath('//table[@class="table table-striped table-rpt"]').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[2]
        userEmail = driver.find_element_by_xpath('//table[@class="table table-striped table-rpt"]').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[3]
        object = driver.find_element_by_xpath('//table[@class="table table-striped table-rpt"]').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[4]
        toSend = driver.find_element_by_xpath('//table[@class="table table-striped table-rpt"]').find_element_by_tag_name("tbody").find_elements_by_tag_name("tr")[j].find_elements_by_tag_name("td")[5]
        print(dealName.text)
        print(userName.text)
        print(status.text)
        print(userEmail.text)
        print(object.text)
        print(toSend.text)

        # # Check if exist the new got row on the table
        # sqlq = "SELECT COUNT(*) FROM report_history WHERE dealname = '"+ dealName.text +"' AND username = '"+ userName.text +"' AND status = '"+ status.text +"' AND email = '"+ userEmail.text +"' AND object = '"+ object.text +"'"
        # mycursor.execute(sqlq)
        # if mycursor.fetchone()[0]:
        #     print("This row exits")
        #     continue
        # else:
        # Insert record if not exists in table
        sql = "INSERT INTO report_history (dealname, username, status, email, object, tosend) VALUES (%s, %s, %s, %s,%s, %s) \
                WHERE not exists \
                (Select * from report_history WHERE dealname = '"+ dealName.text +"' AND username = '"+ userName.text +"' AND status = '"+ status.text +"' AND email = '"+ userEmail.text +"' AND object = '"+ object.text +"') LIMIT 1"
        val = (dealName.text, userName.text, status.text, userEmail.text, object.text, toSend.text)

        mycursor.execute(sql, val)
        mydb.commit()
    nextArrow = driver.find_element_by_xpath("//button[@id='nextArrow']").click()

    time.sleep(3)
    driver.save_screenshot("screenshot1.png")


driver.quit()