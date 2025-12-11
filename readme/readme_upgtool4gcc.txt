### All filenames start with "function4" are actually scripts and each of them can be run separately.
### The upgtool4gcc is the script for main menu. You can utilize it for calling the other scripts.
### Some scripts need "screen" to be run first or they will not allow us to start/continue. 
### For SLES 15 servers w/o screen, to complete the installation of screen and run screen first is required.
###
### How to utilze these scripts ?
### 1. start screen 
###    i.e.  # screen -S VP
### 2. start and run the script
###    i.e.  # ./upgtool4gcc          (to start and select the required options from the main menu)
###      or  # ./function4prepcheck   (to start and select the required options from the script directly)
### 3.Output/Log directory is /var/opt/teradata/bkfiles/gcctools_logs

### Some tips and reminders:
### 1.Kindly consider to put the tool script(s) in the same directory for SW packages or certlist (working directory)
###   The "default directory" in prompt for inputting SW directory will be the working directory
###
### 2.For utilizing the script "function4SCAtools"
###   -Download,transfer and put the full certlist into the SW directory
###   -Run "function4SCAtools" in direcotry "upgtools", select option #7 for running cksum on packages as needed
###   -Select option #0 for installing/upgrading PUT&VMF&GSCTOOLS&SCA tool packages (those packages will be moved away to directory "/var/opt/teradata/packages/moved" in options #1 to #5)
###   -Select ls1940, the script will help to move away application related packages i.e. DSA,tdm-linux,tdactivemq,postgresql packages to directory "moved"
###   -Select ls2620, the script will help to check if the base version of TDBMS packages are present,move away ttupublickey package
###   -When bynet is installed and there is new bynet package,script will prompt for confirming if bynet package will be upgraded or not
### 
### 3.For VoV Base tier system
###   -Disable cron job "TASM_Throttle_Enforce.sh" on all TD VM before starting any upgrade (ls1840 or ls2620)
###    (the ruleset "FirstConfig" will be de-activated or be changed then causes DBS to be restarted every 10 minutes in new BE)
###   -Address issues and enable TASM_Throttle_Enforce.sh in cron and re-activate FirstConfig ruleset manually after the completion of the upgrades
###  
### -upgtool4gcc        : Main menu for calling the other menus or scripts
### -function4prepcheck : Run checks and collect logs for Merge,OSmove,DSA,UDM upgrades.Run scandisk and checktable.
### -function4SCAtools  : An interface and a menu for calling SCA tool scripts,ls873 ls1840,ls1940,ls2020,ls2620
### -function4CSonTD    : A menu for installing/upgrading and uninstalling VAL/BYOM/SageMaker/Python/R
### -function4MHMmon    : Shows the status and progress of MHM data redistribution
### -function4DSAinstall: For doing installation of DSA 17.05 or higher with PG repository
### -function4DSAupgrade: For doing the upgrade of DSA 17.05 or higher with PG repository
### -function4DSAosmove : For doing the installation of DSA packages after the completion of OSmove
### -function4MSupgrade : For doing the upgrade of DSA packages on multiple Media Servers with bpcl command and bpcl.ini file
### -fcuntion4MSosmove  : For doing the installation of DSA packages on multiple Media Server with bpcl&bpcl.ini after the completion of OSmove
### -function4UDMupgrade: For doing the upgrade of UDM packages 
### -function4UDMosmove : For doing the installation of UDM packages after the completion of OSmove
### -function4CHonTD    : For doing ClientHandler upgrades or generating /tmp/dsainputs only on TD nodes
### -function4configTD  : For doing networking configuration i.e. hostname,/etc/hosts,CLAN IPA,bonding,Souce IP Route, ... in the system HW installation
### -function4BARtuning : Follow KB0041587 to tune DSA and NBU BAR servers as recommanded
### -function4DSAinputs : For generating the file /tmp/dsainputs locally
### -function4CHKrelocation : For capturing and compare the outputs of checks pre&post relocation/reboot/power-cycle on TD/VP/BAR/UDM/SWS

### If any assistance is needed, any idea for improvement or any question, please feel free to contact and let me know 
### lh185009@teradata.com

Version 2025-12-20
1.In script "function4CSonTD"
  -skip the check and comparison of host names from output of commands "bam -i" and "whosmp" for teradata_api-requests
  -correct the code for retrieving the version no. from teradata_api-requests*.rpm
2.In script "function4prepcheck"
  -add option #0 for disable logons and abort all sessions in menu of running scandisk and checktable

Version 2025-09-12
1.In script "function4SCAtools"
  -add a check to give warning if KB0061167 is hit before running ls1940_post_reboot_execution in SP2 to SP6 upgrades
  -add checks and enable "--enable-package-optimization" for pre_check and pre_maintenance_execution of SCA 2.127.0 or higher
  -refer to KB0051011 for SWS,SCA "is_active" tests for TDput service timed out and error out because 8443 port conflicts with Symplicity
   change 8443 to 8444 in /opt/netapp/symplicity_web_services_proxy/wsconfig.xml for web_services_proxy.service
  -add a note of adding "-S" to skip actions that rely on VP for option ls2620 of TD17 upgrades
