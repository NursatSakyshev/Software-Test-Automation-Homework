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
        driver.get("https://www.demoblaze.com/")
        wait = WebDriverWait(driver, 20)

        login_button = wait.until(
            EC.presence_of_element_located((By.ID, "login2"))
        )

        driver.execute_script("arguments[0].click();", login_button)

        wait.until(EC.visibility_of_element_located((By.ID, "loginusername"))).send_keys("nursat_sakyshev")

        driver.find_element(By.ID, "loginpassword").send_keys("test12345")

        login_btn = driver.find_element(By.XPATH, "//button[text()='Log in']")
        driver.execute_script("arguments[0].click();", login_btn)

        welcome_text = wait.until(
            EC.visibility_of_element_located((By.ID, "nameofuser"))
        ).text

        assert "Welcome nursat_sakyshev" in welcome_text

        driver.execute_script(
            'browserstack_executor: {"action":"setSessionStatus","arguments":{"status":"passed","reason":"Login successful"}}'
        )

        print(f"{name} - Login Test: PASSED")

    except Exception as e:

        reason = str(e).replace('"', "'")  
        driver.execute_script(
            f'browserstack_executor: {{"action":"setSessionStatus","arguments":{{"status":"failed","reason":"{reason}"}}}}'
        )

        print(f"{name} - Login Test: FAILED\nReason: {e}")

    finally:
        driver.quit()
