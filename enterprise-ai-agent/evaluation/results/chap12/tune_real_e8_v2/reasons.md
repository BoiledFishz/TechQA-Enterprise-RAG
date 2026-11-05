# tune_real_e8_v2: refusal reasons (84)

## M-tune-002 - judge_veto J2 - unanswerable, correct

- Q: How do I correct a BIP3701E: INVALID_CHARACTER_ERR I'm getting on deploy? Receiving a BIP3701E: A Java exception was thrown whilst calling the Java JNI method ''AdminAgentThread_getDeployMessage''. The Java exception was ''org.w3c.dom.DOMException: INVALID_CHARACTER_ERR: An invalid or illegal XML ch
- gold: None  (in evidence: False)
- vetoed: swg1PK01512 IBM PK01512: A COMMENT IN SOAPELEMENT GENERATES ORG.W3C.DOM.DOMEXCEPTION: INV ALID_CHARACTER_ERR - United States (is gold: False)
- reason: The source discusses a different error related to SOAPElement and comments, not BIP3701E.

## M-tune-005 - judge_veto J4 - unanswerable, correct

- Q: CICS VR FRLOG option that logs changes to VSAM datasets Is the information about the NONE option for FRLOG in the CICS VSAM Recovery for z/OS (CICS VR) documentation correct? If it is not, what information is logged when NONE is specified? I am working on a POC for the Classic change data capture (C
- gold: None  (in evidence: False)
- vetoed: swg21296350 IBM Stopping logger writes for ADRDSSU RESTORE of sphere defined with FRLOG ALL, UNDO or REDO - United States (is gold: False)
- reason: The source discusses stopping logger writes for ADRDSSU RESTORE and does not address the NONE option for FRLOG in CICS VSAM Recovery.

## M-tune-007 - selection_empty  - answerable, wrong

- Q: Does ODM 8.5.1 support MQ 9.0? Does ODM 8.5.1 support MQ 9.0 where ODM Rule Execution Server is running on WAS 8.5.0.2 (embedded with ODM)? No MQ version is specified in ODM 8.5.1 System Requirements.
- gold: swg21312967 IBM MQ 7.x, MQ 8.0 and MQ 9.0 compatibility with previous versions - including usage of CCDT files, JMS .bindings, SSL/TLS - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is asking about the compatibility of ODM 8.5.1 with MQ 9.0, specifically when ODM Rule Execution Server is running on WAS 8.5.0.2. However, the provided sources do not contain any information related to this specific compatibility question. The sources discuss event support, virtual environment support, and interim fixes, but do not address the compatibility between ODM 8.5.1 and MQ 9.0, or the interaction with WAS 8.5.0.2.

## M-tune-009 - judge_veto J1 - unanswerable, correct

- Q: Is WebSphere Portal affected by the June 2015 leap second? Is WebSphere Portal affected by the leap second that will be inserted at the end of June 2015? Reference: http://en.wikipedia.org/wiki/Leap_second
- gold: None  (in evidence: False)
- vetoed: swg21701167 IBM Will the June 30, 2015 leap second impact IBM Sterling B2B Integrator (SBI)? - United States (is gold: False)
- reason: The source is about IBM Sterling B2B Integrator (SBI), not WebSphere Portal.

## M-tune-012 - judge_veto J4 - unanswerable, correct

- Q: Why do I get "error: The admin task reported the following: null" if uploading a DataPower scrypt3 firmware image file WAS 8.x DataPower Appliance Manager? How can I manage a set of DataPower appliances that shall run v7 firmware images by using WebSphere Application Server 8.x DataPower Appliance M
- gold: None  (in evidence: False)
- vetoed: swg21637997 IBM DataPower returns "Reflashing firmware failed" running scrypt tools with commands other than the "boot image" command - United States (is gold: False)
- reason: The source discusses a different error message and does not address the 'null' error during firmware upload.

## M-tune-013 - judge_veto J2 - answerable, correct

- Q: Help with Security Bulletin: Multiple vulnerabilities in IBM® Java SDK affect WebSphere Enterprise Service Bus (CVE-2015-2613) I would like to know details on how vulnerabilities in IBM Java SDK affect Websphere Application Server and in turn, Websphere Enterprise Service Bus product.
- gold: swg21965955 IBM Security Bulletin: Multiple vulnerabilities in IBM® Java SDK affect WebSphere Application Server that ships with WebSphere Enterprise Service Bus (CVE-2015-2613, CVE-2015-2601, CVE-2015-4749, CVE-2015-2625, CVE-2015-1931) - United States (in evidence: True)
- vetoed: swg21972124 IBM Security Bulletin: Multiple vulnerabilities in IBM® Java SDK affect WebSphere Application Server that ships with WebSphere Enterprise Service Bus (CVE-2015-4872,CVE-2015-4734, CVE-2015-5006 ) - United States (is gold: False)
- reason: The source discusses different CVEs than the ones mentioned in the question.

## M-tune-014 - judge_veto J4 - unanswerable, correct

- Q: Can CMS certificates be created with a keysize greater than 1024? We are trying to determine if a keysize can be greater than 1024. Any insight would be appreciated.
- gold: None  (in evidence: False)
- vetoed: swg1PK89833 IBM PK89833: WHEN USING SSL WITH CICS IF THE DEFAULT CERTIFICATE USED HAS A  PRIVATE KEY LENGTH OF GREATER THAN 1024 CICS ABENDS DFHXS0002. - United States (is gold: False)
- reason: The source discusses an error when using a key size greater than 1024, but does not directly answer whether CMS certificates can have such a key size.

## M-tune-014 - judge_veto J4 - unanswerable, correct

- Q: Can CMS certificates be created with a keysize greater than 1024? We are trying to determine if a keysize can be greater than 1024. Any insight would be appreciated.
- gold: None  (in evidence: False)
- vetoed: swg1PK89833 IBM PK89833: WHEN USING SSL WITH CICS IF THE DEFAULT CERTIFICATE USED HAS A  PRIVATE KEY LENGTH OF GREATER THAN 1024 CICS ABENDS DFHXS0002. - United States (is gold: False)
- reason: The source advises against using a key size greater than 1024 but does not directly answer whether CMS certificates can have such a key size.

## M-tune-015 - selection_empty  - answerable, wrong

- Q: SPSS will not start on Mac I downloaded SPSS about 3 weeks ago. On the day when I downloaded it, it was working fine. Last week, I tried starting SPSS but it did not start. I tried reinstalling it, it still would not open. I've updated JAVA (thought this would be a problem), it slowly opened the pro
- gold: swg21651225 IBM Performance issue on Mac OS X Launching and Closing SPSS Statistics 21 or 22. - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user's issue involves SPSS not starting at all, while the sources discuss problems like licensing issues, Java environment problems, and silent installation procedures. None of the sources directly address the issue where SPSS only shows the IBM SPSS name screen but does not proceed further.

## M-tune-016 - judge_veto J4 - unanswerable, correct

- Q: WAS 8.5.x - Writing a JMS message to a remote queue takes a long time. How to write the message faster? We are writing a jms message from a websphere cell (cellA) to a queue hosted by another websphere cell (cellB).Sometimes we noticed that writing a message is very slow. Usually when a local queue 
- gold: None  (in evidence: False)
- vetoed: swg21624731 IBM JMSExceptions CWSIT0006E and CWSIA0241E on bus connect - United States (is gold: False)
- reason: The source discusses JMS exceptions CWSIT0006E and CWSIA0241E, not the slow writing issue to a remote queue.

## M-tune-017 - selection_empty  - answerable, wrong

- Q: Is Java 8 supported for EJBDeploy on WebSphere Application Server 8.5.5.9 or later?
- gold: swg21994741 IBM Learning more about EJBDeploy - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The sources indicate that Java 8 is not supported for EJBDeploy on WebSphere Application Server 8.5.5.9 or later, as EJBDeploy does not run on Java 8 and the fix for this issue is not available in the specified version. The sources lack specific information confirming the support status for WebSphere Application Server 8.5.5.9 or later, only providing details for earlier versions or future updates.

## M-tune-018 - judge_veto J2 - unanswerable, correct

- Q: Help with Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with IBM WSRR (CVE-2017-1743) I need to understand details regarding Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with IBM WebSphere Service Registry and Repos
- gold: None  (in evidence: False)
- vetoed: swg21970119 IBM Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with IBM WebSphere Service Registry and Repository (CVE-2015-2017) - United States (is gold: False)
- reason: The source discusses CVE-2015-2017, not CVE-2017-1743.

## M-tune-020 - selection_empty  - answerable, wrong

- Q: Updating SCA applications & internal SCA module queues When updating an existing SCA module using the ISC, I noticed that internal SCA queues (sca/<module>/...) on the SCA.SYSTEM bus) are deleted and recreated. One can potentially loose messages on these queues. Is there a fix to the problem?
- gold: swg21639375 IBM SCA destinations for IBM Business Process Manager (BPM), WebSphere Process Server (WPS) and WebSphere Enterprise Service Bus (WESB) are not preserved when uninstalling and reinstalling a service module - United States (in evidence: True)
- vetoed:   (is gold: False)
- reason: The sources provided do not address the specific issue of internal SCA queues being deleted and recreated during module updates, nor do they discuss potential fixes for message loss. They primarily cover topics such as modifying retry values, managing stuck messages, and handling destination queues during module uninstallation and reinstallations. These sources lack relevant information to directly address the user's concern about preserving messages during updates.

