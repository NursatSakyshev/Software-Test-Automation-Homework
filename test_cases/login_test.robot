*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://www.demoblaze.com/
${USERNAME}    nursat_sakyshev
${PASSWORD}    test12345

*** Test Cases ***
Login Test
    Open Browser    ${URL}    chrome
    Click Element    id:login2
    Sleep    2s
    Input Text    id:loginusername    ${USERNAME}
    Input Text    id:loginpassword    ${PASSWORD}
    Click Button    xpath://button[text()='Log in']
    Sleep    3s
    Page Should Contain    Welcome ${USERNAME}
    Close Browser