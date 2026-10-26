# E1 案例表（调参集，当前配置）

## miss · M-tune-007 · L2 rerank · dense_only, wrong_product, vocab_gap

- 问题：Does ODM 8.5.1 support MQ 9.0? Does ODM 8.5.1 support MQ 9.0 where ODM Rule Execution Server is running on WAS 8.5.0.2 (embedded with ODM)? No MQ version is specified in ODM 8.5.1 System Requirements.
- 改写后：Does ODM 8.5.1 support MQ 9.0? Does ODM 8.5.1 support MQ 9.0 where ODM Rule Execution Server is running on WAS 8.5.0.2 (embedded with ODM)? No MQ version is specified in ODM 8.5.1 System Requirements.
- 答案文档在各阶段名次：{'dense': 1, 'sparse': None, 'fusion': 2, 'rerank': 17}
- **答案文档** swg21312967｜IBM MQ, WebSphere MQ｜IBM MQ 7.x, MQ 8.0 and MQ 9.0 compatibility with previous versions - including usage of CCDT files, JMS .bindings, SSL/TLS - United States
  - compatibility; compatible TECHNOTE (FAQ) QUESTION Are WebSphere MQ (WMQ) V7.0, V7.1, V7.5 and V8.0 compatible with previous versions? Can an MQ 8.0 client use a CCDT created with a previous version? Can an MQ 7.0 client use a CCDT created with a newer version? Can a JMS .bindings file created in 7.1
- 重排第 1：swg21980095｜CICS Transaction Server, SSFVJY｜IBM Integration of CICS event support with ODM Decision Server Insights - United States
  - 5655Y0400 R680 680 R800 800 HCI6800 R690 690 R900 900 HCI6900 R700 700 R000 000 HCI7000 5655Y0401 5655-Y04 5655Y04 KIXINFO NEWS ABSTRACT Events from CICS can be consumed by IBM Operational Decision Ma
- 重排第 2：swg21646410｜IBM Operational Decision Manager｜IBM Operational Decision Manager support statement for virtual environments - United States
  - NEWS ABSTRACT Customers can employ various applications to provide an emulated or virtual operating environment in order to meet their needs, such as to provide production server consolidation, centra
- 重排第 3：ibm10717805｜IBM Operational Decision Manager｜IBM Operational Decision Manager Interim Fixes for V8.0 releases - United States
  - PREVENTIVE SERVICE PLANNING ABSTRACT Use interim fixes to address issues found in the releases in Operational Decision Manager V8.0 series. CONTENT The following table lists the interim fixes by versi

## miss · M-tune-015 · L1 retrieval: fusion cut · sparse_only, same_product, vocab_gap

- 问题：SPSS will not start on Mac I downloaded SPSS about 3 weeks ago. On the day when I downloaded it, it was working fine. Last week, I tried starting SPSS but it did not start. I tried reinstalling it, it still would not open. I've updated JAVA (thought this would be a problem), it slowly opened the program but then now that I have reinstalled it and entered in my code, I've used up my code and I have no authorization. But just now, I started SPSS and the same problem is happening. The IBM SPSS name
- 改写后：SPSS will not start on Mac I downloaded SPSS about 3 weeks ago. On the day when I downloaded it, it was working fine. Last week, I tried starting SPSS but it did not start. I tried reinstalling it, it still would not open. I've updated JAVA (thought this would be a problem), it slowly opened the pro
- 答案文档在各阶段名次：{'dense': None, 'sparse': 18, 'fusion': None, 'rerank': None}
- **答案文档** swg21651225｜SPSS Statistics｜IBM Performance issue on Mac OS X Launching and Closing SPSS Statistics 21 or 22. - United States
  - Mac OS X; Performance; open; close; exit; launch; 10.6.x 10.7.x 10.8.x 10.9.x TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) With SPSS Statistics 21 or 22 software installed on Mac OS X. The software was running normally, but for what ever reason, the program might fail or close improperly by using Fo
- 重排第 1：swg21688476｜SPSS Statistics｜IBM Will IBM SPSS Statistics 22 run on Apple OS Mac OS X, 10.10 Yosemite? - United States
  - TECHNOTE (FAQ) QUESTION I am plannig to update to the new Apple Mac OS X, 10.10 Yosemite and would like to know if IBM SPSS Statistics will run successfully on this OS. CAUSE OS Update ANSWER IBM SPSS
