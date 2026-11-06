# 答案文档在证据里、选证据却没选中（tune_real_e8_base, tune_real_e8_q72, tune_real_e8_l70, tune_real_e8_gpt）

共 28 道；在全部 4 个运行里都没选中：6 道。

## M-tune-062（4/4 个运行）

- 问题：Need help accessing my SPSS access code? I downloaded SPSS GradPack (Standard) 25 6 Months for my Mac. The IBM SPSS Statistics 24 licensing page pops up for me to enter the code. I enter the code provided and then hit next, and it tells me the code is too short to be valid? What code do I use then? I need this resolved fast, my first assignment is due soon. I was only given a 16-digit access code,
- 答案文档：swg21592093 IBM SPSS Student Version and Graduate Pack Resources - United States
- **tune_real_e8_base**：答案文档在 S3；选了 ['swg21989792 IBM License Activation Wizard for SPSS Statistics 24 crashes on MAC OS X 10.11.6 (El Capitan) preventing users to license the product - United States']；判断 ABSTAIN；答错
  - 回答开头：（无）
- **tune_real_e8_q72**：答案文档在 S3；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs a solution for a 16-digit access code being rejected as too short, but the sources only provide general information about SPSS versions, licensing processes, and vendor contact details, without addressing the specific issue of a 16-dig
- **tune_real_e8_l70**：答案文档在 S3；选了 ['swg21989792 IBM License Activation Wizard for SPSS Statistics 24 crashes on MAC OS X 10.11.6 (El Capitan) preventing users to license the product - United States']；判断 ABSTAIN；答错
  - 回答开头：（无）
- **tune_real_e8_gpt**：答案文档在 S3；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs to know why their 16-digit code is rejected and which code or licensing process applies to SPSS GradPack 25 on Mac. The sources only provide general vendor-support guidance and a version-24 workaround requiring a 20-digit code, without

## M-tune-068（4/4 个运行）

- 问题：DB2 Non Reclaimable Storage . We have tablespaces defined under DB2 9.5 that apparently are not able to reclaim storage back to the OS, but does that mean DB2 cannot reuse this space as well?
- 答案文档：swg21438047 IBM SQL1763N error with Reason Code 11 while running "Alter Tablespace" command to reclaim unused storage space against DMS or automatic storage tablespaces. - United States
- **tune_real_e8_base**：答案文档在 S7；选了 ['swg21655828 IBM Reducing the size of the Tivoli Storage Manager database - United States']；判断 ANSWER；答错
  - 回答开头：For DB2 9.7 tablespaces, the values in the RECLAIMABLE_SPACE_ENABLED column are 1. For DB2 9.5 tablespaces, the values are 0. Important: Databases that were formatted with Tivoli Storage Manager serve
- **tune_real_e8_q72**：答案文档在 S7；选了 ['swg21961090 IBM EXTEND DBSPACE operation fails - United States', 'swg21655828 IBM Reducing the size of the Tivoli Storage Manager database - United States']；判断 ABSTAIN；答错
  - 回答开头：For DB2 9.7 tablespaces, the values in the RECLAIMABLE_SPACE_ENABLED column are 1. For DB2 9.5 tablespaces, the values are 0. Important: Databases that were formatted with Tivoli Storage Manager serve
- **tune_real_e8_l70**：答案文档在 S7；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs to know if DB2 can reuse storage space that cannot be reclaimed back to the OS, but the provided sources only discuss how to reclaim storage space or reduce tablespace size, without addressing the specific question of reusing non-recla
- **tune_real_e8_gpt**：答案文档在 S7；选了 ['swg21588881 IBM Reclaiming disk space from DB2 XMeta tablespace after deleting projects - United States', 'swg21655828 IBM Reducing the size of the Tivoli Storage Manager database - United States']；判断 ANSWER；答错
  - 回答开头：With DB2 V9.1, if Automatic Storage is enabled, there is no method to reduce the size of the tablespace already allocated to a database. The database will reuse all free and available space before sta

## M-tune-071（4/4 个运行）

- 问题：'Access is denied' install errors with ICC Installing ICC 4.0.1 and then FP2 gives the 'Access is denied' error on WASSERVICE.exe. How to resolve this?
- 答案文档：swg24042387 IBM Content Collector V4.0.1 Fix Pack 3 - United States
- **tune_real_e8_base**：答案文档在 S2；选了 ['swg21982141 IBM Content Collector install fails - United States']；判断 ANSWER；答错
  - 回答开头：1. Reboot the server and stop the ICC services from Windows Services. 2. Unintall ICC from Start --> Programs -->IBM Content Collector by following below knowledge center link.http://www.ibm.com/suppo
