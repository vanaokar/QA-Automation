*** Settings ***
Documentation     This Suite includes testcases for the most common workflows and functionality of Code Development Process (CDP) for Staff Users
Suite Setup       Launch Web Browser   ${URL}    ${Browser}       #Open Local Chrome     ${URL}
Suite Teardown    Run Keyword   Close Browser
Test Setup        Common wait

Library   SeleniumLibrary
#Library   Selenium2Library
Resource          ./../Resource/Keywords/CommonAction.robot
Resource          ./../Resource/Keywords/LoginPage.robot
Library           ./../Resource/CustomLibrary/MyLibrary.py
Resource          ./../Data/InputData.robot
Variables         ./../Resource/Locators/Elements.py    #C:/Development/robot-scripts/CommonWorkflows/Variables/Variable.py    #./../../Variables/Variable.py
#Resource          ./../Resource/Locators/Elements.py

# How to execute the command
# robot -d ~/CDP/Automation/Results -v ENVIRONMENT:PROD -v BROWSER:chrome  -t "Testcase1:VerifyCDPLogSuccessfully" CDPSmokeTestCases_StaffUser.robot

*** Test Cases ***
#Testcase1:VerifyCDPLogSuccessfully_ForProd
#    [Documentation]    This script Verifies Elements after launching CDP for Staff Users
#    [Tags]    Logo
#    Log   ${TEST NAME}
#    CommonAction.Verify CDP Logo
#    LoginPage.Input Valid Credentials for Prod Env     ${CDP_SA_USER_NAME}
#    [Teardown]   CommonAction.Perform Logout

Testcase1:cdpCMS001_VerifyUserisabletoLogin_StageDev
    [Documentation]    This script Verifies Logins the CDP application successfully for Staff Users
    [Tags]    LaunchApp
    Log   ${TEST NAME}
    CommonAction.Verify CDP Logo
    LoginPage.Input Valid Credentials for StageDev Env
    #[Teardown]   CommonAction.Perform Logout

Testcase3:VerifyUserisunabletologinwithvalidusernameandinvalidpassword
    [Documentation]    This script Verifies it Logins unsuccessfully with valid user but invalid password for Staff Users
    [Tags]    LaunchApp
    Log   ${TEST NAME}
    CommonAction.Verify CDP Logo
    LoginPage.Input Invalid Credentials for Prod Env     ${CDP_SA_USER_NAME}
    LoginPage.Verify Error Message
    LoginPage.Reroute Application
    [Teardown]   CommonAction.Perform Logout

Testcase4:VerifyUserisunabletologinwithinvalidusernameandvalidpassword
    [Documentation]    This script Verifies it Logins unsuccessfully with invalid user but valid password for Staff Users
    [Tags]    LaunchApp
    Log   ${TEST NAME}
    CommonAction.Verify CDP Logo
    LoginPage.Input Invalid Credentials for Prod Env     ${CDP_SA_USER_NAME}
    LoginPage.Verify Error Message
    LoginPage.Reroute Application
    [Teardown]   CommonAction.Perform Logout

Testcase6:cdpCMS006_Verifyuserisabletologout
    [Documentation]    This script Verifies Logins the CDP application successfully for Staff Users
    [Tags]    LaunchApp
    Log   ${TEST NAME}
    CommonAction.Verify CDP Logo
    LoginPage.Input Valid Credentials for StageDev Env
    [Teardown]   CommonAction.Perform Logout