*** Settings ***
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Setup Browser And Navigate
Suite Teardown   Close Browser Instance

*** Variables ***
${CONTACT_NAME}       Test User
${CONTACT_EMAIL}      testuser@automation.com
${CONTACT_SUBJECT}    Test Subject
${CONTACT_MESSAGE}    This is a test message for contact us form automation testing.

*** Test Cases ***
Test_Case_6_Contact_Us_Form
    [Tags]    ui    contact    form    smoke
    [Documentation]    Test Case 6: Contact Us Form
    
    Navigate To Contact Page
    Fill Contact Form    ${CONTACT_NAME}    ${CONTACT_EMAIL}    ${CONTACT_SUBJECT}    ${CONTACT_MESSAGE}
    Submit Contact Form
    Validate Success Message    Success! Your details have been submitted successfully.
    Click And Wait    a[href="/"]    .features_items
    Validate Home Page