## M-tune-021 - judge_veto J2 - answerable, wrong

- Q: ClassCastException IlrStorePolicy$SerializedENamedElement incompatible with EStructuralFeature We keep getting the following error when navigating in Decision Center on Websphere Application Server. java.lang.ClassCastException: ilog.rules.teamserver.web.IlrStorePolicy$SerializedENamedElement incomp
- gold: swg21268440 IBM Getting java.io.NotSerializableException when SessionObjectSize counter is enabled - United States (in evidence: False)
- vetoed: swg1JR29789 IBM JR29789: AVOID CLASS CAST EXCEPTION BY PROVIDING HEADER INFORMATION EARLIER IN THE START-UP PHASE - United States (is gold: False)
- reason: The source discusses a different ClassCastException with incompatible types.

## M-tune-022 - judge_veto J4 - answerable, wrong

- Q: HATS Plugin Download Hi I have RDZ 9.0 and want to install the HATS plugin. I've downloaded from this link: http://www.ibm.com/developerworks/downloads/ws/whats/ HATS 9.0.0.0 but it won't install because RDZ itself is not enough and it sais I need one of the following: IBM Rational Application Devel
- gold: swg24035040 IBM Rational Host Access Transformation Services 9.0 - United States (in evidence: False)
- vetoed: swg21444449 IBM Installing Rational Team Concert v2.x into the workbench in version 8.0 - United States (is gold: False)
- reason: The source is about installing Rational Team Concert and not about downloading a HATS plugin compatible with RDZ 9.0.

## M-tune-024 - judge_veto J4 - answerable, wrong

- Q: ITNM 4.2 Fix Pack 3 link and build number?. ITNM 4.2 FP3 is available, if yes then where we can download?.
- gold: swg24043575 IBM Tivoli Network Manager IP Edition 4.2.0 Fix Pack 3, 4.2.0-TIV-ITNMIP-FP0003 - United States (in evidence: True)
- vetoed: swg24043575 IBM Tivoli Network Manager IP Edition 4.2.0 Fix Pack 3, 4.2.0-TIV-ITNMIP-FP0003 - United States (is gold: True)
- reason: The source describes the fixes in ITNM 4.2 FP3 but does not provide the download link or build number.

## M-tune-026 - selection_empty  - answerable, wrong

- Q: Install path under "Program Files" My path for the OS agent is e:\Program Files\IBM. Is there any issues or underlying problems if I install under "Program Files"? Just want to make sure no issues with a "space" in the install path.
- gold: swg21961222 IBM Trouble installing ITM on Windows OS - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The sources provided do not address the specific issue of installing software in a path with a space, such as 'e:\Program Files\IBM'. Most of the sources discuss problems related to special characters or specific IBM products, but do not provide guidance on the general practice of installing software in directories with spaces in the path.

## M-tune-029 - judge_veto J4 - answerable, correct

- Q: What are the supported Macintosh Operating System versions for IBM SPSS Statistics 19, 20, 21, 22 and 23? I would like to know what are the supported Macintosh Operating system versions for IBM SPSS Statistics versions 18, 19, 20, 21, 22 and 23?
- gold: swg21507587 IBM What are the supported Apple Macintosh Operating System Versions for IBM SPSS Statistics? - United States (in evidence: True)
- vetoed: swg21507587 IBM What are the supported Apple Macintosh Operating System Versions for IBM SPSS Statistics? - United States (is gold: True)
- reason: The source does not provide supported OS versions for SPSS Statistics 18-23.

## M-tune-034 - judge_veto J4 - answerable, wrong

- Q: Does Logout button get disabled in ICM for SSO with Tivoli Access Manager ?
- gold: swg27042940 IBM Content Navigator known issue: In a SPNEGO/Kerberos Single sign-on environment, IBM Content Navigator the Log Out option is enabled - United States (in evidence: False)
- vetoed: swg21599394 IBM Configure IBM Case Manager for SSO with Tivoli Access Manager - United States (is gold: False)
- reason: The source does not mention the Logout button or its behavior in SSO with Tivoli Access Manager.

## M-tune-038 - judge_veto J2 - answerable, wrong

- Q: Why do we observe the transaction rollback errors J2CA0024E and DSRA0080E with Oracle 12c and how can we fix it? We are using BPM Advanced v8.5.6 in connection with the Oracle JDBC Driver 12.1.0.1.0. We observe many database transaction rollback exceptions: J2CA0024E: Method rollback, within transac
- gold: swg21690673 IBM Upgrading default JDBC drivers to Oracle 12c requires the definition of an additional JVM property in IBM Business Monitor - United States (in evidence: False)
- vetoed: swg1PK26490 IBM PK26490: JDBC EXCEPTION UNDER LOAD NO TRANSACTION AVAIL - United States (is gold: False)
- reason: The source describes a different error message DSRA0250E and J2CA0024E with a different context.

## M-tune-040 - selection_empty  - answerable, wrong

