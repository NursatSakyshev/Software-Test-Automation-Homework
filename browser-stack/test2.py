from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = "sakyshevnursat_wnDUNr"
ACCESS_KEY = "41XXaAgVJvZWbVX2Rvbf"

def run_test(options, name):
    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
        options=options
    )

    try:
        wait = WebDriverWait(driver, 20)
        driver.get("https://www.demoblaze.com/")

        login_btn = wait.until(EC.presence_of_element_located((By.ID, "login2")))
        driver.execute_script("arguments[0].click();", login_btn)

        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("nursat_sakyshev")
        driver.find_element(By.ID, "loginpassword").send_keys("test12345")

        login_submit = driver.find_element(By.XPATH, "//button[text()='Log in']")
        driver.execute_script("arguments[0].click();", login_submit)

        welcome = wait.until(EC.visibility_of_element_located((By.ID, "nameofuser"))).text
        assert "Welcome nursat_sakyshev" in welcome

        product = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[text()='Samsung galaxy s6']")))
        driver.execute_script("arguments[0].click();", product)

        add_cart = wait.until(EC.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Add to cart')]")))
        driver.execute_script("arguments[0].click();", add_cart)

        wait.until(EC.alert_is_present())
        driver.switch_to.alert.accept()

        cart_btn = driver.find_element(By.ID, "cartur")
        driver.execute_script("arguments[0].click();", cart_btn)

        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Place Order']")))

        place_order = driver.find_element(By.XPATH, "//button[text()='Place Order']")
        driver.execute_script("arguments[0].click();", place_order)

        wait.until(EC.visibility_of_element_located((By.ID, "name"))).send_keys("Nursat")
        driver.find_element(By.ID, "country").send_keys("Kazakhstan")
        driver.find_element(By.ID, "city").send_keys("Almaty")
        driver.find_element(By.ID, "card").send_keys("1234567890123456")
        driver.find_element(By.ID, "month").send_keys("10")
        driver.find_element(By.ID, "year").send_keys("2025")

        purchase = driver.find_element(By.XPATH, "//button[text()='Purchase']")
        driver.execute_script("arguments[0].click();", purchase)

        wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Thank you for your purchase!')]")))

        ok_btn = driver.find_element(By.XPATH, "//button[text()='OK']")
        driver.execute_script("arguments[0].click();", ok_btn)

        driver.execute_script(
            'browserstack_executor: {"action":"setSessionStatus","arguments":{"status":"passed","reason":"Product purchase completed successfully"}}'
        )

        print(f"{name} - Buy Product Test: PASSED")

    except Exception as e:
        reason = str(e).replace('"', "'")
        driver.execute_script(
            f'browserstack_executor: {{"action":"setSessionStatus","arguments":{{"status":"failed","reason":"{reason}"}}}}'
        )
        print(f"{name} - Buy Product Test: FAILED\nReason: {e}")

    finally:
        driver.quit()
