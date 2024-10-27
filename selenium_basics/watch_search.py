from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
wait = WebDriverWait(driver, 10)


# This function select a "{brand}" in the left navigation block "Brand"
def select_brand(brand):
    return driver.find_element(By.XPATH, f'//li[h3[contains(.,"Brand")]]//input[@aria-label="{brand}"]').click()


# This function returns the i-th item on the first page
# by waiting for its presence using XPath.
def first_page_i_item(i):
    return wait.until(EC.presence_of_element_located((
        By.XPATH, f'(//div[@class="s-item__title"])[{i}]')))


# This function returns the i-th item's title on the first page
# by waiting for its presence using XPath.
def first_page_i_item_title(i):
    return wait.until(EC.presence_of_element_located((
            By.XPATH, f'(//div[@class="s-item__title"])[{i}]')
        )).text


# This function returns the i-th item's price on the first page
# by waiting for its presence using XPath.
def first_page_i_item_price(i):
    return wait.until(EC.presence_of_element_located((
        By.XPATH, f'(//span[@class="s-item__price"])[{i}]'))
    ).text.replace('$', '').replace('/ea', '').strip()


# This function returns the item's price on the second page by using XPath.
def second_page_items_price():
    price = wait.until(EC.presence_of_element_located((
        By.XPATH, '//div[@class="x-price-primary"]//span'
    ))).text.replace('US $', '',).replace('/ea', '').strip()
    return price


# This function returns the item's title on the second page by using XPath.
def second_page_items_title():
    title = wait.until(EC.presence_of_element_located((
        By.XPATH, '(//h1[@class="x-item-title__mainTitle"])[1]'
    ))).text
    return title


# This function verifies that items contain correct brand
def verify_brand_in_title(a, b, c):
    is_valid = True

    if c.lower() not in a.lower():
        print(f"{a} DOESN'T contain {c} in title")
        is_valid = False

    if c.lower() not in b.lower():
        print(f"{b} DOESN'T contain {c} in title")
        is_valid = False

    return is_valid


# This function verifies that title and price for items
# from different pages are the same
def verify_title_and_price(first_page_item_title,
                           second_page_item_title,
                           first_page_item_price,
                           second_page_item_price, brand):
    is_valid = True

    if first_page_item_title != second_page_item_title:
        print(f"Title for {brand} items is different")
        print(f"First page item title: {first_page_item_title}")
        print(f"Second page item title: {second_page_item_title}")
        is_valid = False

    if first_page_item_price != second_page_item_price:
        print(f"Price for {brand} items is different")
        print(f"First page item price: {first_page_item_price}")
        print(f"Second page item price: {second_page_item_price}")
        is_valid = False

    return is_valid


# Open Ebay
driver.get(
    "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p4432023.m570.l1313&_nkw=watch&_sacat=0"
)

# Wait until left navigation block is presented
full_xpath = f"//ul[@class='x-refine__left__nav']//div[text()='Brand']"
element = wait.until(EC.presence_of_element_located((By.XPATH, full_xpath)))

select_brand("Rolex")

# Find items on the first page
first_page_first_item = first_page_i_item(3)
first_page_second_item = first_page_i_item(4)

# Find the title for the items on the first page
first_page_first_item_title = first_page_i_item_title(3)
first_page_second_item_title = first_page_i_item_title(4)

# Verify that first two items contain brand "Rolex" in their title
verify_brand_in_title(first_page_first_item_title,
                      first_page_second_item_title, "Rolex")

# Find the price for the items on the first page
first_page_first_item_price = first_page_i_item_price(3)
first_page_second_item_price = first_page_i_item_price(4)

# Click the first item to go to the item page
first_page_first_item.click()

# Switch to the next opened tab
currentTab = 0
nextTab = currentTab + 1
driver.switch_to.window(driver.window_handles[nextTab])

# Wait for a short time to let the new page load
wait = WebDriverWait(driver, 10)

# Store price and title in a variable
second_page_first_item_price = second_page_items_price()
second_page_first_item_title = second_page_items_title()

# Close tab
driver.close()

# Switch to the first page
driver.switch_to.window(driver.window_handles[currentTab])

# Click the second item to go to the item page
first_page_second_item.click()

# Switch to the next opened tab
driver.switch_to.window(driver.window_handles[nextTab])

# Store price and title in a variable
second_page_second_item_price = second_page_items_price()
second_page_second_item_title = second_page_items_title()

# Close tab
driver.close()

# Switch to the first page
driver.switch_to.window(driver.window_handles[currentTab])

# Verify the title and the price for the first item
# from the first and second page
verify_title_and_price(
    first_page_first_item.text, second_page_first_item_title,
    first_page_first_item_price, second_page_first_item_price, "Rolex")

# Verify the title and the price for the second item
# from the first and second page
verify_title_and_price(
    first_page_second_item_title, second_page_second_item_title,
    first_page_second_item_price, second_page_second_item_price, "Rolex")

# Unselect "Rolex" brand
select_brand("Rolex")

# Select "Casio" brand
select_brand("Casio")

# Find items on the first page
first_page_third_item = first_page_i_item(69)
first_page_fourth_item = first_page_i_item(70)

# Find the title for the items on the first page
first_page_third_item_title = first_page_i_item_title(69)
first_page_fourth_item_title = first_page_i_item_title(70)

# Verify that last two items contain brand "Rolex" in their title
verify_brand_in_title(first_page_third_item_title,
                      first_page_fourth_item_title, "Casio")


# Find the price for the items on the first page
first_page_third_item_price = first_page_i_item_price(69)
first_page_fourth_item_price = first_page_i_item_price(70)

# Click the third item to go to the item page
first_page_third_item.click()

# Switch to the next opened tab
currentTab = 0
nextTab = currentTab + 1
driver.switch_to.window(driver.window_handles[nextTab])

# Store price and title in a variable
second_page_third_item_price = second_page_items_price()
second_page_third_item_title = second_page_items_title()

# Close tab
driver.close()

# Switch to the first page
driver.switch_to.window(driver.window_handles[currentTab])

# Click the second item to go to the item page
first_page_fourth_item.click()

# Switch to the next opened tab
driver.switch_to.window(driver.window_handles[nextTab])

# Store price and title in a variable
second_page_fourth_item_price = second_page_items_price()
second_page_fourth_item_title = second_page_items_title()

# Close tab
driver.close()

# Verify the title and the price for the third item
# from the first and second page
verify_title_and_price(first_page_third_item_title,
                       second_page_third_item_title,
                       first_page_third_item_price,
                       second_page_third_item_price, "Casio")

# Verify the title and the price for the fourth item
# from the first and second page
verify_title_and_price(first_page_fourth_item_title,
                       second_page_fourth_item_title,
                       second_page_fourth_item_price,
                       second_page_fourth_item_price, "Casio")

quit()
