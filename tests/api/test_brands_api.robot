*** Settings ***
Library          ../../libraries/APILibrary.py

*** Test Cases ***
API03 GET All Brands List
    [Tags]    api    brands    smoke
    Get All Brands List
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Should Not Be Empty    ${json}

API04 PUT To All Brands List Should Fail
    [Tags]    api    brands    negative
    Put To Brands List
    Verify Response Status Code    405
    Verify Response Contains Text    This request method is not supported

Verify Brands Response Structure
    [Tags]    api    brands
    Get All Brands List
    Verify Response Status Code    200
    ${response}=    Get Response Json
    Log    ${response}

Performance Brands API Response Time
    [Tags]    api    brands    performance
    Get All Brands List
    Verify Response Status Code    200
    Verify Response Time Less Than    5