- Q: ICC Configuration Store Service is hung? ICC Configuration Store Service is hung and is not responding to start or stop commands. This was observed due to a potential issue with server running out of disk space. What is causing this?
- gold: swg21680391 IBM Content Collector Configuration Store is corrupted - United States (in evidence: True)
- vetoed:   (is gold: False)
- reason: The sources provided do not address the specific issue of the ICC Configuration Store Service hanging due to a potential server running out of disk space. Instead, they discuss various other IBM products and services, such as Content Collector, QRadar, and B2B Persistence, which do not directly relate to the user's question about the ICC Configuration Store Service.

## M-tune-041 - judge_veto J1 - answerable, wrong

- Q: Port number error starting 9.0 Launcher I'm attempting to start up v9.0 for the first time with one .msl file on a Windows server and get the following error. I also have v8.4 on this server and it starts fine. I do not have v8.4 running when I attempt to start v9.0. Cannot recognize if the system R
- gold: swg21986219 IBM Launcher failure when 'On Success' is set to Delete and 'On Failure' is set to Commit - United States (in evidence: False)
- vetoed: swg21976821 IBM The Transformation Extender Management Console is not able to communicate with the Launcher using IPv6 communication - United States (is gold: False)
- reason: The source is about a different product (Transformation Extender Management Console) and a different platform (Linux).

## M-tune-043 - judge_veto J4 - unanswerable, correct

- Q: Help with Security Bulletin: A security vulnerability has been identified in WebSphere Application Server shipped with WebSphere Remote Server (CVE-2014-8917) I need to understand details regarding Security Bulletin: A security vulnerability has been identified in WebSphere Application Server shippe
- gold: None  (in evidence: False)
- vetoed: swg21699940 IBM Security Bulletin: Security vulnerabilities have been identified in IBM WebSphere Application Server shipped with IBM WebSphere Portal - United States (is gold: False)
- reason: The source discusses multiple vulnerabilities but does not specifically address CVE-2014-8917.

## M-tune-045 - selection_empty  - answerable, wrong

- Q: Optim license We bought Optim 11.3, Test data management and data masking module.... I wonder how to get a Optim license?
- gold: swg21973794 IBM Optim, Optim Connect, ODM, and Optim zOS licensing - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is asking how to obtain an Optim 11.3 license, but the sources provided only contain detailed system requirements and installation instructions for various versions of IBM InfoSphere Optim Test Data Management Solution, which do not address the licensing process or where to purchase a license.

## M-tune-046 - judge_veto J4 - unanswerable, correct

- Q: When required, upgrade the IBM Installation Manager rather than install a new copy. During the installation of WebSphere Process Server (WPS) Fix Pack, or IBM Business Process Manager (BPM) Fix Pack, there may be requirement to use a newer version of IBM Installation Manager. What is the right metho
- gold: None  (in evidence: False)
- vetoed: swg21972788 IBM WebSphere Application Server or IBM Business Process Manager upgrade might fail with 'The system cannot find the path specified' errors - United States (is gold: False)
- reason: The source discusses upgrading IBM BPM and WebSphere Application Server, but does not provide specific steps for upgrading IBM Installation Manager.

## M-tune-049 - judge_veto J2 - answerable, wrong

- Q: How do I transfer my SPSS 24 license key to a new computer? I need to transfer my SPSS 24 license key to a new computer. I was able to download IBM® SPSS® Statistics Standard GradPack 24 for Windows (12-Mo Rental) onto the new computer, but every time I put in the activation code, I am met with this
- gold: swg21592093 IBM SPSS Student Version and Graduate Pack Resources - United States (in evidence: False)
- vetoed: swg21486099 IBM Why am I receiving a message with 'Error Code 201' and ' License generation failed'? - United States (is gold: False)
- reason: The source discusses Error Code 201 and 'License generation failed', not the 'Authorization failed' error mentioned.

## M-tune-050 - judge_veto J2 - answerable, wrong

- Q: Does DB2 DBMS implement NIST FIPS 140-2 validated cryptographic modules to provision digital signatures? V-58159 - SV-72589r1_rule says "The DBMS must implement NIST FIPS 140-2 validated cryptographic modules to provision digital signatures." Does DB2 UDB version 8 implement NIST FIPS 140-2 validate
- gold: swg21237078 IBM DB2 UDB Version 8, v10.5 compliance with FIPS 140-2 standard - United States (in evidence: True)
- vetoed: swg21237078 IBM DB2 UDB Version 8, v10.5 compliance with FIPS 140-2 standard - United States (is gold: True)
- reason: The source discusses FIPS 140-2 compliance but does not specifically mention cryptographic modules for digital signatures in DB2 UDB version 8.

## M-tune-054 - judge_veto J2 - answerable, wrong

- Q: Why does my upgrade to Portal 8001 CF14 fail with the following errors, ADMA5008E, ADMA0063E, ADMA5069E, WASX7017E?
- gold: swg21426787 IBM Portal upgrades fail during ejbdeploy with 'Error is Platform not running' message - United States (in evidence: True)
- vetoed: swg21681745 IBM Upgrade to Portal CF12 fails with errors ADMA5069E and CWLAA1031E and IWAE0037E - United States (is gold: False)
- reason: The source discusses errors ADMA5069E, CWLAA1031E, and IWAE0037E, which are different from the ones asked about.

## M-tune-056 - selection_empty  - answerable, wrong

- Q: Help with Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with WSRR (CVE-2017-1741) I need to understand details regarding Security Bulletin: Vulnerability identified in IBM WebSphere Application Server shipped with IBM WebSphere Service Registry and Repositor
- gold: swg22012345 IBM Security Bulletin: Potential Privilege Escalation in WebSphere Application Server Admin Console (CVE-2017-1731) - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The sources lack specific information about the recommended fix for the vulnerability identified in IBM WebSphere Application Server V9.0.0.0, which is the version the user is running. Most sources provide details for different versions (e.g., V8.5, V8.0) and do not address the exact version the user is using. Additionally, some sources refer to other vulnerabilities or do not contain actionable fix information.

## M-tune-057 - selection_empty  - answerable, wrong

- Q: Can I run different levels of the Rational Developer for z Systems host and client? I'd like to know if I can run different versions of the RDz client and host and if so what compatible or supported versions and releases?
- gold: swg21568844 IBM Developer for z Systems and Rational Developer for z Systems Backward/Forward compatibility - United States (in evidence: True)
- vetoed:   (is gold: False)
- reason: The sources provide information on compatibility and versioning between the Rational Developer for z Systems (RDz) host and client, but do not directly address whether different levels of the RDz host and client can be run simultaneously or the specific supported versions for this scenario. The sources focus more on client-server compatibility and version enhancements rather than concurrent version usage.

## M-tune-059 - selection_empty  - answerable, wrong

- Q: On 30th June, could the Leap Second cause Linux to freeze and impact my MQ?
- gold: swg21602521 IBM Leap Second bug in older Linux kernels may affect IBM MQ and WebSphere MQ - United States (in evidence: True)
- vetoed:   (is gold: False)
- reason: The user is specifically asking about the impact on Linux and IBM MQ on June 30th, 2015, but the sources discuss various IBM products and systems, including FileNet Content Manager and IBM Platform Computing, without addressing the specific concerns about Linux and IBM MQ on that date. Additionally, some sources mention potential issues with older Linux kernels, but do not provide clear information on whether modern Linux systems would freeze or impact MQ.

