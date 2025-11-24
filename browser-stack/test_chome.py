from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


USERNAME = "sakyshevnursat_wnDUNr"
ACCESS_KEY = "41XXaAgVJvZWbVX2Rvbf"

capabilities = {
    "browserName": "chrome",
    "browserVersion": "latest",
    "bstack:options": {
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "Chrome Test"
    }
}

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=webdriver.ChromeOptions()
)

driver.capabilities.update(capabilities)

driver.get("https://google.com")
print(driver.title)

driver.quit()
