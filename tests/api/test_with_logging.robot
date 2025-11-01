*** Settings ***
Library          ../../libraries/APILibrary.py

*** Variables ***
${TEST_EMAIL}         test@example.com
${TEST_PASSWORD}      test123

*** Test Cases ***
Example Get Products And Store Response
    [Tags]    api    example    logging
    Get All Products List
    Verify Response Status Code    200
    ${response_json}=    Get Response Json
    Log    Full Response: ${response_json}
    Store Response Json    products_response
    ${stored}=    Get Stored Value    products_response
    Log    Stored Response: ${stored}

Example Search And Store Product Data
    [Tags]    api    example    logging
    Search Product    tshirt
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Log    Search Results: ${json}
    Store Response Json    search_results
    Log Response Details

Example Login With Detailed Logging
    [Tags]    api    example    login    logging
    Verify Login Api    ${TEST_EMAIL}    ${TEST_PASSWORD}
    ${status}=    Get Response Status Code
    Log    Login Status Code: ${status}
    ${response_text}=    Get Response Text
    Log    Login Response: ${response_text}
    Log Response Details

Example Create Account With Logging
    [Tags]    api    example    account    logging
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    logtest${timestamp}@test.com
    Create User Account
    ...    name=Log Test User
    ...    email=${email}
    ...    password=LogTest@123
    ...    title=Mr
    ...    birth_date=15
    ...    birth_month=6
    ...    birth_year=1990
    ...    firstname=Log
    ...    lastname=Test
    ...    company=LogTestCo
    ...    address1=123 Log Street
    ...    address2=
    ...    country=India
    ...    state=LogState
    ...    city=LogCity
    ...    zipcode=12345
    ...    mobile_number=9876543210
    ${status}=    Get Response Status Code
    Log    Create Account Status: ${status}
    ${response}=    Get Response Text
    Log    Create Account Response: ${response}
    Log Response Details
    Store Response Json    created_account

Example Verify Response Time
    [Tags]    api    example    performance    logging
    Get All Products List
    ${time}=    Get Response Time
    Log    Response Time: ${time} seconds
    Should Be True    ${time} < 5
    Verify Response Time Less Than    5

