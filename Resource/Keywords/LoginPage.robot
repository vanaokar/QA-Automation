*** Settings ***
Documentation  This file refers to LoginPage specific actions at LoginPage for FastScout2

Library  SeleniumLibrary
Library  BuiltIn
Library  String

*** Keywords ***
#    Input Without Credentials
#        Click Element   ${LoginUser}    Staff User
#        Sleep  2s
#        Input Text   ${ZERO}   0
#        Sleep  2s
#        Click Button   ${SIGN_IN}
#        Sleep  2s

### Login with Credentials
Input Valid Credentials for Prod Env
     [Arguments]  ${USER_NAME}
     Log to Console  Login Successful
     Input Username  ${USER_NAME.${Environment}}                   #${USER_NAME.STAGE_User}
     Input Password  ${USER_NAME.PASSWORD_New}
     #Uncheck Remember me
     Submit Credentials
     Log to Console  Login Successful

Input Invalid Credentials for Prod Env
     [Arguments]  ${USER_NAME}
     Log to Console    Input Invalid Credentials
     Input Username    ${USER_NAME.${Environment}}                 #${USER_NAME.STAGE_User}
     Invalid Password   ${USER_NAME.INVALID_PASSWORD}
     #Uncheck Remember me
     Submit Credentials
     Log to Console    Input Invalid Credentials

Input Valid Credentials for StageDev Env
     #[Arguments]  ${USER_NAME}
     Log to Console  Login Successful
     Click Element   ${SELECT_USER}
     Sleep  1s
     #LoginPage.Select_UserfromMenu   Staff User
     Click Element    ${Menu_Option}
     #Press key   ${SELECT_USER}   \\27
     Sleep  1s
     Input Text   ${ZERO}   0
     Sleep  1s
     #Uncheck Remember me
     Submit Credentials
     Log to Console  Login Successful

Select_UserfromMenu
    [Arguments]  ${Menu}
    #${Menulist}=    Create List     Regular User     Another Regular User     Auditor     Staff User     VA Staff User     Super Admin
    #:For    ${var}  IN  @{Menulist}
    :For    ${i}  IN RANGE 1 6
    \ ${MenuText}   Get Text   //*[@id="login-cover"]/div/div/div[2]/div/div/form/div[1]/div/select/option[${i}]
    \ Sleep  2s
    \ Run Keyword If   '${MenuText}'=='${Menu}'   Click Element   //*[@id="login-cover"]/div/div/div[2]/div/div/form/div[1]/div/select/option[${i}] AND EXIT FOR LOOP
#    \ Run Keyword If   '${MenuText}'=='Regular User' OR '${MenuText}'=='Another Regular User' OR '${MenuText}'=='Auditor User' OR '${MenuText}'=='Staff User' OR '${MenuText}'=='Super Admin'
    \ Sleep  2s

Input Username
    [Arguments]    ${USER_NAME}
    log to console  Usernameentered
    #Execute Javascript(Presskey  id=email   \\27  # added this line to escape any tooltips)
    press key  id=emailInput   \\27
    Clear Element Text   id=emailInput
    Input Text    id=emailInput    ${USER_NAME}
    log to console  Username entered  no_newline=false

Input Password
    [Arguments]    ${PASSWORD}
    log to console  Passwordentered
    Press key   id=passwordInput    \\27
    #Press keys   id=passwordInput   ESC
    Clear Element Text   id=passwordInput
    Input Text    id=passwordInput    ${PASSWORD}
    log to console  Password entered  no_newline=false

Submit Credentials
    log to console  SubmitCredentials
    #Click Button    Sign In     #Staging [Locator Sign In] #Prod [Locator Sign in]
    ${IsElementVisible}=    Run Keyword And Return Status    Element Should Be Visible    ${SIGN_IN}
    Run Keyword If    ${IsElementVisible}    Click Button    ${SIGN_IN}
    log to console  SubmitCredentials

Invalid Password
    [Arguments]     ${INVALID_PASSWORD}
    Log to Console   InvalidPassword
    #Press key  id=password    \\27
    Press keys   id=password   ESC
    Clear Element Text   id=password
    Input Text    id=password    ${INVALID_PASSWORD}
    Log to Console   InvalidPassword

Verify Error Message
    Log to Console   VerifyErrorMessage
    sleep  4s
    #Element Text Should Be   xpath=//*[@class="error text-center"]   Your email or password is incorrect.  message=none   #matches exact text
    Element Should Contain    ${ERROR_MESSAGE}   Your email or password is incorrect.  message=WARN     #if substring of text needs to be verified
    Reload Page
    Log to Console   VerifyErrorMessage

Reroute Application
   [Documentation]  Will help to reoute the application adhocly.
   Go to   url= ${URL.${Environment}}   #added this line to verify the Logout state...don't remove
   sleep  3s
   Log To Console  Re-outing the application