- **tune_real_e8_q72**：答案文档在 S2；选了 ['swg1HE12537 IBM HE12537: CONTENT COLLECTOR INSTALLATION FAILS WITH ACCESS IS DENIED ERROR ON WASSERVICE.EXE FILE - United States', 'swg21982141 IBM Content Collector install fails - United States']；判断 ANSWER；答错
  - 回答开头：* If an existing copy of the WASService.exe file is copied from a previous installation the upgrade can continue [S1] 1. Reboot the server and stop the ICC services from Windows Services. 2. Unintall 
- **tune_real_e8_l70**：答案文档在 S2；选了 ['swg21982141 IBM Content Collector install fails - United States']；判断 ANSWER；答错
  - 回答开头：1. Reboot the server and stop the ICC services from Windows Services. 2. Unintall ICC from Start --> Programs -->IBM Content Collector by following below knowledge center link.http://www.ibm.com/suppo
- **tune_real_e8_gpt**：答案文档在 S2；选了 ['swg1HE12537 IBM HE12537: CONTENT COLLECTOR INSTALLATION FAILS WITH ACCESS IS DENIED ERROR ON WASSERVICE.EXE FILE - United States']；判断 ANSWER；答错
  - 回答开头：* If an existing copy of the WASService.exe file is copied from a previous installation the upgrade can continue [S1]

## M-tune-100（4/4 个运行）

- 问题：How to remove the default -Xcompressedrefs from my WebSphere Application Server My understanding is that for performance reasons, the WebSphere Application server on 64bit JVMs is, by default, using compressed references (-Xcompressedrefs). Due to native OutOfMemory error, I would like to remove that default, so there is no such limitation imposed on my native memory size.
- 答案文档：swg21660890 IBM Using -Xgc:preferredHeapBase with -Xcompressedrefs - United States
- **tune_real_e8_base**：答案文档在 S1；选了 ['swg1IV46157 IBM IV46157: NATIVE OOM ON AIX 64BIT PLATFORM WHEN COMPRESSED REFERENCES ENAB LED - United States']；判断 ANSWER；答错
  - 回答开头：* This issue can be worked around by disabling the compressed references by removing -Xcompressedrefs from the command line options or specifying -Xnocompressedrefs option at the end of the JVM option
- **tune_real_e8_q72**：答案文档在 S1；选了 ['swg21979693 IBM Performance impact in Threads/Timers initialization while using -Xcompressedrefs - United States', 'swg1IV46157 IBM IV46157: NATIVE OOM ON AIX 64BIT PLATFORM WHEN COMPRESSED REFERENCES ENAB LED - United States']；判断 ANSWER；答错
  - 回答开头：There are two possible workarounds to overcome this issue: 1. There are two possible workarounds to overcome this issue: Set -Dsun.reflect.inflationThreshold to a value which yields performance improv
- **tune_real_e8_l70**：答案文档在 S1；选了 ['swg1IV46157 IBM IV46157: NATIVE OOM ON AIX 64BIT PLATFORM WHEN COMPRESSED REFERENCES ENAB LED - United States']；判断 ANSWER；答错
  - 回答开头：* This issue can be worked around by disabling the compressed references by removing -Xcompressedrefs from the command line options or specifying -Xnocompressedrefs option at the end of the JVM option
- **tune_real_e8_gpt**：答案文档在 S1；选了 ['swg21979693 IBM Performance impact in Threads/Timers initialization while using -Xcompressedrefs - United States']；判断 ANSWER；答错
  - 回答开头：There are two possible workarounds to overcome this issue: 1. There are two possible workarounds to overcome this issue: Set -Dsun.reflect.inflationThreshold to a value which yields performance improv

## M-tune-126（4/4 个运行）

- 问题：Does Linux KVM monitoring agent support CANDLEDATA function? Does Linux KVM monitoring agent in ITM support CANDLEDATA function?
- 答案文档：swg21695194 IBM IV67523 Move local data from CANDLEHOME to another file system - United States
- **tune_real_e8_base**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
- **tune_real_e8_q72**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs to know if the Linux KVM monitoring agent in ITM supports the CANDLEDATA function, but the sources do not provide specific information about the compatibility of the Linux KVM monitoring agent with CANDLEDATA.
- **tune_real_e8_l70**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The provided sources do not contain information about the Linux KVM monitoring agent's support for the CANDLEDATA function.
- **tune_real_e8_gpt**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The sources explain general CANDLEDATA restrictions and note that agent compatibility must be verified individually, but they do not state whether the Linux KVM (KV1) monitoring agent supports CANDLEDATA. The Linux KVM sources address SDA installatio

