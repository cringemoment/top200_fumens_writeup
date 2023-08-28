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

# Add the path to the extension CRX file (jstris.crx) in the same folder as the Python script
extension_path = "jstris.crx"
chrome_options.add_extension(extension_path)

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

    # Scroll the page to bring the "fumen" button into view
    fumen_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[@class='replay-btn' and text()='fumen']"))
    )

    # Click the "fumen" button
    fumen_button.click()

    # Handle the alert dialog after clicking the "fumen" button
    try:
        WebDriverWait(driver, 10).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert.accept()
    except:
        pass

    # Wait for the second "repArea" element to load
    rep_area_elements = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'repArea'))
    )

    # Extract the value of the second "repArea" element
    if len(rep_area_elements) > 1:
        rep_area_value = rep_area_elements[1].get_attribute('value')
        return(rep_area_value)

with open("top200fumens.txt", "w") as fumenfile:
    for index, i in enumerate(pblinks):
        try:
            print(index)
            outputfumen = getfumen(i[0])
            fumenfile.write(f"{i[1]}: {outputfumen}\n")
        except:
            pass

# Quit the browser
driver.quit()
