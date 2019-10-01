*** Settings ***
Documentation     This file refers to all common actions performed across CDP application
Library           SeleniumLibrary  timeout=10    implicit_wait=1.5   #run_on_failure=Nothing
Library           String
Library           BuiltIn
Library           OperatingSystem
Library           Collections
#Resource          ./../../Resources/Keywords/HomePage.robot
#Resource          ./../../Resources/Keywords/LoginPage.robot
#Resource          ./../../Data/InputData.robot
#Variables         ./../../Variables/Variable.py
#Variables         ./../Resource/Locators/Elements.py
#Library            ../CustomLibrary/MyLibrary.py
#Library           ../CustomLibrary/MyLibraryMouseEvents.py

*** Keywords ***
Login Verify Top Menu
    Log To Console  User Intended to verify Login from Top Menu
    LoginPage.Input Valid Credentials    ${USER_NAME}    ${PASSWORD}
    CommonAction.Navigate To Home Page
    TopNav.Verify TopMenu Elements
    Log To Console  User able to verify Login from Top Menu successfully

Launch Web Browser
    [Arguments]    ${URL}    ${Browser}    #${DEV_URL}    ${BROWSER}
    #Log    ${URL.${Environment}}
    Log To Console  User Intended to Launch Web Browser
        Run Keyword If      '${BROWSER}' == 'HeadlessChrome'      Open Headless Chrome Browser and Launch Url  ${URL}
        ...     ELSE IF     '${BROWSER}' == 'HeadlessFirefox'     Open Headless Firefox and Launch Url    ${URL}
        ...     ELSE         Open Browser    url= ${URL.${Environment}}    browser=${BROWSER}
    Set Selenium Speed    ${DELAY}
    #    ${windowsize}    =    Get Window Size
    #    log    ${windowsize}
    #Maximize Browser Window    # Maximizes browser window
    Set Window Size    1400    800
    #Set Window Size    1600    900
    #LOG TO CONSOLE    Browser is Maximized
    #Log to console    ${username} executing the test on ${os}    #%{os}
    #    Page Should Contain    FastScout
    LOG TO CONSOLE    Label verified on LoginPage
    SLEEP    3s
    Log To Console  User able to Launch Web Browser successfully

Close Browser
    Log To Console  User Intended to Close Browser
    Delete All Cookies
    log to console    Deleted cookies
    Close All Browsers
    log to console   Current browser got closed.

Common Wait
   [Documentation]  Common wait used for Test setup
    Sleep  6s

Verify CDP Logo
    # Keyword is used to verify Logo and intro overlay which was earlier availble hence commented
    Log To Console  User Intended to Verify CDP Logo
    SLEEP    9s
    Wait until page contains element    ${CDPLOGO}  timeout=0.15
    LOG TO CONSOLE    Verified CDPLogo  on header is visible
    Log To Console  User able to Verify CDP Logo successfully

Perform Logout
    Log To Console  User Intended to Perform Logout CDP App
    sleep    5s
    Click Link    ${SignOut_Icon}
    Sleep    2s
    Set focus to Element  ${Logout}
    Click Element   ${Logout}
    log to console    A/C Dropdown visible to Perform Logout
    sleep    3s

Page Refresh
    #If any refresh is needed
    Log To Console  User Intended to Refresh Page
    Reload Page
    sleep    6s
    Log To Console  User able to Refresh Page successfuly
