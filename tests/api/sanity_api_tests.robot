*** Settings ***
Library          ../../libraries/APILibrary.py

*** Variables ***
${TEST_EMAIL}         test@example.com
${TEST_PASSWORD}      test123

*** Test Cases ***
Sanity Products API
    [Tags]    sanity    smoke
    Get All Products List
    Verify Response Status Code    200

Sanity Brands API
    [Tags]    sanity    smoke
    Get All Brands List
    Verify Response Status Code    200

Sanity Search API
    [Tags]    sanity    smoke
    Search Product    tshirt
    Verify Response Status Code    200

Sanity Login API
    [Tags]    sanity    smoke
    Verify Login Api    ${TEST_EMAIL}    ${TEST_PASSWORD}
    Verify Response Status Code    200

Sanity Create Account API
    [Tags]    sanity    smoke
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    sanity${timestamp}@test.com
    Create User Account
    ...    name=Sanity User
    ...    email=${email}
    ...    password=Sanity@123
    ...    title=Mr
    ...    birth_date=1
    ...    birth_month=1
    ...    birth_year=1990
    ...    firstname=Sanity
    ...    lastname=User
    ...    company=SanityCo
    ...    address1=123 St
    ...    address2=
    ...    country=India
    ...    state=State
    ...    city=City
    ...    zipcode=12345
    ...    mobile_number=1234567890
    Verify Response Status Code    201

Sanity All APIs Response Time
    [Tags]    sanity    performance
    Get All Products List
    Verify Response Time Less Than    5
    Get All Brands List
    Verify Response Time Less Than    5
    Search Product    top
    Verify Response Time Less Than    5