## M-tune-062 - judge_veto J2 - answerable, wrong

- Q: Need help accessing my SPSS access code? I downloaded SPSS GradPack (Standard) 25 6 Months for my Mac. The IBM SPSS Statistics 24 licensing page pops up for me to enter the code. I enter the code provided and then hit next, and it tells me the code is too short to be valid? What code do I use then? 
- gold: swg21592093 IBM SPSS Student Version and Graduate Pack Resources - United States (in evidence: True)
- vetoed: swg21989792 IBM License Activation Wizard for SPSS Statistics 24 crashes on MAC OS X 10.11.6 (El Capitan) preventing users to license the product - United States (is gold: False)
- reason: The source is about SPSS Statistics 24 and a different issue with the License Activation Wizard.

## M-tune-063 - judge_veto J4 - answerable, wrong

- Q: Unable to locate the More tab of Document class - Property definition tab - property template configuration to update Is Required setting. Unable to locate the More tab of Document class - Property definition tab - property template configuration to update Is Required setting. Environment is running
- gold: swg21696083 IBM How to overwrite property definition properties in a class via IBM Administration Console for Content Platform Engine (ACCE)? - United States (in evidence: True)
- vetoed: swg21977774 IBM 'Audit As' property missing in Property Definition object in Administration Console for Content Platform Engine (ACCE). - United States (is gold: False)
- reason: The source discusses a different issue and does not provide steps to update the 'Is Required' setting.

## M-tune-065 - judge_veto J1 - unanswerable, correct

- Q: Security Bulletin: XXE injection vulnerability in IBM API Connect (CVE-2017-1322) I need to understand details regarding Security Bulletin: XXE injection vulnerability in IBM API Connect (CVE-2017-1322). Where can I find this information?
- gold: None  (in evidence: False)
- vetoed: swg22013432 IBM Security Bulletin: IBM Transformation Extender Advanced is Potentially Vulnerable to an XML External Entity (XXE) Injection in its REST API. - United States (is gold: False)
- reason: The source is about IBM Transformation Extender Advanced, not IBM API Connect.

## M-tune-066 - judge_veto J2 - answerable, wrong

- Q: Will Datacap support Windows 10, if so, which version is fully supported? We want to if Datacap support windows 10, if so, which version supports it. Please provide us official statement for the compatibility.
- gold: swg27047895 IBM Datacap 9.0.1 FP1 - Readme doc - United States (in evidence: False)
- vetoed: swg27020397 IBM System Requirements: Hardware and Software Requirements for IBM Datacap Taskmaster Capture Version 8.0 - United States (is gold: False)
- reason: The source lists supported operating systems but does not mention Windows 10.

## M-tune-068 - judge_veto J3 - answerable, wrong

- Q: DB2 Non Reclaimable Storage . We have tablespaces defined under DB2 9.5 that apparently are not able to reclaim storage back to the OS, but does that mean DB2 cannot reuse this space as well?
- gold: swg21438047 IBM SQL1763N error with Reason Code 11 while running "Alter Tablespace" command to reclaim unused storage space against DMS or automatic storage tablespaces. - United States (in evidence: True)
- vetoed: swg21655828 IBM Reducing the size of the Tivoli Storage Manager database - United States (is gold: False)
- reason: The source explicitly excludes DB2 9.5 and focuses on DB2 9.7.

## M-tune-070 - judge_veto J2 - answerable, wrong

- Q: Why can't I connect to HTTPS server using Installation Manager 1.7.2? When using IBM Installation Manager 1.7.2 to connect to a HTTPS server, I get the following message: The following repositories are not connected: https://www.ibm.com/software/repositorymanager/service/com.ibm. websphere.ND.v85/8.
- gold: swg21688071 IBM Installation Manager 1.7.3.1 or older cannot connect to HTTPS servers that have SSL security protocol disabled - United States (in evidence: False)
- vetoed: swg21685035 IBM NullPointerException error received when installing WebSphere Application Server Liberty profile - United States (is gold: False)
- reason: The source discusses a NullPointerException error, not the HTTPS connection issue with a 404 error.

## M-tune-072 - judge_veto J4 - unanswerable, correct

- Q: Datacap Navigator Verify When i run a Batch for Verification in Datacap Navigator.. Fields are not getting displayed .. same fields can be seen in tmweb. How do I access the client log in Internet Explorer?
- gold: None  (in evidence: False)
- vetoed: swg22005014 IBM Can different clients (eg: TMWeb, Datacap Navigator, DCDesktop, etc..) be used in the same task with IBM Datacap product? - United States (is gold: False)
- reason: The source discusses using different clients for the same task but does not provide steps to access the client log in Internet Explorer.

## M-tune-074 - judge_veto J4 - unanswerable, correct

- Q: We specify the sslProtocol for an Execution Group via "-n sslProtocol -v TLS" as per following: mqsichangeproperties "-o HTTPSConnector" "-n sslProtocol -v TLS" Does WMB support TLS v1.1 protocol or TLS v1.2?
- gold: None  (in evidence: False)
- vetoed: swg1PI40215 IBM PI40215: NOT ABLE TO ENABLE TLSV1.1 AND TLSV1.2 PROTOCOLS FOR HTTPSCONNECTOR IN 8.0.0.4 - United States (is gold: False)
- reason: The source discusses enabling TLS v1.1 and TLS v1.2 but does not explicitly state WMB's support for these versions.

## M-tune-076 - selection_empty  - answerable, wrong

- Q: Does JazzSM 1.1.2.1 support HTTP access?
- gold: swg21974566 IBM Configuring access for HTTP and HTTPS in Jazz for Service Management - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The provided sources do not address whether JazzSM 1.1.2.1 supports HTTP access. The sources discuss various issues, workarounds, and prerequisites related to JazzSM, but none directly confirm or deny HTTP support for the specified version.

## M-tune-077 - judge_veto J2 - unanswerable, correct

- Q: In WebSphere MQ, why am I getting AMQ9776, AMQ9777 Channel was blocked errors? In WebSphere MQ, why am I getting AMQ9776, AMQ9777 Channel was blocked errors
- gold: None  (in evidence: False)
- vetoed: swg1IT12825 IBM IT12825: IBM MQV8: A CLIENT APPLICATION FAILS TO CONNECT TO A QUEUE MANAGER WITH ERROR AMQ9777: CHANNEL WAS BLOCKED. - United States (is gold: False)
- reason: The source only discusses AMQ9777 and does not mention AMQ9776.

## M-tune-077 - judge_veto J2 - unanswerable, correct

- Q: In WebSphere MQ, why am I getting AMQ9776, AMQ9777 Channel was blocked errors? In WebSphere MQ, why am I getting AMQ9776, AMQ9777 Channel was blocked errors
- gold: None  (in evidence: False)
- vetoed: swg1IT12825 IBM IT12825: IBM MQV8: A CLIENT APPLICATION FAILS TO CONNECT TO A QUEUE MANAGER WITH ERROR AMQ9777: CHANNEL WAS BLOCKED. - United States (is gold: False)
- reason: The source only discusses AMQ9777 and does not mention AMQ9776.

