*** Settings ***
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Setup Browser And Navigate
Suite Teardown   Close Browser Instance

*** Variables ***
${USER_NAME}        Test User
${USER_PASSWORD}    Test@123
${FIRST_NAME}       Test
${LAST_NAME}        User
${COMPANY}          Test Company
${ADDRESS}          123 Test Street
${COUNTRY}          India
${STATE}            Test State
${CITY}             Test City
${ZIPCODE}          12345
${MOBILE}           9876543210

*** Test Cases ***
Test_Case_1_Register_User
    [Tags]    ui    registration    smoke
    [Documentation]    Complete user registration flow from Test Case 1
    
    Navigate To Login Page
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    testuser${timestamp}@automation.com
    Fill And Validate    input[data-qa="signup-name"]    ${USER_NAME}    Name
    Fill And Validate    input[data-qa="signup-email"]    ${email}    Email
    Click And Wait    button[data-qa="signup-button"]    h2:has-text("ENTER ACCOUNT INFORMATION")    3
    Validate Page Loaded    /signup    ENTER ACCOUNT INFORMATION    input#id_gender1
    
    Click And Wait    input#id_gender1
    Fill And Validate    input#password    ${USER_PASSWORD}    Password
    Select Options By    select#days    value    1
    Select Options By    select#months    value    1
    Select Options By    select#years    value    1990
    Click And Wait    input#newsletter
    Click And Wait    input#optin
    
    Fill And Validate    input#first_name    ${FIRST_NAME}    First Name
    Fill And Validate    input#last_name    ${LAST_NAME}    Last Name
    Fill And Validate    input#company    ${COMPANY}    Company
    Fill And Validate    input#address1    ${ADDRESS}    Address
    Select Options By    select#country    label    ${COUNTRY}
    Fill And Validate    input#state    ${STATE}    State
    Fill And Validate    input#city    ${CITY}    City
    Fill And Validate    input#zipcode    ${ZIPCODE}    Zipcode
    Fill And Validate    input#mobile_number    ${MOBILE}    Mobile
    
    Click And Wait    button[data-qa="create-account"]    h2:has-text("ACCOUNT CREATED!")    3
    Validate Page Loaded    /account_created    ACCOUNT CREATED!    h2:has-text("ACCOUNT CREATED!")
    Click And Wait    a[data-qa="continue-button"]    a:has-text("Logged in as")
    Validate Element Visible    a:has-text("Logged in as ${USER_NAME}")    Logged In User
    
    Click And Wait    a[href="/delete_account"]    h2:has-text("ACCOUNT DELETED!")
    Validate Page Loaded    /delete_account    ACCOUNT DELETED!    h2:has-text("ACCOUNT DELETED!")
    Click And Wait    a[data-qa="continue-button"]    a[href="/login"]
    Validate Home Page