## M-tune-134（4/4 个运行）

- 问题：What are the known issues with WILY software and WAS or BPM?
- 答案文档：swg21966881 IBM Business Process Manager users receive errors that session has expired - United States
- **tune_real_e8_base**：答案文档在 S1；选了 ['swg27021737 IBM Release Notes - IBM Business Process Manager Healthcare Pack version 7.5 - United States']；判断 ABSTAIN；答错
  - 回答开头：（无）
- **tune_real_e8_q72**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs specific known issues with WILY software and WAS or BPM, but the sources primarily provide troubleshooting steps and general information, lacking a comprehensive list of known issues.
- **tune_real_e8_l70**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs a comprehensive list of known issues with WILY software and its integration with WAS or BPM, but the provided sources lack a detailed and specific account of these issues, instead offering troubleshooting guides, release notes, and des
- **tune_real_e8_gpt**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs a consolidated list of known compatibility, session, and messaging issues involving Wily Introscope with WebSphere Application Server or IBM BPM. The sources provide only one specific BPM session-expiration issue and a vague reference 

## M-tune-036（3/4 个运行）

- 问题：Error when using profilePath parameter with BPMConfig to create a profile When creating a profile using the BPMConfig command and the -profilePath parameter to define a custom directory to store the profile data, the creation fails with the following error message if the directory already exists (even if it is empty): com.ibm.bpm.config.BPMConfig.main(): The profile path <profile_path> must not ex
- 答案文档：swg21649807 IBM Specifying the profile path in the BPMConfig properties file for IBM Business Process Manager (BPM) - United States
- **tune_real_e8_base**：答案文档在 S3；选了 ["swg1JR51714 IBM JR51714: YOU RECEIVE 'THE PROFILE PATH MUST NOT EXIST' ERROR MESSAGE WHEN YOU TRY TO CREATE A PROFILE BY USING BPMCONFIG AND THE - United States", "swg1JR51714 IBM JR51714: YOU RECEIVE 'THE PROFILE PATH MUST NOT EXIST' ERROR MESSAGE WHEN YOU TRY TO CREATE A PROFILE BY USING BPMCONFIG AND THE - United States"]；判断 ANSWER；答错
  - 回答开头：* Use a non-existing profile path with the BPMConfig command if you want to set a custom directory for the profile data. For instance, specify a profile path to the parent directory which will then co
- **tune_real_e8_q72**：答案文档在 S3；选了 ["swg1JR51714 IBM JR51714: YOU RECEIVE 'THE PROFILE PATH MUST NOT EXIST' ERROR MESSAGE WHEN YOU TRY TO CREATE A PROFILE BY USING BPMCONFIG AND THE - United States", "swg1JR51714 IBM JR51714: YOU RECEIVE 'THE PROFILE PATH MUST NOT EXIST' ERROR MESSAGE WHEN YOU TRY TO CREATE A PROFILE BY USING BPMCONFIG AND THE - United States"]；判断 ANSWER；答错
  - 回答开头：* Use a non-existing profile path with the BPMConfig command if you want to set a custom directory for the profile data. For instance, specify a profile path to the parent directory which will then co
- **tune_real_e8_gpt**：答案文档在 S3；选了 ["swg1JR51714 IBM JR51714: YOU RECEIVE 'THE PROFILE PATH MUST NOT EXIST' ERROR MESSAGE WHEN YOU TRY TO CREATE A PROFILE BY USING BPMCONFIG AND THE - United States", "swg1JR51714 IBM JR51714: YOU RECEIVE 'THE PROFILE PATH MUST NOT EXIST' ERROR MESSAGE WHEN YOU TRY TO CREATE A PROFILE BY USING BPMCONFIG AND THE - United States"]；判断 ANSWER；答错
  - 回答开头：* Use a non-existing profile path with the BPMConfig command if you want to set a custom directory for the profile data. For instance, specify a profile path to the parent directory which will then co

## M-tune-048（3/4 个运行）

