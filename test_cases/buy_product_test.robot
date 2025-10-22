*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}      https://www.demoblaze.com/
${USERNAME}    nursat_sakyshev
${PASSWORD}    test12345

*** Test Cases ***
Buy Product Test
    Open Browser    ${URL}    chrome
    Maximize Browser Window
    Sleep    2s

    #login
    Click Element    id:login2
    Sleep    2s
    Input Text    id:loginusername    ${USERNAME}
    Input Text    id:loginpassword    ${PASSWORD}
    Sleep    1s
    Click Button    xpath://button[text()='Log in']
    Wait Until Page Contains    Welcome ${USERNAME}    10s
    Sleep    2s

    # Adding to cart
    Click Element    xpath://a[text()='Samsung galaxy s6']
    Wait Until Element Is Visible    xpath://a[contains(text(),'Add to cart')]    10s
    Sleep    2s
    Click Element    xpath://a[contains(text(),'Add to cart')]
    Handle Alert    ACCEPT
    Sleep    2s

    # Go to the cart
    Click Element    id:cartur
    Wait Until Page Contains Element    xpath://button[text()='Place Order']    10s
    Sleep    2s

    # Place Order
    Click Button    xpath://button[text()='Place Order']
    Wait Until Element Is Visible    id:name    10s
    Sleep    1s
    Input Text    id:name    Nursat
    Input Text    id:country    Kazakhstan
    Input Text    id:city    Almaty
    Input Text    id:card    1234567890123456
    Input Text    id:month    10
    Input Text    id:year    2025
    Sleep    1s
    Click Button    xpath://button[text()='Purchase']
    Sleep    3s

    # Confirm 
    Wait Until Page Contains    Thank you for your purchase!    10s
    Sleep    1s
    Click Button    xpath://button[text()='OK']
    Sleep    2s

    Close Browser