## M-tune-079 - judge_veto J4 - answerable, wrong

- Q: How to get the ODM 8.5.1.2 fixpack of ODM 8.5.1.1? ODM 8.5.1.2 fixpack is not listed in Fix Central when installed platform ODM 8.5.1.1 is used: http://www-933.ibm.com/support/fixcentral/swg/selectFixes?parent=ibm~WebSphere&product=ibm/WebSphere/WebSphere+Operational+Decision+Management&release=8.5.
- gold: swg24039235 IBM Operational Decision Manager V8.5.1.2 Fix Pack - United States (in evidence: True)
- vetoed: swg24039235 IBM Operational Decision Manager V8.5.1.2 Fix Pack - United States (is gold: True)
- reason: The source does not provide steps to obtain the specific fixpack for ODM 8.5.1.1.

## M-tune-080 - judge_veto J1 - answerable, wrong

- Q: Why Plug-in log file reports an error message after install & configure the WebSphere Plugin 8.5 version on a Apache 2.4 webserver. During web server start-up, errors like the following will be logged into the Plug-in log file (http_plugin.log): ERROR: lib_security: loadSecurityLibrary: Failed to lo
- gold: swg21600618 IBM web server Plugin may need LD_LIBRARY_PATH when used with Apache 2.2 - United States (in evidence: True)
- vetoed: swg21600618 IBM web server Plugin may need LD_LIBRARY_PATH when used with Apache 2.2 - United States (is gold: True)
- reason: The source is about Apache 2.2, not Apache 2.4 as asked.

## M-tune-081 - selection_empty  - unanswerable, correct

- Q: Why does the other instance of my multi-instance qmgr seem to hang after a failover?
- gold: None  (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is experiencing an issue with a hanging instance after a failover in a multi-instance qmgr setup, likely related to message selectors or automatic client reconnects. However, the provided sources primarily discuss issues with selectors, poison messages, and failover scripts, without directly addressing why an instance might hang after a failover. The sources lack specific information on hang conditions or troubleshooting steps for hanging instances in multi-instance qmgr scenarios.

## M-tune-082 - judge_veto J2 - unanswerable, correct

- Q: Why Summarization and pruning are failing with SQL Error Code = -4220 on AIX_LPAR table?
- gold: None  (in evidence: False)
- vetoed: swg21595240 IBM UDA-SQL-0196 The table or view "System_DV" was not found - United States (is gold: False)
- reason: The source discusses SQL Error Code -286, not -4220.

## M-tune-082 - judge_veto J2 - unanswerable, correct

- Q: Why Summarization and pruning are failing with SQL Error Code = -4220 on AIX_LPAR table?
- gold: None  (in evidence: False)
- vetoed: swg21595240 IBM UDA-SQL-0196 The table or view "System_DV" was not found - United States (is gold: False)
- reason: The source discusses SQL Error Code -286, not -4220.

## M-tune-084 - judge_veto J4 - answerable, wrong

- Q: How precise is DataPower's backside persistent timeout value related to intermittent "Failed to Process Response Headers" error messages? I have a service on DataPower with a backside persistent timeout value set to 28 seconds. The actual backend device has a persistent timeout setting of 30 seconds
- gold: swg21292808 IBM How to troubleshoot the error "Failed to process response headers" - United States (in evidence: True)
- vetoed: swg21673208 IBM Why does DataPower report that WebSphere Application Server terminated the connection? - United States (is gold: False)
- reason: The source discusses a different configuration scenario and does not address the specific timeout mismatch described.

## M-tune-086 - judge_veto J4 - unanswerable, correct

- Q: What is right trace for investigate the "CWTKE0021W: The expired people assignment (staff query result) cannot be refreshed" in SystemOut.log Hello, after upgrading from Websphere Process Server 7 to Business Process Manager Advanced - Process Server 8.5.6 we are seeing many CWTKE0021W in the System
- gold: None  (in evidence: False)
- vetoed: swg27017046 IBM Open Mic Replay: Troubleshooting WTX, BPE, and EDI in WebSphere Partner Gateway Open Mic - United States (is gold: False)
- reason: The source is about troubleshooting WTX, BPE, and EDI in WebSphere Partner Gateway and does not provide information on the 'CWTKE0021W' error or trace strings.

## M-tune-088 - judge_veto J3 - answerable, wrong

- Q: Why is RPT script for secure application failing during RRT agent playback with URL Unavailable ? In the ITCAM for Transactions, Robotic Response Time agent (t6) - the Rational Performance Tester (RPT) scripts playback is failing for specific secure applications (ones that use https). The scripts wh
- gold: swg21960133 IBM Does the RRT agent support TLS 1.1/1.2 and 256-bit ciphers? - United States (in evidence: False)
- vetoed: swg21608733 IBM RRT fails to playback RPT script with certificate - United States (is gold: False)
- reason: The source discusses a different issue related to client certificates, not the URL Unavailable failure.

## M-tune-089 - judge_veto J4 - answerable, wrong

- Q: Updating SCA applications & internal SCA module queues When updating an existing SCA module using the ISC, I noticed that internal SCA queues (sca/<module>/...) on the SCA.SYSTEM bus) are deleted and recreated. Does this mean that any messages that may still reside on these internal queues would be 
- gold: swg21639375 IBM SCA destinations for IBM Business Process Manager (BPM), WebSphere Process Server (WPS) and WebSphere Enterprise Service Bus (WESB) are not preserved when uninstalling and reinstalling a service module - United States (in evidence: False)
- vetoed: swg21675200 IBM Proper shutdown sequence for SCA applications using WebSphere SAP Adapter in inbound mode in case of planned outages - United States (is gold: False)
- reason: The source discusses pausing SAP Adapter endpoints and does not address SCA module updates or internal queue behavior.

## M-tune-095 - judge_veto J2 - unanswerable, correct

- Q: Upgrade of IBM Integration Designer fails I tried upgrading IID from 7.5.1.0 to 7.5.1.2 using the online repository via an Internet connection. An error is thrown in Installation Manager and the upgrade fails: CRIMC1029E: failed to add module com.ibm.ram.rich.core_7.2.2.v20100224_0426 in warehouse C
- gold: None  (in evidence: False)
- vetoed: swg21598812 IBM "Failed to add the plugin"and "The download retry failed" errors when installing on Windows - United States (is gold: False)
- reason: The source discusses a different error and a different product (Data Tools Platform for SAP MaxDB).

## M-tune-101 - selection_empty  - answerable, wrong

- Q: Portal v8.5 install fails with INSTCONFFAILED - No Portral logs are written
- gold: swg1PI37248 IBM PI37248: A PROPERTY FILE BASED CONFIGURATION (PFBC) FILE MIGHT FAIL TO AP PLY. - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is facing an issue with Portal v8.5 installation failing with INSTCONFFAILED, and none of the provided sources directly address this specific issue. The sources discuss various IBM products and issues like Tivoli Integrated Portal, WebSphere, and Rational Web Platform, but do not provide relevant troubleshooting steps or solutions for Portal v8.5 specifically.

## M-tune-102 - judge_veto J2 - answerable, wrong