- 问题：SPSS free trial not working on MAC - gets stuck in when it should be launching and goes nowhere I downloaded the SPSS software on my mac running Yosemite 10.10.5. The trial was activated by IBM, they sent me several emails stating this. So I tried to launch the app and get stuck here alt text There is no progress after an hour; and I tried to launch several times, it never gets out of this screen.
- 答案文档：swg21507587 IBM What are the supported Apple Macintosh Operating System Versions for IBM SPSS Statistics? - United States
- **tune_real_e8_base**：答案文档在 S1；选了 ['swg21688476 IBM Will IBM SPSS Statistics 22 run on Apple OS Mac OS X, 10.10 Yosemite? - United States']；判断 ANSWER；答错
  - 回答开头：IBM SPSS Statistics (any version) has two issues to resolve before it will run on OS X 10.10: 1. Download and re-install Apple Java 6 - After the OS upgrade is finished, Apple Java 6 no longer exists 
- **tune_real_e8_l70**：答案文档在 S1；选了 ['swg21688476 IBM Will IBM SPSS Statistics 22 run on Apple OS Mac OS X, 10.10 Yosemite? - United States']；判断 ANSWER；答错
  - 回答开头：IBM SPSS Statistics (any version) has two issues to resolve before it will run on OS X 10.10: 1. Download and re-install Apple Java 6 - After the OS upgrade is finished, Apple Java 6 no longer exists 
- **tune_real_e8_gpt**：答案文档在 S1；选了 ['swg21688476 IBM Will IBM SPSS Statistics 22 run on Apple OS Mac OS X, 10.10 Yosemite? - United States']；判断 ANSWER；答错
  - 回答开头：IBM SPSS Statistics (any version) has two issues to resolve before it will run on OS X 10.10: 1. Download and re-install Apple Java 6 - After the OS upgrade is finished, Apple Java 6 no longer exists 

## M-tune-054（3/4 个运行）

- 问题：Why does my upgrade to Portal 8001 CF14 fail with the following errors, ADMA5008E, ADMA0063E, ADMA5069E, WASX7017E?
- 答案文档：swg21426787 IBM Portal upgrades fail during ejbdeploy with 'Error is Platform not running' message - United States
- **tune_real_e8_base**：答案文档在 S5；选了 ['swg21681745 IBM Upgrade to Portal CF12 fails with errors ADMA5069E and CWLAA1031E and IWAE0037E - United States']；判断 ABSTAIN；答错
  - 回答开头：（无）
- **tune_real_e8_q72**：答案文档在 S5；选了 ['swg21681745 IBM Upgrade to Portal CF12 fails with errors ADMA5069E and CWLAA1031E and IWAE0037E - United States', 'swg21903554 IBM The upgrade from Portal 8001 CF13 to CF16 fails during the config task with errors, WASX7023E, WASX7213I, WASX8011W, WASX7017E, and EJPXD0015W - United States']；判断 ABSTAIN；答错
  - 回答开头：（无）
- **tune_real_e8_l70**：答案文档在 S5；选了 ['swg21696074 IBM An attempt to upgrade Portal 8001 to CF14 fails with the following error...Caused by: java.lang.NoClassDefFoundError:\ncom.ibm.wps.wcm.access.draft.DependenciesImpl - United States']；判断 ANSWER；答错
  - 回答开头：In this case, we compared the current services.properties file that was incomplete to another services.properties that they had in their backup and added the missing entries. After adding the entries 

## M-tune-063（3/4 个运行）

- 问题：Unable to locate the More tab of Document class - Property definition tab - property template configuration to update Is Required setting. Unable to locate the More tab of Document class - Property definition tab - property template configuration to update Is Required setting. Environment is running on Content Engine 5.2.0.3.
- 答案文档：swg21696083 IBM How to overwrite property definition properties in a class via IBM Administration Console for Content Platform Engine (ACCE)? - United States
- **tune_real_e8_base**：答案文档在 S6；选了 ["swg21977774 IBM 'Audit As' property missing in Property Definition object in Administration Console for Content Platform Engine (ACCE). - United States"]；判断 ABSTAIN；答错
  - 回答开头：（无）
- **tune_real_e8_q72**：答案文档在 S6；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs to locate the 'More' tab in the Document class - Property definition tab to update the 'Is Required' setting, but the sources lack specific instructions for this task in Content Engine 5.2.0.3. The sources either discuss different vers
- **tune_real_e8_l70**：答案文档在 S6；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs instructions on how to locate the More tab of Document class - Property definition tab - property template configuration to update the Is Required setting in their Content Engine 5.2.0.3 environment. However, the provided sources lack 

