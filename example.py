from google.cloud import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# Initialize a logger instance
client = logging.Client()
logger = client.logger("example_dot_com_logger")

# Setup WebDriver
webdriver_service = Service(ChromeDriverManager().install())
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Go to example.com
driver.get("http://www.example.com")

# Click on the "More information..." link
more_info_link = driver.find_element(By.XPATH, "//a[@href='https://www.iana.org/domains/example']")
more_info_link.click()

# Wait for the new page to load and find the "last-updated" div
driver.implicitly_wait(10)  # wait up to 10 seconds
last_updated_div = driver.find_element(By.CLASS_NAME, "last-updated")

# Write the content of "last-updated" div to Google Cloud Logging
logger.log_text(last_updated_div.text)
print(last_updated_div.text)

# Close the browser
driver.quit()
