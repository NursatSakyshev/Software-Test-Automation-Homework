from selenium import webdriver
from test1 import run_test as run_test1
from test2 import run_test as run_test2

options = webdriver.ChromeOptions()
options.set_capability('browserVersion', 'latest')
options.set_capability('bstack:options', {
    "os": "Windows",
    "osVersion": "11",
    "sessionName": "Chrome Tests"
})

run_test1(options, "Chrome")
run_test2(options, "Chrome")
