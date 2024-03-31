from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Scenario 1


desired_caps = {

  "platformName": "Android",
  "appium:platformVersion": "14",
  "appium:deviceName": "emulator-5554",
  "appium:App": "D:\\nopstationCart_4.40 1.apk",
  "appium:automationName": "UIAutomator2",
  "appium:ensureWebviewsHavePages": "true"

}

# Initializing the driver
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


categories_list = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'categories_list'))
)
# Click on 'Electronics' category
categories_list.find_element_by_android_uiautomator('new UiSelector().text("ELECTRONICS")').click()


mattress_bedroom_product = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'product_mattress_bedroom'))
)
# Click on 'Mattress Bedroom' product
mattress_bedroom_product.click()

# Click the plus button to increase quantity by 2
for _ in range(2):
    plus_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, 'plus_button'))
    )
    plus_button.click()

# Click on the 'Add to Cart' button
add_to_cart_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'add_to_cart_button'))
)
add_to_cart_button.click()

# Close the app and quit the driver
driver.quit()
