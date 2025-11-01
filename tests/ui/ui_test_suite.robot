*** Settings ***
Documentation    UI Test Suite for Automation Exercise
...              Comprehensive UI testing covering Registration, Login, Products, and Contact functionality
...              Author: QA Team | Framework: Robot Framework + Playwright
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Initialize UI Test Environment
Suite Teardown   Cleanup UI Test Environment

*** Variables ***
# Test Configuration
${BASE_URL}             https://automationexercise.com
${UI_TIMEOUT}           30s

# User Registration Data
${USER_NAME}            Test User
${USER_PASSWORD}        Test@123
${FIRST_NAME}           Test
${LAST_NAME}            User
${COMPANY}              Test Company
${ADDRESS}              123 Test Street
${COUNTRY}              India
${STATE}                Test State
${CITY}                 Test City
${ZIPCODE}              12345
${MOBILE}               9876543210

# Contact Form Data
${CONTACT_NAME}         Test User
${CONTACT_EMAIL}        testuser@automation.com
${CONTACT_SUBJECT}      Test Subject
${CONTACT_MESSAGE}      This is a test message for contact us form automation testing.

*** Test Cases ***

TC_UI_001_User_Registration_Complete_Flow
    [Documentation]    UI Test 1: Verify complete user registration workflow
    [Tags]    ui    registration    smoke    regression
    Setup Browser And Navigate
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
    Close Browser Instance

TC_UI_002_Login_Functionality_Verification
    [Documentation]    UI Test 2: Verify login page functionality and error handling
    [Tags]    ui    login    smoke    regression
    Setup Browser And Navigate
    Navigate To Login Page
    Validate Page Loaded    /login    Login    .login-form
    
    Enter Login Credentials    invalid@test.com    wrongpassword
    Submit Login Form
    Validate Login Error
    
    Validate Page Loaded    /login    Login    .login-form
    Close Browser Instance

TC_UI_003_Login_With_Invalid_Credentials
    [Documentation]    UI Test 3: Verify login behavior with incorrect credentials
    [Tags]    ui    login    negative    regression
    Setup Browser And Navigate
    Navigate To Login Page
    Enter Login Credentials    invalid@email.com    wrongpassword
    Submit Login Form
    Validate Login Error
    Close Browser Instance

TC_UI_004_Contact_Us_Form_Submission
    [Documentation]    UI Test 4: Verify contact us form submission functionality
    [Tags]    ui    contact    smoke    regression
    Setup Browser And Navigate
    Navigate To Contact Page
    Fill Contact Form    ${CONTACT_NAME}    ${CONTACT_EMAIL}    ${CONTACT_SUBJECT}    ${CONTACT_MESSAGE}
    Submit Contact Form
    Validate Success Message    Success! Your details have been submitted successfully.
    Click And Wait    a[href="/"]    .features_items
    Validate Home Page
    Close Browser Instance

TC_UI_005_Products_Page_And_Product_Details
    [Documentation]    UI Test 5: Verify products page and individual product details
    [Tags]    ui    products    smoke    regression
    Setup Browser And Navigate
    Navigate To Products Page
    View First Product Details
    Validate Product Details
    Close Browser Instance

TC_UI_006_Product_Search_Functionality
    [Documentation]    UI Test 6: Verify product search functionality
    [Tags]    ui    products    search    regression
    Setup Browser And Navigate
    Navigate To Products Page
    Search Product    dress
    Validate Search Results
    Close Browser Instance

*** Keywords ***
Initialize UI Test Environment
    [Documentation]    Setup for UI test execution
    Log    Initializing UI Test Environment
    Log    Base URL: ${BASE_URL}
    Log    Browser: Chromium (Playwright)
    Log    UI Test Suite Ready

Cleanup UI Test Environment
    [Documentation]    Cleanup after UI test execution
    Run Keyword And Ignore Error    Close Browser Instance
    Log    UI Test Suite Execution Completed
    Log    Cleaning up UI Test Environment