- 重排第 2：swg21480132｜SPSS Statistics｜IBM Assertion Failed! Expression: _env && "Error: Java environment could not initialized in JVizConverter." - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) I successfully installed SPSS for Windows, but when I try to start SPSS I get the following error message: Assertion failed! Program: \spsswin.exe File Z:\
- 重排第 3：swg21999184｜SPSS Statistics｜IBM Silent installation of release IBM SPSS Statistics 24 on Macintosh OSX Sierra (10.12) - United States
  - TECHNOTE (FAQ) QUESTION How do I perform a silent installation of IBM SPSS Statistics for Macintosh OSX Sierra 10.12.x? There are two ways to install Statistics 24 on Macintosh operating systems (Supp

## miss · M-tune-017 · L2 rerank · same_product, vocab_gap

- 问题：Is Java 8 supported for EJBDeploy on WebSphere Application Server 8.5.5.9 or later?
- 改写后：Is Java 8 supported for EJBDeploy on WebSphere Application Server 8.5.5.9 or later?
- 答案文档在各阶段名次：{'dense': 15, 'sparse': 11, 'fusion': 4, 'rerank': 11}
- **答案文档** swg21994741｜WebSphere Application Server｜IBM Learning more about EJBDeploy - United States
  - EJB; EJBDeploy TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Learning more about EJBDeploy is the first step in the troubleshooting process. This document provides you with educational information that can help you learn more about this topic. RESOLVING THE PROBLEM TAB NAVIGATION * Learning more [htt
- 重排第 1：swg24043474｜WebSphere Application Server｜IBM PI73197:Enable Java 8 Support for EJBDeploy on WebSphere Application Server - United States
  - PI73197; PI73197; PI73197 DOWNLOADABLE FILES ABSTRACT Enable Java 8 Support for EJBDeploy on WebSphere Application Server 8.5.5.9 or later. NOTE: After this fix is applied, EJBDeploy can no longer be 
- 重排第 2：swg1PI73197｜WebSphere Application Server｜IBM PI73197: Enable Java 8 Support for EJBDeploy on WebSphere Application Server - United States
  - A FIX IS AVAILABLE PI73197:Enable Java 8 Support for EJBDeploy on WebSphere Application Server [http://www-01.ibm.com/support/docview.wss?uid=swg24043474] SUBSCRIBE You can track all active APARs for 
- 重排第 3：swg21994742｜WebSphere Application Server｜IBM TroubleShooting: WebSphere Application Server Toolkit EJBDeploy problems - United States
  - EJB;EJBDeploy TROUBLESHOOTING PROBLEM Troubleshooting EJBDeploy problems in WebSphere Application Server. This should help address common issues with this component before calling IBM support and save

## miss · M-tune-019 · L1 retrieval: fusion cut · dense_only, wrong_product, vocab_gap

- 问题：Report stuck in current queue We have one report that has been showing in the admin current activities status tab for 20+ days and we have had 2 full re-starts since then. Also it appears we have interactive jobs staying around as well for past days and days. How can we clean this up ?
- 改写后：Report stuck in current queue We have one report that has been showing in the admin current activities status tab for 20+ days and we have had 2 full re-starts since then. Also it appears we have interactive jobs staying around as well for past days and days. How can we clean this up ?
- 答案文档在各阶段名次：{'dense': 23, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21371279｜Cognos Business Intelligence｜IBM Scheduled Cognos BI reports are stuck in Pending state - United States
  - deployment TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Schedules Cognos Business Intelligience reports are not running. Scheduled reports are stuck in "Pending" state forever. - Renewing credentials does not resolve the issue. After credentials are renewed, user still receives the same error indica
- 重排第 1：swg21975556｜IBM Connections｜IBM Community Metrics Reports Group By Geography Option Doesn't Show the Full Report - United States
  - cognos; community; metrics; geography TECHNOTE (TROUBLESHOOTING) PROBLEM When a user runs the People/Participation report and groups it by "Geography", the results don't not show all the data. There i
- 重排第 2：swg1IV93580｜Tivoli Netcool Performance Manager for Wireless｜IBM IV93580: TNPMW ACTIVE_JOB TABLE NOT BEING CLEANED - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS FIXED IF NEXT. ERROR DESCRIPTION * Customer reported that ACTIVE_JOB table has 22232 rows, ideally these should hav
- 重排第 3：isg3T1016388｜Platform LSF, Spectrum LSF｜IBM Jobs in job array still show up in bjobs even if they have completed for many days. - United States
  - job array LSB_CLEAN_PDONE_TIMEOUT bjobs cleanup TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Jobs in job array still show up in bjobs even if they have completed for many days. RESOLVING THE PROBLEM J

## miss · M-tune-021 · L1 retrieval: not retrieved · neither, wrong_product, vocab_gap

- 问题：ClassCastException IlrStorePolicy$SerializedENamedElement incompatible with EStructuralFeature We keep getting the following error when navigating in Decision Center on Websphere Application Server. java.lang.ClassCastException: ilog.rules.teamserver.web.IlrStorePolicy$SerializedENamedElement incompatible with org.eclipse.emf.ecore.EStructuralFeature Does anyone know how we can avoid this error?
- 改写后：ClassCastException IlrStorePolicy$SerializedENamedElement incompatible with EStructuralFeature We keep getting the following error when navigating in Decision Center on Websphere Application Server. java.lang.ClassCastException: ilog.rules.teamserver.web.IlrStorePolicy$SerializedENamedElement incomp
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21268440｜WebSphere Application Server｜IBM Getting java.io.NotSerializableException when SessionObjectSize counter is enabled - United States
  - java.io.NotSerializableException SessionObjectSize counter PMI enabled disable serializable TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When PMI (Performance Monitoring Infrastructure) is enabled with SessionObjectSize counter enabled, getting NotSerializableException. The SystemOut.log shows somet
- 重排第 1：swg1JR29789｜WebSphere Process Server｜IBM JR29789: AVOID CLASS CAST EXCEPTION BY PROVIDING HEADER INFORMATION EARLIER IN THE START-UP PHASE - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * [6/19/08 10:23:53:160 GMT+02:00] 0000002e ExceptionUtil E CNTR0020E: EJB threw a
- 重排第 2：swg1RS01699｜IBM Operational Decision Manager for z/OS｜IBM RS01699: COMPILE ERRORS ON RULES/DECISION TABLES IN DECISION CENTER (z/OS) - United States
  - FIXES ARE AVAILABLE Operational Decision Manager V8.5.1.2 Fix Pack [http://www-01.ibm.com/support/docview.wss?uid=swg24039235] Operational Decison Manager z/OS 8.7.1.2 Fix Pack [http://www-01.ibm.com/
- 重排第 3：swg1JR33928｜WebSphere Process Server｜IBM JR33928: CLASSCAST EXEPTION BY BOXML SERIALIZER - United States
  - A FIX IS AVAILABLE WebSphere Enterprise Service Bus V6.2.0 Fix Pack 2 (6.2.0.2) [http://www-01.ibm.com/support/docview.wss?uid=swg24024407] SUBSCRIBE You can track all active APARs for this component.

## miss · M-tune-022 · L2 rerank · dense_only, wrong_product, vocab_gap

- 问题：HATS Plugin Download Hi I have RDZ 9.0 and want to install the HATS plugin. I've downloaded from this link: http://www.ibm.com/developerworks/downloads/ws/whats/ HATS 9.0.0.0 but it won't install because RDZ itself is not enough and it sais I need one of the following: IBM Rational Application Developer for WebSphere Software IBM Rational Software Architect for WebSphere Software IBM Rational Developer for i for SOA Construction IBM Rational Business Developer IBM Integration Developer which I d
- 改写后：HATS Plugin Download Hi I have RDZ 9.0 and want to install the HATS plugin. I've downloaded from this link: http://www.ibm.com/developerworks/downloads/ws/whats/ HATS 9.0.0.0 but it won't install because RDZ itself is not enough and it sais I need one of the following: IBM Rational Application Devel
- 答案文档在各阶段名次：{'dense': 2, 'sparse': None, 'fusion': 6, 'rerank': None}
- **答案文档** swg24035040｜Rational Host Access Transformation Services｜IBM Rational Host Access Transformation Services 9.0 - United States
  - service release; modpack; mod pack; upgrade; refresh; refresh pack DOWNLOADABLE FILES ABSTRACT IBM Rational Host Access Transformation Services 9.0 has been made generally available and contains fixes to version 9.0. DOWNLOAD DESCRIPTION Table of Contents Sections Description * What's new This secti
- 重排第 1：swg21444449｜Rational Application Developer for WebSphere Software, SS4JCV, SS5JSH, SS8PJ7, SSJVRK｜IBM Installing Rational Team Concert v2.x into the workbench in version 8.0 - United States
  - RN8.0; SRX; RTC; Rational Team Concert; integration TECHNOTE (FAQ) QUESTION How do I install Rational Team Concert v2.x into my workbench (sometimes referred to as "shell-share") of a version 8.0 prod
- 重排第 2：swg27049457｜Debug Tool for z/OS, IBM Developer for z Systems, Rational Developer for System z, SSVSZX｜IBM Fix list for Debug Tool Plug-ins - United States
  - PRODUCT DOCUMENTATION ABSTRACT This document contains a complete listing of Debug Tool Plug-in fixes with the most recent fix at the top. CONTENT TAB NAVIGATION * Version 14- selected tab, * Support R
- 重排第 3：swg21963975｜Rational Host Access Transformation Services｜IBM Rational Business Developer V9 Passport Advantage e-assembly part numbers for Host Access Transformation Services/Webfacing V9.0 - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) What eAssembly part numbers should be downloaded from Passport Advantage to install WebFacing as a component of Host Access Transformation Services V9, Rat

## miss · M-tune-025 · L2 rerank · dense_only, wrong_product, vocab_gap

- 问题：How to set session time out period for a single user in DASH?
- 改写后：How to set session time out period for a single user in DASH?
- 答案文档在各阶段名次：{'dense': 3, 'sparse': None, 'fusion': 10, 'rerank': 20}
- **答案文档** swg21163875｜Runtimes for Java Technology, WebSphere Application Server｜IBM HTTP Session time-out settings and overwrite precedence rules - United States
  - WebSphere http session management time-out wasrun precedence overwrite TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) It is possible to set the HTTP Session time-out in various places on the IBM® WebSphere® Application Server Administrative Console. It is also possible to set HTTP Session time-out for
- 重排第 1：swg21973714｜Tivoli Components ITM Agent Linux V6｜IBM DASH/JazzSM: Change Session time out - United States
  - DASHL2; DASHCONF; DASH session time out TECHNOTE (FAQ) QUESTION How can I change session time out in IBM Dashboard Application Service Hub (DASH) /JazzSM? ANSWER The session time out can be controlled
- 重排第 2：swg21883735｜Tivoli Components ITM Agent Linux V6｜IBM Setting DASH session timeout at the User or Group level. - United States
  - DASH; DASHL2; DASHL2CONF; Session Timeout; Configuration; Controls; User; Group ; level TECHNOTE (FAQ) QUESTION Is it possible to set DASH session timeout parameters on a group and user level? CAUSE F
- 重排第 3：swg21690658｜Tivoli Components ITM Agent Linux V6｜IBM Setting a big session time-out value in DASH causes session lock-out - United States
  - DASHL2; session; time-out; timeout; cannot login; locked out ; 2147483647; security.xml TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Using a big value (2147483647) for the session timeout setting in D

## miss · M-tune-026 · L2 rerank · dense_only, wrong_product

- 问题：Install path under "Program Files" My path for the OS agent is e:\Program Files\IBM. Is there any issues or underlying problems if I install under "Program Files"? Just want to make sure no issues with a "space" in the install path.
- 改写后：Install path under 'Program Files' My path for the OS agent is e:\Program Files\IBM. Is there any issues or underlying problems if I install under 'Program Files'? Just want to make sure no issues with a 'space' in the install path.
- 答案文档在各阶段名次：{'dense': 8, 'sparse': None, 'fusion': 15, 'rerank': 15}
- **答案文档** swg21961222｜IBM Tivoli Monitoring V6｜IBM Trouble installing ITM on Windows OS - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Getting the below error when you try to install ITM on Window OS "D:\Program Files\IBM\ITM" includes blanks. Due to your system settings the installation path cannot include blanks, please specify location with no spaces. SYMPTOM When you try to install I
- 重排第 1：swg1IZ77662｜Tivoli Netcool/OMNIbus｜IBM IZ77662: TEMA OMNIBUS TEPS SUPPORT INSTALLATION FAILS - DERBY DATABASE - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS REQUIREMENT. ERROR DESCRIPTION * Products: Tivoli Monitoring 6.2.2 FP1 and ITM Agent for Netcool OMNIbus 7.3 OS: Wi
- 重排第 2：swg1IV32710｜IBM Tivoli Monitoring V6｜IBM IV32710: INSTALL FAILS WHEN INSTALLING SYSTEM MONITOR AGENT INTO A DIRECTORY WITH A SPECIAL CHARACTER OR SPACE. - United States
  - A FIX IS AVAILABLE IBM Tivoli Monitoring 6.3.0 Fix Pack 3 (6.3.0-TIV-ITM-FP0003) [http://www-01.ibm.com/support/docview.wss?uid=swg24036775] SUBSCRIBE You can track all active APARs for this component
- 重排第 3：swg1IC55668｜Tivoli Storage Productivity Center for Data｜IBM IC55668: UNATTENDED INSTALL FAILS IF LOCAL ADMINISTRATOR ACCOUNT IS IDENTIFIED TO RUN THE COMMON AGENT SERVICE - United States
  - AIX SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * PMR NO: 66848,999,000 APAR SEV: 3 COMPID: 5608TC300 REL: 3.3.x Symptom Code:

## miss · M-tune-034 · L2 rerank · dense_only, same_product, vocab_gap

- 问题：Does Logout button get disabled in ICM for SSO with Tivoli Access Manager ?
- 改写后：Does the Logout button get disabled in ICM for SSO with Tivoli Access Manager?
- 答案文档在各阶段名次：{'dense': 13, 'sparse': None, 'fusion': 22, 'rerank': None}
- **答案文档** swg27042940｜Case Manager, Content Navigator｜IBM Content Navigator known issue: In a SPNEGO/Kerberos Single sign-on environment, IBM Content Navigator the Log Out option is enabled - United States
  - PRODUCT DOCUMENTATION ABSTRACT In a SPNEGO/Kerberos single sign-on (SSO) environment, your IBM Content Navigator session shows the Log Out option as enabled when you select the drop-down menu on the user name. However, the option should be disabled. CONTENT IBM Content Navigator disables the Log Out
- 重排第 1：swg21599402｜Case Manager｜IBM How to log out from Case Manager Client in SSO environments - United States
  - icm; icm sso; icm sso logout; icm tam sso; icm siteminder sso; icm spnego sso; sso logout; case manager sso; case manager sso logout; siteminder TECHNOTE (FAQ) QUESTION When IBM Case Manager is config
- 重排第 2：swg1PJ42889｜Case Manager｜IBM PJ42889: Incorrect Case Builder logon behavior in SSO using Kerberos SPNE GO on WebLogic application server High Availability environment - United States
  - SUBSCRIBE TO THIS APAR By subscribing, you receive periodic emails alerting you to the status of the APAR, along with a link to the fix after it becomes available. You can track this item individually
- 重排第 3：swg21599382｜Case Manager｜IBM In an SSO with Siteminder environment, the IBM Case Manager logo in the Case Manager Client login page does not display after logout - United States
  - icm; icm sso; icm siteminder; siteminder sso; sso login page; siteminder login page; case client login page; case client icm logo; icm logo missing TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When IB

## miss · M-tune-038 · L1 retrieval: not retrieved · neither, wrong_product, vocab_gap

- 问题：Why do we observe the transaction rollback errors J2CA0024E and DSRA0080E with Oracle 12c and how can we fix it? We are using BPM Advanced v8.5.6 in connection with the Oracle JDBC Driver 12.1.0.1.0. We observe many database transaction rollback exceptions: J2CA0024E: Method rollback, within transaction branch ID <null> of resource pool jdbc/BPEDB, caught com.ibm.ws.exception.WsException: DSRA0080E: An exception was received by the Data Store Adapter. See original exception message: Could not ro
- 改写后：Why do we observe the transaction rollback errors J2CA0024E and DSRA0080E with Oracle 12c and how can we fix it? We are using BPM Advanced v8.5.6 in connection with the Oracle JDBC Driver 12.1.0.1.0. We observe many database transaction rollback exceptions: J2CA0024E: Method rollback, within transac
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21690673｜IBM Business Monitor｜IBM Upgrading default JDBC drivers to Oracle 12c requires the definition of an additional JVM property in IBM Business Monitor - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) In IBM Business Monitor V8.5.5, the Monitor server fails if the default JDBC driver included in the product is upgraded to an Oracle 12c JDBC driver. RESOLVING THE PROBLEM To use Oracle 12c with IBM Business Monitor V8.5.5, a new JVM property must be defi
- 重排第 1：swg1PK26490｜WebSphere Application Server｜IBM PK26490: JDBC EXCEPTION UNDER LOAD NO TRANSACTION AVAIL - United States
  - FIXES ARE AVAILABLE 6.1.0.1: WebSphere Application Server V6.1.0 Fix Pack 1 for HP-UX [http://www-01.ibm.com/support/docview.wss?uid=swg24012899] 6.1.0.1: WebSphere Application Server V6.1.0 Fix Pack 
- 重排第 2：swg1PK51392｜WebSphere Application Server｜IBM PK51392: MESSAGE J2CA0024E OCCURRED WHEN USING UOWMANAGER TO PERFORM SOME WORK UNDER A LOCAL TRANSACTION. - United States
  - FIXES ARE AVAILABLE Java SDK 1.5 SR8 Cumulative Fix for WebSphere Application Server [http://www-01.ibm.com/support/docview.wss?uid=swg24020073] Java SDK 1.5 SR8 Cumulative Fix for WebSphere Applicati
- 重排第 3：swg21330555｜WebSphere Process Server｜IBM J2CA0081E and DSRA0080E received during WebSphere Process Server (WPS) deployment manager startup - United States
  - oracle database; J2CA0081E; DSRA0080E; jdbc driver; ojdbc14.jar; v612rnotes; v62rnotes TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Exception and error messages are returned during WebSphere Process S

## miss · M-tune-041 · L1 retrieval: not retrieved · neither, same_product, vocab_gap

- 问题：Port number error starting 9.0 Launcher I'm attempting to start up v9.0 for the first time with one .msl file on a Windows server and get the following error. I also have v8.4 on this server and it starts fine. I do not have v8.4 running when I attempt to start v9.0. Cannot recognize if the system RecordChangeSystem.msl; has started. Reason: Server is unable to get the status of the system on port number 6,002. I have the port range set to 7000/8000. I've never seen this error before. Any help? 
- 改写后：Port number error starting 9.0 Launcher I'm attempting to start up v9.0 for the first time with one .msl file on a Windows server and get the following error. I also have v8.4 on this server and it starts fine. I do not have v8.4 running when I attempt to start v9.0. Cannot recognize if the system R
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21986219｜Transformation Extender｜IBM Launcher failure when 'On Success' is set to Delete and 'On Failure' is set to Commit - United States
  - WTX ITX Launcher On Success Delete On Failure Commit TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) IBM Transformation Extender (ITX) Launcher failure when 'On Success' is set to Delete and 'On Failure' is set to Commit. SYMPTOM Launcher fails to load a watch when On Success = Delete and On Failure = 
- 重排第 1：swg1PK90066｜Transformation Extender｜IBM PK90066: LAUNCHER STARTUP FAILURE . UNABLE TO GET SYSTEM STATUS . SOCKET ERROR : ERROR 221 (MSTATSOC.C:2036) - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * Customer is running WTX8.2.0.4 with Interim Fix Pack 2 on an HP-UX PA-RISC serve
- 重排第 2：swg21976821｜Transformation Extender｜IBM The Transformation Extender Management Console is not able to communicate with the Launcher using IPv6 communication - United States
  - LINUX_GETADDRINFO socket 97 221 unable management console status TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) The Transformation Extender Management Console is not able to communicate with the Launche
- 重排第 3：swg1PK88357｜Transformation Extender｜IBM PK88357: EVENT SERVER/LAUNCHER IS NOT USING AVAILABLE PORTS RESULTING IN PORT IN USE ERRORS. - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * If any of the ports specified in the Connection Port Range of Launcher Administr

## miss · M-tune-045 · L2 rerank · dense_only, same_product, vocab_gap

- 问题：Optim license We bought Optim 11.3, Test data management and data masking module.... I wonder how to get a Optim license?
- 改写后：We bought Optim 11.3, Test data management and data masking module.... I wonder how to get an Optim license?
- 答案文档在各阶段名次：{'dense': 3, 'sparse': None, 'fusion': 9, 'rerank': None}
- **答案文档** swg21973794｜Optim｜IBM Optim, Optim Connect, ODM, and Optim zOS licensing - United States
  - license key; password; fix pack; enable; license file; Open Data Manager; ODM; entitle TECHNOTE (FAQ) QUESTION Are license keys still required for Optim Distributed, Optim Connect, ODM, and Optim zOS products? ANSWER See the attached document for a full explanation of which license keys might be req
- 重排第 1：swg27041901｜Optim｜IBM Detailed System Requirements for IBM InfoSphere Optim Test Data Management Solution for Oracle E-Business Suite with Data Masking Option v11.3 - United States
  - PRODUCT DOCUMENTATION ABSTRACT This document summarizes the hardware, platforms, and software supported by the IBM® InfoSphere® Optim™ Test Data Management Solution for Oracle E-Business Suite with Da
- 重排第 2：swg27024806｜Optim｜IBM Detailed System Requirements for v9.1 of IBM InfoSphere Optim Test Data Management Solution for Oracle E-Business Suite with Data Masking Option - United States
  - PRODUCT DOCUMENTATION ABSTRACT This document summarizes the hardware, platforms, and software supported by v9.1 of the IBM® InfoSphere® Optim™ Test Data Management Solution for Oracle E-Business Suite
- 重排第 3：swg27041962｜Optim｜IBM Detailed System Requirements for the IBM InfoSphere Optim Test Data Management Solution for PeopleSoft Enterprise with Data Masking Option v11.3 - United States
  - DETAILED SYSTEM REQUIREMENTS ABSTRACT This document summarizes the hardware, platforms, and software supported by version 11.3 of the IBM® InfoSphere® Optim™ Test Data Management Solution for PeopleSo

## miss · M-tune-049 · L1 retrieval: not retrieved · neither, same_product, vocab_gap

- 问题：How do I transfer my SPSS 24 license key to a new computer? I need to transfer my SPSS 24 license key to a new computer. I was able to download IBM® SPSS® Statistics Standard GradPack 24 for Windows (12-Mo Rental) onto the new computer, but every time I put in the activation code, I am met with this error message: Authorization failed.: You are not allowed to generate any more new licenses. End Of Transaction. No additional authorizations are permitted on this code. What should I do? This dW Ans
- 改写后：How do I transfer my SPSS 24 license key to a new computer? I need to transfer my SPSS 24 license key to a new computer. I was able to download IBM® SPSS® Statistics Standard GradPack 24 for Windows (12-Mo Rental) onto the new computer, but every time I put in the activation code, I am met with this
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21592093｜SPSS Amos, SPSS Modeler, SPSS Statistics, SPSS Text Analytics for Surveys｜IBM SPSS Student Version and Graduate Pack Resources - United States
  - SPSS Support Acquisition Statistics Stats Grad Pack Student TECHNOTE (FAQ) QUESTION Where do I get support for IBM SPSS Student Version or Graduate Pack software? ANSWER Step 1: For installation & licensing issues on Student version and Graduate pack, contact your vendor. * Hearne [http://www.hearne
- 重排第 1：swg21985888｜SPSS Modeler, SPSS Statistics｜IBM How do I transfer my IBM SPSS product/software license from one machine to another? - United States
  - TECHNOTE (FAQ) QUESTION How do I transfer my IBM SPSS product/software license from one machine to another? ANSWER It is not possible, nor required, to transfer a license from an existing product inst
- 重排第 2：swg21994470｜SPSS Modeler, SPSS SamplePower, SPSS Statistics, SPSS Text Analytics for Surveys, SS69XP, SS6A8C｜IBM Where can I get information about acquiring IBM SPSS software and licensing IBM SPSS products? - United States
  - TECHNOTE (FAQ) QUESTION I have questions or a problem with acquiring IBM SPSS software and licensing IBM SPSS products? Where can I go for more information? ANSWER Where and how do I download and star
- 重排第 3：swg21486099｜SPSS Statistics｜IBM Why am I receiving a message with 'Error Code 201' and ' License generation failed'? - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When running the License Authorization Wizard, I receive the following warning/error message: Error from Generator: Description: License generation failed.

## miss · M-tune-056 · L1 retrieval: not retrieved · neither, wrong_product, near_duplicate, vocab_gap

- 问题：Help with Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with WSRR (CVE-2017-1741) I need to understand details regarding Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with IBM WebSphere Service Registry and Repository (CVE-2017-1741). We are running WAS traditional V9.0.0.0. What is the recommended fix?
- 改写后：Help with Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with WSRR (CVE-2017-1741) I need to understand details regarding Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with IBM WebSphere Service Registry and Repositor
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg22012345｜WebSphere Application Server｜IBM Security Bulletin: Potential Privilege Escalation in WebSphere Application Server Admin Console (CVE-2017-1731) - United States
  - SECURITY BULLETIN SUMMARY There is a potential privilege escalation in WebSphere Application Server Admin Console. VULNERABILITY DETAILS CVEID: CVE-2017-1731 [http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-1731] DESCRIPTION: IBM WebSphere Application Server could provide weaker than expected
- 重排第 1：swg22014520｜WebSphere Service Registry and Repository｜IBM Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with IBM WebSphere Service Registry and Repository (CVE-2017-1741) - United States
  - SECURITY BULLETIN SUMMARY IBM WebSphere Application Server is shipped as a component of IBM WebSphere Service Registry and Repository. Information about a security vulnerability affecting IBM WebSpher
- 重排第 2：swg22004956｜WebSphere Service Registry and Repository｜IBM Security Bulletin: Vulnerability identified in IBM® Java SDK affects WebSphere Service Registry and Repository and WebSphere Service Registry and Repository Studio (CVE-2017-3511). - United States
  - SECURITY BULLETIN SUMMARY Vulnerability in IBM® SDK Java™ Technology Edition, Version 6 used by WebSphere Service Registry and Repository and WebSphere Service Registry and Repository Studio. This iss
- 重排第 3：swg21988198｜WebSphere Service Registry and Repository｜IBM Security Bulletin: Vulnerabilities in Apache Struts and Apache Commons FileUpload affects IBM WebSphere Service Registry and Repository (CVE-2016-1181, CVE-2016-1182, CVE-2016-3092) - United States
  - SECURITY BULLETIN SUMMARY Vulnerability in Apache Struts and Apache Commons FileUpload affects IBM WebSphere Service Registry and Repository (CVE-2016-1181, CVE-2016-1182, CVE-2016-3092) VULNERABILITY

## miss · M-tune-058 · L1 retrieval: fusion cut · dense_only, wrong_product, vocab_gap

- 问题：How to configure the Data Power Agent to communicate on TLSv1.2 ? APM agent for data power is not able to communicate with data power server when SSL is enabled. Since we are connecting to TLS version 1, where data power server supports only TLS 1.2.
- 改写后：How to configure the Data Power Agent to communicate on TLSv1.2 ? APM agent for data power is not able to communicate with data power server when SSL is enabled. Since we are connecting to TLS version 1, where data power server supports only TLS 1.2.
- 答案文档在各阶段名次：{'dense': 26, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg24041563｜Tivoli Composite Application Manager for Applications｜IBM ITCAM Agent for WebSphere DataPower Applications: 7.1.0-TIV-ITM_WDP-FP0003 - United States
  - DataPower; BN; KBN DOWNLOADABLE FILES ABSTRACT This fix resolves the enhancements listed in the "Problems Fixed" section below. DOWNLOAD DESCRIPTION Copyright International Business Machines Corporation 2016. All rights reserved. Component: IBM(R) Tivoli(R) Composite Application Manager Agent for We
- 重排第 1：swg1IJ01104｜Tivoli Monitoring for Virtual Environments｜IBM IJ01104: VI AGENT 07.20.04.01 NOT CONNECTING VCENTER USING ONLY TLS V1.2 - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS DOCUMENTATION ERROR. ERROR DESCRIPTION * If the target vCenter is configured to accept only TLS v1.2, using the def
- 重排第 2：swg22017052｜IBM Workload Scheduler｜IBM How Enable tls 1.2 dynamic agent REST API plugin - United States
  - TECHNOTE (TROUBLESHOOTING) THIS DOCUMENT APPLIES ONLY TO THE FOLLOWING LANGUAGE VERSION(S): English PROBLEM(ABSTRACT) REST API plugin not able to connect to server configured with tls 1.2 enabled SYMP
- 重排第 3：swg22000057｜IBM Security QRadar SIEM｜IBM WinCollect: How to Enable/Disable TLS Communication Options for QRadar - United States
  - TLS; scan result; TLS vulnerabilities; TLSv1.0; TLS v1; TLS 1.0; TLS 1.1; how to enable TLS; how to disable TLS; WinCollect TLS; WinCollect TLS communication TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRAC

## miss · M-tune-066 · L2 rerank · wrong_product, vocab_gap

- 问题：Will Datacap support Windows 10, if so, which version is fully supported? We want to if Datacap support windows 10, if so, which version supports it. Please provide us official statement for the compatibility.
- 改写后：Will Datacap support Windows 10, if so, which version is fully supported? We want to know if Datacap supports Windows 10, if so, which version supports it. Please provide us with the official statement for the compatibility.
- 答案文档在各阶段名次：{'dense': 4, 'sparse': 28, 'fusion': 15, 'rerank': None}
- **答案文档** swg27047895｜Datacap｜IBM Datacap 9.0.1 FP1 - Readme doc - United States
  - PRODUCT README ABSTRACT IBM Datacap 9.0.1 FP1 - Readme doc CONTENT About IBM Datacap 9.0.1 Feature Pack 1 Review this document for installation instructions and other important information before you install IBM® Datacap 9.0.1 Feature Pack 1, which cumulatively contains all feature pack updates sinc
- 重排第 1：swg1HD87484｜CATIA V5｜IBM HD87484: STCAI / UPDATE  DOCUMENTATION REGARDING THE SUPPORT OF DLNAME   . - United States
  - AIX SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PERMANENT RESTRICTION. ERROR DESCRIPTION * VAR would like to use DLNAME for Large amouts of reference data whic
- 重排第 2：swg27020397｜Datacap｜IBM System Requirements: Hardware and Software Requirements for IBM Datacap Taskmaster Capture Version 8.0 - United States
  - PRODUCT DOCUMENTATION ABSTRACT This page describes the minimum system requirements to operate IBM Datacap Taskmaster Capture Version 8.0. Any configuration that exceeds these minimum requirements will
- 重排第 3：swg21584043｜Clarity 7｜IBM Clarity Server - Internet Explorer compatibility - United States
  - IE9; browser; compatible; IE10 TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When using different IBM Clarity Server features in an Internet Explorer version that is not fully compatible with your IBM 

## miss · M-tune-070 · L2 rerank · dense_only, wrong_product, vocab_gap

- 问题：Why can't I connect to HTTPS server using Installation Manager 1.7.2? When using IBM Installation Manager 1.7.2 to connect to a HTTPS server, I get the following message: The following repositories are not connected: https://www.ibm.com/software/repositorymanager/service/com.ibm. websphere.ND.v85/8.5.5.2. When I try to hit the URL, I get a 404 error.
- 改写后：Why can't I connect to HTTPS server using Installation Manager 1.7.2? When using IBM Installation Manager 1.7.2 to connect to a HTTPS server, I get the following message: The following repositories are not connected: https://www.ibm.com/software/repositorymanager/service/com.ibm. websphere.ND.v85/8.
- 答案文档在各阶段名次：{'dense': 2, 'sparse': None, 'fusion': 9, 'rerank': None}
- **答案文档** swg21688071｜IBM Installation Manager｜IBM Installation Manager 1.7.3.1 or older cannot connect to HTTPS servers that have SSL security protocol disabled - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When using IBM Installation Manager to connect to a HTTPS server, if the server has SSL disabled, versions of IBM Installation Manager older than 1.8 will not be able to connect to it RESOLVING THE PROBLEM IBM Installation Manager has added support for th
- 重排第 1：swg21979394｜IBM Business Process Manager Advanced, IBM Business Process Manager Standard｜IBM Upgrading IBM Process Federation Server Version 8.5.6.0 to Version 8.5.7.0 or Version 8.5.7.0 to Version 8.5.7 CF2016.09 fails in IBM Business Process Manager - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When you try to upgrade IBM Process Federation Server Version 8.5.6.0 to IBM Process Federation Server Version 8.5.7.0 interactively, using IBM Installatio
- 重排第 2：swg21685035｜WebSphere Application Server｜IBM NullPointerException error received when installing WebSphere Application Server Liberty profile - United States
  - WASV855RNotes TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) If you are installing WebSphere Application Server Liberty profile with the -imcl command, you might encounter problems. If you are connectin
- 重排第 3：swg1PM21560｜WebSphere Application Server V7 Feature Pack for Communications Enabled Applications General｜IBM PM21560: WAS IMPORT OFFERING.SERVICE.REPOSITORIES PROPERTY NOT DEFINED; INSTALLATION MANAGER CANNOT CONNECT TO WEB SERVICE REPOSITORY - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * WebSphere Application Server V7.0 uses the IBM Installation Manager to install a

## miss · M-tune-076 · L2 rerank · dense_only, same_product, vocab_gap

- 问题：Does JazzSM 1.1.2.1 support HTTP access?
- 改写后：Does JazzSM 1.1.2.1 support HTTP access?
- 答案文档在各阶段名次：{'dense': 6, 'sparse': None, 'fusion': 14, 'rerank': 12}
- **答案文档** swg21974566｜Tivoli Components ITM Agent Linux V6｜IBM Configuring access for HTTP and HTTPS in Jazz for Service Management - United States
  - jazzsm11relnotes; jazzsm1101relnotes; jazzsm1102; jazzsm1103relnotes; relnotes; jazzsm1110relnotes; jazzsm1120relnotes; jazzsm1121relnotes; HTTP; HTTPS TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) By default, the Jazz™ for Service Management application server requires HTTPS access. You can set up t
- 重排第 1：swg21971363｜Tivoli Components ITM Agent Linux V6｜IBM HTTP access does not work in DASH 3.1.0.3 (JazzSM 1.1.0.3) - United States
  - DASHL2; HTTP access; web.xml; transport; confidential; 3.1.0.3; dashboard application services hub; jazzsm TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) The configuration of HTTP access does not work i
- 重排第 2：swg21696081｜Tivoli Components ITM Agent Linux V6｜IBM Jazz TCR requires web access in a locked down environment - United States
  - Jazz; Port; Internet; web; access; WebSphere; update TECHNOTE (FAQ) QUESTION During the installation of 1.1.1.-TIV-JazzSM-multi available from this link http://www-01.ibm.com/support/docview.wss?uid=s
- 重排第 3：swg21963919｜Tivoli Components ITM Agent Linux V6｜IBM Accessing one DASH/JazzSM server from an other JazzSM server - United States
  - DASHL2; DASHL2CONF; integrating; jazzsm ; DASH ; SSO; single sign on TECHNOTE (FAQ) QUESTION How can I open a page from one DASH/JazzSM server on an other DASH server? CAUSE Suppose you have a Server 

## miss · M-tune-085 · L2 rerank · same_product, vocab_gap

- 问题：Installation of Portal 7.0 CF fails with version mismatch Installation of Portal 7.0 CF fails with message, "Profile version is not the same as portal binary version before updating portal binary."
- 改写后：Installation of Portal 7.0 CF fails with version mismatch Installation of Portal 7.0 CF fails with message, "Profile version is not the same as portal binary version before updating portal binary."
- 答案文档在各阶段名次：{'dense': 14, 'sparse': 12, 'fusion': 8, 'rerank': 13}
- **答案文档** swg27023910｜WebSphere Portal｜IBM WebSphere Portal 7.0.0.2  Combined Cumulative Fix Readme - stand-alone - United States
  - WPWCMCF WPWCMCF02 7002CCF PRODUCT README ABSTRACT IBM WebSphere Portal 7.0.0.2 Combined Cumulative Fix stand-alone installation instructions for all editions, including WebSphere Portal Express. CONTENT 7.0.0.2: Readme for IBM WebSphere Portal 7.0.0.2 Combined Cumulative fix - stand-alone Table of C
- 重排第 1：swg21677833｜WebSphere Portal｜IBM Installation of Portal CF fails with version mismatch - United States
  - upgrade; cf; version mismatch TECHNOTE (TROUBLESHOOTING) PROBLEM Installation of Portal CF fails with message, "Profile version is not the same as portal binary version before updating portal binary."
- 重排第 2：swg21701048｜WebSphere Portal｜IBM Receive the message, "ERROR: Product maintenance level does not match profile" when running the Portal Health Check utility before applying CF15 - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM While preparing to install CF15 on your existing Portal 8.0.0.1 CF09 you run the Portal Health Check utility and receive the following message: >>> Test: Profile mai
- 重排第 3：swg21685680｜WebSphere Portal｜IBM Base version of Portal 8.5 install fails noting a cumulative fix conflict during silent install - United States
  - base install fails; CF conflict TECHNOTE (TROUBLESHOOTING) PROBLEM Attempts to install the Base version of Portal 8.5 using a response file fails as it notes that the cumulative fix fails as it requir

## miss · M-tune-087 · L2 rerank · dense_only, wrong_product, vocab_gap

- 问题：completeness report causes StackOverflowError in Decision Center When running the completeness report in Decision Center we sometimes get a StackOverflowError such as: ... Caused by: java.lang.StackOverflowError at ilog.rules.validation.solver.IlcIntScalProd.extract(IlcIntScalProd.java:89) at ilog.rules.validation.solver.IlcIntExpr.getPIntExp(IlcIntExpr.java:156) ...
- 改写后：completeness report causes StackOverflowError in Decision Center When running the completeness report in Decision Center we sometimes get a StackOverflowError such as: ... Caused by: java.lang.StackOverflowError at ilog.rules.validation.solver.IlcIntScalProd.extract(IlcIntScalProd.java:89) at ilog.r
- 答案文档在各阶段名次：{'dense': 2, 'sparse': None, 'fusion': 7, 'rerank': 20}
- **答案文档** swg21162896｜Runtimes for Java Technology, WebSphere Application Server｜IBM Diagnosing a java.lang.StackOverflowError - United States
  - StackOverflow; overflowing; recursion; recursively; jit; JustInTime; Hot; Spot; WebSphere; Just-In-Time TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Stack Overflow exceptions can occur when a thread stack continues to grow in size until reaching the maximum limit. SYMPTOM A stack overflow can result
- 重排第 1：swg21499459｜IBM Operational Decision Manager, SS6MUU｜IBM StackOverflowError when checking a project or building a ruleset - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Building or checking the consistency of large rule projects in Rule Team Server (RTS) or Decision Center can generate a StackOverflowError. SYMPTOM The fol
- 重排第 2：swg21678239｜IBM Operational Decision Manager｜IBM "NoClassDefFoundError: ilog/rules/vocabulary/model/util/IlrResourceLoader" error when running Decision Validation Services (DVS) tests - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When running a Decision Validation Services (DVS) test, the test fails with the following error: java.lang.NoClassDefFoundError: ilog/rules/vocabulary/mode
- 重排第 3：swg1RS01990｜IBM Operational Decision Manager for z/OS｜IBM RS01990: UNABLE TO VIEW OR EDIT RULE AFTER SAVING UNPARSEABLE DATE - United States
  - FIXES ARE AVAILABLE Operational Decision Manager V8.7.1.1 Fix Pack [http://www-01.ibm.com/support/docview.wss?uid=swg24040633] Operational Decision Manager V8.6.0.3 Fix Pack [http://www-01.ibm.com/sup

## miss · M-tune-088 · L2 rerank · same_product, vocab_gap

- 问题：Why is RPT script for secure application failing during RRT agent playback with URL Unavailable ? In the ITCAM for Transactions, Robotic Response Time agent (t6) - the Rational Performance Tester (RPT) scripts playback is failing for specific secure applications (ones that use https). The scripts which invoke the http URLs work fine. The TEP workspace Robotic Response Time -> Playback Status->Robotic Script Verification Point Failures shows following Event Types for the RPT Script when it fails:
- 改写后：Why is RPT script for secure application failing during RRT agent playback with URL Unavailable ? In the ITCAM for Transactions, Robotic Response Time agent (t6) - the Rational Performance Tester (RPT) scripts playback is failing for specific secure applications (ones that use https). The scripts wh
- 答案文档在各阶段名次：{'dense': 12, 'sparse': 24, 'fusion': 8, 'rerank': 19}
- **答案文档** swg21960133｜Tivoli Composite Application Manager for Transactions｜IBM Does the RRT agent support TLS 1.1/1.2 and 256-bit ciphers? - United States
  - 256-bit ciphers; Strong Encryption; TLS 1.1; TLS 1.2; SSL; Generic Failure; Cannot support; RPT; RRT; T6; 71RRT-RPTPLAN; 71RRT-RPTINS; 71RRT-RPTCONF; 71RRT-RPTPLAY; 71RRT-RPTWV; 71RRT-RPTTS TECHNOTE (FAQ) QUESTION What do you need to do to configure the Robotic Response Time (RRT) agent to support T
- 重排第 1：swg21498401｜Tivoli Composite Application Manager for Transactions｜IBM ITCAM4Tx : robotic RRT T6 integration with RPT and ARM - United States
  - 71RRT-RPTPLAY TECHNOTE (FAQ) QUESTION Describe how the Robotic Response Time "T6" agent integrates with Rational Performance Tester (RPT) in order to playback RPT scripts, and produce response time an
- 重排第 2：swg21660008｜Tivoli Composite Application Manager for Transactions｜IBM ITCAM4Tx : Robotic RPT script playback fails on t6 agent while using proxy service - United States
  - 71RRT-RPTPLAY; 71RRT-RPTWV; 71RRT-RPTTS; 71RRT-CONF; 71RRT-PLAY; 71RRT-TS TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Robotic Response Time agent (t6) can't play back successfully a RPT test script, 
- 重排第 3：swg21580748｜Tivoli Composite Application Manager for Transactions｜IBM ITCAMfT - RRT (T6) RPT Kerberos HTTP test script playback - high response time - United States
  - 71RRT-RPTREC; 71RRT-RPTPLAY; 71RRT-RPTRPTG; 71RRT-RPTWV; 71RRT-RPTTS; 71RRT-RPTG; 71RRT-WV; 71RRT-TS; rpt; rational performance tester; kerberos TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) RPT V8.2 H

## miss · M-tune-090 · L1 retrieval: fusion cut · dense_only, same_product, vocab_gap

- 问题：Can not create a portal wcm syndicator-subscriber pair. The "Subscribe Now" window pops up but is blank or corrupted. Why? Can not create a portal wcm syndicator-subscriber pair. The "Subscribe Now" window pops up but is blank or corrupted.
- 改写后：Can not create a portal wcm syndicator-subscriber pair. The 'Subscribe Now' window pops up but is blank or corrupted. Why?
- 答案文档在各阶段名次：{'dense': 25, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21445801｜IBM Web Content Manager, WebSphere Portal｜IBM WCM page and authoring portlet may not display after migration - United States
  - WPv7000eGA; migrating; migrate; migration; V7.0; v7; WCM; out-of-box page; out of the box; page; authoring portlet; may not reach; cannot reach; cannot access; no access; exceptions; IWKAP0009E; Servlet not enabled TECHNOTE (TROUBLESHOOTING) PROBLEM After migrating to IBM WebSphere Portal V7.0, you 
- 重排第 1：swg1PI11138｜IBM Web Content Manager｜IBM PI11138: Add optional subscriberURL to allow specific URL in task RUN-WCM-ADMIN-TASK-SUBSCRIBE-NOW - United States
  - FIXES ARE AVAILABLE Fixes integrated in WebSphere Portal 8.0.0.1 Combined Cumulative Fixes [http://www-01.ibm.com/support/docview.wss?uid=swg24034497] Fixes integrated in WebSphere Portal 8.5.0.0 Comb
- 重排第 2：swg21648259｜IBM Web Content Manager｜IBM New syndication pair created on 8001 CF06 or CF07 fails to syndicate if the subscriber is a virtual portal with a different hostname. - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM New syndication pair created on 8001 CF06 or CF07 fails to syndicate if the subscriber is a virtual portal with a different hostname. SYMPTOM Syndication does not wo
- 重排第 3：swg21587102｜IBM Web Content Manager, SS6JVW｜IBM Unable to create syndicator-subscriber pair while setting up syndication, with IWKWC0016E error. - United States
  - credential vault; setup syndication; IWKWC0016E TECHNOTE (TROUBLESHOOTING) PROBLEM Unable to create syndicator-subscriber pair, and getting following error:- "IWKWC0016E: The remote service can not be

## miss · M-tune-099 · L2 rerank · sparse_only, wrong_product, vocab_gap

- 问题：The configuration task database-transfer failed with DB2 SQL Error: SQLCODE=-1585, SQLSTATE=54048 While attempting to run the database-transfer task the following error is logged to the ConfigTrace.log: action-process-constraints: Fri Oct 10 13:20:34 CDT 2014 Target started: action-process-constraints [java] Executing java with empty input string [java] [10/10/14 13:20:35.877 CDT] Attempting to create a new Instance of com.ibm.db2.jcc.DB2Driver [java] [10/10/14 13:20:36.016 CDT] Instance of com.
- 改写后：The configuration task database-transfer failed with DB2 SQL Error: SQLCODE=-1585, SQLSTATE=54048 While attempting to run the database-transfer task the following error is logged to the ConfigTrace.log: action-process-constraints: Fri Oct 10 13:20:34 CDT 2014 Target started: action-process-constrain
- 答案文档在各阶段名次：{'dense': None, 'sparse': 6, 'fusion': 11, 'rerank': 12}
- **答案文档** swg21529563｜Sterling B2B Integrator｜IBM DB2 SQL error from Sterling B2B Integrator: SQLCODE: -1585, SQLSTATE: 54048 - United States
  - STERLINGPRI TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) This DB2 SQL error occurs with Sterling B2B Integrator: SQLCODE: -1585, SQLSTATE: 54048 SYMPTOM com.sterlingcommerce.woodstock.profile.ProfileFinderException: listAllByEntityName: Finder Exception occurred: SQLState: 54048 Message: DB2 SQL err
- 重排第 1：swg21686939｜WebSphere Portal｜IBM The configuration task database-transfer failed with DB2 SQL Error: SQLCODE=-1585, SQLSTATE=54048 - United States
  - database-transfer; DB2; SQLCODE=-1585; SQLSTATE=54048 TECHNOTE (TROUBLESHOOTING) PROBLEM While attempting to run the database-transfer task the customer gets the following error: action-process-constr
- 重排第 2：swg21962624｜WebSphere Portal｜IBM While running the ConfigWizard to transfer the Portal databases to DB2 the process fails and the following errors are in the ConfigTrace.log, SQLCODE=-286, SQLSTATE=42727 - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) While running the ConfigWizard to transfer the Portal databases to DB2 the process fails and the following errors are in the ConfigTrace.log, SQLCODE=-286,
- 重排第 3：swg21517964｜Sterling B2B Integrator｜IBM Unable to Create AS2 Organization via AS2 Wizard with DB2 Database - UI Log Shows Profile Finder Exception - United States
  - Database Performance; STERLINGFAQ TECHNOTE (FAQ) QUESTION Unable to Create AS2 Organization via AS2 Wizard with DB2 Database - UI Log Shows Profile Finder Exception ANSWER Able to create an Organizati

## miss · M-tune-101 · L1 retrieval: not retrieved · neither, wrong_product, vocab_gap

- 问题：Portal v8.5 install fails with INSTCONFFAILED - No Portral logs are written
- 改写后：Portal v8.5 install fails with INSTCONFFAILED - No Portal logs are written
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg1PI37248｜WebSphere Application Server｜IBM PI37248: A PROPERTY FILE BASED CONFIGURATION (PFBC) FILE MIGHT FAIL TO AP PLY. - United States
  - FIXES ARE AVAILABLE 8.5.5.6: WebSphere Application Server V8.5.5 Fix Pack 6 [http://www-01.ibm.com/support/docview.wss?uid=swg24040035] 8.0.0.11: WebSphere Application Server V8.0 Fix Pack 11 [http://www-01.ibm.com/support/docview.wss?uid=swg24040425] 8.5.5.7: WebSphere Application Server V8.5.5 Fix
- 重排第 1：swg21619511｜Tivoli Components ITM Agent Linux V6｜IBM TIP upgrade is failing with error  INSTCONFFAILED - United States
  - TIPL2INST; upgrade; install fails ; eWAS files already exist; INSTCONFFAILED TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) An attempt to upgrade the Tivoli Integrated Portal is failing with errors that
- 重排第 2：swg21594974｜WebSphere Enterprise Service Bus｜IBM The profile creation process fails with a "INSTCONFFAILED: The profile could not be created" error for WebSphere Enterprise Service Bus (WESB) - United States
  - INSTCONFFAILED profileRegistry.xml_LOCK FileLockerException TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When you attempt to create a profile for WebSphere Enterprise Service, you might encounter a " 
- 重排第 3：swg21613065｜WebSphere Portal｜IBM Portal 8 silent install fails with CRIMA1076E on Windows if path uses standard " \ " delimiter - United States
  - Portal 8 silent install fail Windows / \ CRIMA1076E manageprofiles TECHNOTE (TROUBLESHOOTING) PROBLEM After manually editing a Portal 8 response file, the installation may fail on Windows if the path 

## miss · M-tune-105 · L2 rerank · same_product, vocab_gap

- 问题：ICO's Roadmap of supporting next OpenStack versions Hello, ICO 2.5.0.2 is compatible with OpenStack kilo, is there a plan making it work with OpenStack Liberty/Mitika ? Would you share any information or link about the roadmap, please? Thanks in advance.
- 改写后：ICO's Roadmap of supporting next OpenStack versions Hello, ICO 2.5.0.2 is compatible with OpenStack kilo, is there a plan making it work with OpenStack Liberty/Mitaka ? Would you share any information or link about the roadmap, please? Thanks in advance.
- 答案文档在各阶段名次：{'dense': 9, 'sparse': 30, 'fusion': 4, 'rerank': 16}
- **答案文档** swg2C1000132｜IBM Cloud Orchestrator｜IBM Cloud Orchestrator (ICO) continues to be a strategic solution for IBM - United States
  - FLASH (ALERT) ABSTRACT Cloud Orchestrator (ICO) continues to be a strategic solution for IBM CONTENT IBM Cloud Orchestrator continues to be a strategic solution for IBM in Hybrid Cloud management and will continue to be actively developed. Future IBM Cloud Orchestrator releases will enable managemen
- 重排第 1：swg1ZZ00704｜IBM Cloud Orchestrator｜IBM ZZ00704: ICO WITH BRING YOUR OWN OPENSTACK (BYOOS) REQUIRES 'DEFAULT' DOMAIN TO BE CREATED IN OPENSTACK PRIOR TO ICO INSTALL. - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS DOCUMENTATION ERROR. ERROR DESCRIPTION * ICO with BYOOS installation fail pre-checker indicating the problem with t
- 重排第 2：swg1ZZ00648｜IBM Cloud Orchestrator｜IBM ZZ00648: INSTALLING IBM CLOUD ORCHESTRATOR (ICO) WITH BRING YOUR OWN OPENSTACK, ICO EXPECTS SPECIFIC NAMING FOR OPENSTACK SERVICES - United States
  - SUBSCRIBE TO THIS APAR By subscribing, you receive periodic emails alerting you to the status of the APAR, along with a link to the fix after it becomes available. You can track this item individually
- 重排第 3：swg1ZZ00465｜IBM Cloud Orchestrator｜IBM ZZ00465: ICO 2.4 UNABLE TO OPEN ICO ADMIN UI, GETTING ERROR 'OPERATIONALERROR AT / NO EXCEPTION MESSAGE SUPPLIED' - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS DOCUMENTATION ERROR. ERROR DESCRIPTION * PROBLEM DEFINITION: Upon building ICO 2.4 environment, unable to open the 

## miss · M-tune-106 · L1 retrieval: not retrieved · neither, wrong_product, vocab_gap

- 问题：Is Internet Explorer 11 supported by Lombardi 7.2.XX We are using Lombardi 7.2.0.5 version. We are planning to upgrade Internet Explorer to IE 11 version. Is IE 11 supported? Are there any known issues?
- 改写后：Is Internet Explorer 11 supported by Lombardi 7.2.XX We are using Lombardi 7.2.0.5 version. We are planning to upgrade Internet Explorer to IE 11 version. Is IE 11 supported? Are there any known issues?
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg27023007｜IBM Business Process Manager Standard｜IBM Business Process Manager Standard detailed system requirements - United States
  - DSREntry; SystemRequirementsDocument; prereq; coreq; installation prerequisites; DSRdoc DETAILED SYSTEM REQUIREMENTS ABSTRACT This document provides access to the detailed system requirements information on the supported releases of IBM Business Process Manager Standard. CONTENT The detailed system 
- 重排第 1：swg21675676｜FileNet Business Process Framework｜IBM Does Business Process Framework (BPF) 4.1 support Microsoft Internet Explorer (IE) 11.0? - United States
  - IE; Microsoft; version; support; plan TECHNOTE (FAQ) QUESTION The customer plans to upgrade Microsoft Internet Explorer to vesion 11 and wants to know if BPF 4.1 supports it. Does Business Process Fra
- 重排第 2：swg21688764｜Case Manager｜IBM Known Limitation: IBM Case Manager 5.2.x and Microsoft Internet Explorer versions prior to 11.0.10 - United States
  - icm 521; if002; 5210-if2 TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) The Case Manager v5.2.x minimum required (minor) version of Internet Explorer 11 is 11.0.10 (with IE-11 update KB2962872). SYMPTOM
- 重排第 3：swg21677519｜Tivoli Netcool/OMNIbus｜IBM WebGUI Support for IE 11 in Enterprise Mode - United States
  - ie; internet explorer; enterprise mode; webgui; tip TECHNOTE (FAQ) QUESTION Will the WebGUI work with the new operating mode in Internet Explorer 11 called Enterprise Mode? ANSWER Internet Explorer En

## miss · M-tune-111 · L2 rerank · dense_only, same_product, vocab_gap

- 问题：1040ez 9.0 Application Hi I have downloaded sample Datacap 9 applications (1040ez, Express, Survey) using below link and copied in my local system C:\Datacap and added reference in Datacap.xml file. IBM Datacap 9.0 and IBM Datacap 9.0.1 DDK sample applications But i'm unable to login Datacap Studio & Tmweb.net . (I tried to with re generating encryption keys but no luck). Can anyone let me know the reason, anything I missed in configuration ? My Datacap version in Local Machine IBM Datacap 9.0.0
- 改写后：1040ez 9.0 Application Hi I have downloaded sample Datacap 9 applications (1040ez, Express, Survey) using below link and copied in my local system C:\Datacap and added reference in Datacap.xml file. IBM Datacap 9.0 and IBM Datacap 9.0.1 DDK sample applications But i'm unable to login Datacap Studio 
- 答案文档在各阶段名次：{'dense': 5, 'sparse': None, 'fusion': 11, 'rerank': 10}
- **答案文档** swg21968549｜Datacap｜IBM Couldn't validate parameters error logging in with IBM Datacap - United States
  - login connect couldnt validate parameters TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Users are unable to log in with any client to any application. The Taskmaster Server (tms) log shows: Connect couldn't validate parameters SYMPTOM This is most commonly seen on a new installed Taskmaster Server. U
- 重排第 1：swg21675631｜Datacap｜IBM TMWeb cannot connect to the Admin DB in IBM Datacap Taskmaster - United States
  - tmweb; logon; admin db TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Attempts to log into the TMWeb server using IBM TMWeb client results in the following error: "Unable to logon to Admin DB" SYMPTOM N
- 重排第 2：swg21503678｜Datacap｜IBM Datacap Taskmaster Capture is allowing only one client connection at a time - United States
  - connect connection TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Datacap Taskmaster client application is allowing only one connection at a time. CAUSE The UNC path of Taskmaster client application is 
- 重排第 3：swg21503322｜Datacap｜IBM Unable to connect to admin database with IBM Datacap Taskmaster Capture - United States
  - database connection problem error unable connect admin data source datasource TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When attempting to login using Taskmaster Web or another Datacap executable, 

## miss · M-tune-113 · L2 rerank · dense_only, wrong_product

- 问题：Can I change the ITCAM J2EE Agent Monitoring Level via the TEPS in version 7.1.1? In the 7.1 version of the J2EE agent I could use the Agent Configuration to change the Monitoring Level for the agent- https://www.ibm.com/support/knowledgecenter/en/SS3JRN_7.2.0/com.ibm.itcamfapps_ad.doc_72/J2EE_agent_tema_install_guide/step10.html So how can I change the Monitoring Level in the 7.1.1 agent?
- 改写后：Can I change the ITCAM J2EE Agent Monitoring Level via the TEPS in version 7.1.1? In the 7.1 version of the J2EE agent I could use the Agent Configuration to change the Monitoring Level for the agent- https://www.ibm.com/support/knowledgecenter/en/SS3JRN_7.2.0/com.ibm.itcamfapps_ad.doc_72/J2EE_agent
- 答案文档在各阶段名次：{'dense': 1, 'sparse': None, 'fusion': 13, 'rerank': None}
- **答案文档** swg21700308｜Tivoli Composite Application Manager for J2EE｜IBM Modifying the default Monitoring Level and Sampling Rate in the J2EE v7.1.1.0.0 agent. - United States
  - J2EE TEMA Monitoring Level Sampling Rate xml files CAMADALL CAMJ2INST DC WebLogic TECHNOTE (FAQ) THIS DOCUMENT APPLIES ONLY TO THE FOLLOWING LANGUAGE VERSION(S): US English QUESTION How do I modify the default Monitoring Level and Sampling Rate in the new J2EE v7.1.1.0.0 agent? ANSWER In the older r
- 重排第 1：swg21689678｜Tivoli Composite Application Manager for Application Diagnostics｜IBM The ITCAM Agent for J2EE 7.1.1 Installation and Customization Guide? - United States
  - CAMJ2INST CAMJ2ALL J2EE TEMA Install Customization Guide; 5724N9500 TECHNOTE (FAQ) QUESTION Where can I find the ITCAM Agent for J2EE 7.1.1 Installation and Customization Guide? ANSWER The ITCAM Agent
- 重排第 2：swg21689680｜Tivoli Composite Application Manager for Application Diagnostics｜IBM The ITCAM Agent for J2EE 7.1.1 User's Guide - United States
  - J2EE TEMA User Guide CAMJ2INST CAMJ2ALL; 5724N9500 TECHNOTE (FAQ) THIS DOCUMENT APPLIES ONLY TO THE FOLLOWING LANGUAGE VERSION(S): US English QUESTION Where can I find the ITCAM Agent for J2EE 7.1.1 U
- 重排第 3：swg27050335｜PureApplication System｜IBM PureApplication System Release Note: Application server does not start after uninstalling Monitoring Agent for WebSphere Application Server - United States
  - v2240rlsnotes RELEASE NOTES ABSTRACT In rare cases, a permissions issue could cause the ITCAM WebSphere Application Server agent uninstall to fail. CONTENT Problem: In cases where the ITCAM monitoring

## miss · M-tune-116 · L1 retrieval: not retrieved · neither, wrong_product, vocab_gap

- 问题：fixlets do not appear in console bigfix Work with ILTM 9.2.7 / 9.5.4.38. In the bigfix console the fixlets do not appear, under the tree: Sites-> IBM License Reporting (ILTM) v9 -> Fixlets and Task. Attached image. Do you have any ideas? Greetings and thank you BigFix
- 改写后：fixlets do not appear in console bigfix Work with ILTM 9.2.7 / 9.5.4.38. In the bigfix console the fixlets do not appear, under the tree: Sites-> IBM License Reporting (ILTM) v9 -> Fixlets and Task. Attached image. Do you have any ideas? Greetings and thank you BigFix
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21974546｜IBM BigFix family｜IBM BigFix Server unable to gather site content from sync.bigfix.com (error: Unexpected HTTP response: 404) - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Identifying a block between the BigFix Server and IBM BigFix's sync.bigfix.com content servers. SYMPTOM Error messages similar to the following in the BESRelay.log on the BigFix server: * * * http://sync.bigfix.com/cgi-bin/bfgather/bessupport?Time=1452540
- 重排第 1：swg21995037｜IBM BigFix Inventory, IBM License Metric Tool｜IBM Security Bulletin: Vulnerability in URL Redirection affects IBM License Metric Tool v9.x and IBM BigFix Inventory v9.x (CVE-2016-8961) - United States
  - SECURITY BULLETIN SUMMARY IBM License Metric Tool v9.x and IBM BigFix Inventory v9.x accepts a user-controlled input that specifies a link to an external site, and uses that link in a redirect. This s
- 重排第 2：swg21995029｜IBM BigFix Inventory, IBM License Metric Tool｜IBM Security Bulletin: Vulnerability due to Server log files exposure affects IBM License Metric Tool v9 and IBM BigFix Inventory v9 (CVE-2016-8963) - United States
  - SECURITY BULLETIN SUMMARY IBM License Metric Tool v9 and IBM BigFix Inventory v9 Server log files can potentially reveal sensitive information. VULNERABILITY DETAILS CVEID: CVE-2016-8963 [http://cve.m
- 重排第 3：swg21995031｜IBM BigFix Inventory, IBM License Metric Tool｜IBM Security Bulletin: Vulnerability in password strength policy affects IBM License Metric Tool v9.x and IBM BigFix Inventory v9.x (CVE-2016-8962) - United States
  - SECURITY BULLETIN SUMMARY IBM License Metric Tool v9.x and IBM BigFix Inventory v9.x does not require strong passwords by default, which makes it easier for attackers to compromise user accounts. VULN

## miss · M-tune-119 · L1 retrieval: not retrieved · neither, same_product, vocab_gap

- 问题：Does ITCAM for MQ monitoring agent (kmq) use SYSTEM.MQXR.COMMAND.QUEUE causing Unknown Object Name [2085] event? Using the ITCAM MQ Monitoring agent, we have a situation that generates alerts when a 2085 event (object unknown) occurs. We have recently seen alerts for the queue SYSTEM.MQXR.COMMAND.QUEUE We found following technote: Unknown Object Name [2085], SYSTEM.MQXR.COMMAND.QUEUE http://www-01.ibm.com/support/docview.wss?uid=swg21681687 This technote does not mention Tivoli monitoring produc
- 改写后：Does ITCAM for MQ monitoring agent (kmq) use SYSTEM.MQXR.COMMAND.QUEUE causing Unknown Object Name [2085] event? Using the ITCAM MQ Monitoring agent, we have a situation that generates alerts when a 2085 event (object unknown) occurs. We have recently seen alerts for the queue SYSTEM.MQXR.COMMAND.QU
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21318303｜WebSphere MQ｜IBM Identify the application that has a WMQ queue opened - United States
  - Identify application program connected queue TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Your WebSphere MQ queue manager will not stop if there are applications that still have a queue opened. Your goal is to allow a graceful stop of the queue manager, also called controlled (or quiesced) shutdown.
- 重排第 1：swg21681687｜WebSphere MQ｜IBM Unknown Object Name [2085], SYSTEM.MQXR.COMMAND.QUEUE - United States
  - TECHNOTE (FAQ) QUESTION You see the following record added to the WebSphere MQ event messages queue 'SYSTEM.ADMIN.QMGR.EVENT'. [timestamp] Unknown Object Name [2085] Event Type: Queue Manager Queue Ma
- 重排第 2：swg1IV86027｜IBM Monitoring｜IBM IV86027: UNKNOWN OBJECT NAME EVENT IS GENERATED DUE TO KMQ.IRA.AGENT.QUEUE - United States
  - DIRECT LINKS TO FIXES 7.3.0.2-TIV-XEforMsg-LA0002 [http://www.ibm.com/support/fixcentral/quickorder?product=ibm%2FTivoli%2FTivoli+Composite+Application+Manager+for+Applications&fixids=7.3.0.2-TIV-XEfo
- 重排第 3：swg1IT14417｜IBM MQ｜IBM IT14417: Command dmpmqcfg -a times out with message: 'MQSC timed out waiting for a response from the command server.' - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * Running dmpmqcfg -a locally against a queue manager fails with error: "MQSC time

## miss · M-tune-121 · L2 rerank · same_product, vocab_gap

- 问题：Why are we seeing MQRC_NOT_AUTHORIZED errors after upgrading Websphere from V7.0 to V8.5.5? https://www-01.ibm.com/support/docview.wss?uid=swg21662193
- 改写后：Why are we seeing MQRC_NOT_AUTHORIZED errors after upgrading Websphere from V7.0 to V8.5.5? https://www-01.ibm.com/support/docview.wss?uid=swg21662193
- 答案文档在各阶段名次：{'dense': 19, 'sparse': 7, 'fusion': 6, 'rerank': 12}
- **答案文档** swg21662193｜WebSphere Application Server, WebSphere MQ｜IBM Changes in the default user identifier between WebSphere MQ V7.0.1 classes for JMS and WebSphere MQ V7.1 classes for JMS - United States
  - TECHNOTE (FAQ) QUESTION You have configured a WebSphere Application Server WebSphere MQ messaging provider connection factory without an Authentication Alias and do not programmatically supply user identifier information when creating a connection to a queue manager. You notice a change in the defau
- 重排第 1：swg21651526｜WebSphere MQ｜IBM MQJMS2013 (V6) JMSWMQ2013 (V7) 無効なセキュリティ認証 (RC 2035) - United States
  - TECHNOTE(トラブルシューティング) 問題(概要) WebSphere MQとMQ JMSアプリケーションを使用する場合のセキュリティ認証エラーに関して You are running WebSphere MQ and your MQ JMS application fails with security authentication errors. 症状 MQRC 2035 MQRC_NO
- 重排第 2：swg21138961｜WebSphere Application Server, WebSphere MQ｜IBM MQJMS2013 (V6) JMSWMQ2013 (V7 and later) invalid security authentication (RC 2035) - United States
  - mqminfo permissions sec auth TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) You are running WebSphere MQ and your MQ JMS application fails with security authentication errors. SYMPTOM MQRC 2035 MQRC_NOT
- 重排第 3：swg21420469｜WebSphere MQ｜IBM 2035 MQRC_NOT_AUTHORIZED Java or JMS applications fail after upgrading from MQ V5.3 to V6 or V7 - United States
  - 2035; JMS; java; MQRC_NOT_AUTHORIZED; client application; upgrade TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) You upgrade from WebSphere MQ V5.3 to V6 or V7 on the box where your client application i

## miss · M-tune-125 · L1 retrieval: not retrieved · neither, wrong_product, vocab_gap

- 问题：ITMv6 issue: Cognos reports run for an extended period, sometimes never finishes
- 改写后：ITMv6 issue: Cognos reports run for an extended period, sometimes never finishes
- 答案文档在各阶段名次：{'dense': None, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21585678｜Tivoli Common Reporting｜IBM Increasing Java Heap Memory in IBM Tivoli Common Reporting 2.1/2.1.1 - United States
  - TCR - Tivoli Common Reporting TECHNOTE (FAQ) QUESTION How to increase Java heap memory size in IBM Tivoli Common Reporting (TCR) 2.1/2.1.1 versions? CAUSE Running a large scale report with Default java heap settings might result in OutOfMemory error ANSWER TCR 2.1/2.1.1 server provides a default set
- 重排第 1：swg1IT23603｜IBM Control Center｜IBM IT23603: COGNOS NEVER FINISHES STARTING - United States
  - SUBSCRIBE TO THIS APAR By subscribing, you receive periodic emails alerting you to the status of the APAR, along with a link to the fix after it becomes available. You can track this item individually
- 重排第 2：swg21673565｜Cognos Business Intelligence, Cognos Controller｜IBM ** Troubleshooting ** Standard Reports appear to hang / freeze when sending the output to PDF - United States
  - PDF report progress bar intermittently hangs TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) User runs a report (e.g. a BI report or a Controller 'standard report', also known as a 'system report'). By d
- 重排第 3：swg21902141｜Cognos Business Intelligence｜IBM Scheduled reports stay in "Executing" - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Scheduled reports begin to run and will sometimes complete successfully, but other times will remain in "Executing" and never complete. ENVIRONMENT A VPN C

## miss · M-tune-127 · L2 rerank · wrong_product

- 问题：CR is not inserted for textarea using IE We are using IBM Case Manager 5.2.1.4 and IBM Content Navigator 2.0.3.7. Using Properties View Designer of Case Builder, we tried to input CR ("Enter") on the text area, but CR is not inserted. This issue occurs only on IE, not on Firefox or Chrome.
- 改写后：CR is not inserted for textarea using IE We are using IBM Case Manager 5.2.1.4 and IBM Content Navigator 2.0.3.7. Using Properties View Designer of Case Builder, we tried to input CR ('Enter') on the text area, but CR is not inserted. This issue occurs only on IE, not on Firefox or Chrome.
- 答案文档在各阶段名次：{'dense': 23, 'sparse': 17, 'fusion': 30, 'rerank': 18}
- **答案文档** swg27049061｜Content Navigator｜IBM Fix list for IBM Content Navigator Version 3.0.0 - United States
  - PRODUCT DOCUMENTATION ABSTRACT The following table contains the complete listing of fixes for Version 3.0.0. CONTENT APARs fixed in IBM Content Navigator Version 3.0.0 APAR Description IO24490 (IBM FileNet P8 users) When EDS is used to hide workflow properties in the in-basket filter, moving the inp
- 重排第 1：swg1PJ44413｜Case Manager｜IBM PJ44413: PRESSING CARRIAGE RETURN DOES NOT START A NEW LINE FOR STRING PROPERTY WHEN CONFIGURED AS TEXTAREA AND WITHIN A PROPERTY LIST - United States
  - DIRECT LINKS TO FIXES IBM Case Manager V5.2.1 Fix Pack 6 for Linux for System Z [http://www.ibm.com/support/fixcentral/quickorder?product=ibm%2FInformation+Management%2FCase+Manager&fixids=5.2.1.6-ICM
- 重排第 2：swg21994511｜Case Manager｜IBM In IBM Case Manager [ICM], text area displays as a normal text box in Internal Explorer [IE]11. - United States
  - ICM; IE 11 TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) In ICM Case Builder, define a text area for a String type property. Fill in the value in ICM Case Client with IE 11, text area displays as a nor
- 重排第 3：swg1PJ44031｜Case Manager｜IBM PJ44031: WRAPPING OF TEXT IN A TEXTAREA INSIDE A PROPERTY TABLE CONTAINER DOES NOT WORK AS EXPECTED - United States
  - SUBSCRIBE TO THIS APAR By subscribing, you receive periodic emails alerting you to the status of the APAR, along with a link to the fix after it becomes available. You can track this item individually

## miss · M-tune-135 · L1 retrieval: fusion cut · dense_only, same_product, vocab_gap

- 问题：Load SPSS 25 on a new computer I purchased SPSS 25 with a 12 month license on Jan 27. I loaded it and used it on my MacBook Pro. I now have a new MacBookPro. I was able to download the program but get a message that says I don't have a license. I do have the activation code. Can you please help me use this product on my new computer? Thanks!
- 改写后：Load SPSS 25 on a new computer I purchased SPSS 25 with a 12 month license on Jan 27. I loaded it and used it on my MacBook Pro. I now have a new MacBookPro. I was able to download the program but get a message that says I don't have a license. I do have the activation code. Can you help me use this
- 答案文档在各阶段名次：{'dense': 27, 'sparse': None, 'fusion': None, 'rerank': None}
- **答案文档** swg21966637｜SPSS Statistics｜IBM Getting a warning message 'You do not have the correct administrator privileges' when attempting to license a SPSS Statistics product on Mac OS. - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) You have successfully installed an IBM SPSS Statistics product on a Mac computer. When you start the License Authorization Wizard (LAW) to enter the authorization code for licensing. You receive the following message: "Warning! You do not have the correct
- 重排第 1：swg21985888｜SPSS Modeler, SPSS Statistics｜IBM How do I transfer my IBM SPSS product/software license from one machine to another? - United States
  - TECHNOTE (FAQ) QUESTION How do I transfer my IBM SPSS product/software license from one machine to another? ANSWER It is not possible, nor required, to transfer a license from an existing product inst
- 重排第 2：swg21985805｜SPSS Statistics｜IBM Error #2072 'There was an unanticipated problem with the license for this product.' A license check is performed by the system when IBM SPSS Statistics or Modeler is started. - United States
  - TECHNOTE (FAQ) QUESTION Error #2072 'There was an unanticipated problem with the license for this product.' When running IBM SPSS Statistics or Modeler. CAUSE When starting IBM SPSS Statistics or Mode
- 重排第 3：swg1PI47268｜SPSS Statistics｜IBM PI47268: DOUBLE-CLICK ON .SAV. .SPV OR .SPS FILE --> IF STATISTICS IS OPEN GET ERROR THAT SPSSSTATISTICS CAN'T BE OPENED - United States
  - SUBSCRIBE TO THIS APAR By subscribing, you receive periodic emails alerting you to the status of the APAR, along with a link to the fix after it becomes available. You can track this item individually

## miss · M-tune-138 · L2 rerank · sparse_only, same_product, vocab_gap

- 问题：TWS / DWC and WebSphere 8.5.5.4+ WebSphere for TWS & DWC were upgraded to 8.5.5.4 on most servers in a particular environment. However, any TWS servers that still had 8.5.5.2, could no longer be seen by the new DWC / WAS 8.5.5.4 servers. Those lower WAS version engines could not be added to the DWC. Errors seen are: AWSUI0833E The operation could not be completed. There has been a communication failure. The internal message is: AWSJCO005E WebSphere Application Server has given the following erro
- 改写后：TWS / DWC and WebSphere 8.5.5.4+ WebSphere for TWS & DWC were upgraded to 8.5.5.4 on most servers in a particular environment. However, any TWS servers that still had 8.5.5.2, could no longer be seen by the new DWC / WAS 8.5.5.4 servers. Those lower WAS version engines could not be added to the DWC.
- 答案文档在各阶段名次：{'dense': None, 'sparse': 10, 'fusion': 17, 'rerank': 10}
- **答案文档** swg21964202｜IBM Workload Scheduler｜IBM How Connect TDWC 9.3 to TWS Engine lower level release - United States
  - dwc 93; connect; SSL ; TLS TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) DWC 9.3 users cannot connect to TWS Engine lower level releases (8.5.1 until 9.2) SYMPTOM Unable to connect to TWS 8.5.1 ,8.6 or 9.1/9.2 from DWC 9.3. Check the WAS SystemOut.log for error : SSL0080E: javax.net.ssl.SSLHandshakeE
