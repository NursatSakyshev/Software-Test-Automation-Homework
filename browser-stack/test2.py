from selenium import webdriver

USERNAME = "sakyshevnursat_wnDUNr"
ACCESS_KEY = "41XXaAgVJvZWbVX2Rvbf"

def run_test(options, name):
    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
        options=options
    )
    driver.get("https://youtube.com")
    print(f"{name} - Test 2: PASSED")
    driver.quit()
