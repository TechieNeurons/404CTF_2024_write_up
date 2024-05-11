# Coup de circuit [1/3]

## Speech
```
Ce challenge est le premier d'une série de trois challenges faciles. Le challenge suivant sera disponible dans la catégorie Renseignement en sources ouvertes une fois que vous aurez validé celui-ci.

C'est la catastrophe ! Je me prépare pour mon prochain match de baseball, mais on m'a volé mon mojo ! Sans lui, je vais perdre, c'est certain... Je crois qu'on m'a eu en me faisant télécharger un virus ou je ne sais quoi, et le fichier a été supprimé de mon ordinateur. J'ai demandé de l'aide à un ami expert et il a extrait des choses du PC, mais il n'a pas le temps d'aller plus loin. Vous pourriez m'aider ?

Identifiez le malware et donnez son condensat sha1. Le flag est au format suivant : 404CTF{sha1}
```

## Author

**@Smyler**

## MD5

Collection.zip --> b018d1f191cb506275ea3ff6820a2065

## Analysis
1. Looks likea windows chall :/
```bash
$ unzip Collection.zip 
Archive:  Collection.zip
   creating: Collection/amcache/
  inflating: Collection/amcache/20240505010820_Amcache_DeviceContainers.csv  
  inflating: Collection/amcache/20240505010820_Amcache_DevicePnps.csv  
  inflating: Collection/amcache/20240505010820_Amcache_DriveBinaries.csv  
  inflating: Collection/amcache/20240505010820_Amcache_DriverPackages.csv  
  inflating: Collection/amcache/20240505010820_Amcache_ShortCuts.csv  
  inflating: Collection/amcache/20240505010820_Amcache_UnassociatedFileEntries.csv  
   creating: Collection/mft/
  inflating: Collection/mft/20240505000512_MFTECmd_$MFT_Output.csv  
   creating: Collection/prefetch/
  inflating: Collection/prefetch/20240504235816_PECmd_Output.csv  
  inflating: Collection/prefetch/20240504235816_PECmd_Output_Timeline.csv 
```
2. I don't understand :/ 
    - I opened : `20240504235816_PECmd_Output_Timeline.csv`
    - I filtered the `IsOsComponent` column in order to see non os file and I see that : `c:\users\rick\downloads\sflgdqsfhbl.exe`
    - The sha1 is the flag : 404CTF{`5cf530e19c9df091f89cede690e5295c285ece3c`}