- 重排第 1：swg21460225｜IBM Workload Scheduler｜IBM AWSJCO005E or SRVE0255E errors logging in to TDWC - United States
  - unable; cannot; connect; webui; dwc; tip; isc; AWSUI0766E; AWSUI0833E TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) SRVE0255E error is received when attempting to navigate to the Tivoli Dynamic Workloa
- 重排第 2：swg21624718｜IBM Workload Scheduler｜IBM TDWC Test connection Error when hostname contains underscore "_" - United States
  - webui engine connect TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Installation completes ok but when we define a new TWS engine, the connection fails AWSUI0766E. SYMPTOM When testing you receive error
- 重排第 3：swg21883616｜IBM Workload Scheduler｜IBM AWSJCO005E and AWSZAP006E Event rule errors with SSL certificates - United States
  - TDWC; DWC; authentication SSL TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) While creating an event rule to add a jobstream to a z/OS master from TDWC the following error is shown: "AWSJCO005E WebSpher

## miss · M-tune-139 · L2 rerank · dense_only, same_product, vocab_gap

- 问题：Latest deployed ruleset not executing in clustered environment We are using ODM 8.7.0.1 and are running into an issue in our clustered environment. After deploying an updated to the ruleapp, using "Replace RuleApp Version" versioning policy, the that the decision service is still executing the previous version of the business rules.
- 改写后：Latest deployed ruleset not executing in clustered environment We are using ODM 8.7.0.1 and are running into an issue in our clustered environment. After deploying an updated to the ruleapp, using 'Replace RuleApp Version' versioning policy, the decision service is still executing the previous versi
- 答案文档在各阶段名次：{'dense': 2, 'sparse': None, 'fusion': 9, 'rerank': 18}
- **答案文档** swg21598779｜IBM Operational Decision Manager, WebSphere ILOG JRules｜IBM An unexpected ruleset version is executed - United States
  - TECHNOTE (FAQ) QUESTION Why is Rule Execution Server (RES) not executing the expected version of a ruleset ? What are the possible causes after a hot deployment for Rule Execution Server not to use the updated ruleset ? CAUSE Possible causes for unexpected versions to be executed are: - the RES clie
