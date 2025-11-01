*** Settings ***
Library          ../../libraries/PlaywrightLibrary.py
Suite Setup      Setup Browser And Navigate
Suite Teardown   Close Browser Instance

*** Test Cases ***
Test_Case_8_Verify_All_Products_And_Product_Detail_Page
    [Tags]    ui    products    detail    smoke
    [Documentation]    Test Case 8: Verify All Products and product detail page using XPath and Playwright
    
    Navigate To Products Page
    View First Product Details
    Validate Product Details