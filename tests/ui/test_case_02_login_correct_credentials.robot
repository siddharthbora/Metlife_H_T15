*** Settings ***
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Setup Browser And Navigate
Suite Teardown   Close Browser Instance

*** Variables ***
${USER_NAME}        Test User Login
${USER_PASSWORD}    Test@123

*** Test Cases ***
Test_Case_2_Login_User_With_Correct_Credentials
    [Tags]    ui    login    positive    smoke
    [Documentation]    Test Case 2: Login User with correct email and password
    
    # First create a user account
    Navigate To Login Page
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    logintest${timestamp}@automation.com
    Fill And Validate    //input[@data-qa="signup-name"]    ${USER_NAME}    Name
    Fill And Validate    //input[@data-qa="signup-email"]    ${email}    Email
    Click And Wait    //button[@data-qa="signup-button"]    //h2[contains(text(), "ENTER ACCOUNT INFORMATION")]    3
    
    # Complete registration
    Click And Wait    //input[@id="id_gender1"]
    Fill And Validate    //input[@id="password"]    ${USER_PASSWORD}    Password
    Select Options By    select#days    value    1
    Select Options By    select#months    value    1
    Select Options By    select#years    value    1990
    Click And Wait    //button[@data-qa="create-account"]    //h2[contains(text(), "ACCOUNT CREATED!")]    3
    Click And Wait    //a[@data-qa="continue-button"]    //a[contains(text(), "Logged in as")]
    
    # Logout and then login with the created credentials
    Click And Wait    //a[@href="/logout"]    //h2[contains(text(), "Login to your account")]
    Enter Login Credentials    ${email}    ${USER_PASSWORD}
    Submit Login Form
    Validate Logged In Status
    Delete Account And Validate