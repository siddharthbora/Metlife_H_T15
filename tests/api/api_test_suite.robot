*** Settings ***
Library          ../../libraries/APILibrary.py
Suite Setup      Initialize API Test Environment
Suite Teardown   Cleanup API Test Environment

*** Variables ***
${BASE_URL}             https://automationexercise.com
${API_TIMEOUT}          30s

${VALID_EMAIL}          test@example.com
${VALID_PASSWORD}       test123
${INVALID_EMAIL}        notfound@test.com
${INVALID_PASSWORD}     wrongpass
${BASE_EMAIL}           testuser
${TEST_PASSWORD}        Test@123

*** Test Cases ***
TC_API_001_Get_Products_List_Positive
    [Tags]    api    get    products    positive    smoke
    Get All Products List
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Should Not Be Empty    ${json}
    Log    Products list retrieved successfully

TC_API_002_Get_Brands_List_Positive
    [Tags]    api    get    brands    positive    smoke
    Get All Brands List
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Should Not Be Empty    ${json}
    Log    Brands list retrieved successfully

TC_API_003_Get_User_Account_Detail_Positive
    [Tags]    api    get    account    positive
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    getuser${timestamp}@test.com
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
    Get User Account Detail By Email    ${email}
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Log    User account details retrieved successfully
TC_API_004_Post_Search_Product_Positive
    [Tags]    api    post    products    positive    smoke    validation
    Search Product    tshirt
    Verify Response Status Code    200
    ${search_results}=    Get Response Json
    Should Not Be Empty    ${search_results['products']}
    ${product_count}=    Get Length    ${search_results['products']}
    Should Be True    ${product_count} > 0
    ${first_product}=    Set Variable    ${search_results['products'][0]}
    Should Contain    ${first_product['name']}    shirt    ignore_case=True
    Should Not Be Empty    ${first_product['price']}
    Should Not Be Empty    ${first_product['brand']}
    Should Not Be Empty    ${first_product['category']}
    Log    Search returned ${product_count} products matching 'tshirt'
    Log    Product search completed and validated successfully

TC_API_005_Post_Login_Valid_Credentials_Positive
    [Tags]    api    post    login    positive    smoke
    Verify Login Api    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Verify Response Status Code    200
    Verify Response Contains Text    User exists

TC_API_006_Post_Create_User_Account_Positive
    [Tags]    api    post    account    positive    smoke    validation
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
    Get User Account Detail By Email    ${email}
    Verify Response Status Code    200
    ${user_data}=    Get Response Json
    Should Be Equal    ${user_data['user']['name']}    Test User
    Should Be Equal    ${user_data['user']['email']}    ${email}
    Should Be Equal    ${user_data['user']['first_name']}    Test
    Should Be Equal    ${user_data['user']['last_name']}    User
    Should Be Equal    ${user_data['user']['company']}    TestCo
    Should Be Equal    ${user_data['user']['address1']}    123 Street
    Should Be Equal    ${user_data['user']['address2']}    Apt 1
    Should Be Equal    ${user_data['user']['country']}    India
    Should Be Equal    ${user_data['user']['state']}    TestState
    Should Be Equal    ${user_data['user']['city']}    TestCity
    Should Be Equal    ${user_data['user']['zipcode']}    560001
    Log    User account created and validated successfully
TC_API_007_Put_Update_User_Account_Positive
    [Tags]    api    put    account    positive    validation
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    update${timestamp}@test.com
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
    Get User Account Detail By Email    ${email}
    Verify Response Status Code    200
    ${updated_data}=    Get Response Json
    Should Be Equal    ${updated_data['user']['name']}    Updated User
    Should Be Equal    ${updated_data['user']['email']}    ${email}
    Should Be Equal    ${updated_data['user']['first_name']}    Updated
    Should Be Equal    ${updated_data['user']['last_name']}    UserName
    Should Be Equal    ${updated_data['user']['company']}    UpdatedCo
    Should Be Equal    ${updated_data['user']['address1']}    Updated Street
    Should Be Equal    ${updated_data['user']['address2']}    Floor 5
    Should Be Equal    ${updated_data['user']['state']}    UpdatedState
    Should Be Equal    ${updated_data['user']['city']}    UpdatedCity
    Should Be Equal    ${updated_data['user']['zipcode']}    999999
    Log    User account updated and validated successfully
TC_API_008_Delete_User_Account_Positive
    [Tags]    api    delete    account    positive    validation
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    delete${timestamp}@test.com
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
    Delete User Account    ${email}    Delete@123
    Verify Response Status Code    200
    Verify Response Contains Text    Account deleted
    Get User Account Detail By Email    ${email}
    Verify Response Status Code    200
    ${delete_response}=    Get Response Json
    Should Be Equal    ${delete_response['message']}    User not found!
    Log    User account deleted and validated successfully
TC_API_009_Post_Products_List_Negative
    [Tags]    api    post    products    negative
    Post To Products List
    Verify Response Status Code    200
    Verify Response Contains Text    This request method is not supported

TC_API_010_Post_Search_Product_Missing_Parameter_Negative
    [Tags]    api    post    products    negative
    Search Product Without Parameter
    Verify Response Status Code    400
    Verify Response Contains Text    Bad request

TC_API_011_Post_Login_Missing_Email_Negative
    [Tags]    api    post    login    negative
    Verify Login Without Email    ${VALID_PASSWORD}
    Verify Response Status Code    400
    Verify Response Contains Text    Bad request

TC_API_012_Post_Login_Invalid_Credentials_Negative
    [Tags]    api    post    login    negative
    Verify Login Api    ${INVALID_EMAIL}    ${INVALID_PASSWORD}
    Verify Response Status Code    200
    Verify Response Contains Text    User not found
TC_API_013_Put_Brands_List_Negative
    [Tags]    api    put    brands    negative
    Put To Brands List
    Verify Response Status Code    200
    Verify Response Contains Text    This request method is not supported
TC_API_014_Delete_Login_Endpoint_Negative
    [Tags]    api    delete    login    negative
    Delete Verify Login
    Verify Response Status Code    200
    Verify Response Contains Text    This request method is not supported

*** Keywords ***
Initialize API Test Environment
    Log    Initializing API Test Environment
    Log    Base URL: ${BASE_URL}
    Log    API Test Suite Ready

Cleanup API Test Environment
    Log    API Test Suite Execution Completed
    Log    Cleaning up API Test Environment
