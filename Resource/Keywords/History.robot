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
Variables         ./../../Resources/Locators/Elements.py
Library            ../CustomLibrary/MyLibrary.py
#Library           ../CustomLibrary/MyLibraryMouseEvents.py