2.In script "function4UDMupgrade" and "function4UDMosmove"
  -add checks for JAVA 17 and support for DM 20.05 upgrades
  -add checks and note/reminder to show python 3.11 packages are required for the upgrades of DM 20.05 or higher
3.In script "function4prepcheck"
  -add an output SSD_wear_info.out for the information of SSD health and remaining lifespan in function check4merge
4.In script "function4DSAosmove"
  -add copyfromabe to restore /usr/lib/systemd/system/dsc.service from SLES12SP3 ABE 
5.In script "function4MHMmon"
  -options #1 and #2 had been corrected,tested and can be used for monitoring the status of MHM data redistribution 
  
Version 2025-07-26
1.In scripts "function4DSAinstall","function4DSAosmove" and "function4DSAupgrade"
  -correct and add the support information for DSA 17.20.06.03
  -convert http to https with the password "tdrestd" for DSA 20.00.28.00/higher in script function4DSAupgrade
  -improve function for generating /tmp/dsainputs and add setting "DSARESTPORT"
  -add support for MS where BARCmdline is not installed in "function4DSAosmove" and "function4DSAupgrade"
  -prompt for upgrading tdactivemq when the current and new versions are the same but build number is higher
2.In script "function4prepcheck"
  -add check for cloud systems in the option "5. TD system expansion/merge check"
3.In script "function4CHonTD"
  -correct codes for converting "SELF" to "SERVERID" and for extracting version info from the new CH package name
4.In script "function4UDMupgrade"
  -check "dmuser" group and add it if not present,refer to CS2945842

Version 2025-06-20
1.In script "function4SCAtools"
  -add checks and support for TD20 certlist upgrade
  -add checks to sync /etc/opt/teradata/dsa/client.ts of two BEs in service pack upgrade for DM
  -backup,compare and restore /etc/sudoers and /etc/cron.allow in SLES15SP6 service pack upgrades 
  -add notes for the postgres and libpq5 packages in DSC SLES15SP6 service pack upgrades
  -add notes for IB support packages (Linux OFED packages) in SLES15SP6 service pack upgrades
  -add checks to delete /etc/systemd/system/TDput.service for addressing issue of TDput in systemctl in SLES15SP6
  -refer to KB0060652, check&add "exprot JAVA_HOME&PATH" to /etc/profile in post reboot step of DM with SLES15SP6
  -refer to KB0045086, check&remind users to add byn0 to BINDABLE_SUBNETS_NAME_COMMA_DELEMINATED if it's not empty
  -add notes for the requirement of CMIC 15.03.xx or higher for SWS in SLES15SP6 (ls873 and ls2750)
2.In script "function4CSonTD"
  -modify and add notes for the installation/upgrade BYOM 6.1,6.2 or higher
3.In script "function4UDMupgrade"
  -add check for tdm-linux*.gz and prompt for running "tar xzvf tdm-linux*.gz"  
  
Version 2025-05-02
1.In script "function4SCAtools"
  -add an option "6. LS2750" for SLES15SP6 OSmove on SWS/VP/VMS
  -package libibverbs* are required for RDMA capabilities in VMS/CTMS,leave libibverbs* packages when IB packages are moved away in SW directory 
  -correct codes to handle the situation when the timestamps of two debug logs are the latest two in logs directory 
  -add the check and warning for PUT-17521 if ClientHandler is installed and TDput3.9.7.11 is used in SLES15SP6 SP upgrade 
  -add a check on /etc/sudoers in both BEs and reminder to do the sysc if needed before the reboot
2.In script "function4CSonTD"
  -correct GPLUDFSERVERMEMSIZE to GPLUDFServerMemSize for cufconfig command
  -add Warnings to remind implementers that the new values of ScriptMemLimit or GPLUDFServerMemSize is smaller than the existing 
  -modify permanent=70e6*(HASHAMP()+1) for byom user as the template LS2682 instructed  
3.In scripts "function4DSAinstall","function4DSAupgrade","function4DSAosmove"
  -set "DSARESTSCHEME=http" in dsainputs when "dsarest.webservice.scheme=" is blank but not http
  -add checks and reminders for the installations of JDK11.00.26/newer and tdactivemq 5.19.0 for DSC 20.00.26.02 or higher
  -add BARCMDLINE_JAVA_HOME into /tmp/dsainputs for installation and upgrade of BARCmdline package (required for Redhat)
4.In script4tuningBARpt "function4prepcheck"
  -add prompt for input username which is used for running reconfig_estimator

Version 2025-04-06:
1.In script "function4DSAupgrade"
  -update the md5sum of 17.20.02.00&17.20.05.00 xml in bar.databasechangelog for fixing failures in the upgrades from 20.00.22.xx
2.In script "function4SCAtools"
  -correct the minimum required DM version to 20.04 from 24.04 for the option of running ls1940 on DM
  -modify the minimum required TDput version to 3.09.07.11 from 3.09.07.10
3.In script "function4CSonTD"
  -support installation of API_request 20.00 in SLES15SP4
  -add notes to remind only one version of each SW/package to be saved in the SW directory
  