- 重排第 1：swg21663707｜IBM Operational Decision Manager｜IBM Decision Center utility Ant tasks - United States
  - TECHNOTE (FAQ) QUESTION Do you need to publish a RuleApp from a command line? Are you looking for information regarding branch security? Are you trying to automate Decision Center operations with Ant 
- 重排第 2：swg21668133｜IBM Decision Server｜IBM Making sure that the cached ruleset that is created by the loadUptodateRuleset method is used - United States
  - TECHNOTE (FAQ) QUESTION Why does the rule invocation not reuse the ruleset cache? How to develop an application which warms up rulesets? I have a web application that uses the loadUptodateRuleset meth
- 重排第 3：swg21679666｜IBM Operational Decision Manager｜IBM How to deploy .dsar ruleset archive using the res-deploy Ant task in ODM - United States
  - TECHNOTE (FAQ) QUESTION When I use res-deploy Ant task to deploy a ruleset archive for the decision engine ruleset (.dsar file), I get the error: [res-deploy] [ERROR] ilog.rules.res.tools.http.IlrDepl

## miss · M-tune-142 · L1 retrieval: fusion cut · sparse_only, same_product, vocab_gap

- 问题：XGS 5.3.0.6: Is there a way to replicate an inspection object under the same policy repository? Is there a way to replicate an inspection object under the same policy repository?
- 改写后：XGS 5.3.0.6: Is there a way to replicate an inspection object under the same policy repository?
- 答案文档在各阶段名次：{'dense': None, 'sparse': 30, 'fusion': None, 'rerank': None}
- **答案文档** swg21902778｜IBM Security Network Protection Documentation｜IBM Security Network Protection firmware 5.3.1 release notes - United States
  - release notes; readme; firmware; xgs FIX README ABSTRACT IBM Security Network Protection Firmware Version 5.3.1 is a firmware update for the XGS NGIPS network protection platform. This release provides the following updates to IBM Security Network Protection Firmware Version 5.3.1. CONTENT Serviceab
