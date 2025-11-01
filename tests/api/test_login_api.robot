*** Settings ***
Library          ../../libraries/APILibrary.py

*** Variables ***
${VALID_EMAIL}          test@example.com
${VALID_PASSWORD}       test123
${INVALID_EMAIL}        notfound@test.com
${INVALID_PASSWORD}     wrongpass

*** Test Cases ***
API07 POST Verify Login With Valid Credentials
    [Tags]    api    login    smoke
    Verify Login Api    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Verify Response Status Code    200
    Verify Response Contains Text    User exists

API08 POST Verify Login Without Email Parameter
    [Tags]    api    login    negative
    Verify Login Without Email    ${VALID_PASSWORD}
    Verify Response Status Code    400
    Verify Response Contains Text    Bad request

API08 POST Verify Login Without Password Parameter
    [Tags]    api    login    negative
    Verify Login Without Password    ${VALID_EMAIL}
    Verify Response Status Code    400
    Verify Response Contains Text    Bad request

API09 DELETE To Verify Login Should Fail
    [Tags]    api    login    negative
    Delete Verify Login
    Verify Response Status Code    405
    Verify Response Contains Text    This request method is not supported

API10 POST Verify Login With Invalid Email
    [Tags]    api    login    negative
    Verify Login Api    ${INVALID_EMAIL}    ${VALID_PASSWORD}
    Verify Response Status Code    404
    Verify Response Contains Text    User not found

API10 POST Verify Login With Invalid Password
    [Tags]    api    login    negative
    Verify Login Api    ${VALID_EMAIL}    ${INVALID_PASSWORD}
    Verify Response Status Code    404
    Verify Response Contains Text    User not found

API10 POST Verify Login With Both Invalid
    [Tags]    api    login    negative
    Verify Login Api    ${INVALID_EMAIL}    ${INVALID_PASSWORD}
    Verify Response Status Code    404
    Verify Response Contains Text    User not found

Edge Case Login Empty Email
    [Tags]    api    login    edge    negative
    Verify Login Api    ${EMPTY}    ${VALID_PASSWORD}
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Login Empty Password
    [Tags]    api    login    edge    negative
    Verify Login Api    ${VALID_EMAIL}    ${EMPTY}
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Login Both Empty
    [Tags]    api    login    edge    negative
    Verify Login Api    ${EMPTY}    ${EMPTY}
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Login Special Characters
    [Tags]    api    login    edge    negative
    Verify Login Api    !@#$%^&*    !@#$%^&*
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Login SQL Injection Attempt
    [Tags]    api    login    edge    security
    Verify Login Api    ' OR '1'='1    password
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Login XSS Attempt
    [Tags]    api    login    edge    security
    Verify Login Api    <script>alert('XSS')</script>    password
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Performance Login API Response Time
    [Tags]    api    login    performance
    Verify Login Api    ${VALID_EMAIL}    ${VALID_PASSWORD}
    Verify Response Status Code    200
    Verify Response Time Less Than    5

