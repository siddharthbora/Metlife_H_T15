*** Settings ***
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Setup Browser And Navigate
Suite Teardown   Close Browser Instance

*** Variables ***
${INVALID_EMAIL}      invalid@email.com
${INVALID_PASSWORD}   wrongpassword

*** Test Cases ***
Test_Case_3_Login_User_With_Incorrect_Credentials
    [Tags]    ui    login    negative    smoke
    [Documentation]    Test Case 3: Login User with incorrect email and password using XPath and Playwright
    
    Navigate To Login Page
    Enter Login Credentials    ${INVALID_EMAIL}    ${INVALID_PASSWORD}
    Submit Login Form
    Validate Login Error