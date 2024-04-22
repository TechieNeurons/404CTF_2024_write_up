# Vaut mieux sécuriser que guérir 

## Speech
```
Lors d'une compétition de lancer de poids, un athlète laisse son ordinateur allumé avec sa session ouverte. Cependant, une personne a utilisé son ordinateur et, a vraisemblablement fait des cachoteries. Nous vous mettons à disposition le dump de la RAM de l'ordinateur après l'incident.
Investiguez ce dump mémoire pour comprendre ce qu'il s'est passé.

La deuxième partie du flag est le nom d'une certaine tâche.
Les deux parties sont séparées d'un tiret "-". Par exemple si le flag de la première partie est "flag1" et celui de la deuxième partie est "flag2". Le réel flag du challenge sera 404CTF{flag1-flag2}
```

## Author
@ElPouleto

## MD5
memory.zip = cdde5527ea648b4907b0db08f75a4a02 (652MB so can't put it on github :/)

## Analysis
1. Begin with some info on the file :
```bash
$ /opt/volatility3/vol.py -f memory.dmp windows.info
Volatility 3 Framework 2.7.0
Progress:  100.00		PDB scanning finished                                                                                              
Variable	Value

Kernel Base	0xf802724a4000
DTB	0x1aa000
Symbols	file:///opt/volatility3/volatility3/symbols/windows/ntkrnlmp.pdb/039281E5F80D4711858194C121C9D89D-1.json.xz
Is64Bit	True
IsPAE	False
layer_name	0 WindowsIntel32e
memory_layer	1 FileLayer
KdVersionBlock	0xf8027284dd50
Major/Minor	15.17134
MachineType	34404
KeNumberProcessors	1
SystemTime	2024-03-12 09:10:11
NtSystemRoot	C:\Windows
NtProductType	NtProductWinNt
NtMajorVersion	10
NtMinorVersion	0
PE MajorOperatingSystemVersion	10
PE MinorOperatingSystemVersion	0
PE Machine	34404
PE TimeDateStamp	Wed Apr 11 04:04:54 2018
```
2. Now check the process :
    ```bash
    $ /opt/volatility3/vol.py -f memory.dmp windows.pstree
    Volatility 3 Framework 2.7.0
    Progress:  100.00		PDB scanning finished                        
    PID	PPID	ImageFileName	Offset(V)	Threads	Handles	SessionId	Wow64	CreateTime	ExitTime	Audit	Cmd	Path

    4	0	System	0xd50eb9287440	97	-	N/A	False	2024-03-12 09:57:33.000000 	N/A	-	-	-
    * 1832	4	MemCompression	0xd50ebadae580	82	-	N/A	False	2024-03-12 08:57:52.000000 	N/A	MemCompression	-	-
    * 68	4	Registry	0xd50eb9310040	3	-	N/A	False	2024-03-12 09:57:32.000000 	N/A	Registry	-	-
    * 300	4	smss.exe	0xd50eba852040	2	-	N/A	False	2024-03-12 09:57:33.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\smss.exe	\SystemRoot\System32\smss.exe	\SystemRoot\System32\smss.exe
    460	444	csrss.exe	0xd50ebabcb240	10	-	1	False	2024-03-12 09:57:36.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\csrss.exe	%SystemRoot%\system32\csrss.exe ObjectDirectory=\Windows SharedSection=1024,20480,768 Windows=On SubSystemType=Windows ServerDll=basesrv,1 ServerDll=winsrv:UserServerDllInitialization,3 ServerDll=sxssrv,4 ProfileControl=Off MaxRequestThreads=16	C:\Windows\system32\csrss.exe
    516	444	winlogon.exe	0xd50ebabff080	3	-	1	False	2024-03-12 09:57:36.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\winlogon.exe	winlogon.exe	C:\Windows\system32\winlogon.exe
    * 680	516	fontdrvhost.ex	0xd50ebb026580	5	-	1	False	2024-03-12 09:57:37.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\fontdrvhost.exe	"fontdrvhost.exe"	C:\Windows\system32\fontdrvhost.exe
    * 860	516	dwm.exe	0xd50ebb10c080	13	-	1	False	2024-03-12 09:57:37.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\dwm.exe	"dwm.exe"	C:\Windows\system32\dwm.exe
    * 2968	516	userinit.exe	0xd50ebb93e580	0	-	1	False	2024-03-12 08:58:11.000000 	2024-03-12 08:58:40.000000 	\Device\HarddiskVolume1\Windows\System32\userinit.exe	-	-
    ** 2528	2968	explorer.exe	0xd50ebb940580	61	-	1	False	2024-03-12 08:58:11.000000 	N/A	\Device\HarddiskVolume1\Windows\explorer.exe	C:\Windows\Explorer.EXE	C:\Windows\Explorer.EXE
    *** 4736	2528	OneDriveSetup.	0xd50eb9b7a580	0	-	1	True	2024-03-12 09:00:13.000000 	2024-03-12 09:03:45.000000 	\Device\HarddiskVolume1\Windows\SysWOW64\OneDriveSetup.exe	-	-
    *** 4612	2528	fsquirt.exe	0xd50eba11d580	0	-	1	False	2024-03-12 09:00:02.000000 	2024-03-12 09:00:02.000000 	\Device\HarddiskVolume1\Windows\System32\fsquirt.exe	-	-
    *** 3432	2528	unregmp2.exe	0xd50ebb9f1580	0	-	1	False	2024-03-12 08:58:14.000000 	2024-03-12 08:58:14.000000 	\Device\HarddiskVolume1\Windows\System32\unregmp2.exe	-	-
    *** 5512	2528	MSASCuiL.exe	0xd50eb9aef580	1	-	1	False	2024-03-12 09:00:12.000000 	N/A	\Device\HarddiskVolume1\Program Files\Windows Defender\MSASCuiL.exe	"C:\Program Files\Windows Defender\MSASCuiL.exe" 	C:\Program Files\Windows Defender\MSASCuiL.exe
    *** 1012	2528	FirstLogonAnim	0xd50ebb972300	0	-	1	False	2024-03-12 08:58:11.000000 	2024-03-12 08:59:58.000000 	\Device\HarddiskVolume1\Windows\System32\oobe\FirstLogonAnim.exe	-	-
    *** 3668	2528	unregmp2.exe	0xd50ebba91580	0	-	1	False	2024-03-12 08:58:15.000000 	2024-03-12 08:58:15.000000 	\Device\HarddiskVolume1\Windows\System32\unregmp2.exe	-	-
    *** 4852	2528	powershell.exe	0xd50eb9707080	13	-	1	False	2024-03-12 09:07:46.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\WindowsPowerShell\v1.0\powershell.exe	"C:\Windows\system32\WindowsPowerShell\v1.0\PowerShell.exe" 	C:\Windows\system32\WindowsPowerShell\v1.0\PowerShell.exe
    **** 4544	4852	conhost.exe	0xd50ebbd88580	4	-	1	False	2024-03-12 09:07:46.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\conhost.exe	\??\C:\Windows\system32\conhost.exe 0x4	C:\Windows\system32\conhost.exe
    *** 3452	2528	ie4uinit.exe	0xd50ebb9f4580	0	-	1	False	2024-03-12 08:58:14.000000 	2024-03-12 08:58:15.000000 	\Device\HarddiskVolume1\Windows\System32\ie4uinit.exe	-	-
    5168	3664	SystemSettings	0xd50eb9b33580	3	-	1	False	2024-03-12 09:00:48.000000 	N/A	\Device\HarddiskVolume1\Windows\System32\SystemSettingsAdminFlows.exe	"C:\Windows\system32\SystemSettingsAdminFlows.exe" LanguagePackInstaller	C:\Windows\system32\SystemSettingsAdminFlows.exe
    904	3600	OneDrive.exe	0xd50eba0ee580	17	-	1	True	2024-03-12 09:04:03.000000 	N/A	\Device\HarddiskVolume1\Users\Maison\AppData\Local\Microsoft\OneDrive\OneDrive.exe	 /updateInstalled /background	C:\Users\Maison\AppData\Local\Microsoft\OneDrive\OneDrive.exe
    ```
    - Some weird process, fsquirt.exe, unregmp2.exe, MSASCuiL.exe, FirstLogonAnim.exe also they are some powershell.
    - Some info :
        - fsquirt.exe:
        > used for sending/receiving files using Bluetooth
        Legitimate binary but we don't saw him often, also can indicate we could find some bluetooth file
        - unregmp2.exe:
        > Microsoft Windows Media Player Setup Utility
        Seems legitimate but when we search it we get [lolbas](https://lolbas-project.github.io/lolbas/Binaries/Unregmp2/) also get [bleepingcomputer](https://www.bleepingcomputer.com/startups/25537/unregmp2.exe/) who say it's legitimate
        - MSASCuiL.exe:
        > The MSASCuiL.exe process is, at its simplest, a way to show the icon for Windows Security in the taskbar
        Shitty binary without importance !
        - FirstLogonAnim.exe:
        > First Sign-in Animation
        Shitty but can do joke with it (see [here](https://twitter.com/Hexacorn/status/1482297012116668419?lang=en))
3. Let's get the powershell history
    - First I used this command : `/opt/volatility3/vol.py -f memory.dmp windows.filescan | grep -i consolehost` to find the history file of powershell. I get :
    ```
    0xd50ebacefba0.0\Windows\Microsoft.NET\assembly\GAC_MSIL\Microsoft.PowerShell.ConsoleHost.Resources\v4.0_3.0.0.0_fr_31bf3856ad364e35\Microsoft.PowerShell.ConsoleHost.Resources.dll	216
    0xd50ebae088f0	\Windows\assembly\NativeImages_v4.0.30319_64\Microsoft.Pb378ec07#\58553ff4dedf0b1dd22a283773a566fc\Microsoft.PowerShell.ConsoleHost.ni.dll	216
    0xd50ebb98a080	\Users\Maison\AppData\Roaming\Microsoft\Windows\PowerShell\PSReadline\ConsoleHost_history.txt	216
    0xd50ebbba2db0	\Windows\assembly\NativeImages_v4.0.30319_64\Microsoft.Pb378ec07#\58553ff4dedf0b1dd22a283773a566fc\Microsoft.PowerShell.ConsoleHost.ni.dll.aux	216
    ```
    - Now I extract the *ConsoleHost_history.txt* file with this command : `/opt/volatility3/vol.py -f memory.dmp -o ./dump/ windows.dumpfiles --virtaddr 0xd50ebb98a080`
    - the powershell history has only one line which is `rm hacked.ps1`
4. `/opt/volatility3/vol.py -f memory.dmp windows.pslist --pid 4852 --dump`


### On windows 
1. `Install-Module WinDbg -Scope CurrentUser`
2. 