- 重排第 1：swg21902773｜IBM QRadar Network Security, IBM Security Network Intrusion Prevention System, IBM Security Network Protection Documentation｜IBM Policy migration limitations and facts to consider - United States
  - gx xgs migration TECHNOTE (FAQ) QUESTION What are the limitations and facts that need to be considered before running the policy migration utility for Network IPS (GX) to IBM QRadar Network Security(I
- 重排第 2：swg21972184｜IBM QRadar Network Security, IBM Security Network Protection Documentation｜IBM Using domain certificate objects for Outbound SSL Inspection Policy on IBM Qradar Network Security - United States
  - classifications; certification authority; CA; customize; general; inspection rules; Network Access Policy; XGS TECHNOTE (FAQ) QUESTION How can you use domain certificate categories and lists objects i
- 重排第 3：swg21667633｜IBM Security Network Intrusion Prevention System, IBM Security Network Protection Documentation｜IBM Policy differences between the Security Network IPS and Security Network Protection System - United States
  - policy; difference; firewall; user-defined; protection domains; wap; connection events; snort TECHNOTE (FAQ) QUESTION What are the policy differences between the Security Network IPS (GX) and the Secu

## miss · M-tune-150 · L2 rerank · wrong_product, near_duplicate, vocab_gap

- 问题：Does DataPower support SHA-2? Is DataPower able to support SHA-2 (SHA256)? 1
- 改写后：Does DataPower support SHA-2? Is DataPower able to support SHA-2 (SHA256)? 1
- 答案文档在各阶段名次：{'dense': 5, 'sparse': 20, 'fusion': 4, 'rerank': 19}
- **答案文档** swg21406783｜WebSphere DataPower Integration Appliance XI50｜IBM When a Certificate Authority (CA) signs a certificate using SHA2(SHA-256), IBM Websphere DataPower SOA Appliance can validate the signature of CA on certificate. - United States
  - Datapower DP valcred SHA2 SHA-2 SHA-256 certificate trust CA TECHNOTE (FAQ) QUESTION When a Certificate Authority(CA) signs a certificate using SHA2(SHA-256), can IBM Websphere DataPower SOA Appliance validate the certificate and trust chain? ANSWER Yes, if a Certificate Authority(CA) signs a certif
- 重排第 1：swg1PJ41598｜FileNet P8 Platform｜IBM PJ41598: IMAGE SERVICES (IS) 4.2.0 NEEDS TO SUPPORT FIPS SHA-256 - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * Image Services (IS) 4.2.0 Needs to support FIPS SHA-256 LOCAL FIX PROBLEM SUMMAR
- 重排第 2：swg21962011｜IBM DataPower Gateways｜IBM SSL communication between Datapower and MQ Queue Manager requires same exact cipher - United States
  - mq ssl mq-qm handshake failure cipher suite TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) SSL connections between Datapower and MQ Queue Manager may fail if the cipher on the MQ Queue Manager channel d
