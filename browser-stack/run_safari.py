from selenium import webdriver
from test1 import run_test as run_test1
from test2 import run_test as run_test2

options = webdriver.SafariOptions()
options.set_capability('browserVersion', 'latest')
options.set_capability('bstack:options', {
    "os": "OS X",
    "osVersion": "Sonoma",
    "sessionName": "Safari Tests"
})

run_test1(options, "Safari")
run_test2(options, "Safari")
