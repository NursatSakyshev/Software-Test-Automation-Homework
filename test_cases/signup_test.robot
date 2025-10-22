*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://www.demoblaze.com/
${USERNAME}    nursat_sakyshev
${PASSWORD}    test12345

*** Test Cases ***
Sign Up Test
    Open Browser    ${URL}    chrome
    Click Element    id:signin2
    Sleep    2s
    Input Text    id:sign-username    ${USERNAME}
    Input Text    id:sign-password    ${PASSWORD}
    Click Button    xpath://button[text()='Sign up']
    Sleep    2s
    Handle Alert    ACCEPT
    Close Browser