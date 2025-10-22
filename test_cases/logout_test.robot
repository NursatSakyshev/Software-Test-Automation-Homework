*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://www.demoblaze.com/
${USERNAME}    nursat_sakyshev
${PASSWORD}    test12345

*** Test Cases ***
Logout Test
    Open Browser    ${URL}    chrome
    Maximize Browser Window

    Click Element    id:login2
    Sleep    2s
    Input Text    id:loginusername    ${USERNAME}
    Input Text    id:loginpassword    ${PASSWORD}
    Click Button    xpath://button[text()='Log in']
    
    Wait Until Page Contains Element    id:logout2    10s
    Sleep    3s
    Click Element    id:logout2
    Sleep    3s
    Page Should Contain Element    id:login2
    Close Browser
