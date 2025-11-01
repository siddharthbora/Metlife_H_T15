*** Settings ***
Documentation    API Test Suite for Automation Exercise
...              Comprehensive API testing covering Products, Brands, Login, and Account management
...              Author: QA Team | Framework: Robot Framework
Library          ../libraries/APILibrary.py
Suite Setup      Initialize API Test Environment
Suite Teardown   Cleanup API Test Environment

*** Variables ***
# Test Configuration
${BASE_URL}             https://automationexercise.com
${API_TIMEOUT}          30s

# Test Data
${VALID_EMAIL}          test@example.com
${VALID_PASSWORD}       test123
${INVALID_EMAIL}        notfound@test.com
${INVALID_PASSWORD}     wrongpass
${BASE_EMAIL}           testuser
${TEST_PASSWORD}        Test@123

*** Test Cases ***

# ========== GET METHOD TESTS - POSITIVE ==========
TC_API_001_Get_Products_List_Positive
    [Documentation]    Positive GET Test: Successfully retrieve all products list
    [Tags]    api    get    products    positive    smoke
    Get All Products List
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Should Not Be Empty    ${json}
    Log    Products list retrieved successfully

TC_API_002_Get_Brands_List_Positive
    [Documentation]    Positive GET Test: Successfully retrieve all brands list
    [Tags]    api    get    brands    positive    smoke
    Get All Brands List
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Should Not Be Empty    ${json}
    Log    Brands list retrieved successfully

TC_API_003_Get_User_Account_Detail_Positive
    [Documentation]    Positive GET Test: Successfully retrieve user account details by email
    [Tags]    api    get    account    positive
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    getuser${timestamp}@test.com
    # Setup: Create user first
    Create User Account
    ...    name=Get User
    ...    email=${email}
    ...    password=Get@123
    ...    title=Mr
    ...    birth_date=15
    ...    birth_month=8
    ...    birth_year=1988
    ...    firstname=Get
    ...    lastname=User
    ...    company=GetCo
    ...    address1=Get Street
    ...    address2=
    ...    country=India
    ...    state=GetState
    ...    city=GetCity
    ...    zipcode=555555
    ...    mobile_number=5555555555
    Verify Response Status Code    200
    # Actual GET test
    Get User Account Detail By Email    ${email}
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Log    User account details retrieved successfully

# ========== POST METHOD TESTS - POSITIVE ==========
TC_API_004_Post_Search_Product_Positive
    [Documentation]    Positive POST Test: Successfully search product with valid search term
    [Tags]    api    post    products    positive    smoke
    Search Product    tshirt
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Log    Product search completed successfully

TC_API_005_Post_Login_Valid_Credentials_Positive
    [Documentation]    Positive POST Test: Successfully login with valid credentials
    [Tags]    api    post    login    positive    smoke
    Verify Login Api    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Verify Response Status Code    200
    Verify Response Contains Text    User exists

TC_API_006_Post_Create_User_Account_Positive
    [Documentation]    Positive POST Test: Successfully create new user account
    [Tags]    api    post    account    positive    smoke
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    ${BASE_EMAIL}${timestamp}@test.com
    Create User Account
    ...    name=Test User
    ...    email=${email}
    ...    password=${TEST_PASSWORD}
    ...    title=Mr
    ...    birth_date=15
    ...    birth_month=6
    ...    birth_year=1990
    ...    firstname=Test
    ...    lastname=User
    ...    company=TestCo
    ...    address1=123 Street
    ...    address2=Apt 1
    ...    country=India
    ...    state=TestState
    ...    city=TestCity
    ...    zipcode=560001
    ...    mobile_number=9876543210
    Verify Response Status Code    200
    Verify Response Contains Text    User created

