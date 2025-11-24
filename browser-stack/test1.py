from selenium import webdriver

USERNAME = "sakyshevnursat_wnDUNr"
ACCESS_KEY = "41XXaAgVJvZWbVX2Rvbf"

def run_test(options, name):
    driver = webdriver.Remote(
        command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
        options=options
    )
    driver.get("https://google.com")
    print(f"{name} - Test 1: PASSED")
    driver.quit()