- 重排第 3：swg1PJ41664｜FileNet P8 Platform｜IBM PJ41664: IMAGE SERVICES (IS) 4.2.0 NEEDS TO SUPPORT FIPS SHA-256 - United States
  - SUBSCRIBE TO THIS APAR By subscribing, you receive periodic emails alerting you to the status of the APAR, along with a link to the fix after it becomes available. You can track this item individually

## control · M-tune-001 · correct · 

- 问题：I am running WebSphere App server on 64bit JVM with plenty of free system memory, how come I still get Native OutOfMemory errors (NOOM)?
- 改写后：I am running WebSphere App server on 64bit JVM with plenty of free system memory, how come I still get Native OutOfMemory errors (NOOM)?
- 答案文档在各阶段名次：{'dense': 13, 'sparse': 1, 'fusion': 3, 'rerank': 1}
- **答案文档** swg21660890｜WebSphere Application Server｜IBM Using -Xgc:preferredHeapBase with -Xcompressedrefs - United States
  - TECHNOTE (FAQ) QUESTION "Why does the JVM report a native out-of-memory (NOOM) when using compressed references? I am using a 64bit JVM and I clearly have plenty of memory left. How can I resolve this problem?" CAUSE *In this note, please refer to Java Versioning: Java Version.Release.ServiceRelease
- 重排第 1：swg21660890｜WebSphere Application Server｜IBM Using -Xgc:preferredHeapBase with -Xcompressedrefs - United States
  - TECHNOTE (FAQ) QUESTION "Why does the JVM report a native out-of-memory (NOOM) when using compressed references? I am using a 64bit JVM and I clearly have plenty of memory left. How can I resolve this
- 重排第 2：swg21425419｜Content Manager｜IBM The resource manager component of Content Manager for Enterprise Edition V8.4 (CM) crashes with an OutOfMemory error. - United States
  - javacore jvm out of memory jni -Xjni:arrayCacheMax=0 tsm TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) During high volume stores or migrates into Tivoli Storage Manager (TSM) the resource manager java 
- 重排第 3：swg21504345｜WebSphere Application Server｜IBM Using libumem to diagnose Native OutOfMemoryErrors or leaks on Solaris - United States
  - WebSphere Solaris native outofmemory libumem TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) This technote details how to set up and use libumem to track native memory usage for IBM WebSphere Application

## control · M-tune-028 · correct · 

- 问题：What happens if I run arssyscr -I instance_name -r without having Report Distribution enabled or installed? What could cause problems if I run arssyscr -I instance_name -r without having Report Distribution enabled or installed in CMOD v9.0?
- 改写后：What happens if I run arssyscr -I instance_name -r without having Report Distribution enabled or installed? What could cause problems if I run arssyscr -I instance_name -r without having Report Distribution enabled or installed in CMOD v9.0?
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21672402｜Content Manager OnDemand for Multiplatforms｜IBM What happens if I run arssyscr -I instance_name -r  without having Report Distribution enabled or installed? - United States
  - arssyscr; Report Distribution TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Running arssyscr -I instance_name -r during upgrade without RDF installed or enabled can lead to errors during load. SYMPTOM You will see errors similar to (depending on database brand) DB Error: ORA-00942: table or view does
- 重排第 1：swg21672402｜Content Manager OnDemand for Multiplatforms｜IBM What happens if I run arssyscr -I instance_name -r  without having Report Distribution enabled or installed? - United States
  - arssyscr; Report Distribution TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Running arssyscr -I instance_name -r during upgrade without RDF installed or enabled can lead to errors during load. SYMPTOM 
- 重排第 2：swg21620754｜Content Manager OnDemand for Multiplatforms｜IBM Upgrade guide for Content Manager OnDemand server V9.0.0 - United States
  - TECHNOTE (FAQ) QUESTION This guide contains step by step instructions and information to migrate your IBM Content Manager OnDemand server to V9.0.0. Follow the instructions for the version of Content 
- 重排第 3：swg1PM20892｜Content Manager OnDemand for z/OS｜IBM PM20892: CMOD ISSUES  DSNT408I SQLCODE = -104, ERROR:  ILLEGAL SYMBOL    "ª--" - United States
  - z/os A FIX IS AVAILABLE Obtain the fix for this APAR. SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * DB Error: &#65425;DB2 FOR 

## control · M-tune-029 · correct · 

- 问题：What are the supported Macintosh Operating System versions for IBM SPSS Statistics 19, 20, 21, 22 and 23? I would like to know what are the supported Macintosh Operating system versions for IBM SPSS Statistics versions 18, 19, 20, 21, 22 and 23?
- 改写后：What are the supported Macintosh Operating System versions for IBM SPSS Statistics 19, 20, 21, 22 and 23? I would like to know what are the supported Macintosh Operating system versions for IBM SPSS Statistics versions 18, 19, 20, 21, 22 and 23?
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 2, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21507587｜SPSS Statistics｜IBM What are the supported Apple Macintosh Operating System Versions for IBM SPSS Statistics? - United States
  - SPSS mac macintosh Apple Macintosh statistics OS supported version compatibility matrix leopard Snow Leopard Lion Mountain Lion 10.8 Mavericks 10.9 22 Yosemite 10.10 (Yosemite) el capitan 10.11 spss 24 Sierra 10.12 High Sierra 10.13 TECHNOTE (FAQ) QUESTION I would like to know what are the supported