- Q: Non-admin users cannot access webDAV filestore. What is the likely reason? A non-admin user trying to access the webDAV filestore is unable to do so and they see the below exception in the portal logs: Caused by: com.ibm.icm.da.DBAccessException: User id can not be null at com.ibm.icm.da.portable.co
- gold: swg21664629 IBM Policy (EJQAB0067E) and JCR Login (WSP0005E) exceptions in System*.logs - United States (in evidence: True)
- vetoed: swg21664629 IBM Policy (EJQAB0067E) and JCR Login (WSP0005E) exceptions in System*.logs - United States (is gold: True)
- reason: The source discusses different exceptions (EJQAB0067E and WSP0005E) not related to the DBAccessException mentioned in the question.

## M-tune-103 - judge_veto J2 - unanswerable, correct

- Q: WebSphere Adapter for JDBC receives DB2 SQL Error: SQLCODE=-104 WebSphere Adapter for JDBC throws an exception when executing a retrieveAll operation against a z/OS mainframe DB2 database. The following error message is seen when WebSphere Adapter for JDBC executes a retrieveAll operation against a 
- gold: None  (in evidence: False)
- vetoed: swg21638737 IBM JDBC Adapter V7.5 - RetrieveAll operation throws ResourceException: Resource Adapter instance is NULL - United States (is gold: False)
- reason: The source discusses a different error (ResourceException: Resource Adapter instance is NULL) and does not mention SQLCODE=-104.

## M-tune-105 - selection_empty  - answerable, wrong

- Q: ICO's Roadmap of supporting next OpenStack versions Hello, ICO 2.5.0.2 is compatible with OpenStack kilo, is there a plan making it work with OpenStack Liberty/Mitika ? Would you share any information or link about the roadmap, please? Thanks in advance.
- gold: swg2C1000132 IBM Cloud Orchestrator (ICO) continues to be a strategic solution for IBM - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The provided sources focus on specific issues and documentation errors related to IBM Cloud Orchestrator (ICO) and OpenStack, but do not address the user's query about the roadmap for supporting OpenStack Liberty/Mitaka versions. The sources mainly discuss pre-check failures and naming conventions, rather than providing a roadmap or timeline for compatibility updates.

## M-tune-106 - selection_empty  - answerable, wrong

- Q: Is Internet Explorer 11 supported by Lombardi 7.2.XX We are using Lombardi 7.2.0.5 version. We are planning to upgrade Internet Explorer to IE 11 version. Is IE 11 supported? Are there any known issues?
- gold: swg27023007 IBM Business Process Manager Standard detailed system requirements - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The sources provided do not specifically address support for Internet Explorer 11 with Lombardi 7.2.XX. They discuss support for IE 11 with other IBM products like BPF, Case Manager, Connections, and Datacap, but do not provide information relevant to Lombardi 7.2.0.5.

## M-tune-107 - selection_empty  - answerable, wrong

- Q: What is the equivalent of the .LG0 file for the OS agent - A4 - on i5 systems?
- gold: swg21657023 IBM Pdcollect tool for ITM IBM i OS agent - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is asking for the equivalent of the .LG0 file for the OS agent - A4 on i5 systems, but the provided sources discuss topics such as Event Integration Facility (EIF) support, private situation errors, agent installation issues, and log collection settings. None of these sources address the specific .LG0 file equivalent for the OS agent - A4 on i5 systems.

## M-tune-109 - judge_veto J4 - unanswerable, correct

- Q: Why cant I load and AEL when using IE 11 JRE 8 Application Blocked by Java Security
- gold: None  (in evidence: False)
- vetoed: swg21987920 IBM Unable to open AEL from TIP console - United States (is gold: False)
- reason: The source does not describe the cause of the Java Security block or provide a direct fix for loading AEL in IE 11 with JRE 8.

## M-tune-111 - judge_veto J2 - answerable, wrong

- Q: 1040ez 9.0 Application Hi I have downloaded sample Datacap 9 applications (1040ez, Express, Survey) using below link and copied in my local system C:\Datacap and added reference in Datacap.xml file. IBM Datacap 9.0 and IBM Datacap 9.0.1 DDK sample applications But i'm unable to login Datacap Studio 
- gold: swg21968549 IBM Couldn't validate parameters error logging in with IBM Datacap - United States (in evidence: False)
- vetoed: swg21675631 IBM TMWeb cannot connect to the Admin DB in IBM Datacap Taskmaster - United States (is gold: False)
- reason: The source discusses a different error related to 'Unable to logon to Admin DB' which is not the same as the user's login issue.

## M-tune-112 - selection_empty  - unanswerable, correct

- Q: BPM v8012 is compatible with oracle 12c or 11.2.0.4? Does anyone know if BPM v8012 is compatible with Oracle 12c or 11.2.0.4?
- gold: None  (in evidence: False)
- vetoed:   (is gold: False)
- reason: The sources provided do not specifically address the compatibility of IBM BPM v8012 with Oracle 12c or Oracle 11.2.0.4. Most of the sources discuss compatibility with other IBM products or Oracle versions, and one source mentions a fix for IBM BPM V8.5.0.2 with Oracle 12c, but does not directly address BPM v8012.

## M-tune-113 - judge_veto J4 - answerable, wrong

- Q: Can I change the ITCAM J2EE Agent Monitoring Level via the TEPS in version 7.1.1? In the 7.1 version of the J2EE agent I could use the Agent Configuration to change the Monitoring Level for the agent- https://www.ibm.com/support/knowledgecenter/en/SS3JRN_7.2.0/com.ibm.itcamfapps_ad.doc_72/J2EE_agent
- gold: swg21700308 IBM Modifying the default Monitoring Level and Sampling Rate in the J2EE v7.1.1.0.0 agent. - United States (in evidence: False)
- vetoed: swg21689678 IBM The ITCAM Agent for J2EE 7.1.1 Installation and Customization Guide? - United States (is gold: False)
- reason: The source does not provide information on changing the Monitoring Level in version 7.1.1.

## M-tune-113 - judge_veto J4 - answerable, wrong

- Q: Can I change the ITCAM J2EE Agent Monitoring Level via the TEPS in version 7.1.1? In the 7.1 version of the J2EE agent I could use the Agent Configuration to change the Monitoring Level for the agent- https://www.ibm.com/support/knowledgecenter/en/SS3JRN_7.2.0/com.ibm.itcamfapps_ad.doc_72/J2EE_agent
- gold: swg21700308 IBM Modifying the default Monitoring Level and Sampling Rate in the J2EE v7.1.1.0.0 agent. - United States (in evidence: False)
- vetoed: swg21689680 IBM The ITCAM Agent for J2EE 7.1.1 User's Guide - United States (is gold: False)
- reason: The source does not provide information on changing the Monitoring Level in version 7.1.1.

## M-tune-114 - judge_veto J2 - answerable, correct

