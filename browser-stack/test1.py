from selenium import webdriver

USERNAME = "sakyshevnursat_wnDUNr"
ACCESS_KEY = "41XXaAgVJvZWbVX2Rvbf"

def run_test(options, name):
    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
        options=options
    )

    try:
        driver.get("https://google.com")
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", '
            '"arguments": {"status":"passed", "reason":"Google opened successfully"}}'
        )

        print(f"{name} - Test 1: PASSED")

    except Exception as e:
        driver.execute_script(
            f'browserstack_executor: {{"action": "setSessionStatus", '
            f'"arguments": {{"status":"failed", "reason":"{str(e)}"}}}}'
        )

        print(f"{name} - Test 1: FAILED")

    finally:
        driver.quit()