## M-tune-102（3/4 个运行）

- 问题：Non-admin users cannot access webDAV filestore. What is the likely reason? A non-admin user trying to access the webDAV filestore is unable to do so and they see the below exception in the portal logs: Caused by: com.ibm.icm.da.DBAccessException: User id can not be null at com.ibm.icm.da.portable.connection.Logon.logon(Logon.java:159) at com.ibm.icm.da.portable.connection.ConnectionManager.logon(C
- 答案文档：swg21664629 IBM Policy (EJQAB0067E) and JCR Login (WSP0005E) exceptions in System*.logs - United States
- **tune_real_e8_q72**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs information on why non-admin users cannot access the webDAV filestore and how to resolve the 'User id can not be null' exception. The provided sources do not address this specific issue or provide a solution for it.
- **tune_real_e8_l70**：答案文档在 S1；选了 ['swg21608902 IBM The Deploy Case Manager Client task in IBM Case Manager Administrator Client can fail to create folders and files under the Business Space WebDAV filestore - United States']；判断 ANSWER；答错
  - 回答开头：Ensure that the user that runs the IBM Case Manager administration client has read, write, and execute permissions to the folders and files under the <ICM_HOME> and <WAS_HOME> directories. [S6]
- **tune_real_e8_gpt**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The question requires the likely cause of a non-admin WebDAV login failure involving a null user ID, but the sources do not address this specific exception or its required WebDAV user-mapping/configuration. They mainly cover unrelated Portal/JCR issu

## M-tune-133（3/4 个运行）

- 问题：P8 CPE 5.2.1 error: FNRCC0110E - ERROR FixedContentProviderCache.getProvider failed to init provider New P8 CPE 5.2.1 install does not see the Centera Fixed Storage. The following error is returned: FNRCC0110E: CONTENT_FCP_OPERATION_FAILED: The [initialize] operation on the fixed content provider [com.filenet.engine.content.fcprovider.centera.CenteraFCP(0)] failed. FPLibrary (Not found in java.lib
- 答案文档：swg21502037 IBM Unable to add Centera Device in FileNet Content  Engine - United States
- **tune_real_e8_q72**：答案文档在 S2；选了 ['swg21621403 IBM Connecting to a EMC Centera storage fails with java.lang.UnsatisfiedLinkError in IBM FileNet Content Platform Engine 5.2 - United States', 'swg21982745 IBM After upgrade to FileNet Content Engine 5.2 error received Adding Documents . - United States']；判断 ANSWER；答错
  - 回答开头：On the system where FileNet Content Platform Engine is deployed: 1. Follow the instruction on Information Center: Installing or updating EMC Centera SDK library files to install EMC Centera SDK librar
- **tune_real_e8_l70**：答案文档在 S2；选了 ['swg21621403 IBM Connecting to a EMC Centera storage fails with java.lang.UnsatisfiedLinkError in IBM FileNet Content Platform Engine 5.2 - United States', 'swg21982745 IBM After upgrade to FileNet Content Engine 5.2 error received Adding Documents . - United States']；判断 ANSWER；答错
  - 回答开头：On the system where FileNet Content Platform Engine is deployed: 1. Follow the instruction on Information Center: Installing or updating EMC Centera SDK library files to install EMC Centera SDK librar
- **tune_real_e8_gpt**：答案文档在 S2；选了 ['swg21621403 IBM Connecting to a EMC Centera storage fails with java.lang.UnsatisfiedLinkError in IBM FileNet Content Platform Engine 5.2 - United States', 'swg21982745 IBM After upgrade to FileNet Content Engine 5.2 error received Adding Documents . - United States']；判断 ANSWER；答错
  - 回答开头：On the system where FileNet Content Platform Engine is deployed: 1. Follow the instruction on Information Center: Installing or updating EMC Centera SDK library files to install EMC Centera SDK librar

## M-tune-020（2/4 个运行）

- 问题：Updating SCA applications & internal SCA module queues When updating an existing SCA module using the ISC, I noticed that internal SCA queues (sca/<module>/...) on the SCA.SYSTEM bus) are deleted and recreated. One can potentially loose messages on these queues. Is there a fix to the problem?
- 答案文档：swg21639375 IBM SCA destinations for IBM Business Process Manager (BPM), WebSphere Process Server (WPS) and WebSphere Enterprise Service Bus (WESB) are not preserved when uninstalling and reinstalling a service module - United States
- **tune_real_e8_base**：答案文档在 S3；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
- **tune_real_e8_gpt**：答案文档在 S3；选了 ['swg1JR43392 IBM JR43392: STORE AND FORWARD DESTINATIONS ARE INCORRECTLY REMOVED WHEN UPDATING AN SCA MODULE - United States']；判断 ANSWER；答错
  - 回答开头：LOCAL FIX * n.a PROBLEM SUMMARY * **************************************************************** * USERS AFFECTED: WebSphere Process Server V7 Users * ***********************************************

## M-tune-044（2/4 个运行）

- 问题：P8 CPE 5.2.1 error: FNRCC0110E - ERROR FixedContentProviderCache.getProvider failed to init provider New P8 CPE 5.2.1 install does not see the Centera Fixed Storage. The following error is returned: FNRCC0110E: CONTENT_FCP_OPERATION_FAILED: The [initialize] operation on the fixed content provider [com.filenet.engine.content.fcprovider.centera.CenteraFCP(0)] failed. FPLibrary (Not found in java.lib
- 答案文档：swg21502037 IBM Unable to add Centera Device in FileNet Content  Engine - United States
- **tune_real_e8_q72**：答案文档在 S2；选了 ['swg21621403 IBM Connecting to a EMC Centera storage fails with java.lang.UnsatisfiedLinkError in IBM FileNet Content Platform Engine 5.2 - United States', 'swg21982745 IBM After upgrade to FileNet Content Engine 5.2 error received Adding Documents . - United States']；判断 ANSWER；答错
  - 回答开头：On the system where FileNet Content Platform Engine is deployed: 1. Follow the instruction on Information Center: Installing or updating EMC Centera SDK library files to install EMC Centera SDK librar
- **tune_real_e8_l70**：答案文档在 S2；选了 ['swg21621403 IBM Connecting to a EMC Centera storage fails with java.lang.UnsatisfiedLinkError in IBM FileNet Content Platform Engine 5.2 - United States', 'swg21982745 IBM After upgrade to FileNet Content Engine 5.2 error received Adding Documents . - United States']；判断 ANSWER；答错
  - 回答开头：On the system where FileNet Content Platform Engine is deployed: 1. Follow the instruction on Information Center: Installing or updating EMC Centera SDK library files to install EMC Centera SDK librar

## M-tune-059（2/4 个运行）

- 问题：On 30th June, could the Leap Second cause Linux to freeze and impact my MQ?
- 答案文档：swg21602521 IBM Leap Second bug in older Linux kernels may affect IBM MQ and WebSphere MQ - United States
- **tune_real_e8_base**：答案文档在 S2；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
- **tune_real_e8_q72**：答案文档在 S2；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs specific information about the potential impact of the Leap Second on Linux systems and IBM MQ on June 30th, 2015. The sources lack a direct answer to this specific date and system combination, focusing instead on general impacts and o

## M-tune-080（2/4 个运行）

- 问题：Why Plug-in log file reports an error message after install & configure the WebSphere Plugin 8.5 version on a Apache 2.4 webserver. During web server start-up, errors like the following will be logged into the Plug-in log file (http_plugin.log): ERROR: lib_security: loadSecurityLibrary: Failed to load gsk library from /opt/IBM/WebSphere/Plugins/gsk8/gsk8_64 ERROR: ws_transport: transportInitialize
- 答案文档：swg21600618 IBM web server Plugin may need LD_LIBRARY_PATH when used with Apache 2.2 - United States
- **tune_real_e8_q72**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs a solution for the specific error messages related to the WebSphere Plugin 8.5 on Apache 2.4, but the sources lack a direct solution or detailed steps for this specific version and web server combination.
- **tune_real_e8_l70**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs to know why the Plug-in log file reports an error message after installing and configuring the WebSphere Plugin 8.5 version on an Apache 2.4 web server, but the provided sources lack specific information about this version and configur

## M-tune-027（1/4 个运行）

- 问题：How can I query the Derby database in Portal via SQL statements? I have a Portal system I just installed. I have not yet run database-transfer to copy the data from the Derby database to a DB2, Oracle, or SQL Server database. I don't wish to transfer to an external database and I have a need to run a SQL query against a table or two in the Derby database to troubleshoot an issue. How can I perform
- 答案文档：swg21381009 IBM Using dblook and ij to work with the embedded Apache Derby in WebSphere Portal - United States
- **tune_real_e8_gpt**：答案文档在 S2；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs concrete instructions for safely connecting to Portal’s embedded Derby database and executing SQL queries. Although one source mentions the Derby `ij` utility and example commands, the retrieved material is incomplete and version-speci

## M-tune-032（1/4 个运行）

- 问题：What does the end-file-message mean while doing a launchpad.sh in the MS" I am getting an end-file-message means while doing a launchpad.sh in the MS. How do I solve the problem?
- 答案文档：swg21985630 IBM Using launchpad.sh or silent_MS_linux.bin results in end-of-file message. - United States
- **tune_real_e8_gpt**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The question needs a product- and system-specific explanation of the `end-of-file` warning and exact remediation steps. The sources only suggest possible missing 32-bit Linux libraries or unrelated browser/X11 issues, without enough context to determ

## M-tune-040（1/4 个运行）

- 问题：ICC Configuration Store Service is hung? ICC Configuration Store Service is hung and is not responding to start or stop commands. This was observed due to a potential issue with server running out of disk space. What is causing this?
- 答案文档：swg21680391 IBM Content Collector Configuration Store is corrupted - United States
- **tune_real_e8_base**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）

## M-tune-047（1/4 个运行）

- 问题：How can I obtain a Java thread dump against an execution group in IIB v10? This Q&A is abstracted from a PMR How can I obtain a Java thread dump against an execution group in IIB v10?
- 答案文档：swg21618139 IBM Generating Java diagnostic dumps for IBM Integration Bus - United States
- **tune_real_e8_q72**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs specific instructions on how to obtain a Java thread dump for an execution group in IIB v10, but the provided sources lack detailed, step-by-step guidance on this specific task.

## M-tune-052（1/4 个运行）

- 问题：How does Session timeout work in WebSphere Portal? and How do I change the timeout behavior? How does Session timeout work in WebSphere Portal V6.1.0.1?
- 答案文档：swg21419230 IBM WebSphere Portal inactive session time out and redirect - United States
- **tune_real_e8_base**：答案文档在 S1；选了 ['swg21485643 IBM How can we change the session timeout for Deployment Portal users? - United States']；判断 ANSWER；答错
  - 回答开头：For WebSphere, edit this file.... /qibm/UserData/WebSphere/AppServer/V61/Express/profiles/<CADS SERVER>/config/cells/<CADS CELL NAME>/applications/peb.ear/deployments/peb/peb.war/WEB-INF/web.xml Modif

## M-tune-053（1/4 个运行）

- 问题：How to control SDMS database size? ITCAM for SOA 7.1.1 was installed about 3 years ago. I already know that SDMS database size may increase with no limit. Has anyone found a way to keep under control this behavior?
- 答案文档：swg21959281 IBM ITCAM for SOA KD4SDMS database size grows - United States
- **tune_real_e8_l70**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs a solution to control the size of the SDMS database for ITCAM for SOA 7.1.1, but the provided sources either offer solutions for different versions or scenarios, such as pruning the database for newer versions or resolving corruption i

## M-tune-057（1/4 个运行）

- 问题：Can I run different levels of the Rational Developer for z Systems host and client? I'd like to know if I can run different versions of the RDz client and host and if so what compatible or supported versions and releases?
- 答案文档：swg21568844 IBM Developer for z Systems and Rational Developer for z Systems Backward/Forward compatibility - United States
- **tune_real_e8_base**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）

## M-tune-064（1/4 个运行）

- 问题：Command Line and Silent configuration for ITCAM J2EE 7.1.1 agent I am seeing unexpected behaviors when using Command Line (interactive or silent) configuration for J2EE DC when trying to enable MS or TT features. These do not seem to work. Are these configuration methods supported?
- 答案文档：swg21902438 IBM Command Line configuration for J2EE Data Collector - United States
- **tune_real_e8_l70**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs information on whether Command Line and Silent configuration methods are supported for ITCAM J2EE 7.1.1 agent, specifically for enabling MS or TT features. However, the provided sources lack specific information on the support for thes

## M-tune-067（1/4 个运行）

- 问题：How to find details of Corrupted Object from the entries in db2diag.log? We have corruption in DB2 Database and got entries for corrupted Object in db2diag.log ,Need to find details of the Object using information dumped in db2diag.log
- 答案文档：swg21983129 IBM How to find details of Corrupted Object from the entries in db2diag.log? - United States
- **tune_real_e8_gpt**：答案文档在 S1；选了 ['swg21649221 IBM Runstats reads non-leaf page due to index corruption - United States']；判断 ANSWER；答错
  - 回答开头：IBM Runstats reads non-leaf page due to index corruption - United States SQLI_PRG_ERR ; sqlischs; non-leaf; runstats; db2dart; index; corruption TECHNOTE (TROUBLESHOOTING) PROBLEM(ABSTRACT) During run

## M-tune-078（1/4 个运行）

- 问题：How do I change the default 'fit content by' behaviour of Daeja viewer in IBM Content Navigator, to fit content by height or width? How do I change the default 'fit content by' behaviour of Daeja viewer in IBM Content Navigator v2.0.2, to fit content by height or width?
- 答案文档：swg21674924 IBM How do I change the default 'fit content by' behaviour of Daeja viewer in IBM Content Navigator, to fit content by height or width? - United States
- **tune_real_e8_q72**：答案文档在 S1；选了 （一篇不选）；判断 None；答错
  - 回答开头：（无）
  - 拒答理由：The user needs specific instructions to change the default 'fit content by' behavior in Daeja viewer for IBM Content Navigator v2.0.2. While the sources provide relevant information, they do not clearly and concisely outline the steps needed to achie

## M-tune-084（1/4 个运行）

- 问题：How precise is DataPower's backside persistent timeout value related to intermittent "Failed to Process Response Headers" error messages? I have a service on DataPower with a backside persistent timeout value set to 28 seconds. The actual backend device has a persistent timeout setting of 30 seconds. Since my service is configured with a lower persistent timeout value than 30 seconds, why am I sti
- 答案文档：swg21292808 IBM How to troubleshoot the error "Failed to process response headers" - United States
- **tune_real_e8_base**：答案文档在 S3；选了 ['swg21673208 IBM Why does DataPower report that WebSphere Application Server terminated the connection? - United States']；判断 ANSWER；答错
  - 回答开头：This can be due to two possible configuration values, 1) If the HTTP transport of the WAS App server is set to a lower value than the DataPower service. For example the DataPower Back Persistent timeo

## M-tune-145（1/4 个运行）

- 问题：Cannot start the IBM Content Collector Configuration Store Service How to resolve when the IBM Content Collector Configuration Store Service cannot be started?
- 答案文档：swg21680391 IBM Content Collector Configuration Store is corrupted - United States
- **tune_real_e8_base**：答案文档在 S1；选了 ['swg21688502 IBM Reset the Configuration Store in IBM Content Collector 4.0 - United States']；判断 ANSWER；答错
  - 回答开头：Perform the following steps to reset the configuration store in IBM Content Collector 4.0: 1. Shut down all IBM Content Collector services. 2. In a command window, navigate to the ContentCollector\ctm

---

## 人工初读（Claude 阅读每题的问题、答案文档标题、各模型选中的文档标题与回答开头，2026-11-06；需人工确认）

28 道（4 个运行合计）中，四个模型都没选中的只有 6 道，其余 22 道只在 1–3 个运行里出现：

| 类别 | 题号 | 初读 |
| --- | --- | --- |
| 选了另一篇，看起来也能答 | 036、048、071、100、145（054 的 Llama 选择也可能） | 例如 071 选的 APAR 标题就是“安装时 WASSERVICE.exe Access is denied”；100 选的 APAR 正是“去掉 -Xcompressedrefs / 加 -Xnocompressedrefs”。与 E1 的 A 类相同，单一标准文档评分不认 |
| 答案文档本身偏间接/泛泛，拒答可以理解 | 062、068、126、134 | 例如 126 问 KVM 代理是否支持 CANDLEDATA，标准文档是“把本地数据移出 CANDLEHOME”的 APAR；134 问题本身很宽泛 |
| 选了明显不对的文档 | 052、054（CF12/CF13 而非 CF14）、084、044/133（同一问题出现两次） | 产品或错误码不对 |
| 答案文档标题几乎就是问题本身，却一篇不选 | 020、027、032、040、047、053、057、059、063、064、067、078、080、102 | **每道只在 1–2 个运行里漏掉**，不同模型漏的不是同一批题，例如 078 的标题与问题逐字相同，只有 Qwen-72B 漏了 |

初步判断：四个模型都漏的 6 道主要是“另一篇也能答”或“标准文档本身间接”，不是模型能力问题；真正的“明显该选却没选”分散在不同模型、不同题上，更像单次调用的不稳定。可行方向是对“一篇不选”的情况做一致性检查（同一模型再选一次或换一个模型复核），而不是继续换更大的模型。
