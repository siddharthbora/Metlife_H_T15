*** Settings ***
Library          ../../libraries/APILibrary.py

*** Test Cases ***
API01 GET All Products List
    [Tags]    api    products    smoke
    Get All Products List
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Should Not Be Empty    ${json}

API02 POST To All Products List Should Fail
    [Tags]    api    products    negative
    Post To Products List
    Verify Response Status Code    405
    Verify Response Contains Text    This request method is not supported

API05 POST Search Product With Valid Term
    [Tags]    api    products    search    smoke
    Search Product    tshirt
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Log    ${json}

API05 Search Product Dress
    [Tags]    api    products    search
    Search Product    dress
    Verify Response Status Code    200

API05 Search Product Jeans
    [Tags]    api    products    search
    Search Product    jeans
    Verify Response Status Code    200

API05 Search Product Top
    [Tags]    api    products    search
    Search Product    top
    Verify Response Status Code    200

API06 POST Search Product Without Parameter
    [Tags]    api    products    search    negative
    Search Product Without Parameter
    Verify Response Status Code    400
    Verify Response Contains Text    Bad request

Edge Case Search Empty String
    [Tags]    api    products    edge    negative
    Search Product    ${EMPTY}
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Search Special Characters
    [Tags]    api    products    edge
    Search Product    !@#$%
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Search Numbers Only
    [Tags]    api    products    edge
    Search Product    123456
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Search Very Long String
    [Tags]    api    products    edge
    ${long_string}=    Evaluate    'A' * 500
    Search Product    ${long_string}
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Performance Products API Response Time
    [Tags]    api    products    performance
    Get All Products List
    Verify Response Status Code    200
    Verify Response Time Less Than    5

Performance Search API Response Time
    [Tags]    api    products    performance
    Search Product    shirt
    Verify Response Status Code    200
    Verify Response Time Less Than    5

