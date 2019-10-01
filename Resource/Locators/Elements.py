# This document contains all the Page specific Elements for CDP Web applications
# Browser URL

URL = 'https://www.cdpaccess.com/login/'
#CDPLOGO
CDPLOGO = '//*[@id=\'app\']/header[2]/nav/a/img'

#LoginPage
LoginUser = '//*[@id=\'login-cover\']/div/div/div[2]/div/div/form/div[1]/div/select'
ZERO = '//input[@id=\'challenge\']'
SIGN_IN = '//*[@class="btn btn-block btn-primary"][contains(text(),"Sign In")]'
SELECT_USER = '//*[@id="login-cover"]/div/div/div[2]/div/div/form/div[1]/div/select'
Menu_Option = '//*[@id="login-cover"]/div/div/div[2]/div/div/form/div[1]/div/select/option[4]'
#ERROR_MESSAGE = '//*[@class=\'error-message\']'

#SIGNOUT
SignOut_Icon='//a[@id=\'userDrop\']'
Logout = '//a[@class=\'dropdown-item\'][contains(text(),\'Logout\')]'

#############################################################################################################################################################################################

# #############(I)TopNavPage  Locators
# # TopNav Locators
# TopNav_MyTeamLink_NavLink = '//a[@id=\'my-team-nav-link\']'
# TopNav_MyOpponent_NavLink = '//a[@id=\'my-opponents-nav-link\']'
# TopNav_MyScouts_NavLink = '//a[@id=\'library-nav-link\']'
# # TopNav_ScoutBuilder_NavLink = '//a[@id=\'library-nav-link\']'  #Previous naming convention
# TopNav_ScoutBuilder_Link = '//a[@id=\'library-nav-link\']'
# #Season = '//*[@id=\'navbar\']//div[@class=\'display-flex md-font\']'
# #Season = '//*[@id=\'seasonDropdown\']'
# #Season_Text='//div[text()=\'2018-2019\']'
# Season = '//div[@id="seasonDropdown"]'
# Season_Text = '//div[@id="season-0"]/a'
# Season_Text_Previous = '//div[@id="season-1"]/a'
# Get_Season='(//*[@id="seasonDropdown"]//span)[2]' #updated in FS2.5.0 #'//*[@id=\'seasonDropdown\']/span/div'  #//i[@class =\'fa fa-caret-down mg-left-sm mg-right-sm\']'
# Account_ID = '//*[@id=\'accountDropdown\']'
# Ac_DropDown = '//*[@id=\'accountDropdown\']'
# Get_Team_Name_Prefix ='//*[@id=\'accountDropdown\']/span/div/span[2]'
# Get_Team_Name='//h1'
# Get_User_Name = '//*[@id=\'accountDropdown\']/span/div/span[1]' #'//*[@id=\'accountDropdown\']//i[@class=\'fa fa-caret-down mg-left-sm\']'
# FS_Logout = '//*[@id=\'logOutLink\']'  #css=#logOutLink
#
# #############HomePage Page Locators Alias MyScouts Page Locators ####Depreciated
# # HomePage Locators Or Landing Page Constant Elements
# #Commenting At_A_Glance element because of UI change.
# #At_A_Glance = '//*[@id=\'appContainer\']//li[contains(text(),\'AT A GLANCE\')]'
# #HomePage_AtAGlance_xpath = '//*[@id=\'appContainer\']//a[1]//li'
#
# #############(II)MyTeamPage Locators
# HomePage_Roster_xpath = '//*[@id=\'appContainer\']//li[contains(text(),\'ROSTER\')]'
# Four_Factors_Header = 'myTeamFourFactors'   #'//*[@id=\'home-page-four-factors\']/header/div/span'
# FF_Chart_Icon= '//*[@id=\'myTeamFourFactorsChartIcon\']'     #'//*[@id=\'myTeamFourFactorsChartIcon\']//i'     #'//*[@id=\'home-page-four-factors\']//i[@class=\'fa fa-bar-chart\']'
# Point_Period_Header = 'pointsPeriodTableHeader'#'//*[@id=\'appContainer\']//header/div/span[contains(text(),\'Points Per Period\')]'
# #toggle button overtime toggle button to be do
# Point_Overtime_Toggle = 'OvertimeHeaderIcon'      #'//*[@id=\'appContainer\']//div[@class=\'react-toggle-track-x\']
# Pace_Header = '//*[@id=\'paceTableHeader\']'   #'//*[@id=\'appContainer\']//header/div/span[contains(text(),\'Pace (Possessions Per Game)\')]'
# #P_Chart_Icon = '//*[@id=\'paceIcon\']/i'#'//*[@id=\'appContainer\']//div[2]/header//i'
# Myteam_Box_Score_Header ='//*[@id=\'team-record-title-id\' and @name=\'team-record-title-name\']' #'//*[@id=\'appContainer\']//div[contains(text(),\'Box Scores\')]'
# Roster = '//*[@id=\'appContainer\']//li[contains(text(),\'ROSTER\')]'
# AdvancedStats_Header='//*[@id=\'advanced-stats-title-id\']'
# Boxscore_Normal_Filter='//*[@id=\'current-season-filter-normal-id\']'
# Boxscore_Advance_Filter='//*[@id=\'current-season-filter-advanced-id\']'
# Boxscore_Per40_Filter='//*[@id=\'current-season-filter-per40-id\']'
# Boxscore_Total_Filter = '//*[@id=\'current-season-filter-totals-id\']'
# MyTeam_Print_Boxscores = '*//div//i[@class=\'fa fa-print mg-right-sm\']'
# Myteam_PrintIcon = '//*[@id=\'Icons-/-Print\']'  #update in FS2.4.5  #'*//div//i[@class=\'fa fa-print mg-right-sm\']'
# PlayByPlay_PrintIcon='*//div//i[@class=\'fa fa-print color-white\']'
# MOBILE_USAGE = '//*[@class=\'display-flex align-items-center justify-content-space-between pd-bottom-sm\']'
# MOBILEUSAGE_MENU = '//*[@id=\'usageMenu\']'
# Close_MobileUsage = '//*[@class=\'fa fa-times\']'
#
# #Roster='//*[@id="ROSTER-2"]'
# #New elements added per NewDesign which are CONSTANT Irrespective of Any Team Selected
#
# FastStat_Header = '//*[@id=\'stats-0\']'              #old locator#'//*[@id=\'FASTSTAT-0\']'
# Schedule_Header = '//*[@id=\'games-1\']'                 #old locator #'//*[@id=\'SCHEDULE-1\']'
# Roster_Header = '//*[@id=\'myTeam-2\']'              #old locator #'//*[@id=normalize-space(\'SELF SCOUTS-3\')]'
# MyTeam_SelfScouts_Header = '//*[@id=\'documents-3\']'                         # '//*[@id=\'appContainer\']//li[contains(text(),\'SELF SCOUTS\')]'
# FastStat_AllGames = '//*[@id=\'all-0\']'     #oldlocator'#'//*[@id=\'[object Object]-0\']'
# FastStat_Last5 = '//*[@id=\'last-five-1\']'               #old locator #''//*[@id=\'[object Object]-1\']'
# FastStat_WinsVsLosses = '//*[@id=\'win-loss-2\']'         # old locator#''//*[@id=\'[object Object]-2\']'
# FastStat_HomeVsAway = '//*[@id=\'home-away-3\']'          #old locator #'//*[@id=\'[object Object]-3\']'
# FastStat_ConfVsNonConf = '//*[@id=\'conf-non-conf-4\']'  #old locator #'//*[@id=\'[object Object]-4\']'
# RankingButton = '//i[@class=\'fa fa-caret-down hidden-print\']'
#
# PROD_Myteam_PrintIcon = '//*[@id=\'appContainer\']//div/i[@class=\'fa fa-print mg-right-sm\']'
# #AdvancedStats_Header = ''
# Team_Roster_SampleImage='*//table[@id=\'playersRoster\']//img'
#
# #List of VARIABLE Locators
#
# MyOpponents_SelfScouts_Header = '//*[@id=\'documents-3\']'
#
# #MyTeam_Last5=''
# MyTeam_Name='//*[@id=\'accountDropdown\']//span[@class=\'md-font\']'
#
#
# #############(III)MyOpponents Page Locators
# # MyOpponents Page Locators
# All_Teams_FilterBy = '//*[@id=\'collegeFilter-all\']'# oldname  All_Teams_FilterByChkbox = //*[@id=\'collegeFilter-all\']//img'  #//*[@id="collegeFilter-all"]
# GetProp_FilterByAllTeams_chkbox='//*[@id=\'collegeFilter-all\']/label'
#
# ##
# Scheduled_To_Play_FilterByCheckBox = '//*[@id="collegeFilter-opponents"]//img'
# GetProp_FilterByScheduledToPlay_chkbox='//*[@id=\'collegeFilter-opponents\']/label'
#
#
# #TeamName_SortByCheckBox ='//*[@id="SortOptions-name"]//img'
# #GetProp_SortByTeamName_chkbox=''
# Overall_Record_SortByCheckBox ='//*[@id="SortOptions-overallrecord"]//img'
# GetProp_SortByOverallRecord_chkbox= '//*[@id=\'SortOptions-overallrecord\']/label'
#
# SearchTeam_Input ='//*[@id=\'appContainer\']//div/input'
# Myopp_Search = '//*[@id=\'appContainer\']//div/span/i'
#
# SortBy_TeamName_Checkbox = '//*[@id=\'SortOptions-name\']//img'   #//*[@id="SortOptions-name"]//span[1]/img
# GetProp_SortyByTeamName_chkbox='//*[@id=\'SortOptions-name\']/label'
#
# #below filter is only for league
# SorBy_DatePlaying_Checkbox= '//*[@id=\'SortOptions-date\']//img'
# GetProp_SortyByDatePlaying_chkbox='//*[@id=\'SortOptions-date\']/label'
# SortBy_OverAllRecord_Checkbox='//*[@id=\'SortOptions-overallrecord\']//img'
# GetProp_SortByOverAllRecord_chkbox='//*[@id=\'SortOptions-overallrecord\']/label'
# MyTeam_Schedule_SingleBoxscore = '(//a[@class=\'no-underline\'])[6]'
# #'//*[@id=\'myTeamSchedule\']/tbody/tr[1]/td[6]'
# ######added on sep 25th
# CollegeFilterAll ='//*[@id=\'collegeFilter-all\']' #old name CollegeFilterAll_chckbox ='//*[@id=\'collegeFilter-all\']/label[@id=\'checkboxLabel\']'
# CollegeFilterSchedule='//*[@id=\'collegeFilter-opponents\']'
# MyOpponents_ScoutsHeader = '//*[@id=\'SCOUTS-3\']'
# MyOpponent_Last5_FilterCheckbox = '//*[@id=\'opponent-schedule-LAST_N\']' #//*[@id=\'opponent-schedule-LAST_N\']//img'
# Check_Last5Schedule = '//*[@id=\'select-all-opponent-schedule\']'
# Schedule_Last5_Select = '//*[@id="opponent-schedule-LAST_N"]/span'
# MyOpponents_PrintIcon = '//*[@id="print-boxscore"]'#'//*[@id=\'appContainer\']//div/i[@class=\'fa fa-print mg-right-sm\']'#'//*[@id="print-boxscore"]'
# MyOpponents_FastStat_PrintIcon = '*//div/i[@class=\'fa fa-print mg-right-sm\']'
# Schedule_PrintIcon = '//*[@id=\'print-boxscore\']'     #'//*[@id=\'team-schedule-print-button\']'
# #ReadyToPrint_MsgBox =''
# ReadyToPrint_Icon = '//*[@id=\'team-schedule-print-button\']'
# #Select_An_Opponent= '//*[@id=\'container-team-name-column\'][1]//li[3]/a'    #'//*[@id=\'container-team-name-column\']/li[3]//span[1]/img'
# Select_An_Opponent = '//div[@id=\'container-team-name\']/ul[1]/li[1]'                   #'//*[@id=\'container-team-name-column\']/li[1]/a/span/span/span[2]/span' #'//*[@id=\'container-team-name-column\']/li[3]//span[1]/img'
# OpponentTeam_Scouts_Header = '//*[@id=\'appContainer\']//li[contains(text(),\'SCOUTS\')]'
# All_Games_Select='//*[@id=\'[object Object]-0\']/span'
# Last_5_Select='//*[@id=\'[object Object]-1\']/span'
# MyOpponents_Schedule_Boxscore = '//*[@id="container-all-teams"]/div/div/div/table/tbody/tr[1]/td[6]/a/span/span/span'
# MyOpponents_FastStat_Schedule_Boxscore = '//*[@id=\'select-all-opponent-schedule\']'    #'//*[@id="appContainer"]/div/div[1]/div/div/div/div[2]/div/main/div/div[2]/div/table/tbody/tr[1]/td[6]/a/span/span/span'
# CloseSearch = '//i[@class=\'fa fa-times-circle fa-lg cursor-pointer color-primary hover-color-primary\']'
# OppRoster = '//*[@id=\'myTeam-2\']'
# Wins_vs_Looses_Select='//*[@id=\'[object Object]-2\']/span'
# Home_vs_Away_Select='//*[@id=\'[object Object]-3\']/span'
# Conf_vs_NonConf_Select='//*[@id=\'[object Object]-4\']/span'
# AllSetPrint = '//*[@id="team-schedule-print-button"]'
# ##############Added as part of FS2.5.0 release######
# Schedule_AllGames='//*[@id=\'opponent-schedule-SELECT_ALL\']'
# Schedule_Common='//*[@id=\'opponent-schedule-COMMON\']'
# Schedule_Conference='//*[@id=\'opponent-schedule-CONFERENCE_GAMES\']'
# #Schedule_Last5=alias old locator Schedule_Last5_Select
# Schedule_Wins='//*[@id=\'opponent-schedule-WINS\']'
# Schedule_Losses='//*[@id=\'opponent-schedule-LOSSES\']'
# Schedule_Home='//*[@id=\'opponent-schedule-HOME_GAMES\']'
# Schedule_Away='//*[@id="opponent-schedule-AWAY_GAMES"]'
#
# ###########College Division Locators
# ChangeDivision_Label='//*[@id=\'appContainer\']//div/p[contains(text(),\'Change Division\')]'
# GetChangeDivison_Label='//*[@id=\'appContainer\']//div/p[contains(text(),\'Change Division\')]'
# Select_College_Opponent='//*[@id=\'container-team-column\']//li[1]'
#
# #############MyScouts Page Locators
# # MyScouts Locators  alias ScoutLibrary Page locators got changed because of UI design change
# Create_Report_Btn = '//*[@id=\'appContainer\']//a[contains(text(),\'Create Report\')]'
# Templates_Header = '//*[@id=\'appContainer\']//div[contains(text(),\'Templates\')]'
# Date_FilterByCheckBox ='//*[@id=\'checkboxLabel\']//i[1]'
# Asc_Dsc_Icon = '//*[@id=\'scoutReportSortBy\']//i'
# #need formatting
# #SL_Search_Icon ='//*[@id="appContainer"]//i[@class='fa fa-search']'
# Templates_SideHeader='//*[@id=\'appContainer\']//div[contains(text(),\'Templates\')]'
# ScoutLibrary_Add_Template='//*[@id=\'appContainer\']//i[@class=\'fa fa-plus-circle fa-1x\']'
# ##############Create New Report Locators
# ReportName_Input ='//input[@placeholder=\'Scouting Report Name\']'
# ScoutReportName_Input ='//input[@placeholder=\'Scouting Report Name\']'
# #Opponent_Dropdown=''
# #GameDate_Dropdown=''
# BlankTemplate_Checkbox= '//*[@id=\'blankTemplate\']'
# SavedTemplate_Checkbox= '//*[@id=\'savedTemplates-label\']'
# #SavedTemOpp_Dropdown = '//input[@id=\'choosesavedTemplateDropdown\']'
# #BlankTemplate_Checkbox= '//label[contains(text(,\'Blank Template\')]'
# INPUT_SELECTYOURGM = '//*[@class=\'Select-input\']/child::input'
# SavedTemplate_Dropdown= '//label[contains(text(),\'Choose your Template\')]'
# #'//*[@class="Select-placeholder"][contains(text(),'Choose your Template')]'
# SavedTemplate_List= '//input[@id=\'choosesavedTemplateDropdown\']'
# ScoutLibrary_Start_Button='//*[@id="start-scout-button"]'
# #ScoutLibrary_Cancel_Button=''
# #Commented out below GameDate_CalendarIcon element as it was not being identified.
# #GameDate_CalendarIcon='*//i[@class=\'fa fa-calendar\']'
# GameDate_CalendarIcon='//input[@placeholder=\'Select Game Date\']'
# GameDate_Calendar='//*[@id=\'createReportOpenCalendar\']/div'
# GameDate = '//*[@id=\'createReportOpenCalendar\']//button[15]/time'
# MySocuts_From_TopMenu ='//*[@id=\'library-nav-link\']'
# QA_Template_Building ='//td//span[text()="selfscout1"]'
# Change_Date = '(//span[@class=\'cursor-pointer\'])[2]'
# Edit_Game_Date = '(//input[@type=\'text\'])[2]'
# Click_Date = '//time[@datetime=\'2019-03-29T00:00:00.000\']'
# Save_Report = '//span[text()=\'Save\']'
# #####
# ERROR_MESSAGE = '//*[@class=\'error-message\']'
# #++++++++++++++++++newly added ones
# #Locators added on Sep21st 2018 after redesign
# MyScouts_MainHeader_OpponentScouts = '//*[@id=\'opponents-0\']'
# MyScouts_MainHeader_SelfScouts = '//*[@id=\'self-1\']'
# MyScouts_ManinHeader_OfflineScouts = '//*[@id=\'offline-2\']'
# MyScouts_ManinHeader_Templates =  '//*[@id=\'templates-3\']'
# #MyScouts_MainHeader_Archived = '//span[@class="display-flex align-items-center"][contains(text(),"ARCHIVED")]'
# MyScouts_ManinHeader_Archived ='//*[@id=\'archived-4\']'
# MyScouts_AddReport_Icon = '//span[@class=\'helvetica-neue-bold cursor-pointer\'][contains(text(),\'NEW SCOUTING REPORT\')]'    #'//*[@id=\'plus-id\']'
# MyScouts_OpponentScout_LastModified = '//*[@id=\'modified-by-header-id\']/i'
# My_Template = '//*[@id=\'report-row-id\']/td[3]/span/span'
# Create_Template = '//span[@class=\'cursor-pointer\']'
# Insert_TemplateName = '//input[@class=\'round-input full-width md-font height-30\']'
# Save_Template = '//span[@class=\'pd-right-lg pd-left-lg\']'
# CURR_EDIT = '//*[@id=\'report-row-id\']/td[9]'
# SHOW_MENU = '//*[@id=\'reportsTable\']/tbody/tr[${i}]/td[11]'
# DUPLICATE_MENU = '//*[@id=\'duplicate\']'
# OFFLINE_MENU = '//*[@id=\'offlineAccess\']'
# ONLINE_MENU = '//*[@id=\'onlineAccess\']'
# MyOpponents_Select_A_Team_Pro = '//span[text()="Atlanta"]'
# MyOpponents_Select_A_Team = '//span[text()=\'Cincinnati\']'
# Four_Factors_Graph_Verify = '//i[@class="fa fa-refresh fa-spin"]'
# Four_Factors_Graph ='(//i[@class=\'fa fa-bar-chart\'])[1]'
# ENTER_DUPLICATE = '//Input[@class=\'placeholder-light-gray display-block\']'
# DUPLICATE_SAVE = '//a[contains(.,\'Save\')]/Span'
# CLICK_OPPONENTSCOUT_DELETE = '//*[@id=\'delete\']'
# CLICK_OPPONENTSCOUT_ARCHIVE = '//*[@id=\'archive\']'     #'//*[@id=\'archive\']'
# DELETE_ICON = '//a[contains(.,\'Delete\')]'
# SB_Delete_Icon ='//a[text()="Delete"]'
# # OPPONENTSCOUT_DELETE = '//a[@class=\'color-danger hover-color-danger-darken outline-none bg-color-white color-danger border-width-1px border-style-solid border-radius-xxl border-color-danger hover-border-color-danger-darken cursor-pointer md-font pd-top-sm pd-right-md pd-bottom-sm pd-left-md hover-bg-color-danger hover-color-white\']'
# DUP_RPT_VALI = '//*[@id=\'reportsTable\']/tbody/tr[2]/td[3]'
# MOBILE_MENU = '//*[@id=\'mobileAccess\']'
# CLICK_MOBILE = '//i[@class=\'fa fa-square-o color-light-gray mg-right-sm hover-color-primary\']'
# MOBILE_SAVE = '//a[contains(.,\'Save\')]/Span'
# MOBILE_ICON = '//*[@id="reportsTable"]/tbody/tr[2]/td[9]/span[1]/span/i'
# CLICK_LOCK = '//*[@id=\'lockReport\'][contains(.,\'Lock\')]'
# CLICK_UNLOCK = '//*[@id=\'lockReport\'][contains(.,\'Unlock\')]'
# LOCK_ADDED = '//*[@id=\'reportsTable\']/tbody/tr[2]/td[9]/span/span/i'
# UNLOCK_STATUS = '//*[@id=\'reportsTable\']/tbody/tr[2]/td[9]'
# CLICK_RESTORE = '//*[@id=\'importFromBackup\']'
# RESTORE_TITLE = '//*[@class=\'Modal--content sm\']/div/div/child::h3'
# RESTORE_CANCEL = '//*[@id=\'import-scout-version-button\']'
# RESTORE_IMPORT = '//*[@id=\'cancel-version-import-button\']'
# POPUP_MENU='*//div[@class=\'light-box-shadow\']'
# #Exit_Template = '//*[@id=\'exitScoutBuilder\']/span'
# MyScouts_OpponentScout = '//*[@id=reportsTable\']/tbody/tr[${i}]/td[8]'
# MyScouts_Templates = '//*[@id=\'templatesTable\']/tbody/tr[${i}]/td[3]'  #'//*[@id=\'scout-report-container-id\']/div/div/div/div/table/tbody/tr[2]/td[3]/span/span'
# MyScouts_DeleteTemplates = '//*[@id=\'delete\']'
# MyScouts_RenameTemplates = '//*[@id=\'rename\']'
# MyScouts_SelfScouts = '//*[@id=\'self-1\']'   #'//*[@id=\'[object Object]-1\']/span'
# ID_OF_YOUR_DATEPICKER = '//input[@class=\'border-style-solid border-width-1px border-color-light-gray align-items-center color-black bg-color-white display-flex focused-border-shadow line-height-1 mg-none pd-top-sm pd-bottom-sm pd-right-md pd-left-md resize-none\']'
# Calender_PickerID = '//*[@id=\'createReportOpenCalendar\']'
# #ScoutBuilder Locators
# SB_PrintReport_Icon = '//*[@id=\'appContainer\']//li/span/i[@class=\'fa fa-print\']'
# INPUT_SELECTYOURGM = '//*[@class=\'Select-input\']/child::input'
# Support_Portal_Icon ='//*[@class=\'font-awesome-count\']'
# ###added by Uma
# Divison_I='(//div[@class=\'display-flex\'])[1]/div[1]'
# Division_II='(//div[@class=\'display-flex\'])[1]/div[2]'
# Division_III='(//div[@class=\'display-flex\'])[1]/div[3]'
# #############Print Modal Locator
#
# ########(IV)Print Modal Locators
# #PrintPreview_Modal = '//*[@id=\'print-preview\']'
# PrintPreview_Modal = '//*[@id=\'print-preview-header\']'
#
# #############(V)Scout Builder Locators
# #SB_FS_Logo&Title=''
# SB_DESIGN = '//div[contains(text(),\'DESIGN\')]'
# SB_TILES = '//div[contains(text(),\'TILES\')]'
# SB_Collapse_SideMenuPointer='//*[@id="scoutBuilderSideBarOptions"]/div/span/i'
# SB_PageHeader ='//*[@id="scoutBuilderSideBarOptions"]'
# SB_Reportstyle_SectionHeader ='//div[@class=\'Collapsible cursor-pointer\']/span[starts-with(text(),\'Report Style\')]'
# SB_Reportstyle_Collapse='//span[@class=\'Collapsible__trigger is-open  collapse-heading active\'][contains(text(),\'Report Style\')]'
# SB_Tiles_Collapse='//span[@class=\'Collapsible__trigger is-closed  collapse-heading\'][contains(text(),\'Tiles\')]'
# #some additional xpath //*[@id="appContainer"]//span[contains(text(),"Report Style")]
# SB_Tiles_SectionHeader ='//*[@id=\'appContainer\']//div[@class=\'Collapsible cursor-pointer\']//span[starts-with(text(),\'Tiles\')]'
# SB_AccountCustomTiles_SectionHeader ='//*[@id=\'appContainer\']//span[starts-with(text(),\'Custom Tiles\')]'
# SB_Spacer_Tile='//*[@id=\'individualTileMenuOption-spacer\']'
# SB_SectionHeaderTile='//*[@id=\'individualTileMenuOption-section\']'
# SB_Pagination_SectionHeader ='//*[@id=\'scoutBuilderPagination\']'
# SB_LeaderTile='//*[@id=\'individualTileMenuOption-leaders\']'
# SB_EXIT_ICON = '//*[@id=\'exitScoutBuilder\']'      #'//*[@id=\'appContainer\']//span[@title=\'Exit\']'
# CLICKUPLOADFILE = '//*[@class=\'display-flex justify-content-center align-items-center full-width flex-direction-column\']/div/child::a'  #'//a[@id[contains(.,\'image-upload\')]]'
# CLICKIMAGEPLAY = '//*[@id=\'individualTileMenuOption-image\']'
# UPLOADFILRFRAME = '//*[@id=\'tile419531\']/div/div[2]/div[2]/div/div/div/div'
# FILEPATH = 'C://Vrushali//Report//QATeam'
# #MyOpponents
# MyOpponents_Search_Teams_Box = '//*[@id=\'react-select-2--value\']//input'#'//input[@type="text"]'
# Result_Indiana = '//span[text()="Indiana"]'
# #Season_Text_Previous = '//a[@class=\'display-block pd-left-lg pd-right-lg hover-color-yellow-green pd-bottom-md\'][contains(text(),\'2017-2018\')]'      #'//div[text()=\'2017-2018\']'
# MyOpponents_Search_Template = '//*[@id="templatesTable"]/tbody/tr[1]/td[3]'     #'//table[@id="reportsTable"]/tbody//td[@id="search-icon-id"]'           #'//*[@id=\'templatesTable\']/tbody/tr[1]/td[3]/input'
# MyOpponent_Scout_Search = '//*[@id=\'search-icon-id\']/input'
# ArrowDropDown = '//*[@id=\'team-dropdown-id\']/span/span/i'    #'//span[@class=\'text_nowrap\']'
# #Click_Arrow_Drop_Down = '//div[@id=\'team-dropdown-id\']/span'
# ArrowDropDownIndianaText = '//div[@class=\'position-absolute text-center box-shadow-sm bg-color-white color-black mg-top-sm\']/div[12]/span'
# ArrowDroDownAllText = '//div[@class=\'position-absolute text-center box-shadow-sm bg-color-white color-black mg-top-sm\']/div[1]/span'
# MS_Templates_Search_Result = '//span[text()=\'QA Template\']'
# MyOpponentsSearchIcon = '//*[@id="templatesTable"]/tbody/tr[1]/td[3]/input'   #'//table[@id="reportsTable"]/tbody//td[@id="search-icon-id"]/input'
# #ScoutBuilder PageNotifications
# #SB_PageNotification="*//div[@class="Modal--content xs"]"
# #Scout Builder TopNav Locators
# SB_TopNav_CreateTemplate_Icon = '//*[@id=\'createTemplate\']'
# SB_TopNav_EditDate_Icon = '//*[@id=\'editDate\']'
# SB_TopNav_DuplicateReport_Icon= '//*[@id=\'copy\']'
# SB_TopNav_Print_Icon= '//*[@id=\'print\']'
# SB_TopNav_HelpIcon= '//*[@id=\'help\']'
# UPDATE_TEMPLATE = '//input[@value=\'update\']'
# SB_PageIsFull_MsgBox = '//div[@class=\'Modal--content xs\']//span'
# #SB_AddNewPage_ChkBox = '*//div[@class=\'Modal--content xs\']//li[@class=\'mg-right-lg\']//input[@type=\'checkbox\']'      #*//div[@class="Modal--content xs"]//li[@class="mg-right-lg"]//
# SB_AddNewPage_ChkBox='*//li[@class=\'mg-right-lg\']//input[@type=\'checkbox\']'
# SB_TileSave_Btn = '//div[@class=\'Modal--content xs\']//a'
# Report_Style='//div[@class=\'Collapsible cursor-pointer\']/span[contains(text(),\'Report Style\')]'
# Themes='//*[@id=\'reportStyleThemes\']'
# Colors='//span[@id=\'reportStyleColors\']'
# Our_Opponent_Text_Area ='//span[contains(text(),\'Our Opponent\')]'
# Our_Opponent_Hamburger ='//i[@class="fa fa-bars fa-lg"][1]'
# SB_TextTile = '//*[@id=\'individualTileMenuOption-text\']'
# SAVE_CUSTOMTILE = '//*[@class=\'fa fa-save\']'
# #'//*[@class=\'fa fa-save\'][contains(text(),\' Save as Custom Tile\')]'
# Chart_Options = '//span[text()="OPTIONS"]'
# Chart_Games = '//span[text()="GAMES"]'
# SM_Short_Chart = '//span[text()="Shot Chart"]'
# Last_5_Games = '//input[@id="gamesLast#OfGamesRadioButton"]'
# CSS_SVG = 'svg[class="helvetica-neue-medium"]'
# CSS_Hex_Group = 'g#hex-group'
# CSS_Hexagon = 'path[class="hexagon"]'
# CSS_Zone_Group = 'g#zone-group'
# CSS_Class_Zone = 'path[class="zones"]'
# CSS_Made_Shot = 'circle[class="made-shot"]'
# CSS_Missed_Shot = 'path[class="missed-shot"]'
# SM_Player_Chart = '//div[@id="individualTileMenuOption-Player Chart"]'
# CSS_MyTeam_TeamComparison = 'svg[class="recharts-surface"]'
# SP_TeamComparison = '//div[contains(text(),\'Team Comparison\')]'
# Text_Tiles= '//div[contains(text(),"Text")]'
# INPUT_CUSTTILE = '//*[@class=\'mg-bottom-md font-weight-bold\']//following-sibling::input'
# SAVE_CUSTOMTILEBTN = '//span[@class=\'pd-right-md pd-left-md\']'
# ADD_CUSTOMTILE = '//*[@id=\'individualTileMenuOption-EDITABLE_TABLE\']'
# ADD_TEXTTITLE = '//*[@id=\'individualTileMenuOption-text\']'
# OFFLINESCOUTS = '//*[@id=\'offline-2\']'    #'//*[@id=\'[object Object]-2\']'
# OPPONENTSCOUTS = '//*[@id=\'opponents-0\']'   #'//*[@id=\'[object Object]-0\']'
# TEXT_PENCIL = '//div[@class=\'public-DraftStyleDefault-block public-DraftStyleDefault-ltr\']'
# TextArea_Editor='(*//div[@class=\'DraftEditor-editorContainer\']//div[@role=\'textbox\'])[1]'
# ADD_CUSTOMTABLE = '//span[@class=\'color-light-gray hidden-print whitespace-nowrap\']'
# CLICK_CUSTOMTILES = '//*[@class=\'Collapsible__trigger is-open  collapse-heading active\']'
# TEXTADDED = '//*[@id=\'accountCustomTile-TextAdded\']'
# CHECKMARK = '//*[starts-with(@id,\'checkmark\')]'
# CUSTOM_TABLEADDED = '//*[@id=\'418003-custom-table\']/thead/tr/th[2]/div/span'
# SB_Custom_Tiles='//span[text()="Custom Tiles"]'
# TextArea_Editor='(*//div[@class=\'DraftEditor-editorContainer\']//div[@role=\'textbox\'])[1]'
# ADD_RECENTTABLETILE = '//*[@id=\'individualTileMenuOption-recentGames\']'
# RECENT_SAVEMENU = '//*[starts-with(@id,\'tile\')]/div/div[1]/ul'
# SB_RecentGamesTile = '//*[@id=\'individualTileMenuOption-recentGames\']'
# Page_Management_Exit_Icon= '//*[@id=\'appContainer\']//i[@class=\'fa fa-times fa-1x pd-bottom-sm\']'
# Get_OpponentsReportName='//*[@id=\'scout-report-container-id\']//tr[@id=\'report-row-id\'][2]/td[3]//span/span'
# Get_SelfScoutsReportName='//*[@id=\'scout-report-container-id\']//tr[@id=\'report-row-id\'][2]/td[3]//span/span'
# Delete_Page_Icon ='//*[@class="fa fa-trash fa-1x pd-bottom-sm"]'
# Delete_Page ='//i/span[text()="2"]'
# SB_FirstPage='*//i[@class=\'fa fa-angle-double-left\']'
# SB_LastPage= '*//i[@class=\'fa fa-angle-double-right\']'
# SB_Delete_Icon ='//a[text()="Delete"]'
# SB_Cancel_Icon ='//a[contains(text(),"Cancel")]'
# Get_Pagecount_fromHeader='//*[@id=\'appContainer\']//span[@class=\'pd-left-sm pd-right-sm\']'
# Get_PageCount_fromPM='*//span[starts-with(@id,\'pagination\')]'
# PageNumber='1'
# Modify_Text ='//span[text()="Our Opponent"]/../../following-sibling::div//div[@class="DraftEditor-editorContainer"]'
# #Modify_Text = '//*[@class="public-DraftStyleDefault-block public-DraftStyleDefault-ltr"]/span/span'
# SB_Text_Modify_I ='//em[text()="I"]'
# SB_Text_Modify_U ='//span[text()="U"]'
# SB_Text_Modify ='//*[@class="fa fa-code"]'  # </>
# SB_Text_Modify_Brush ='//*[@class="fa fa-paint-brush"]'
# Arrow_Down ='//*[@class="fa fa-angle-down"]'
# Arrow_Up ='//*[@class="fa fa-angle-up"]'
# Dubol_Core ='//*[@class="fa fa-quote-right"]'
# Left_Side ='//*[@class="fa fa-list-ul"]'
# Right_Side ='//*[@class="fa fa-list-ol"]'
# SB_Text_Modify_Color_Red ='//*[@title="#DB3E00"]'
# SB_Text_Modify_Color_Blue ='//*[@title="#1273DE"]'
# SB_Colors_Main_Color_Blue ='//div[text()="Main Color"]/..//div[contains(@title,"00539B")]' #'//div[@title="#00539B"]'
# SB_Text_Modify_B ='//strong[text()="B"]'
# SB_Click_Arrow_To_Next_Page ='//*[@class="fa fa-angle-right"]'
# Personnel_Text = '(//div[@class=\'flex-grow-1 tile-content\'])[18]'
# Select_Text ='//span[text()="Our Opponent"]/../../following-sibling::div//div//span[text()="This is a Test Text "]'
# Page_Management ='//*[@id="scoutBuilderPagination"]'
# Add_Page ='//*[@class="cursor-pointer flex-basis-0 flex-grow-1"]'
# Add_Page_Redesign='//*[@id=\'reportArea\']//i[@class=\'fa fa-plus-circle fa-2x color-white hidden-print\']'
# Delete_Page_Icon ='//*[@class="fa fa-trash fa-1x pd-bottom-sm"]'
# Delete_Page ='//i/span[text()="2"]'
# SB_Report_Style_Header_Design = '//*[@id=\'reportStyleHeaderDesigns\']'
#
# # Changed by Vrushali - Rel 2.4.10
# SB_Team_Record_On_Off_ND='//label[@id=\'teamRecordToggle-label\']'
#
# #Old Staging Element as of Rel 2.4.9
# SB_Team_Record_On_Off ='//label[text()="Team Record"]/../div'
# #Old Staging Element
#
# #SB_Header_Design_After_One_Page_01 ='//*[@id="appContainer"]//div[1]//div/main/span//div[2]/section/div[11]/label/span'
#
# # # Old code on Staging until Rel 2.4.9
# # SB_Header_Design_After_One_Page_01 = '//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[11]/label/span/div/span/span'
# # SB_Header_Design_After_One_Page_02 = '//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[12]/label/span/div/span/span'
# # SB_Header_Design_After_One_Page_03 = '//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[13]/label/span/div/span/span'
#
# #Changed by Vrushali - Rel 2.5.1
# SB_Header_Design_First_One_Page_first = '//span[@id=\'first-header-size-option-FULL\']'
# SB_Header_Design_First_One_Page_second = '//span[@id=\'first-header-size-option-CONDENSED\']'
# SB_Header_Design_First_One_Page_third = '//span[@id=\'first-header-size-option-NONE\']'
#
# SB_Header_Design_After_One_Page_second = '//span[@id=\'header-size-option-CONDENSED\']'
# SB_Header_Design_After_One_Page_first = '//span[@id=\'header-size-option-FULL\']'
# SB_Header_Design_After_One_Page_third = '//span[@id=\'header-size-option-NONE\']'
#
# #SB_Header_#Design_After_One_Page_02 ='//*[@id="appContainer"]//div[1]//div/main/span//div[2]/section/div[12]/label/span'
#
# # Old code on Staging until Rel 2.4.9
# SB_Header_design_First_One_page_01='//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[7]/label/span/div/span/span'
# SB_Header_design_First_One_page_02='//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[8]/label/span/div/span/span'
# SB_Header_design_First_One_page_03='//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[9]/label/span/div/span/span'
#
# SB_Header_Design_After_One_Page_01 ='//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[11]/label/span/div/span/span'
# SB_Header_Design_After_One_Page_02 ='//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[12]/label/span/div/span/span'
# SB_Header_Design_After_One_Page_03 ='//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/div[2]/div/div/div[2]/section/div[13]/label/span/div/span/span'
#
# #SB_Header_Design_After_One_Page_03 ='//*[@id="appContainer"]//div[1]//div/main/span//div[2]/section/div[13]/label/span'
#
# SB_Custom_Table_Tile='//*[@id=\'individualTileMenuOption-EDITABLE_TABLE\']'
# SB_DepthChart_Tile='//*[@id=\'individualTileMenuOption-depthChart\']'
# Click_On_VideoCam ='//*[@class="fa fa-video-camera"]'
# Click_Upload = '//*[@id=\'uploadButton\']'     #'//div[@class=\'display-flex justify-content-center\']/child::a'      #'//span[text()="Upload"]'
# Click_Another_Upload = '//i[@class=\'fa fa-plus fa-lg pd-right-sm\']'
# Save_Image ='//span[text()="Save"]'
# SB_Tile_Formatting = '//*[text()=\' Tile Formatting\']'
# Header_Size = '//div[text()=\'Header Size\']'
# Size_Bar = '//div[@class=\'rangeslider__handle\']'
#
# ### Old Code on Staging
#
# Size_Bar_Color = '//div[@class=\'slidecontainer\']'
#
# ############# Added by Vrushali - Rel 2.4.10 instead of Size_Bar_Color
#
# TableRowAccent1 = '//span[@id=\'row-accent-1\']'
# TableRowAccent2 = '//span[@id=\'row-accent-2\']'
# TableRowAccent3 = '//span[@id=\'row-accent-3\']'
# TableRowAccent4 = '//span[@id=\'row-accent-4\']'
#
# ######################################################
# Header_Color = '//div[text()=\' Header Color\']'
# Text_Color = '//div[text()=\' Text Color\']'
# Header_Color_Blue1 = '(//div[@title=\'#00539B\'])[1]'
# Header_Color_Blue2 = '(//div[@title=\'#00539B\'])[2]'
# Header_Color_Black2 = '(//div[@title=\'#000000\'])[2]'
# Header_Color_Gray = '//div[@title=\'#434343\']'
# Header_Color_White = '//div[@title=\'#FFFFFF\']'
# Header_Color_Black1 = '(//div[@title=\'#000000\'])[1]'
# Text_Size = '//div[text()=\'Text_Size\']'
# Text_Size_Pro = '//div[text()=\'Text Size\']'
# Header_Color_Blue_Pro = '//div[@title=\'#4FA8FF\']'
# Header_Color_Red_Pro = '//div[@title=\'#E03A3E\']'
# Header_Color_Yellow_Pro = '//div[@title=\'#FFB20F\']'
# Header_Color_Green_Pro = '//div[@title=\'#C3D600\']'
# Header_Color_Black_Pro = '//div[@title=\'#434343\']'
# SB_Tiles_Team_Stats = '//div[text()=\'Team Stats\']'
# SB_Tiles_Personnel = '//div[text()=\'Personnel\']'
# SB_Tiles_TeamStats_FourFactors_TC5 = '//div[@id=\'individualTileMenuOption-FastScout Factors\']'
# SB_Tiles_TeamStats_FourFactors = '//div[text()=\'FastScout Factors\']'
# SB_Tiles_TeamStats_FourFactorsChart ='//*[@id="individualTileMenuOption-FastScout Factors Chart"]'  #'//div[text()=\'Four Factors Chart\']'
# SB_Tiles_TeamStats_PointsPerPeriod = '//div[text()=\'Points Per Period\']'
# SB_Tiles_TeamStats_TeamPaceChart ='//*[@id="individualTileMenuOption-Team Pace Chart"]'   #'//div[text()=\'Team Pace Chart\']'    #locators corrected
# SB_Tiles_TeamStats_TeamPace ='//*[@id="individualTileMenuOption-Team Pace"]' #'//div[text()=\'Team Pace\']'              #locators corrected
# SB_Tiles_TS_CS_TimeRem = '//input[@id=\'timeRemaining\']'
# SB_Tiles_TS_CS_ScoreWithin = '//input[@id=\'scoreWithin\']'
# SB_Tiles_IndividualBoxscore='//*[@id="individualTileMenuOption-Individual Boxscore"]'
# SB_Tiles_CumulativeBoxscore ='//*[@id="individualTileMenuOption-Cumulative Boxscore"]'
# SB_Tiles_TeamStatComparision = '//*[@id="individualTileMenuOption-Team Stat Comparison"]'
# SB_Tiles_TeamStatSplits = '//*[@id="individualTileMenuOption-Team Stat Splits"]'   # //*[@id="individualTileMenuOption-Team Stat Splits"]
# SB_Tiles_TeamAdvancedStats = '//div[contains(text(),\'Team Advanced Stats\')]'       #//*[@id="individualTileMenuOption-Team Advanced Stats"]
# SB_Tiles_TeamStats_ClutchStats = '//div[contains(text(),\'Clutch Stats\')]'          #//*[@id="individualTileMenuOption-Clutch Stats"]
# SB_Tiles_IndividualBoxscore = '//*[@id=\'individualTileMenuOption-Individual Boxscore\']'
# SB_Tiles_CumulativeBoxscore = '//*[@id=\'individualTileMenuOption-Cumulative Boxscore\']'
# SB_Tiles_TeamStatComparision = '//div[@id=\'individualTileMenuOption-Team Stat Comparison\']'
# SB_Tiles_TeamStatSplits = '//*[@id=\'individualTileMenuOption-Team Stat Splits\']'
# SB_Tiles_TeamAdvancedStats = '//div[contains(text(),\'Team Advanced Stats\')]'
# SB_Tiles_TeamStats_ClutchStats = '//div[contains(text(),\'Clutch Stats\')]'
# SB_Tiles_TeamStats_LineupStats = '//div[contains(text(),\'Lineup Stats\')]'    #'//*[@id=\'individualTileMenuOption-Lineup Stats\']'
# SB_Tiles_TSS_PTS = '//*[@id=\'col-item-PTS\']'
# SB_Tiles_TSS_FGMA = '//*[@id=\'col-item-FGM-A\']'
# SB_Tiles_TSS_3PM = '//*[@id=\'col-item-3PM-A\']'
# SB_Tiles_TSComp_GamesTab = '//li[@class="display-inline-block"]/child::span'
# SB_PageMang_Page1 = '//*[@id=\'pagination-0\']/i[2]'
# #SB_Tiles_TSComp_CurrSea_Chx5 = '//*[@id=\'checkbox-5\']'
# #SB_Tiles_TSComp_CurrSea_Chx6 = '//*[@id=\'checkbox-6\']'
# #SB_Tiles_TSComp_CurrSea_Chx7 = '//*[@id=\'checkbox-7\']'
# SB_Tiles_CB_Per40 = '//*[@id=\'aggregate-input-1\']'
# SB_Tiles_CB_RoundingNum = '//*[@id=\'input-1\']'
# Add_Page_Redesign='//*[@id=\'reportArea\']//i[@class=\'fa fa-plus-circle fa-2x color-white hidden-print\']'
# SB_IndividualBoxscore_Season = '//div[@class=\'react-toggle player-menu-toggle has-border mg-right-sm mg-left-sm\']'    #'//input[@name=\'lastSeason\']'
# SeasonTeam_Selected = '(//*[@id="input-2"])[1]' #'//*[@id=\'input-2\']'   #corrected
# TeamPace_OpponentCol = '//*[@id=\'col-item-Opponent\']'
# TeamPace_DIAverage = '//*[@id=\'col-item-D-I Average\']'
# SB_Tiles_PointsPerPeriodTab = '//div[@class=\'display-flex pd-right-xl mg-bottom-lg\']/child::div[2]'
# #'//*[@id=\'Duke Blue Devils\']'
# #SB_Tiles_PointsPerPeriodDenver = '//*[@id=\'Denver Nuggets\']'
# DepthChartFilter = '//i[@class=\'fa fa-exchange hidden-print color-medium-gray hover-color-primary\']'
# EXIT_SHOTCHART = '//*[@id="appContainer"]/div/div[1]/div/div/div/div/div/div/main/span/div/div/div[2]/div[1]/span/img'
# ShotChartText = '//div[text()=\'Shot Charts\']'
# SelectStatPer = '//*[@id=\'fourFactorChartStatDropdown\']'
# SelectTurnOver = '//*[@id=\'fourFactorChartStatDropdownOption-1\']'
# SelectPlayersDropDown = '//select[@class=\'hidden-print\']'
# SelectPlayer = '//select[@class=\'hidden-print\']/child::option[2]'
# #SB_Tiles_Team_Stats_Add_Tile = '//span[text()=\'Add Tile\']'   #Making more reusable aka AddTile
# Add_Tile='//span[text()="Add Tile"]'
# ClickTitle = '//span[text()=\'Tiles\']'
# ###ByUma_Apr19
# Tile_OptionsTab_CheckBox_MyOffense='//*[@id=\'checkbox-self_offense\']'
# Tile_GamesTab='//span[contains(text(),\'GAMES\')]/parent::li' # FS2.4.8 changes '//div[@class=\'menu-overlay-left\']//span[contains(text(),\'GAMES\')]/parent::li'
# Tile_OptionsTab='//span[contains(text(),\'OPTIONS\')]'  # FS2.4.8 changes  '*//div[@class=\'menu-overlay-left\']//span[contains(text(),\'OPTIONS\')]'
# Tile_StatsTab='//span[contains(text(),\'STATS\')]'     #FS2.4.8 changes  '*//div[@class=\'menu-overlay-left\']//span[contains(text(),\'STATS\')]'
# Tile_PlayersTab='//span[contains(text(),"PLAYERS")]' # FS2.4.8 changes  '*//div[@class="menu-overlay-left"]//span[contains(text(),"PLAYERS")]'
# Tile_GamesTab_CheckBox_Last5='//*[@id=\'gamesLast#OfGamesRadioButton\']'
# #############(VI)Chrome Print Modal Locators
# # Chrome Print and save locators
# #PrintButton_PR_Modal = '//*[@id=\'print-header\']//button[contains(text(),\'Print\')]'
# PrintButton_PR_Modal = '//*[@id=\'print-preview-header\']/div/child::paper-button[1]'
# ChangeButton_PR_Modal = '//*[@id=\'destination-settings\']//button'
# SelectDestination_View = '//*[@id="destination-search"]/div[@class="page"]'
# SelectDestination_Header = '//*[@id="destination-search"]/div/h1'
# Close_PR_Modal = '//*[@id=\'destination-search\']//div[@class=\'page\']/div[@class="close-button"]'
# CancelButton_PR_ModalInset = '//*[@id=\'destination-search\']//div[@class=\'page\']//div/button'
# SaveAsPDF_PR_ModalInset='//*[@id=\'destination-search\']//div[@class=\'destination-list\']//span[@title=\'Save as PDF\']'
# SaveButton_PR_Modal = '//*[@id=\'print-header\']/div/button[text()=\'Save\']'
#
# ###########(VII)Duplicate Report Modal Locators
# #Duplicate Report modal locators
# DR_Modal='*//h4[contains(text(),\'Duplicate Report\')]'  #*//div[@class=\'Modal--content xs\']//h4[contains(text(),\'Duplicate Report\')]'
# ReportName_Label_DR_Modal= '*//label[contains(text(),\'Name Your Report\')]' #'*//div[@class=\'Modal--content xs\']//section[@class=\'pd-md pd-md avenir-regular md-font\']//label'
# ReportName_Input_DR_Modal= '*//input[@placeholder=\'Report Name\']' #'*//div[@class=\'Modal--content xs\']//section[@class=\'pd-md pd-md avenir-regular md-font\']//input[@placeholder=\'Report Name\']'
# SaveButton_DR_Modal= '*//div/footer//a' #'*//div/footer//span[contains(text(),\'Save\')]'
#
# #############Some additional locators
#
# email_x = '//*[@id=\'email\']'
# #############Schedule Page Boxscore Locators
# Play_By_Play = '//*[@id=\'playByPlay-2\']'
#
# ###FS2.4.3 New Locators####FS2.4.3
# Header_Color_Position1='(//div[@tabindex=0])[1]'
# Header_Color_Position2='(//div[@tabindex=0])[2]'
# Header_Color_Position3='(//div[@tabindex=0])[3]'
#
# ####################################################################################
#
# ##Main Color Palatte - Old Staging Code
#
# mainbluecolor = '//span[@id=\'mainColorPicker\']/div/div[3]/span[1]/div'
# mainblackcolor = '//span[@id=\'mainColorPicker\']/div/div[3]/span[2]/div'
# mainredcolor = '//span[@id=\'mainColorPicker\']/div/div[3]/span[3]/div'
# mainblack1color = '//span[@id=\'mainColorPicker\']/div/div[3]/span[4]/div'
# maingraycolor = '//span[@id=\'mainColorPicker\']/div/div[3]/span[5]/div'
#
# ###################################################################################
#
# # Changed by Vrushali - Rel 2.4.10
#
# mainbluecolor1 = '//span[@id=\'main-color-2\']'
# mainblackcolor2 = '//span[@id=\'main-color-1\']'
# mainredcolor3 = '//span[@id=\'main-color-0\']'
# mainblack1color4 = '//span[@id=\'main-color-3\']'
# maingraycolor5 = '//span[@id=\'main-color-custom\']'
#
# ##################################################################################
#
# ## Accent Color Palatte - Old Staging Code
#
# accentbluecolor = '//span[@id=\'accentColorPicker\']/div/div[3]/span[1]/div'
# accentblackcolor = '//span[@id=\'accentColorPicker\']/div/div[3]/span[2]/div'
# accentredcolor = '//span[@id=\'accentColorPicker\']/div/div[3]/span[3]/div'
# accentblack1color = '//span[@id=\'accentColorPicker\']/div/div[3]/span[4]/div'
# accentgraycolor = '//span[@id=\'accentColorPicker\']/div/div[3]/span[5]/div'
#
# #################################################################################
#
# # Changed by Vrushali - Rel 2.4.10
#
# accentbluecolor1 = '//span[@id=\'accent-color-2\']'
# accentblackcolor2 = '//span[@id=\'accent-color-1\']'
# accentredcolor3 = '//span[@id=\'accent-color-0\']'
# accentblack1color4 = '//span[@id=\'accent-color-3\']'
# accentgraycolor5 = '//span[@id=\'accent-color-custom\']'
#
# ##################################################################################
#
# PlayByPlay = '//*[@id=\'playByPlay-2\']'
# Result = '//*[@id=\'myTeamSchedule\']/tbody/tr[1]/td[6]/a/span/span'
# P_Chart_Icon = '//span[@id="paceTableHeader"]'
# #P_Chart_Icon = '//span[@id=\'paceTableIcon\']'
# FourFactor_GraphIcon = '//span[@id=\'fourFactorsChartIcon\']'              #'//*[@id=\'myTeamFourFactorsChartIcon\']//i[@class=\'fa fa-bar-chart\']'
# Pace_GraphIcon= '//span[@id=\'paceChartIcon\']'         #'//*[@id=\'paceChartIcon\']/i'
# InputCreateTemplate = '//input[@class=\'round-input full-width md-font height-30\']'
#
# #SB_Presenter Mode
# SB_TopNav_PresenterModeIcon = '//i[@class=\'fa fa-play fa-lg\']'  #or //*[@id=\'startPresenterModeButton\']
# PM_Panel = '//*[@id=\'report-presenter\']'
# PM_TopNav_Exit = '//*[@id=\'report-presenter\']//a[contains(text(),EXIT)][2]'
# PM_TopNav_MaxMinIcon = '//*[@id=\'report-presenter\']//a[1]'
# PM_TopNav_DownArrow = '//*[@id=\'report-presenter\']//i[@class=\'fa fa-caret-down\']'
# PM_TopNav_RightArrow = '//*[@id=\'report-presenter\']//i[@class=\'fa fa-caret-right\']'
# PM_Teamlogo = '(//*[@id="report-presenter"]//img)[1]'
# Get_ReportName_inPM = '//*[@id="report-presenter"]//span[1]'
# PM_LeftCarousel = '//*[@id=\'report-presenter\']//div/i[@class=\'fa fa-chevron-left\']'
# PM_RightCarousel = '//*[@id=\'report-presenter\']//div/i[@class=\'fa fa-chevron-right\']'
#
# SB_StatType_Totals = '//i[@class="fa fa-circle color-primary"]//following-sibling::span'
#
# SB_TS_OPtions_STLPer = '//*[@id=\'checkbox-STL%-2\']'
# SB_TS_OPtions_OREBPer = '//*[@id=\'checkbox-OR%-3\']'
# SB_TS_OPtions_ASTPer = '//*[@id=\'checkbox-AST%-3\']'
# SB_TS_OPtions_BLKPer = '//*[@id=\'checkbox-BLK%-3\']'
# SB_TS_OPtions_DRPer = '//*[@id=\'checkbox-DR%-4\']'
# SB_TS_OPtions_TOPer = '//*[@id=\'checkbox-TO%-4\']'
# SB_TS_OPtions_eFGPer = '//*[@id=\'checkbox-eFG%-5\']'
# SB_TS_OPtions_TSPer = '//*[@id=\'checkbox-TS%-6\']'
# SB_TS_OPtions_USGPer = '//*[@id=\'checkbox-Usg%-7\']'
# SB_TS_StatType_Average = '//*[@id="aggregate-input-0"]'
# SB_TS_Stats_ORTG = ' //*[@id="checkbox-ORtg-0-label"]/span/div'
# SB_TS_Stats_DRTG = '//*[@id="checkbox-DRtg-1-label"]/span/div'
# SB_TS_Stats_NRTG = '//*[@id="checkbox-NRtg-2-label"]/span/div'
# SB_TS_USG_ToolTip = '//*[contains(text(),\'Included with Advanced Stats Package\')]'
# SB_TS_eFG_Tooltip = '(//div[contains(text(),"Included with Advanced Stats Package")])[2]'
# SB_TS_USG_ChxBox = '//i[@id=\'checkbox-Usg%-7\']'
# SB_TS_NRTG_ChxBox = '//i[@id=\'checkbox-NRtg-2\']'
# SB_TS_NRTG_Tooltip = '(//div[contains(text(),"Included with Advanced Stats Package")])[1]'
# SB_TS_IndivBox_Options = '//span[contains(text(),\'OPTIONS\')]'
# SB_SubTile_OptionsTab='//span[contains(text(),\'OPTIONS\')]'
# SB_SubTile_SampleTab='//span[contains(text(),\'SAMPLE\')]'
# SB_SubTile_GamesTab='//span[contains(text(),\'GAMES\')]'
# SB_Subtile_PlayersTab='//span[contains(text(),\'PLAYERS\')]'
# SB_TS_STATS = '//span[contains(text(),\'STATS\')]'
# SB_TS_TAS_ToolTip = '(//span[contains(text(),"Included in Advanced Stats Package")])[1]'
# SB_TS_CS_ToolTip = '(//span[contains(text(),"Included in Advanced Stats Package")])[2]'
# SB_TS_LupS_ToolTip = '//*[contains(text(),\'Included in Lineup Stats Package\')]'
# SB_TS_STL_Tooltip ='/html/body/div[53]/div/div[1]/div'
# SB_TS_OREB_Tooltip ='/html/body/div[44]/div/div[1]/div'
# SB_TS_AST_Tooltip ='/html/body/div[49]/div/div[1]/div'
# SB_TS_BLK_ToolTip = '/html/body/div[54]/div/div[1]/div'
# SB_TS_DREB_Tooltip = '/html/body/div[45]/div/div[1]/div'
# SB_TS_TO_Tooltip = '/html/body/div[50]/div/div[1]/div'
# #SB_TS_eFG_Tooltip = '/html/body/div[29]/div/div[1]/div'
# SB_TS_TS_Tooltip = '/html/body/div[30]/div/div[1]/div'
# SB_AddAfterPage = '(//i[@class="fa fa-plus-circle fa-2x color-white hidden-print"])[1]'
# SB_NextPage = '//*[@id=\'next-page-arrow\']'
# SB_ADDPageND='//div[@id=\'add-report-page-button\']'
# SB_Page1ND='//li[@id=\'page-1\']'
# SB_Page2ND='//li[@id=\'page-2\']'
# SB_Page3ND='//li[@id=\'page-3\']'
# ClosePanel = '//i[@class=\'fa fa-times\']'
# #====================Locators by Uma Teamstats
# ###Below are locators in side ScoutBuilder TeamStats Tile Default Options checkboxes and Labels
# SB_TeamStats_OptionsLabel_OpponentOffense='//*[@id=\'checkbox-opponent_offense-label\']'
# SB_TeamStats_Checkbox_OpponentOffense='//*[@id=\'checkbox-opponent_offense\']'
# SB_TeamStats_OptionsLabel_OpponentDefense = '//*[@id=\'checkbox-opponent_defense-label\']'
# SB_TeamStats_Checkbox_OpponentDefense='//*[@id=\'checkbox-opponent_defense\']'
# SB_TeamStats_OptionLabel_MyOffense='//*[@id=\'checkbox-self_offense-label\']'
# SB_TeamStats_Checkbox_MyOffense='//*[@id=\'checkbox-self_offense\']'
# SB_TeamStats_OptionLabel_MyDefense='//*[@id=\'checkbox-self_defense-label\']'
# SB_TeamStats_Checkbox_MyDefense='//*[@id=\'checkbox-self_defense\']'
# SB_TeamStats_OptionsLabel_LeagueAvg='//*[@id=\'checkbox-league-label\']'
# SB_TeamStats_Checkbox_LeagueAvg='//*[@id="checkbox-league"]'
# ###Below are locators in side ScoutBuilder TeamStats Tile Default Options
# SB_TeamStats_StatsLabel_RebPer='//*[@id=\'checkbox-Reb %-0-label\']'
# SB_TeamStats_Checkbox_RebPer='//*[@id=\'checkbox-Reb %-0\']'
# SB_TeamStats_StatsLabel_FTR='//*[@id=\'checkbox-FTRate-1-label\']'
# SB_TeamStats_Checkbox_FTR='//*[@id=\'checkbox-FTRate-1\']'
# SB_TeamStats_StatsLabel_FTPer='//*[@id=\'checkbox-FT%-2-label\']'
# SB_TeamStats_Checkbox_FTPer='//*[@id=\'checkbox-FT%-2\']'
# #=====New in FS2.5.0
# SB_Tiles_ShotChart='//*[@id="individualTileMenuOption-shotChart"]'
