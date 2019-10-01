*** Settings ***
Documentation     This Suite includes testcases for the most common workflows and functionality of Code Development Process (CDP) for Regular Users
Suite Setup       Launch Web Browser   ${URL}    ${Browser}       #Open Local Chrome     ${URL}
Suite Teardown    Run Keyword   Close Browser
Test Setup        Common wait

Library   SeleniumLibrary
#Library   Selenium2Library
Resource          ./../Resource/Keywords/CommonAction.robot
Resource          ./../Resource/Keywords/LoginPage.robot
Library           ./../Resource/CustomLibrary/MyLibrary.py
Resource          ./../Data/InputData.robot
#Variables         ./../Resource/Locators/Elements.py    #C:/Development/robot-scripts/CommonWorkflows/Variables/Variable.py    #./../../Variables/Variable.py
Resource          ./../Resource/Locators/Elements.py

# How to execute the command
# robot -d ~/CDP/Automation/Results -v ENVIRONMENT:PROD -v BROWSER:chrome  -t "Testcase1:VerifyCDPLogSuccessfully" CDPSmokeTestCases_StaffUser.robot

*** Test Cases ***
Testcase1:VerifyCDPLogSuccessfully_ForProd
    [Documentation]    This script Verifies Elements after launching CDP for Regular Users
    [Tags]    Logo
    Log   ${TEST NAME}
    CommonAction.Verify CDP Logo
    LoginPage.Input Valid Credentials for Prod Env     ${CDP_SA_USER_NAME}
    [Teardown]   CommonAction.Perform Logout

Testcase1:VerifyCDPLogSuccessfully_ForStageDev
    [Documentation]    This script Verifies Elements after launching CDP for Staff Users
    [Tags]    Logo
    Log   ${TEST NAME}
    CommonAction.Verify CDP Logo
    LoginPage.Input Valid Credentials     ${CDP_SA_USER_NAME}
    [Teardown]   CommonAction.Perform Logout