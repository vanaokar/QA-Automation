#####Created this InputData to implement DataDriven
*** Variables ***
${DELAY}  0s
${Environment} =  DEV
${Browser} =  Chrome
&{URL}        DEV=http://cdpcms-test.iccdev.org  STAGE=http://cdpcms-stage.iccdev.org/login/  PROD=https://www.cdpaccess.com/login/
&{CDP_SA_USER_NAME}   DEV=qa-test-1@caxy.com  STAGE=qa-test-1@caxy.com   PROD=vanaokar@iccsafe.org  PASSWORD_New=Ganapati1$   INVALID_PASSWORD=Pass  STAGE_AccountID=3853537   PROD_AccountID=3882858  Passwordcommon=password
&{CDP_RE_USER_NAME}   DEV=qa-test-1@caxy.com  STAGE=qa-test-1@caxy.com   PROD=qa-test-1@caxy.com   PASSWORD_New=caxy1234   INVALID_PASSWORD=Pass

#InputData
#&{UnRegistered_user}  Email=guest@fastmodeltechnologies.com   Password=guestpassword    ExpectedErrorMsg=Your email or password is incorrect.
#&{Invalid_Password_user}  Email=uma@fastmodeltechologies.com  Password=invalidpassword  ExpectedErrorMsg=Your email or password is incorrect.
#&{Blank_Credentials}       Email=#Blank                       Password=#Blank           ExpectedErrorMsg=Please fill out this field.
### Variable for data storge
#@{noteslist}
#@{currentseasonschedules}
#@{pastseasonschedules}

#__________________________________________________________________________#
#${stats_DBHost}         dev-pg.c1nnfbljcvf2.us-east-1.rds.amazonaws.com
#${stats_DBName}         stats-dev
#${stats_DBPass}         AiBAaID/1pmz
#${DBPort}               5432
#${stats_DBUser}         stats_ro_user
#
#${report_DBHost}        dev-pg.c1nnfbljcvf2.us-east-1.rds.amazonaws.com
#${report_DBName}        report-staging    #stats-dev
#${report_DBPass}        jE-:HL6@TP5s       #AiBAaID/1pmz
##${DBPort}              5432
#${report_DBUser}        report_sbo2       #stats_ro_user

