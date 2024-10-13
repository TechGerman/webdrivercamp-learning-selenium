from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

driver.get("https://www.ebay.com/")

wait = WebDriverWait(driver, 10)
element = wait.until(EC.presence_of_element_located((By.ID, 'gh-ac')))

print(driver.current_url)

search = driver.find_element(By.ID, 'gh-ac')
search.send_keys('women watch')

search_button = driver.find_element(By.ID, 'gh-btn').click()

results_heading = driver.find_element(By.XPATH, '//h1[@class="srp-controls__count-heading"]')
search_word = 'results for women watch'
if search_word in results_heading.text:
    print(f'Header contains "results for women watch"')
else:
    print(f'Header does not contain "results for women watch"')

driver.quit()