Version 2025-03-04:
1.In scripts "function4DSAinstall","function4DSAupgrade","function4DSAosmove
  -modify the cut commands for retriving new versions of packages because "vce" added in archives of DSA 20.00.26.00
  -add options for checking,installing or upgrading AXMAzure,AXMGCP,AXMS3
  -add an option for running "dsaextract -s","dsc run_repository_job -t backup","vmf_make" in "function4DSAupgrade"
2.In script "function4SCAtools"
  -modify the check for requesting the installation of TDput 3.9.7.10 or higher in 15SP6 service pack upgrades 
  -refer to KB0059699,add check on sshd_config and insert "PubkeyAcceptedAlgorithms=+ssh-rsa" into it if not present     
  
Version 2025-02-13:
1.In script "function4SCAtools"
  -follow KB0059407 to add note and exclude package teradata-udfgpl if teradata-R 4.4.1 or higher is installed
  -exclud and move away package teradata-serviceconnect for service pack upgrade in SWS
2.In script "function4prepcheck"
  -add an option(#13) for running function4CHKrelocation,capturing and comparing the outputs pre&post relocation/reboot/power-cycle
3.In script "function4MHMmon"
  -replace the query for showing the information of tables in progress with James' query
  -add menu with one option for showing the full status and the other for showing a shorter version in monitoring page  
 
Version 2025-01-23:
1.Functions of encrypting and decrypting dbc password with passphrase were added in script "function4CSonTD"
2.Improvement was made on reducing the requests/prompts of entering the dbc password in script "function4CSonTD"
3.An option,#12,added for identifying unsupported plugin(s) before CMIC16.00 upgrade in script "function4prepcheck"
4.In "function4SCAtools",add notes for upgrading teradata-vmf and installing audit, libauparse, system-group-audit(if installed in 15SP2) in 15SP6

Version 2025-01-13:
1.Correct the typos and made improvments on options 2.LS1840 and 5.LS2620 in the main menu of the script "function4SCAtools"
2.Add a check to ensure the cksum on teradata-R-4.4.1-sles12sp3 is correct before starting the installation/upgrade

Version 2025-01-08:
1.Add option for SLES15SP2 to SLES15SP6 service pack and certlist upgrade in the script "function4SCAtools"
2.Add an option(#8) in "function4SCAtools" to run "function4sshd" for disabling&restoring auto-logout,enabling&restoring root logon in sshd service
3.Change the name of the script "function4MLEonTD" to "function4CSonTD","CS" stands for ClearScape
4.Add options for install/upgrade/uninstall teradata-python* and teradata-R* packages in script "function4CSonTD"

Version 2024-12-20:
1.Add option #8 for generating /tmp/dsainputs in scripts "function4DSAosmove" and "function4DSAupgrade"
2.Add option #3 for generating /tmp/dsainputs in script "function4prepcheck"
3.Add a script "function4DSAinputs" for generating /tmp/dsainputs locally
4.Add check on /opt/teradata/byom/06.00.xx.xx/examples for BYOM 06.00.xx.xx installation/upgrade in script "function4MLEonTD"
5.Add check for table names with non-ASCII characters (KB0042794) for MHM data redistribution in script "function4prepcheck"

Version 2024-11-20:
1.In the script "function4SCAtools"
  -Modify and show the working directory as the default SW directory
  -Modify the default command "ls2020_post_check -a" and add "-k viewpoint-portal" to it
  -Add command to move away packages "teradata-connect*" for VoV systems in case packages "teradata-connect*" are present
2.In the script "function4prepcheck"
  -Add the check for Join Index tables for merge/expansion
  -Add check and ensure HOSTNM used for making a directory is not empty in option #10 for a backup before fresh OS instalaltion
3.Modify the displayed message of choosing to generate /tmp/dsainputs only in the script "function4CHonTD"
4.Add prompt for input tdmaps password in the script "function4MHMmon"
5.Add commands "systemctl enable tdactivemq" in scripts "function4DSAinstall","function4DSAupgrade","function4DSAosmove","function4UDMosmove","function4UDMupgrade"
6.Change the Log directory to /var/opt/teradata/bkfiles/gcctools_logs in scripts

Version 2024-10-29:
1.In the scripts "function4DSAupgrade","function4DSAosmove" and "function4DSAinstall"
  -Add notes for showing the required versions of jdk11,tdactivemq 5.18.4 and VP24.08 for supporting DSC 17.20.06
  -Add codes (INC0347016) for copying PG packages from “DSAMetaDataMigrator.17.20.06.00/pkgs/sles152stnd" to "sles154tdc"&"sles154stnd",incorrect version 14.8 were found in directories for SLES15SP4(VoV)
2.Add codes in script "function4DSAosmove to uninstall libpq5 and set POSTGRES_DATADIR to "/var/opt/teradata/postgres/data" in /etc/sysconfig/postgresql before starting postgres
3.Add "GRANT LOGON ON ALL to" API user in the script "function4MLEonTD"

Version 2024-10-11:
1.Refer to KB0057066, add codes in "function4SCAtools" to move away and exclude teradata-gsctools package if version is 04.01.01.97 on VoV TPA nodes
2.Add notes for KB0053342 to notify re-activate ruleset manually is required in the script "function4SCAtools" if a first-time upgrade to 17.10.03.33+ or 17.20.03.21+
3.Add notes for reminding VP 24.08 is required for supporting DSA 17.20.06 in "function4DSAinstall" and "function4DSAupgrade"
4.Add notes for reminding barportlets 17.20.06.xx is required for supporting VP 24.08 in "function4SCAtools"
5.Add options of selecting the running level for checktable in script "function4prepcheck",level two/three for dbc, level one/two for all user tables
6.Correct typos in script "function4BARtuning" which might be related to a stuck in executing "script4tuningBAR"
7.Modify the script "function4MSupgrade" and "function4MSosmove to utilize "bpcl_dsa.ini" instead of "bpcl.ini" for upgrading DSA packages on Media Servers
8.Add a script "function4CSRcreate" for generating a CSR. Add the option #8 in "function4prepcheck" for "function4CSRcreate"

Version 2024-09-16:
1.Add "python3-base__sles12_x8664.3.4.*" into the moved-away list in the script "function4SCAtools"
2.Add commands to enable postgresql to be started automatically after a server reboot in the script function4DSAupgrade
3.Correct a typo in the script "upgtool4gsc" for checking the existence of the script "function4UDMupgrade"
4.Add option for running ls2750_prep_check,ls2752_prep_check,ls2754_prep_check in the script "function4prepcheck"
5.Add a menu with options for checking and rotating self-signed certificates of tomcat,broker,postgres,tmsmonitor in the script "function4prepcheck" for VP

Version 2024-08-21:
1.Correct the TDput path for re-newing certificate of TDput in the script "function4prepcheck"
2.Add checks in the script "function4prepcheck" for NBU.To capture the status of NBDB,licenses,java version,MANIFEST.MF.
3.Add codes to disable TASM_Throttle_Enforce.sh in cron and add reminder of re-enabling it in ls1840/ls2620 options of the script "function4SCAtools" for VoV with the base tier 
4.In case OS certlist upgrade is needed only, add codes to allow options "ls1840" or "ls2020" in function4SCAtools to be run w/o the existence of the new ptdbms or viewpoint  
5.Add options of disabling TDput and TCA services(ls2020 option only) in the script "function4SCAtools" after the completion of post_check execution
6.Correct the showed version of SCA in the menu of script "function4SCAtools" after option #0 for upgrading SCA tool packages is done
7.Make the default software direcotory be more helpful for users in "function4SCAtools".Utilize "certlist-td" for ls1840&ls2620,"certlist-vp" for ls2020,"certlist-tms" for ls1940,"certlist-sws" for ls873
8.Add reminder for checking and increasing permspace for td_mldb user from 5MB/AMP to 300/AMP manually if needed
9.Increased permspace for tapidb user creation(from 1e6*(HASHAMP()+1) to 5e6*(HASHAMP()+1)) in script "function4MLEonTD
10.Add the script "Restore_DSA_JMS_Pass.sh" from DM Engineering.Problem:DSARest was in unused state after instance restarted(password issue).The script is a workaround and permanent fix is DSC 17.20.06.00.

Version 2024-07-19:
1.Improve "function4MLEonTD" to support the installation of API_request on VoV systems because node id byn001-0x is expected instead of byn001-x
2.Marked out the lines of changing "SELF" to hostname of server.id in "function4MSupgrade","function4DSAupgrade","function4DSAosmove".In TDVM, server.id is IPA+ch and no entry in /etc/hosts for it. 
3.Added step to rename the /tmp/install_tapiudf.log before running install.sh in "function4MLEonTD"
4.Corrected typo "cln -s" to "ln -s" in function4configTD for configuring source IP routes on TMS

Version 2024-06-14:
1.Modify codes in "function4MLEonTD" of installing API on VoV systems because byent entries in mpplist with an extra "0" in chassis number i.e. byn001-01,byn001-02
2.Add an option for configuring source IP routes in the script "function4configTD" (option #4)
3.Add an option for backup the configuration files and outputs before OS fresh installation(s) on node(s) in the script "function4prepcheck (option #8)
4.Add code in the script "function4SCAtools" to move away package "python3-PyNaCl" 1.4.0-150000.3.8.2 from the certlist directory

Version 2024-05-20:
1.Add an option for running scandisk on all data in the script "function4prepcheck"function4DSAupgrade",
2.Add codes for checking&correcting users "postgres","dscuser","teradata" in /etc/passwd,ensure "/bin/bash" is used for "shell" (some restricted systems set the shell to /sbin/nologin)
3.Add ".set session transaction btet;" in the scripts "function4MLEonTD" and "function4prepcheck" (Some customers set transaction mode to ANSI for user DBC)
4.Per Engieenring's instruction to remove the prep checks for SLES15 OSmove because prep and post checks (ls2750,ls2752,ls2754) are available in SCA scripts
5.Add command to check the log level for Datamover services and generate an output file "rootLogger_level.out" in the script "function4prepcheck"

Version 2024-05-07:
1.Add codes for retrieving actionlistname with "InProgress" tables from tdmaps.actionhistorytbl and correct codes for logging in "function4MHMmon"
2.Add the check to list out IR tables and append suggestions from GSO to the output file in "function4prepcheck"
3.Add a script "function4UDMrestart" for starting or stopping Data Mover cluster. Add an option for the new script in "upgtool4gcc"
4.Add codes for running "passwd -x -1 nbwebsvc" in "function4prepcheck"

Version 2024-04-25:
1.Codes to show a note for KB0043939 (reset dbc.syssecdefaults to the default) in LS2620 for TD 17.20 Minor Version upgrades in "function4SCAtools"
2.Add "MPPInfo",cod info with "tvam",SQL queries into prep checks for system expansion in "function4prepcheck"
3.Add codes for capturing the output of running the script in the directory "working-dir-name/logs"
4.Add codes for implementer to input username&password for API_request installation and "rpm -e --noscripts" for uninstallation in "function4MLEonTD"
5.Add codes for moving away away the problematic sudo 1.8.27-150000.4.50.1 if found in the certlist directory in "function4SCAtools"
6.Correct codes for renewing the certificate of TDput if the certificate has been expired in "function4SCAtools"

Version 2024-04-15:
1.Add a script "function4udmconfig" for configuring internal DSC in DataMover

Version 2024-04-03:
1.In function4MLEonTD
  - Add options for uninstalling VAL,BYOM,API in "function4MLEonTD" 
  - Add checks for API installation to ensure the node is the first entry from command "bam -i" in "function4MLEonTD" 

Version 2024-03-27:
1.Revise codes for validating the cksums of packages. Some pkg names are a part of other pkgs and the checks were done incorrectly.
2.Add check for package tdwallet in DM,add prompts for reminding implementers to upgrade/install tdwallet accodingly in "function4UDMupgrade" and "function4UDMosmove"
3.Add a script "function4hardening" for node hardening. I did not add it into any menu because the requirements and requested settings should be various between systems

Version 2024-03-14:
1.Add an option into "function4prepcheck" for checking the validity of certificates of VP services
2.Add a new script "function4bartuning"
3.Address several issues on "function4dSCAtools" and "function4DSAupgrade"

Version 2024-02-28:
1.Fix several problems on "function4dSCAtools" and "function4configTD"
2.Add a function fix4KB0042426 into "function4dSCAtools" and "function4prepcheck" for renewing the expired SSL certificate of TDput before starting checks or upgrades

Version 2024-02-23:
1.Add an option for installing/upgrading SCA tool, TDput, gsctools, VMF and PUTTools packages
2.Correct several coding problems on "function4DSAupgrade" and "function4SCAtools"

Version 2024-02-21:
1.Add an option for installing SCA packages on Media Servs with bpcl command and bpcl.ini
2.Change "bartrust -a" to "bartrust -d" in "function4MSupg" and "function4MSosmove"
3.Add check for leftover DSARestProject process, kill it if found in "function4DSAupgrade"

Version 2024-02-15:
1.Improve the prep_check for TD expansion
2.Add options in "fuction4SCAtool" for input and allow user to modify the commands to be run if the default one is not correct

Version 2024-02-11:
1.Initial Versions of the scripts

###
### Run "./upgtool4gcc" for the main menu
### Need to start "screen -S GCC" first or it will not continue to show the main menu
### The script (function4xxxxxxxx) of each option in main menu can be run separately also
###

###############################################################################################
Main Menu 
###############################################################################################


Tue Oct  1 18:31:38 PDT 2024

### Note:
### ClientHandler pkg and "function4CHonTD" should be in the same directory for option #7

=================================================================================
=================================================================================
                   Main Menu (VersionOfTool:20240916)
Options:
1. Preparation checks for CRs
2. Upgrades with SCA AutoPUT
3. VAL,BYOM,SageMaker(teradata-api_request) installation/upgrade
4. MHM status and progress monitor
5. DSA Installation/upgrade (DSC,CH,BARCmdline,AXM,tdactivemq ...)
6. Data Mover upgrades and Config Internal DSC (17.05 or higher with Postgres)
7. Upgrade ClientHandler package on TD system
8. Configure TD on-prem system (hostname,/etc/hosts,CLAN IPA,Bonding,NTP...)
9. Exit
=================================================================================
=================================================================================
Enter your choice (1-9,default is 9):



###############################################################################################
Manu for option "1. Preparation checks for CRs"
###############################################################################################


Thu Jan 23 05:11:07 PST 2025
Note:
The requirements for options #2 (KB0013447),
 -The script should be run from NBU master or DSC node
 -/opt/teradata/gsctools/bin/bpcl_dsa.ini is present (bpcl -a -g)
 -Add entries to bpcl.ini if any is missed accordingly
 -Passwordless(bartrust -a) logon to all entries in bpcl.ini
 -Config passwordless logon (scp authorized_keys,known_hosts) for nodes added manually and test
 -Script will ask if "bpcl -a -g" and "bartrust" to be run when bpcl.ini is not present

============================================================================
============================================================================
               CR Prep/Post Check (VersionOfTool:20250123)
Options:
1. NBU/DSA standalone check w/o using bpcl and bpcl.ini
2. Big NBU/DSA configuration check w/ command bpcl and file bpcl.ini
3. Generate /tmp/dsainputs only
4. Unity DATAMOVER check
5. TD system expansion/merge check
6. SLES15SP2/SP6 OSmove prep checks
7. Run scandisk and checktable on TD PDN node
8. Check the validity of and rotate the self-signed certificates in VP
9. Generate the private key and CSR for a certificate
10. Validate the pakages with cksum
11. Backup configuration files and outputs before fresh OS installations
12. Check unsupported plugins before CMIC16 upgrade in On-Prem systems
13. Exit
===========================================================================
===========================================================================
Enter your choice (1-13,default is 13):



###############################################################################################
Menu for "2. Upgrades with SCA AutoPUT"
###############################################################################################


Thu Jan 23 05:14:26 PST 2025

SCA Version: 2.89.0   Platform Model: Vantage on On-Prem

### Note:
### Always follow the latest template closely and have the latest SCA tool packages installed
### When each sca script exits for actions. Open another ssh session to address the issues
### Select option 1 or 2 to continue after the issues are addressed
### If the task failed and in a unknown status (no options for retry or skip)
### ,fix the problem and redo or a case to engage support may be needed


========================================================================================
========================================================================================
               SCA Main Menu(VersionOfTool:20250304) 
Options:
0. Install/Upgrade SCA tool packages (System-change-tool,TDput,PUTTools,gsctools,vmf)
1. LS873 - SWS Certlist and Service-Pack(15SP2 to 15SP6)Upgrade
2. LS1840 - TD Certlist Upgrade
3. LS1940 - TMS BASE Certlist and Service-Pack(15SP2 to 15SP6)Upgrade
4. LS2020 - Viewpoint 1600And Higher Certlist and Service-Pack(15SP2 to 15SP6)Upgrade
5. LS2620 - TD 17.xx Upgrade
6. LS2750 - TMS(SWS/VP/VMS) OSmove to SLES15SP6 from SLES12SP3
7. Reset SCA AUTOPUT (putadmin --resetall)
8. Validate the pakages with cksum
9. exit
========================================================================================
========================================================================================
Enter your choice (1-9,default is 9):



#######################################################################################################
Menu for "3. VAL,BYOM,SageMaker(teradata-api_request),teradata-python,teradata-R installation/upgrade"
#######################################################################################################

Thu Jan 23 05:12:17 PST 2025
### Note:
    API request/SageMaker need to be installed or uninstalled from byn001-10
    But this script is running at byn001-06

DBS Version: 17.20.03.30    OS Release Version: SLES12SP3
===================================================================================
===================================================================================
Install/Upgrade/Uninstall VAL,BYOM,SageMaker,Python,R (VersionOfTool:20250113)
Options:
1. VAL Installation/Upgrade (LS2740)
   Current: 2.2.0.0
   New    : 02.02.00.00
2. BYOM Installation/Upgrade (LS2682)
   Current: 05.00.00.05
   New    : 05.00.00.05
3. API Request/SageMaker Installation (LS2684)(Upgrade is not supported yet)
   Current: 01.04.00.00
   New    : 01.04.00.00
4. Teradata Python Installation (LS2400)
   Current: 3.8.17
   New    : 3.8.17
5. Teradata R Installation (LS2400,teradata-R-4.4.1-sles12sp3 only is supported)
   Current: 4.4.1
   New    : 4.4.1
6. Drop JAR of BYOM 4.00.00.02 in 5.00.00.00 upgrade ( if Failure 6839 is hit )
7. Remove/Uninstall VAL,BYOM,API,teradat-python,teradata-R
8. Exit
===================================================================================
===================================================================================
Enter your choice (1-8,default is 8): 




###############################################################################################
Menu for "4. MHM status and progress monitor"
###############################################################################################


Status will be refreshed in 45 seconds

            Current TimeStamp(6)
--------------------------------
2024-02-17 09:59:49.320000+01:00

Status                                Count(*)  Sum(TableSize)
------------------------  --------------------  --------------
Complete                                266884         2.05E13

Tables Still to Move
--------------------
             1732312
Size of Tables Still to Move
----------------------------
               8858750736384

StartTime            DatabaseName                    TableName                       TableSize
-------------------  ------------------------------  ------------------------------  ---------
2024-02-17 09:59:44  D52_NWU_D_EDWH_LZ               L1_DPO_23_1_0                     1.05E07
2024-02-17 09:59:44  D52_NWU_D_EDWH_LZ               L1_FCLAGT_23_1_0                  9.97E06
2024-02-17 09:59:44  D52_NWU_D_EDWH_LZ               L2_FCLAGT_12_C_23_1_0             9.81E06
2024-02-17 09:59:44  D52_NWU_D_EDWH_LZ               L1_DPO_12_23_1_0                  1.05E07
2024-02-17 09:59:44  D52_NWU_D_EDWH_LZ               L1_FCLAGT_12_23_1_0               9.97E06
2024-02-17 09:59:47  D52_NWU_D_EDWH_LZ               L2_DFTPRB_C_23_4_0                7.76E06
2024-02-17 09:59:48  D52_NWU_D_EDWH_LZ               L1_DFTPRB_23_4_0                  6.76E06
2024-02-17 09:59:48  D52_NWU_D_EDWH_LZ               L1_DFTPRB_12_23_4_0               6.76E06
2024-02-17 09:59:49  D52_NWU_D_EDWH_LZ               L2_OGNCNUCFL_H_23_4_0             6.18E06
2024-02-17 09:59:49  D52_NWU_D_EDWH_LZ               L2_OGNCNUCFL_C_23_4_0             6.16E06



###############################################################################################
Menu for "5. DSA Installation/upgrade (DSC,CH,BARCmdline,AXM,tdactivemq ...)"
###############################################################################################


Sun Apr 14 22:40:37 PDT 2024

Note:
Only DSA 17.05 or higher with Postgres repository are supported

================================================================================
================================================================================
            Main Menu For DSA Installation/Upgrade (VersionOfTool:20240415)
Options:
1. Fresh/Initial Installation of DSA
2. Upgrade DSA packages on DSC and/or Media Server
3. Install DSA packages on DSC and/or Media Server after SLES OSmove
4. Upgrade DSA packages on Media Servers w/ bpcl&bpcl.ini
5. Install DSA packages on Media Servers w/ bpcl&bpcl.ini after SLES OSmove
6. Recommended NBU and DSA BAR Tunings - On-Prem
7. Exit

===============================================================================
===============================================================================



###############################################################################################
Menu for "6. Data Mover upgrades and Config Internal DSC (17.05 or higher with Postgres)"
###############################################################################################


Sun Apr 14 22:40:37 PDT 2024


=================================================================================
=================================================================================
                   Main Menu for Data Mover Changes (VersionOfTool:20240415)
Options:
1. Upgrade Data Mover Versions
2. Install Data Mover Versions after OSmove
3. Configure Internal DSC in Data Mover
4. Exit
=================================================================================
=================================================================================
Enter your choice (1-4,default is 4):




###############################################################################################
Menu for "7. Upgrade ClientHandler package on TD system"
###############################################################################################


Sat Feb 17 17:56:25 PST 2024

 Usage:
 Put the new and only one clienthandler package (*.gz format) in the direcotry of TD PDN node with this script
 The script will generate  /tmp/dsainputs for CH upgrade by extracting the settings from clienthandler.properties on each node.
 If the new /tmp/dsainputs is not correct or misses any specific setting, please correct the settings before upgrading CH.

Press any key to start pre_upg checks and upgrade for ClientHandler package



###############################################################################################
Menu for "8. Configure TD on-prem system (hostname,/etc/hosts,CLAN IPA,Bonding,NTP...)"
###############################################################################################


Mon Feb  5 05:29:24 PST 2024
Usage:
### A file with the required entries as "bynet-entry hostname CLAN-IPA CLAN-subnetmask" must be existing
### It can be created during the preparation phase and put it in working directory
### Or the script will let you input the required information in option #0 for generating the file
### The default name is : host-info.out


===========================================================================================================================================
===========================================================================================================================================
                Menu for configuring Vantage systems (VersionOfTool:20240425)
Choose an option:
0. Preparation (must be done first) - To add the required information bynet-entry hostname CLAN-IPA CLAN-subnetmask into host-info.txt
1. To change the hostname of all TD nodes
2. To update the /etc/hosts for nodes and populate /etc/hosts to all TD nodes
3. To configure CLAN and the default gateway on all nodes (for ethx or bondx)
4. To configure Source IP Route (Redundancy and Segregating Network Traffic)
5. To config NTP on All nodes
6. Exit
===========================================================================================================================================
===========================================================================================================================================
Enter your choice (1-6,default is 6):  



Sun Apr 14 22:42:31 PDT 2024
Action Type: Configure internal DSC in DataMover

Note:
# ports 61616(for TD with CH) on DM,1025/443(for DM&VP) and 15401(between TD sys) on TD nodes are opened
# Test and validate with commands "curl -v telnet://IPA:port-no"
# Add entries for DataMover, TD systems into /etc/hosts of VP
# Add entries into /etc/hosts of TD nodes with packages ClientHandler installed
#     -IPA and hostname for broker/tdactivemq (check "BURL" in /tmp/dsainputs)
#     -IPA and node name(s) for Master Media Server(s) (check "MASTERHOSTNAME" in /tmp/dsainputs)
# Install package ClientHandler on only one TD system for one DM.Easier for configuration and maintenance

Package Name              Current Version           
DataMover bundle          17.20.01.03               
DSC                       17.20.02.01               

============================================================================================================
============================================================================================================
            Internal DSC Configuration in DataMover (VersionOfTool:20240415)
Options:
1. Configure/Add a TD System
2. Generate/Populate /tmp/dsainputs for all nodes in a TD system
3. Generate/Populate /tmp/dsainputs for each node separately in a TD system
4. Install ClientHandler on TD System (user root logon TD node is required)
5. Configure/Add Networking Fabric
6. Exit
============================================================================================
============================================================================================
Enter your choice (1-6 or q,default is 6):

What had been done and changed in the in-house testing systems:
1.	Configure/Add a TD System
-To add systems “MARIO” and “ROMIO”
-In /etc/hosts of DM, two entries were added by script
10.25.xx.xx     MARIO
10.27.172.xx   ROMIO
              -In /etc/hosts of “MARIO” and “ROMIO”, one entry was added manually
10.27.116.107	 cs-dm-0612
               -DSMain was restarted manually
2.	Generate/Populate /tmp/dsainputs for all nodes in a TD system 
-To select system “MARIO” for populating dsainputs to TD nodes
-Entries as below were added into /etc/hosts of DM by the script
10.25.xx.xx     MARIO001-06 MARIOcop1
10.25.xx.xx     MARIO001-10 MARIOcop2
10.25.xx.xx    MARIO001-11 MARIOcop3
10.25.xx.xx    MARIO001-12 MARIOcop4
10.25.xx.xx    MARIO001-13 MARIOcop5
10.25.xx.xx    MARIO001-14 MARIOcop6
-A entry as below was added for HSN into /etc/hosts of DM and the command "./build_dsainputs -m MARIO001-15 -u User_name" was run manually
10.25.23.xx    MARIO001-15 MARIOcop7
3.	Install ClientHandler on TD System (user root logon TD node is required)
-To select system “MARIO” for the installation of TD nodes
-Entries as below were added into /etc/hosts of TD nodes in MARIO by the script
10.27.116.107   cs-dm-0612
10.25.xx.xx     MARIO001-06 MARIOcop1
10.25.xx.xx     MARIO001-10 MARIOcop2
10.25.xx.xx    MARIO001-11 MARIOcop3
10.25.xx.xx    MARIO001-12 MARIOcop4
10.25.xx.xx    MARIO001-13 MARIOcop5
10.25.xx.xx    MARIO001-14 MARIOcop6
10.25.xx.xx    MARIO001-15 MARIOcop7
-Package ClientHandler was installed with /tmp/dsainputs generated in step #2 on all TD nodes of MARIO
Client Id                             Destination                 Selector                        
--------------------------------------------------------------------------------------------------
ID:destiny1-44060-1713151445145-1:0   DSC.ExecutionRequestQueue   JMSType LIKE 'MARIO001-06_ms'   
ID:destiny2-39064-1713151445005-1:0   DSC.ExecutionRequestQueue   JMSType LIKE 'MARIO001-10_ms'   
ID:destiny3-46087-1713151444983-1:0   DSC.ExecutionRequestQueue   JMSType LIKE 'MARIO001-11_ms'   
ID:destiny4-34791-1713151445064-1:0   DSC.ExecutionRequestQueue   JMSType LIKE 'MARIO001-12_ms'   
ID:destiny5-38976-1713151444928-1:0   DSC.ExecutionRequestQueue   JMSType LIKE 'MARIO001-13_ms'   
ID:destiny6-37065-1713151445026-1:0   DSC.ExecutionRequestQueue   JMSType LIKE 'MARIO001-14_ms'   
ID:destiny7-41050-1713151444973-1:0   DSC.ExecutionRequestQueue   JMSType LIKE 'MARIO001-15_ms'   
4.	Configure/Add Networking Fabrics
-Select “MARIO” as local system with MS and “ROMIO” as remote system w/o MS
-The script ran command “dsa_configfabric” and answers were input manually for the xml files (the failures/warnings/errors were ignored)
Fabric Name    System Name   Is Enabled   
------------------------------------------
MARIO_fabric   MARIO         Y            

Node Name     Media Server Name   Media Server IP   
----------------------------------------------------
mario001-11   mario001-11_ms      39.0.8.11         
mario001-12   mario001-12_ms      39.0.8.12         
mario001-13   mario001-13_ms      39.0.8.13         
mario001-14   mario001-14_ms      39.0.8.14         
mario001-15   mario001-15_ms      39.0.8.15         
mario001-06   mario001-06_ms      39.0.8.6          
mario001-10   mario001-10_ms      39.0.8.10         

Fabric Name    System Name   Is Enabled   
------------------------------------------
ROMIO_fabric   ROMIO         Y            

Node Name     Media Server Name   Media Server IP   
----------------------------------------------------
romio001-02   mario001-15_ms      10.25.xx.xx      
                          mario001-13_ms      10.25.xx.xx      
                          mario001-11_ms      10.25.xx.xx      
                          mario001-10_ms      10.25.xx.xx       
romio001-01   mario001-14_ms      10.25.xx.xx      
                          mario001-12_ms      10.25.xx.xx      
                          mario001-06_ms      10.25.xx.xx

5.	Add entries into /etc/hosts, install tdmportlets-17.20.01.01-1.noarch,config DM, add and test jobs in VP
-Entries as below were added into /etc/hosts
10.27.116.107   cs-dm-0612
10.25.xx.xx     MARIO001-06 MARIOcop1
10.25.xx.xx     MARIO001-10 MARIOcop2
10.25.xx.xx    MARIO001-11 MARIOcop3
10.25.xx.xx    MARIO001-12 MARIOcop4
10.25.xx.xx    MARIO001-13 MARIOcop5
10.25.xx.xx    MARIO001-14 MARIOcop6
10.25.xx.xx    MARIO001-15 MARIOcop7
10.27.172.214   ROMIO001-01 ROMIOcop1
10.27.173.16    ROMIO001-02 ROMIOcop2
-Activities in VP GUI

