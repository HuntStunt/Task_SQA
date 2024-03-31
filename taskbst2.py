from appium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# Scenario 2


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

# Step 1: Go to Shopping Cart
top_cart_icon = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'top_cart_icon'))
)
top_cart_icon.click()

# Step 2: Click Checkout Button
checkout_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'checkout_button'))
)
checkout_button.click()

# Step 3: Select Checkout as Guest
checkout_as_guest_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'checkout_as_guest_button'))
)
checkout_as_guest_button.click()

# Step 4: Input Billing Details and Click Continue
# Assuming input fields have IDs like 'billing_name', 'billing_address', etc.
billing_name_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'billing_name'))
)
billing_name_input.send_keys('Mike')

# Similar steps for other billing details input fields

continue_billing_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'continue_billing_button'))
)
continue_billing_button.click()

# Step 5: Select Shipping Method
next_day_air_shipping = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'next_day_air_shipping'))
)
next_day_air_shipping.click()

continue_shipping_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'continue_shipping_button'))
)
continue_shipping_button.click()

# Step 6: Select Payment Method
check_money_order_payment = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'check_money_order_payment'))
)
check_money_order_payment.click()

continue_payment_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'continue_payment_button'))
)
continue_payment_button.click()

# Step 7: Click Next on Payment Information Page
next_payment_info_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'next_payment_info_button'))
)
next_payment_info_button.click()

# Step 8: Confirm Order
confirm_order_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, 'confirm_order_button'))
)
confirm_order_button.click()

# Verification: Verify Order Confirmation Popup Message
order_confirmation_message = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.XPATH, "//android.widget.Toast[@text='Your order has been successfully processed!']"))
)

# Close the app and quit the driver
driver.quit()
