from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import requests

jstrisurl = "https://jstris.jezevec10.com/PC-mode"
pbsraw = requests.get(jstrisurl).text.splitlines()
pblinks = []

for lineindex, line in enumerate(pbsraw):
    if "time-mil" in line:
        pblink = pbsraw[lineindex + 6].split('" target')[0].split('a href="')[1]
        username = pbsraw[lineindex - 3].replace("</a>", "")
        pblinks.append([pblink, username])

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless=new")  # Run Chrome in headless mode

# Set up the Selenium WebDriver with the configured options
driver = webdriver.Chrome(options=chrome_options)

def getfumen(url):
    # Navigate to the target webpage
    driver.get(url)

    # Close the alert dialog if it appears
    try:
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass

    # Click the "load" button
    load_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'load')))
    load_button.click()

    wait = WebDriverWait(driver, 10)  # Maximum wait time of 10 seconds
    rep0_element = wait.until(EC.presence_of_element_located((By.ID, 'rep0')))
    rep0_value = rep0_element.get_attribute('value')

    url = "https://fumen.tstman.net/jstris"
    replay_data = {
        "replay": rep0_value
    }

    response = requests.post(url, data=replay_data).json()

    return(response["fumen"])

with open("top200fumens.txt", "w") as fumenfile:
    for index, i in enumerate(pblinks):
        try:
            print(index)
            outputfumen = getfumen(i[0])
            fumenfile.write(f"{i[1]}: {outputfumen}\n")
        except:
            pass

driver.quit()