- 重排第 1：swg21507587｜SPSS Statistics｜IBM What are the supported Apple Macintosh Operating System Versions for IBM SPSS Statistics? - United States
  - SPSS mac macintosh Apple Macintosh statistics OS supported version compatibility matrix leopard Snow Leopard Lion Mountain Lion 10.8 Mavericks 10.9 22 Yosemite 10.10 (Yosemite) el capitan 10.11 spss 2
- 重排第 2：swg21903203｜SPSS Statistics｜IBM SPSS Statistics 18、 19、 20、 21、 22 和 23支持的Mac操作系统版本是什么 - United States
  - TECHNOTE (FAQ) 疑问 IBM SPSS Statistics 18、 19、 20、 21、 22 和 23支持的Mac操作系统版本是什么 答案 建议阅读 IBM 软件产品的兼容性报告 www-969.ibm.com/software/reports/compatibility/clarity/index.jsp [http://www-969.ibm.com/software/re
- 重排第 3：swg1PM81098｜SPSS Statistics｜IBM PM81098: INCONSISTENT DOCUMENTATION OF SUPPORTED MACINTOSH OPERATING SYSTEM 10.6 AND IBM SPSS STATISTICS 21 - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS FIXED IF NEXT. ERROR DESCRIPTION * You would like to know if you can install IBM SPSS Statistics 21 on a Macintosh 

## control · M-tune-030 · correct · 

- 问题：Security Bulletin: IBM MQ and IBM MQ Appliance MQOPEN call might succeed when it should have failed (CVE-2017-1341) I need to understand details regarding Security Bulletin: IBM MQ and IBM MQ Appliance MQOPEN call might succeed when it should have failed (CVE-2017-1341). Where can I find this information?
- 改写后：Security Bulletin: IBM MQ and IBM MQ Appliance MQOPEN call might succeed when it should have failed (CVE-2017-1341) I need to understand details regarding Security Bulletin: IBM MQ and IBM MQ Appliance MQOPEN call might succeed when it should have failed (CVE-2017-1341). Where can I find this inform
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg22005400｜IBM MQ｜IBM Security Bulletin: IBM MQ and IBM MQ Appliance MQOPEN call might succeed when it should have failed.  (CVE-2017-1341 ) - United States
  - SECURITY BULLETIN SUMMARY MQOPEN call might succeed when it should have failed, when using generic profile authority matching for remotely defined MQ object. VULNERABILITY DETAILS CVEID: CVE-2017-1341 [http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2017-1341] DESCRIPTION: IBM WebSphere MQ could a
- 重排第 1：swg22005400｜IBM MQ｜IBM Security Bulletin: IBM MQ and IBM MQ Appliance MQOPEN call might succeed when it should have failed.  (CVE-2017-1341 ) - United States
  - SECURITY BULLETIN SUMMARY MQOPEN call might succeed when it should have failed, when using generic profile authority matching for remotely defined MQ object. VULNERABILITY DETAILS CVEID: CVE-2017-1341
- 重排第 2：swg22011395｜IBM MQ｜IBM Security Bulletin: IBM MQとIBM MQアプライアンス において、本来なら失敗するべきMQOPEN 呼び出しが成功する可能性があります。(CVE-2017-1341 ) - United States
  - SECURITY BULLETIN SUMMARY リモートで定義されたMQオブジェクトに一致する汎用プロファイル権限を使用しているときに、本来なら失敗するべきMQOPEN 呼び出しが成功する可能性があります。 最新情報はオリジナルの技術文書（英文）をご参照ください。 http://www.ibm.com/support/docview.wss?uid=swg22005400 [http://ww
- 重排第 3：swg21999672｜WebSphere MQ｜IBM Security Bulletin: IBM WebSphere MQ and IBM MQ Appliance proliferation of channel agents causes denial of service (CVE-2017-1145) - United States
  - SECURITY BULLETIN SUMMARY Threaded channel agents (amqrmppa) might not terminate when they are no longer required. This can lead to a denial of service through exhausting server resources. VULNERABILI

## control · M-tune-032 · correct · 

- 问题：What does the end-file-message mean while doing a launchpad.sh in the MS" I am getting an end-file-message means while doing a launchpad.sh in the MS. How do I solve the problem?
- 改写后：What does the end-file-message mean while doing a launchpad.sh in the MS?
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21985630｜Tivoli Composite Application Manager for Application Diagnostics｜IBM Using launchpad.sh or silent_MS_linux.bin results in end-of-file message. - United States
  - ITCAM compat-libstdc++ libstdc++ libraries silent_MS_linux.bin launchpad.sh errors TECHNOTE (TROUBLESHOOTING) THIS DOCUMENT APPLIES ONLY TO THE FOLLOWING LANGUAGE VERSION(S): US English PROBLEM(ABSTRACT) Using the DC or MS 'launchpad.sh' script results in the following error message: ./setup_MS_lin.
- 重排第 1：swg21985630｜Tivoli Composite Application Manager for Application Diagnostics｜IBM Using launchpad.sh or silent_MS_linux.bin results in end-of-file message. - United States
  - ITCAM compat-libstdc++ libstdc++ libraries silent_MS_linux.bin launchpad.sh errors TECHNOTE (TROUBLESHOOTING) THIS DOCUMENT APPLIES ONLY TO THE FOLLOWING LANGUAGE VERSION(S): US English PROBLEM(ABSTRA
- 重排第 2：swg21671107｜Tivoli Composite Application Manager for Application Diagnostics｜IBM Installing the Linux library on a 64-bit in preparation for the MS. - United States
  - Linux library libpam.so.6 libpam.so.1 yum install tema CAMADALL CAMADINST MS install launchpad.sh TECHNOTE (FAQ) THIS DOCUMENT APPLIES ONLY TO THE FOLLOWING LANGUAGE VERSION(S): US English QUESTION In
- 重排第 3：swg21619205｜IBM Security Identity Manager｜IBM File not found when installing RaPM - United States
  - install error missing launchpad.sh manually manual installing TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) The installation of Tivoli Integrated Portal component fails when IBM Security Role and Polic

## control · M-tune-035 · correct · 

- 问题：Help with Security Bulletin: Apache Commons FileUpload Vulnerabilities in IBM WebSphere MQ File Transfer Edition component (CVE-2016-1000031) I need to understand details regarding Security Bulletin: Apache Commons FileUpload Vulnerabilities in IBM WebSphere MQ File Transfer Edition component (CVE-2016-1000031).
- 改写后：Help with Security Bulletin: Apache Commons FileUpload Vulnerabilities in IBM WebSphere MQ File Transfer Edition component (CVE-2016-1000031)
- 答案文档在各阶段名次：{'dense': 5, 'sparse': 1, 'fusion': 2, 'rerank': 1}
- **答案文档** swg22011689｜WebSphere MQ｜IBM Security Bulletin: Apache Commons FileUpload Vulnerabilities in IBM WebSphere MQ File Transfer Edition component (CVE-2016-1000031) - United States
  - SECURITY BULLETIN SUMMARY The DiskFileItem class in Apache Commons Fileupload before version 1.3.3, used in IBM WebSphere MQ File Transfer Edition, specifically the Web Gateway component, could allow remote attackers to execute arbitrary code under the context of the current process, causing an unde
- 重排第 1：swg22011689｜WebSphere MQ｜IBM Security Bulletin: Apache Commons FileUpload Vulnerabilities in IBM WebSphere MQ File Transfer Edition component (CVE-2016-1000031) - United States
  - SECURITY BULLETIN SUMMARY The DiskFileItem class in Apache Commons Fileupload before version 1.3.3, used in IBM WebSphere MQ File Transfer Edition, specifically the Web Gateway component, could allow 
- 重排第 2：swg22011788｜WebSphere MQ｜IBM Security Bulletin: Apache Commons FileUpload Vulnerabilities in IBM WebSphere MQ Managed File Transfer component (CVE-2016-1000031) - United States
  - SECURITY BULLETIN SUMMARY The DiskFileItem class in Apache Commons Fileupload before 1.3.3, as used in IBM WebSphere MQ Managed File Transfer, specifically the Web Gateway component, allows remote att
- 重排第 3：swg22012109｜WebSphere MQ｜IBM Security Bulletin: Apache Commons FileUpload Vulnerabilities in IBM WebSphere MQ File Transfer Edition(CVE-2016-3092) - United States
  - SECURITY BULLETIN SUMMARY The MultipartStream class in Apache Commons Fileupload before 1.3.2, as used in IBM WebSphere MQ File Transfer Edition, specifically the Web Gateway component, allows remote 

## control · M-tune-037 · correct · 

- 问题：Help with Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition Tool (CVE-2015-0410 and CVE-2014-6593) I need to understand details regarding "Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition Tool (CVE-2015-0410 and CVE-2014-6593)." Where can I find information regarding CVE-2014-6593?
- 改写后：Help with Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition Tool (CVE-2015-0410 and CVE-2014-6593) I need to understand details regarding 'Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition
- 答案文档在各阶段名次：{'dense': 10, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21962370｜PureApplication System｜IBM Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition Tool (CVE-2015-0410 and CVE-2014-6593) - United States
  - SECURITY BULLETIN SUMMARY There are multiple vulnerabilities in IBM® SDK Java™ Technology Edition Version 6 and 7 that are used by IBM Image Construction and Composition Tool. These issues were disclosed as part of the IBM Java SDK updates in January 2015. VULNERABILITY DETAILS CVEID: CVE-2015-0410 
- 重排第 1：swg21962370｜PureApplication System｜IBM Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition Tool (CVE-2015-0410 and CVE-2014-6593) - United States
  - SECURITY BULLETIN SUMMARY There are multiple vulnerabilities in IBM® SDK Java™ Technology Edition Version 6 and 7 that are used by IBM Image Construction and Composition Tool. These issues were disclo
- 重排第 2：swg21903249｜PureApplication System｜IBM Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition Tool (CVE-2014-3566 and CVE-2014-6457) - United States
  - SECURITY BULLETIN SUMMARY There are multiple vulnerabilities in IBM® SDK Java™ Technology Edition, Version 6 that is used by IBM PureApplication System. This also includes a fix for the Padding Oracle
- 重排第 3：swg21962837｜PureApplication System｜IBM Security Bulletin: Multiple vulnerabilities in IBM Java SDK affect IBM Image Construction and Composition Tool (CVE-2015-2808, CVE-2015-1916, CVE-2015-0204, CVE-2015-0138) - United States
  - SECURITY BULLETIN SUMMARY There are multiple vulnerabilities in IBM SDK Java Technology Edition, Version 6 and 7, that is used by IBM Image Construction and Composition Tool. These issues were disclos

## control · M-tune-053 · correct · 

- 问题：How to control SDMS database size? ITCAM for SOA 7.1.1 was installed about 3 years ago. I already know that SDMS database size may increase with no limit. Has anyone found a way to keep under control this behavior?
- 改写后：How to control SDMS database size? ITCAM for SOA 7.1.1 was installed about 3 years ago. I already know that SDMS database size may increase with no limit. Has anyone found a way to keep under control this behavior?
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21959281｜Tivoli Composite Application Manager for SOA｜IBM ITCAM for SOA KD4SDMS database size grows - United States
  - CAMSOAALL CAMSOADB CAMSOAPERF REQMETRICS RESPMETRICS kd4TrimDB2db TECHNOTE (FAQ) QUESTION As the KD4SDMS grows unbounded, is there a way to regularly prune it? ANSWER Regarding the older release ITCAM for SOA 7.1.1, there is no a mechanism to automatically regularly prune the KD4SDMS database. The f
- 重排第 1：swg21959281｜Tivoli Composite Application Manager for SOA｜IBM ITCAM for SOA KD4SDMS database size grows - United States
  - CAMSOAALL CAMSOADB CAMSOAPERF REQMETRICS RESPMETRICS kd4TrimDB2db TECHNOTE (FAQ) QUESTION As the KD4SDMS grows unbounded, is there a way to regularly prune it? ANSWER Regarding the older release ITCAM
- 重排第 2：swg21381100｜Tivoli Composite Application Manager for SOA｜IBM ITCAM for SOA 7.1.x with a corrupted SDMS database - United States
  - soa; datapower; sdms; database; corruption; CAMSOAALL CAMSOADB TECHNOTE (FAQ) QUESTION How to regenerate the SDMS database after a data corruption or installation problem? ANSWER In this situation, th
- 重排第 3：swg21681048｜Tivoli Composite Application Manager for SOA｜IBM Pruning ITCAM for SOA - SDMS Relationship Metrics Tables - United States
  - CAMSOAALL CAMSOAPERF CAMSOADB CAMSOAAgent Prune DB Database SDMS Metric Table Tables TECHNOTE (FAQ) QUESTION ITCAM for SOA database appears to be full. Is there a way to prune it ? CAUSE The relations

## control · M-tune-067 · correct · 

- 问题：How to find details of Corrupted Object from the entries in db2diag.log? We have corruption in DB2 Database and got entries for corrupted Object in db2diag.log ,Need to find details of the Object using information dumped in db2diag.log
- 改写后：How to find details of Corrupted Object from the entries in db2diag.log? We have corruption in DB2 Database and got entries for corrupted Object in db2diag.log, Need to find details of the Object using information dumped in db2diag.log
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21983129｜DB2 for Linux, UNIX and Windows｜IBM How to find details of Corrupted Object from the entries in db2diag.log? - United States
  - TECHNOTE (FAQ) QUESTION How to find details of Corrupted Object from the entries in db2diag.log? ANSWER When we have corruption in the database we may received following kind of entries in db2diag.log These also notify object where we t where we have detected corruption in the Database. Sample db2di
- 重排第 1：swg21983129｜DB2 for Linux, UNIX and Windows｜IBM How to find details of Corrupted Object from the entries in db2diag.log? - United States
  - TECHNOTE (FAQ) QUESTION How to find details of Corrupted Object from the entries in db2diag.log? ANSWER When we have corruption in the database we may received following kind of entries in db2diag.log
- 重排第 2：swg21322155｜DB2 for Linux, UNIX and Windows｜IBM Collecting data: DB2 data corruption - United States
  - MustGather; MustGather; MustGather; MustGatherDocument; CollectTroubleshootingData; bad page; CBIT; data corruption TECHNOTE (FAQ) QUESTION Collecting data for troubleshooting corruption problems such
- 重排第 3：swg1IY92909｜DB2 for Linux, UNIX and Windows｜IBM IY92909: INCORRECT MESSAGE DISK FULL WAS REPORTED (DIA8312C) IN DB2DIAG  AND SQL0968C TO THE PROMPT WHEN SMS TEMP PAGE IS MISSING/CORRUPT - United States
  - AIX SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS FIXED IF NEXT. ERROR DESCRIPTION * When db2 is missing a SMS temporary page during sort/reorg, it reports misle

## control · M-tune-073 · correct · 

- 问题：Help with Security Bulletin: IBM WebSphere MQ MQXR insecure passwords (CVE-2015-2012) I need to understand details regarding Security Bulletin: IBM WebSphere MQ MQXR insecure passwords (CVE-2015-2012). Where can I find this information?
- 改写后：Help with Security Bulletin: IBM WebSphere MQ MQXR insecure passwords (CVE-2015-2012) I need to understand details regarding Security Bulletin: IBM WebSphere MQ MQXR insecure passwords (CVE-2015-2012). Where can I find this information?
- 答案文档在各阶段名次：{'dense': 2, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21968399｜WebSphere MQ｜IBM Security Bulletin: IBM WebSphere MQ MQXR insecure passwords (CVE-2015-2012) - United States
  - SECURITY BULLETIN SUMMARY The Telemetry (MQXR) service can be configured to use SSL/TLS connections - the passphrase used to access the keystore is written to the file system in clear text in a properties file that is world readable. VULNERABILITY DETAILS CVEID: CVE-2015-2012 [http://cve.mitre.org/c
- 重排第 1：swg21968399｜WebSphere MQ｜IBM Security Bulletin: IBM WebSphere MQ MQXR insecure passwords (CVE-2015-2012) - United States
  - SECURITY BULLETIN SUMMARY The Telemetry (MQXR) service can be configured to use SSL/TLS connections - the passphrase used to access the keystore is written to the file system in clear text in a proper
- 重排第 2：swg21977183｜WebSphere MQ｜IBM 【セキュリティ情報】IBM MQ Telemetry (遠隔測定) (MQXR) 安全でないパスワード  (CVE-2015-2012) - United States
  - SECURITY BULLETIN SUMMARY IBM MQ Telemetry (遠隔測定) (MQXR)サービスは、SSL/ TLS接続を使用するように設定することができます。 キーストアにアクセスするために使用するパスフレーズは、プロパティファイルにテキストとして書き込まれているため、読み込み可能です。 VULNERABILITY DETAILS 脆弱性の詳細： CVEID: CVE-2
- 重排第 3：swg21972019｜IBM MQ Light｜IBM Security Bulletin: IBM MQ Light is vulnerable to a remote attack on the MQXR service (CVE-2015-4941) - United States
  - SECURITY BULLETIN SUMMARY IBM MQ Light could allow a remote attacker to crash the MQXR service due to incorrect handling of abbreviated TLS handshake. VULNERABILITY DETAILS CVEID: CVE-2015-4941 [http:

## control · M-tune-097 · correct · 

- 问题：Why is an error seen while running run-svrssl-config? Following error is seen while running run-svrssl-config ConfigEngine task: action-run-pdjrte-config-zos-wp.ac.impl: [validateHost] Validating hostname(s) in the following argument: tam001:7136:1,tam002:7136:2 [echo] Command to run is: java com.tivoli.pd.jcfg.SvrSslCfg -action config -admin_id sec_master -admin_pwd ****** -appsvr_id myAppSvr -port 7223 -mode remote -policysvr tam001:7135:1,tam002:7135:2 -authzsvr tam001:7136:1,tam002:7136:2 -c
- 改写后：Why is an error seen while running run-svrssl-config? Following error is seen while running run-svrssl-config ConfigEngine task: action-run-pdjrte-config-zos-wp.ac.impl: [validateHost] Validating hostname(s) in the following argument: tam001:7136:1,tam002:7136:2 [echo] Command to run is: java com.ti
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21319595｜WebSphere Portal｜IBM HPDMG0759W error when creating the AMJRTE properties file - United States
  - TAM; run-svrssl-config; svrssl; HPDMG0759W; AMJRTE TECHNOTE (TROUBLESHOOTING) PROBLEM When executing the "run-svrssl-config" task via the ConfigEngine to create the AMJRTE properties file, you receive the following error: Command to run is: java com.tivoli.pd.jcfg.SvrSslCfg -action config -admin_id 
- 重排第 1：swg21319595｜WebSphere Portal｜IBM HPDMG0759W error when creating the AMJRTE properties file - United States
  - TAM; run-svrssl-config; svrssl; HPDMG0759W; AMJRTE TECHNOTE (TROUBLESHOOTING) PROBLEM When executing the "run-svrssl-config" task via the ConfigEngine to create the AMJRTE properties file, you receive
- 重排第 2：swg1IY65917｜IBM Security Access Manager for Web｜IBM IY65917: TAM JAVA CLASSES DON'T WORK WITH IDI 5.2 1.4.1 JVM. - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PERMANENT RESTRICTION. ERROR DESCRIPTION * Customer is running TAM 5.1 on Windows and Linux. They have configured t
- 重排第 3：swg21222010｜IBM Security Access Manager for Web｜IBM HPDJA0116E Cannot contact server. (0x307a8074) - United States
  - HPDJA0116E (0x307a8074) TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) We can't login to pdadmin webpage, but via command line we can log in. Comes up with following message HPDJA0116E Cannot contact se

## control · M-tune-110 · correct · 

- 问题：Help with Security Bulletin: Vulnerability in Diffie-Hellman ciphers affects IBM WebSphere MQ Internet Passthru (CVE-2015-4000) I need to understand details regarding Security Bulletin: Vulnerability in Diffie-Hellman ciphers affects IBM WebSphere MQ Internet Passthru (CVE-2015-4000). Where can I find this information?
- 改写后：Help with Security Bulletin: Vulnerability in Diffie-Hellman ciphers affects IBM WebSphere MQ Internet Passthru (CVE-2015-4000) I need to understand details regarding Security Bulletin: Vulnerability in Diffie-Hellman ciphers affects IBM WebSphere MQ Internet Passthru (CVE-2015-4000). Where can I fi
- 答案文档在各阶段名次：{'dense': 13, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21959745｜WebSphere MQ｜IBM Security Bulletin: Vulnerability in Diffie-Hellman ciphers affects IBM WebSphere MQ Internet Passthru (CVE-2015-4000) - United States
  - SECURITY BULLETIN SUMMARY The Logjam Attack on TLS connections using the Diffie-Hellman (DH) key exchange protocol affects IBM WebSphere MQ Internet Pass-thru (MQIPT). VULNERABILITY DETAILS CVEID: CVE-2015-4000 [http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2015-4000] DESCRIPTION: The TLS protoc
- 重排第 1：swg21959745｜WebSphere MQ｜IBM Security Bulletin: Vulnerability in Diffie-Hellman ciphers affects IBM WebSphere MQ Internet Passthru (CVE-2015-4000) - United States
  - SECURITY BULLETIN SUMMARY The Logjam Attack on TLS connections using the Diffie-Hellman (DH) key exchange protocol affects IBM WebSphere MQ Internet Pass-thru (MQIPT). VULNERABILITY DETAILS CVEID: CVE
- 重排第 2：swg21962347｜WebSphere MQ｜IBM 【セキュリティ情報】 IBM WebSphere MQ Internet PassthruのDiffie-Hellman (DH) 暗号の脆弱性 (CVE-2015-4000) - United States
  - SECURITY BULLETIN SUMMARY Diffie-Hellman (DH) 暗号を使用した TLSプロトコルに脆弱性が発見されました。(通称 Logjam) TLS接続を行うIBM WebSphere MQ Internet Pass-Thru (MQIPT) に影響があります。 TLS 接続を使用する場合、中間者攻撃により TLS 接続が暗号強度の低い輸出グレードの 512 ビッ
- 重排第 3：swg21961072｜Predictive Customer Intelligence｜IBM Security Bulletin: A security vulnerability has been identified in muiltiple products shipped with Predictive Customer Intelligence (CVE-2015-4000) - United States
  - SECURITY BULLETIN SUMMARY WebSphere Application Server, Cognos Business Intelligence, Integration Bus, and WebSphere MQ are shipped as components of Predictive Customer Intelligence. Information about

## control · M-tune-117 · correct · 

- 问题：Why dbheap memory keeps increasing when I am running select count(*) for each table in my BLU database? I am running DB2 V11.1. It is a BLU database size of about 70T, most of the tables are column organized. I run select count(*) for each table, and finally got out of memory for dbheap. My question is: How to release the data in dbheap.
- 改写后：Why dbheap memory keeps increasing when I am running select count(*) for each table in my BLU database? I am running DB2 V11.1. It is a BLU database size of about 70T, most of the tables are column organized. I run select count(*) for each table, and finally got out of memory for dbheap. My question
- 答案文档在各阶段名次：{'dense': 6, 'sparse': 2, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21986534｜DB2 for Linux, UNIX and Windows｜IBM Newly accessed tables result in increasing of dbheap - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Newly accessed tables result in increasing of dbheap SYMPTOM From output of command "db2pd -db <db name> -mempools" you can find LogSz/PhySz of the memory pool named "dbh" keeps on increasing. CAUSE This is expected result. Every newly accessed table load
- 重排第 1：swg21986534｜DB2 for Linux, UNIX and Windows｜IBM Newly accessed tables result in increasing of dbheap - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Newly accessed tables result in increasing of dbheap SYMPTOM From output of command "db2pd -db <db name> -mempools" you can find LogSz/PhySz of the memory 
- 重排第 2：swg21697436｜DB2 for Linux, UNIX and Windows｜IBM Missing Rows on Select With UR When Concurrent Update is Executed on Column-Organized Table - United States
  - Missing rows; BLU; column-organized TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Rows may appear to be missing when SELECT with UR statements are executed on a column-organized table simultaneously wi
- 重排第 3：swg1IT07256｜DB2 for Linux, UNIX and Windows｜IBM IT07256: DB2SUPPORT FAILED TO COLLECT DATA FOR SYNOPSIS TABLES IF THE TABLES INVOLVED CONTAIN '/' IN THE TABLE NAME - United States
  - z/os A FIX IS AVAILABLE DB2 Version 10.5 Fix Pack 9 for Linux, UNIX, and Windows [http://www-01.ibm.com/support/docview.wss?uid=swg24044110] SUBSCRIBE You can track all active APARs for this component

## control · M-tune-128 · correct · 

- 问题：User environment variables no longer getting picked up after upgrade to 4.1.1.1 or 4.1.1.2? Have you found that after upgrade to Streams 4.1.1.1 or 4.1.1.2, that environment variables set in your .bashrc are no longer being set? For example ODBCINI is not set for the database toolkit and you get An SQL operation failed. The SQL state is 08003, the SQL code is 0 and the SQL message is [unixODBC][Driver Manager]Connnection does not exist.
- 改写后：User environment variables no longer getting picked up after upgrade to 4.1.1.1 or 4.1.1.2? Have you found that after upgrade to Streams 4.1.1.1 or 4.1.1.2, that environment variables set in your .bashrc are no longer being set? For example ODBCINI is not set for the database toolkit and you get An 
- 答案文档在各阶段名次：{'dense': 1, 'sparse': 1, 'fusion': 1, 'rerank': 1}
- **答案文档** swg21996508｜IBM Streams｜IBM STREAMS 4.1.1.1 and 4.1.1.2  JOBS DO NOT INHERIT THE ENVIRONMENT VARIABLES SET IN .BASHRC, WHEN STREAMS IS RUN AS A SYSTEM SERVICE - United States
  - FLASH (ALERT) ABSTRACT In Streams 4.1.1.1 and 4.1.1.2 Streams jobs may not pick up the user enviroment from the streams user's .bashrc. This behavior is different from earlier releases. With these versions, when Streams is run as a system service, application environment variables must be set with s
- 重排第 1：swg21996508｜IBM Streams｜IBM STREAMS 4.1.1.1 and 4.1.1.2  JOBS DO NOT INHERIT THE ENVIRONMENT VARIABLES SET IN .BASHRC, WHEN STREAMS IS RUN AS A SYSTEM SERVICE - United States
  - FLASH (ALERT) ABSTRACT In Streams 4.1.1.1 and 4.1.1.2 Streams jobs may not pick up the user enviroment from the streams user's .bashrc. This behavior is different from earlier releases. With these ver
- 重排第 2：swg1IT18432｜IBM Streams｜IBM IT18432: STREAMS JOBS DO NOT INHERIT THE ENVIRONMENT VARIABLES SET IN .BASHRC, WHEN RUN AS A SYSTEM SERVICE. - United States
  - FIXES ARE AVAILABLE IBM Streams Version 4.1.1 Fix Pack 4 [http://www-01.ibm.com/support/docview.wss?uid=swg24043581] IBM Streams Version 4.1.1 Fix Pack 5 [http://www-01.ibm.com/support/docview.wss?uid
- 重排第 3：swg1PM68165｜Cognos TM1｜IBM PM68165: THE ODBC INTERFACE OF TM1 10.1.0 AND TM1 10.1.0 FP1 SERVER FOR IBM AIX IS BROKEN - United States
  - SUBSCRIBE You can track all active APARs for this component. APAR STATUS * CLOSED AS PROGRAM ERROR. ERROR DESCRIPTION * The ODBC interface of both TM1 10.1.0 and TM1 10.1.0.1 aka TM1 10.1.0 FP1 Server

## control · M-tune-132 · correct · sparse_only

- 问题：WAS 8.5.x - Writing a JMS message to a remote queue takes a long time. How to write the message faster? We are writing a jms message from a websphere cell (cellA) to a queue hosted by another websphere cell (cellB). Sometimes we noticed that writing a message is very slow. Usually when a local queue will be used the time to write this messages is about 8 ms, but if the queue is located on a other cell is took significant longer (about 3000ms+ ). Our findings: After enabling following trace "=inf
- 改写后：WAS 8.5.x - Writing a JMS message to a remote queue takes a long time. How to write the message faster? We are writing a jms message from a websphere cell (cellA) to a queue hosted by another websphere cell (cellB). Sometimes we noticed that writing a message is very slow. Usually when a local queue
- 答案文档在各阶段名次：{'dense': None, 'sparse': 1, 'fusion': 4, 'rerank': 1}
- **答案文档** swg21624731｜IBM Business Process Manager Standard, WebSphere Application Server, WebSphere Enterprise Service Bus, WebSphere MQ, WebSphere Partner Gateway Advanced Edition, WebSphere Process Server, WebSphere Service Registry and Repository｜IBM JMSExceptions CWSIT0006E and CWSIA0241E on bus connect - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Your application throws JMS exceptions CWSIT0006E and CWSIA0241E when trying to connect to a WebSphere Application Server (WAS) Service Integration Bus (SIBus). SYMPTOM Application throws the following JMS exceptions in the stack trace while trying to con
- 重排第 1：swg21624731｜IBM Business Process Manager Standard, WebSphere Application Server, WebSphere Enterprise Service Bus, WebSphere MQ, WebSphere Partner Gateway Advanced Edition, WebSphere Process Server, WebSphere Service Registry and Repository｜IBM JMSExceptions CWSIT0006E and CWSIA0241E on bus connect - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Your application throws JMS exceptions CWSIT0006E and CWSIA0241E when trying to connect to a WebSphere Application Server (WAS) Service Integration Bus (SI
- 重排第 2：swg21624736｜IBM Business Monitor, SSDKJ8, WebSphere Application Server, WebSphere Enterprise Service Bus, WebSphere MQ, WebSphere Partner Gateway Advanced Edition, WebSphere Process Server, WebSphere Service Registry and Repository｜IBM SIMPLimitExceededException occurred while sending messages to a queue - United States
  - TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) When using the WebSphere Application Server (WAS) Message Engine, at either the client or applicaiton side you see this exception: SIMPLimitExceededExcepti
- 重排第 3：swg21293752｜WebSphere Enterprise Service Bus, WebSphere Process Server｜IBM A J2CA0138E and CWSIT0010E message is issued for WebSphere Process Server (WPS) when a user is not authorized to connect to a CEI bus - United States
  - v61rnotes; J2CA0138E; CWSIV0961E; CWSIT0020E; CWSIP0302E TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) Messaging operations cannot be performed on the Common Event Infrastructure bus (CommonEventInfras