- Q: Help with Security Bulletin: Multiple Vulnerabilities identified in IBM Java SDK affect WSRR and WSRR Studio I need to understand details regarding Security Bulletin: Multiple Vulnerabilities identified in IBM® Java SDK affect WebSphere Service Registry and Repository and WebSphere Service Registry 
- gold: swg22013955 IBM Security Bulletin: Multiple Vulnerabilities identified in IBM® Java SDK affect WebSphere Service Registry and Repository and WebSphere Service Registry and Repository Studio - United States (in evidence: True)
- vetoed: swg22016430 IBM Security Bulletin: Multiple Vulnerabilities identified in IBM® Java SDK affect WebSphere Service Registry and Repository and WebSphere Service Registry and Repository Studio - United States (is gold: False)
- reason: The source discusses different CVE IDs (CVE-2018-2783, CVE-2018-2800) not requested by the user.

## M-tune-116 - judge_veto J4 - answerable, wrong

- Q: fixlets do not appear in console bigfix Work with ILTM 9.2.7 / 9.5.4.38. In the bigfix console the fixlets do not appear, under the tree: Sites-> IBM License Reporting (ILTM) v9 -> Fixlets and Task. Attached image. Do you have any ideas? Greetings and thank you BigFix
- gold: swg21974546 IBM BigFix Server unable to gather site content from sync.bigfix.com (error: Unexpected HTTP response: 404) - United States (in evidence: False)
- vetoed: swg21995031 IBM Security Bulletin: Vulnerability in password strength policy affects IBM License Metric Tool v9.x and IBM BigFix Inventory v9.x (CVE-2016-8962) - United States (is gold: False)
- reason: The source discusses a security vulnerability and does not address the issue of fixlets not appearing in the console.

## M-tune-118 - judge_veto J3 - answerable, wrong

- Q: Why does DSM error log have errors for SQLCODE=-206 errors reported for ISAS core warehouse database?
- gold: swg21983739 IBM Data Server Manager (DSM) showing SQLCODE=-206 "<name> is not valid in the context where it is used." - United States (in evidence: True)
- vetoed: swg21983739 IBM Data Server Manager (DSM) showing SQLCODE=-206 "<name> is not valid in the context where it is used." - United States (is gold: True)
- reason: The source does not describe the cause of SQLCODE=-206 errors in DSM error logs.

## M-tune-119 - judge_veto J2 - answerable, wrong

- Q: Does ITCAM for MQ monitoring agent (kmq) use SYSTEM.MQXR.COMMAND.QUEUE causing Unknown Object Name [2085] event? Using the ITCAM MQ Monitoring agent, we have a situation that generates alerts when a 2085 event (object unknown) occurs. We have recently seen alerts for the queue SYSTEM.MQXR.COMMAND.QU
- gold: swg21318303 IBM Identify the application that has a WMQ queue opened - United States (in evidence: False)
- vetoed: swg1IV86027 IBM IV86027: UNKNOWN OBJECT NAME EVENT IS GENERATED DUE TO KMQ.IRA.AGENT.QUEUE - United States (is gold: False)
- reason: The source mentions a different queue (KMQ.IRA.AGENT.QUEUE) and does not discuss SYSTEM.MQXR.COMMAND.QUEUE.

## M-tune-120 - judge_veto J4 - unanswerable, correct

- Q: How to download IBM MQ ? How and where to download IBM MQ V8 or IBM Websphere MQ V7.1 or 7.5 for production environment ?
- gold: None  (in evidence: False)
- vetoed: swg21687382 IBM Identifying Windows 32-bit and 64-bit systems - United States (is gold: False)
- reason: The source discusses identifying 32-bit vs 64-bit systems and does not provide download instructions for IBM MQ V8 or IBM Websphere MQ V7.1 or 7.5.

## M-tune-123 - selection_empty  - unanswerable, correct

