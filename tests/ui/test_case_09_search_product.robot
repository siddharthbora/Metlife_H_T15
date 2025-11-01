*** Settings ***
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Setup Browser And Navigate
Suite Teardown   Close Browser Instance

*** Variables ***
${SEARCH_PRODUCT}    Blue Top

*** Test Cases ***
Test_Case_9_Search_Product
    [Tags]    ui    search    products    smoke
    [Documentation]    Test Case 9: Search Product using XPath and Playwright
    
    Navigate To Products Page
    Search Product    ${SEARCH_PRODUCT}
    Validate Search Results