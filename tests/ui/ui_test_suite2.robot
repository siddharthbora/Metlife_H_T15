*** Settings ***
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Initialize UI Test Environment
Suite Teardown   Cleanup UI Test Environment

*** Variables ***
${BASE_URL}             https://automationexercise.com
${UI_TIMEOUT}           30s

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

${CONTACT_NAME}         Test User
${CONTACT_EMAIL}        testuser@automation.com
${CONTACT_SUBJECT}      Test Subject
${CONTACT_MESSAGE}      This is a test message for contact us form automation testing.

*** Test Cases ***
TC_UI_004_Contact_Us_Form_Submission
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
    [Tags]    ui    products    smoke    regression
    Setup Browser And Navigate
    Navigate To Products Page
    View First Product Details
    Validate Product Details
    Close Browser Instance

TC_UI_006_Product_Search_Functionality
    [Tags]    ui    products    search    regression
    Setup Browser And Navigate
    Navigate To Products Page
    Search Product    dress
    Validate Search Results
    Close Browser Instance

*** Keywords ***
Initialize UI Test Environment
    Log    Initializing UI Test Environment
    Log    Base URL: ${BASE_URL}
    Log    Browser: Chromium (Playwright)
    Log    UI Test Suite Ready

Cleanup UI Test Environment
    Run Keyword And Ignore Error    Close Browser Instance
    Log    UI Test Suite Execution Completed
    Log    Cleaning up UI Test Environment