- Q: Why are replies going to the DLQ with reason 2189 MQRC_CLUSTER_RESOLUTION_ERROR I have changed my cluster receiver to match the IP address used and now I am seeing replies in my DLQ with 2189 MQRC_CLUSTER_RESOLUTION_ERROR. The reply queue is on a different cluster which this qmgr is a member of. The
- gold: None  (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is experiencing replies going to the DLQ with reason code 2189 MQRC_CLUSTER_RESOLUTION_ERROR, despite having the correct cluster receiver setup. The sources provided discuss issues related to QAlias base queue resolution, COD messages, and DLQ handling in different contexts, but do not address the specific issue of MQRC_CLUSTER_RESOLUTION_ERROR in the context of reply queues and cluster membership.

## M-tune-125 - judge_veto J2 - answerable, wrong

- Q: ITMv6 issue: Cognos reports run for an extended period, sometimes never finishes
- gold: swg21585678 IBM Increasing Java Heap Memory in IBM Tivoli Common Reporting 2.1/2.1.1 - United States (in evidence: False)
- vetoed: swg1IT23603 IBM IT23603: COGNOS NEVER FINISHES STARTING - United States (is gold: False)
- reason: The source discusses Cognos never finishing starting, not reports running indefinitely.

## M-tune-126 - selection_empty  - answerable, wrong

- Q: Does Linux KVM monitoring agent support CANDLEDATA function? Does Linux KVM monitoring agent in ITM support CANDLEDATA function?
- gold: swg21695194 IBM IV67523 Move local data from CANDLEHOME to another file system - United States (in evidence: True)
- vetoed:   (is gold: False)
- reason: The provided sources do not address the specific question about whether the Linux KVM monitoring agent supports the CANDLEDATA function, either in ITM or in general. The sources discuss CANDLEDATA in the context of IBM Tivoli Monitoring and other agents, but do not provide clear information on the Linux KVM agent's compatibility with CANDLEDATA.

## M-tune-131 - judge_veto J4 - answerable, wrong

- Q: Is it possible to monitor Memory/LPAR metrics using ITM HMC agent? I understand the ITM AIX Premium agent captures these metrics but like to know if it is possible to monitor Memory/LPAR metrics using ITM HMC agent?
- gold: swg24042283 IBM Tivoli Monitoring: HMC Base Agent 6.2.2.3-TIV-ITM_HMC_BASE-IF0004 - United States (in evidence: False)
- vetoed: swg21683210 IBM SystemP agents on AIX 7.1 TL3 - United States (is gold: False)
- reason: The source discusses the HMC Base agent but does not specify if it can monitor Memory/LPAR metrics.

## M-tune-131 - judge_veto J4 - answerable, wrong

- Q: Is it possible to monitor Memory/LPAR metrics using ITM HMC agent? I understand the ITM AIX Premium agent captures these metrics but like to know if it is possible to monitor Memory/LPAR metrics using ITM HMC agent?
- gold: swg24042283 IBM Tivoli Monitoring: HMC Base Agent 6.2.2.3-TIV-ITM_HMC_BASE-IF0004 - United States (in evidence: False)
- vetoed: swg21683210 IBM SystemP agents on AIX 7.1 TL3 - United States (is gold: False)
- reason: The source discusses the HMC Base agent but does not specify if it can monitor Memory/LPAR metrics.

## M-tune-132 - judge_veto J4 - answerable, wrong

- Q: WAS 8.5.x - Writing a JMS message to a remote queue takes a long time. How to write the message faster? We are writing a jms message from a websphere cell (cellA) to a queue hosted by another websphere cell (cellB). Sometimes we noticed that writing a message is very slow. Usually when a local queue
- gold: swg21624731 IBM JMSExceptions CWSIT0006E and CWSIA0241E on bus connect - United States (in evidence: True)
- vetoed: swg21624731 IBM JMSExceptions CWSIT0006E and CWSIA0241E on bus connect - United States (is gold: True)
- reason: The source discusses JMS exceptions CWSIT0006E and CWSIA0241E, not the slow writing issue.

## M-tune-134 - judge_veto J4 - answerable, wrong

- Q: What are the known issues with WILY software and WAS or BPM?
- gold: swg21966881 IBM Business Process Manager users receive errors that session has expired - United States (in evidence: True)
- vetoed: swg27021737 IBM Release Notes - IBM Business Process Manager Healthcare Pack version 7.5 - United States (is gold: False)
- reason: The source discusses system requirements and installation instructions for BPM Healthcare Pack v7.5, but does not mention known issues related to WILY software or WAS.

## M-tune-138 - selection_empty  - answerable, wrong

- Q: TWS / DWC and WebSphere 8.5.5.4+ WebSphere for TWS & DWC were upgraded to 8.5.5.4 on most servers in a particular environment. However, any TWS servers that still had 8.5.5.2, could no longer be seen by the new DWC / WAS 8.5.5.4 servers. Those lower WAS version engines could not be added to the DWC.
- gold: swg21964202 IBM How Connect TDWC 9.3 to TWS Engine lower level release - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is facing issues with TWS servers running 8.5.5.2 not being able to communicate with DWC and WAS 8.5.5.4 servers, which is causing AWSUI0833E and AWSJCO005E errors. However, the sources provided mainly discuss issues related to different versions, security configurations, and alternate plans, without addressing the specific communication failure between servers of different versions.

## M-tune-139 - judge_veto J4 - answerable, wrong

- Q: Latest deployed ruleset not executing in clustered environment We are using ODM 8.7.0.1 and are running into an issue in our clustered environment. After deploying an updated to the ruleapp, using "Replace RuleApp Version" versioning policy, the that the decision service is still executing the previ
- gold: swg21598779 IBM An unexpected ruleset version is executed - United States (in evidence: False)
- vetoed: swg21663707 IBM Decision Center utility Ant tasks - United States (is gold: False)
- reason: The source describes deployment attributes and policies but does not address the issue of the latest deployed ruleset not executing in a clustered environment.

## M-tune-140 - judge_veto J1 - unanswerable, correct

- Q: Is IIBv9x affected by vulnerability CVE-2016-6304? This Q&A is abstracted from a PMR I would like to know if IIBv9x is affected by vulnerability CVE-2016-6304. There was a report that Open SSL vulnerabilities were included in IIB but I could not find anything regarding specifically for CVE-2016-6304
- gold: None  (in evidence: False)
- vetoed: swg22002870 IBM Security Bulletin: Vulnerabilities in OpenSSL affect the BigFix Platform (CVE-2016-2177 CVE-2016-6304 CVE-2016-6305 CVE-2016-2182 CVE-2016-6306 CVE-2016-2183) - United States (is gold: False)
- reason: The source is about BigFix Platform, not IIBv9x.

## M-tune-141 - judge_veto J2 - answerable, wrong

- Q: java.lang.IllegalStateException when I'm trying to stop a service in BPM Process Admin Console In the Process Admin Console, under Monitoring > Process Monitor, when I try to stop a service, I get the following exception: java.lang.IllegalStateException: SRVE0199E: OutputStream already obtained What
- gold: swg21282614 IBM TroubleShooting: JavaServer Pages (JSP) problems - United States (in evidence: False)
- vetoed: swg1PK22134 IBM PK22134: JAVA.LANG.ILLEGALSTATEEXCEPTION-SRVE0199E-OUTPUTSTREAM ALREADY O BTAINED, WHEN PRINT/EXPORT (AS PDF) IS DONE IN JSP WITH CR - United States (is gold: False)
- reason: The source describes a different error related to JSP and Crystal Reports, not BPM Process Admin Console.

## M-tune-141 - judge_veto J2 - answerable, wrong

- Q: java.lang.IllegalStateException when I'm trying to stop a service in BPM Process Admin Console In the Process Admin Console, under Monitoring > Process Monitor, when I try to stop a service, I get the following exception: java.lang.IllegalStateException: SRVE0199E: OutputStream already obtained What
- gold: swg21282614 IBM TroubleShooting: JavaServer Pages (JSP) problems - United States (in evidence: False)
- vetoed: swg1PK22134 IBM PK22134: JAVA.LANG.ILLEGALSTATEEXCEPTION-SRVE0199E-OUTPUTSTREAM ALREADY O BTAINED, WHEN PRINT/EXPORT (AS PDF) IS DONE IN JSP WITH CR - United States (is gold: False)
- reason: The source describes a different error related to JSP and Crystal Reports, not BPM Process Admin Console.

## M-tune-142 - selection_empty  - answerable, wrong

- Q: XGS 5.3.0.6: Is there a way to replicate an inspection object under the same policy repository? Is there a way to replicate an inspection object under the same policy repository?
- gold: swg21902778 IBM Security Network Protection firmware 5.3.1 release notes - United States (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is asking about replicating an inspection object under the same policy repository, but the provided sources focus on policy migration, integration, and differences between different security systems. They do not address how to replicate inspection objects within the same repository.

## M-tune-147 - selection_empty  - unanswerable, correct

- Q: Why are data source connections to Microsoft SQL Server failing after upgrading WebSphere Application Server? WebSphere Application Server v7 and Java SDK were updated to Fix Pack v7.0.0.37. Afterward, all data source connections to Microsoft SQL Server failed.
- gold: None  (in evidence: False)
- vetoed:   (is gold: False)
- reason: The user is experiencing issues with data source connections to Microsoft SQL Server after upgrading WebSphere Application Server, specifically with connection failures. However, the provided sources discuss various unrelated issues such as mapping SQL exceptions, JDBC driver compatibility, and stored procedure installations. None of the sources directly address the connection failure issue after the upgrade.

## M-tune-150 - judge_veto J1 - answerable, wrong

- Q: Does DataPower support SHA-2? Is DataPower able to support SHA-2 (SHA256)? 1
- gold: swg21406783 IBM When a Certificate Authority (CA) signs a certificate using SHA2(SHA-256), IBM Websphere DataPower SOA Appliance can validate the signature of CA on certificate. - United States (in evidence: False)
- vetoed: swg1PJ41598 IBM PJ41598: IMAGE SERVICES (IS) 4.2.0 NEEDS TO SUPPORT FIPS SHA-256 - United States (is gold: False)
- reason: The source is about Image Services (IS) 4.2.0, not DataPower.

## M-tune-150 - judge_veto J1 - answerable, wrong

- Q: Does DataPower support SHA-2? Is DataPower able to support SHA-2 (SHA256)? 1
- gold: swg21406783 IBM When a Certificate Authority (CA) signs a certificate using SHA2(SHA-256), IBM Websphere DataPower SOA Appliance can validate the signature of CA on certificate. - United States (in evidence: False)
- vetoed: swg1PJ41664 IBM PJ41664: IMAGE SERVICES (IS) 4.2.0 NEEDS TO SUPPORT FIPS SHA-256 - United States (is gold: False)
- reason: The source is about Image Services (IS) 4.2.0, not DataPower.