# ========== PUT METHOD TESTS - POSITIVE ==========
TC_API_007_Put_Update_User_Account_Positive
    [Documentation]    Positive PUT Test: Successfully update user account details
    [Tags]    api    put    account    positive
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    update${timestamp}@test.com
    # Setup: Create user first
    Create User Account
    ...    name=Original User
    ...    email=${email}
    ...    password=Original@123
    ...    title=Mr
    ...    birth_date=1
    ...    birth_month=1
    ...    birth_year=1990
    ...    firstname=Original
    ...    lastname=User
    ...    company=OriginalCo
    ...    address1=Original St
    ...    address2=
    ...    country=India
    ...    state=OriginalState
    ...    city=OriginalCity
    ...    zipcode=111111
    ...    mobile_number=1111111111
    Verify Response Status Code    200
    # Actual PUT test
    Update User Account
    ...    name=Updated User
    ...    email=${email}
    ...    password=Updated@123
    ...    title=Mrs
    ...    birth_date=20
    ...    birth_month=10
    ...    birth_year=1995
    ...    firstname=Updated
    ...    lastname=UserName
    ...    company=UpdatedCo
    ...    address1=Updated Street
    ...    address2=Floor 5
    ...    country=India
    ...    state=UpdatedState
    ...    city=UpdatedCity
    ...    zipcode=999999
    ...    mobile_number=9999999999
    Verify Response Status Code    200
    Verify Response Contains Text    User updated

# ========== DELETE METHOD TESTS - POSITIVE ==========
TC_API_008_Delete_User_Account_Positive
    [Documentation]    Positive DELETE Test: Successfully delete user account
    [Tags]    api    delete    account    positive
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    delete${timestamp}@test.com
    # Setup: Create user first
    Create User Account
    ...    name=Delete User
    ...    email=${email}
    ...    password=Delete@123
    ...    title=Mr
    ...    birth_date=10
    ...    birth_month=5
    ...    birth_year=1992
    ...    firstname=Delete
    ...    lastname=User
    ...    company=DeleteCo
    ...    address1=789 Delete St
    ...    address2=
    ...    country=India
    ...    state=DeleteState
    ...    city=DeleteCity
    ...    zipcode=123456
    ...    mobile_number=9988776655
    Verify Response Status Code    200
    # Actual DELETE test
    Delete User Account    ${email}    Delete@123
    Verify Response Status Code    200
    Verify Response Contains Text    Account deleted

# ========== POST METHOD TESTS - NEGATIVE ==========
TC_API_009_Post_Products_List_Negative
    [Documentation]    Negative POST Test: POST request to products list should fail (method not allowed)
    [Tags]    api    post    products    negative
    Post To Products List
    Verify Response Status Code    200
    Verify Response Contains Text    This request method is not supported

TC_API_010_Post_Search_Product_Missing_Parameter_Negative
    [Documentation]    Negative POST Test: Search product without required parameter should fail
    [Tags]    api    post    products    negative
    Search Product Without Parameter
    Verify Response Status Code    400
    Verify Response Contains Text    Bad request

TC_API_011_Post_Login_Missing_Email_Negative
    [Documentation]    Negative POST Test: Login without email parameter should fail
    [Tags]    api    post    login    negative
    Verify Login Without Email    ${VALID_PASSWORD}
    Verify Response Status Code    400
    Verify Response Contains Text    Bad request

TC_API_012_Post_Login_Invalid_Credentials_Negative
    [Documentation]    Negative POST Test: Login with invalid credentials should fail
    [Tags]    api    post    login    negative
    Verify Login Api    ${INVALID_EMAIL}    ${INVALID_PASSWORD}
    Verify Response Status Code    200
    Verify Response Contains Text    User not found

# ========== PUT METHOD TESTS - NEGATIVE ==========
TC_API_013_Put_Brands_List_Negative
    [Documentation]    Negative PUT Test: PUT request to brands list should fail (method not allowed)
    [Tags]    api    put    brands    negative
    Put To Brands List
    Verify Response Status Code    200
    Verify Response Contains Text    This request method is not supported

# ========== DELETE METHOD TESTS - NEGATIVE ==========
TC_API_014_Delete_Login_Endpoint_Negative
    [Documentation]    Negative DELETE Test: DELETE request to login endpoint should fail (method not allowed)
    [Tags]    api    delete    login    negative
    Delete Verify Login
    Verify Response Status Code    200
    Verify Response Contains Text    This request method is not supported

*** Keywords ***
Initialize API Test Environment
    [Documentation]    Setup for API test execution
    Log    Initializing API Test Environment
    Log    Base URL: ${BASE_URL}
    Log    API Test Suite Ready

Cleanup API Test Environment
    [Documentation]    Cleanup after API test execution
    Log    API Test Suite Execution Completed
    Log    Cleaning up API Test Environment
