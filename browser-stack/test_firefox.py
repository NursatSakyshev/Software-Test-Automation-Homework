from selenium import webdriver

USERNAME = "sakyshevnursat_wnDUNr"
ACCESS_KEY = "41XXaAgVJvZWbVX2Rvbf"

options = webdriver.FirefoxOptions()

bstack_options = {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "Firefox Test"
}

options.set_capability('bstack:options', bstack_options)
options.set_capability('browserVersion', 'latest')

driver = webdriver.Remote(
    command_executor=f"https://{USERNAME}:{ACCESS_KEY}@hub.browserstack.com/wd/hub",
    options=options
)

driver.get("https://google.com")
print(driver.title)

driver.quit()
