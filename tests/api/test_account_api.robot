*** Settings ***
Library          ../../libraries/APILibrary.py

*** Variables ***
${BASE_EMAIL}           testuser
${TEST_PASSWORD}        Test@123

*** Test Cases ***
API11 POST Create User Account
    [Tags]    api    account    smoke
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
    Verify Response Status Code    201
    Verify Response Contains Text    User created

API11 Create User With All Valid Details
    [Tags]    api    account
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    fulluser${timestamp}@test.com
    Create User Account
    ...    name=Full Name User
    ...    email=${email}
    ...    password=Full@123
    ...    title=Mrs
    ...    birth_date=25
    ...    birth_month=12
    ...    birth_year=1985
    ...    firstname=Full
    ...    lastname=UserName
    ...    company=Full Company Ltd
    ...    address1=456 Main Road
    ...    address2=Building B
    ...    country=India
    ...    state=Karnataka
    ...    city=Bangalore
    ...    zipcode=560100
    ...    mobile_number=9123456789
    Verify Response Status Code    201
    Verify Response Contains Text    User created

API12 DELETE User Account After Creation
    [Tags]    api    account
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
    Verify Response Status Code    201
    Delete User Account    ${email}    Delete@123
    Verify Response Status Code    200
    Verify Response Contains Text    Account deleted

API13 PUT Update User Account After Creation
    [Tags]    api    account
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
    Verify Response Status Code    201
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

API14 GET User Account Detail By Email
    [Tags]    api    account
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
    Verify Response Status Code    201
    Get User Account Detail By Email    ${email}
    Verify Response Status Code    200
    ${json}=    Get Response Json
    Log    ${json}

Edge Case Create User Empty Name
    [Tags]    api    account    edge    negative
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    empty${timestamp}@test.com
    Create User Account
    ...    name=${EMPTY}
    ...    email=${email}
    ...    password=Test@123
    ...    title=Mr
    ...    birth_date=1
    ...    birth_month=1
    ...    birth_year=1990
    ...    firstname=Test
    ...    lastname=User
    ...    company=Co
    ...    address1=St
    ...    address2=
    ...    country=India
    ...    state=State
    ...    city=City
    ...    zipcode=12345
    ...    mobile_number=1234567890
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Create User Invalid Email Format
    [Tags]    api    account    edge    negative
    Create User Account
    ...    name=Invalid Email User
    ...    email=invalidemail
    ...    password=Test@123
    ...    title=Mr
    ...    birth_date=1
    ...    birth_month=1
    ...    birth_year=1990
    ...    firstname=Test
    ...    lastname=User
    ...    company=Co
    ...    address1=St
    ...    address2=
    ...    country=India
    ...    state=State
    ...    city=City
    ...    zipcode=12345
    ...    mobile_number=1234567890
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Delete Non Existing Account
    [Tags]    api    account    edge    negative
    Delete User Account    nonexist@notfound.com    password123
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Update Non Existing Account
    [Tags]    api    account    edge    negative
    Update User Account
    ...    name=Non Exist
    ...    email=nonexist@notfound.com
    ...    password=Pass@123
    ...    title=Mr
    ...    birth_date=1
    ...    birth_month=1
    ...    birth_year=1990
    ...    firstname=Non
    ...    lastname=Exist
    ...    company=NonCo
    ...    address1=123 St
    ...    address2=
    ...    country=India
    ...    state=State
    ...    city=City
    ...    zipcode=12345
    ...    mobile_number=1234567890
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Get User Details Invalid Email
    [Tags]    api    account    edge    negative
    Get User Account Detail By Email    invalid@notfound.com
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Edge Case Get User Details Empty Email
    [Tags]    api    account    edge    negative
    Get User Account Detail By Email    ${EMPTY}
    ${status}=    Get Response Status Code
    Log    Status: ${status}

Performance Create Account API Response Time
    [Tags]    api    account    performance
    ${timestamp}=    Evaluate    int(__import__('time').time())
    ${email}=    Set Variable    perf${timestamp}@test.com
    Create User Account
    ...    name=Perf User
    ...    email=${email}
    ...    password=Perf@123
    ...    title=Mr
    ...    birth_date=1
    ...    birth_month=1
    ...    birth_year=1990
    ...    firstname=Perf
    ...    lastname=User
    ...    company=PerfCo
    ...    address1=St
    ...    address2=
    ...    country=India
    ...    state=State
    ...    city=City
    ...    zipcode=12345
    ...    mobile_number=1234567890
    Verify Response Status Code    201
    Verify Response Time Less Than    5

