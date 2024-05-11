# 404CTF_2024_write_up
Write up for the 404CTF 2024 from the DGSE

## Reverse
### Introduction
- [x] [Echauffement](./rev/échauffement/)

### Easy
- [x] [Intronisation du CHAUSSURE](./rev/intronisation_du_chaussure/)
- [x] [Bugdroid Fight 1/2](./rev/bugdroid_fight_1/)

### Medium
- [ ] [Bugdroid Fight 2/2](./rev/bugdroid_fight_2/)

## Forensics
### Introduction
- [x] [Le tir aux logs](./forensics/le_tir_aux_logs/)
- [x] [Un boulevard pour pointer](./forensics/)

### Easy
- [x] [Coup de circuit 1/3](./forensics/coup_de_circuit_1/)

### Medium
- [x] [Darts Bank](./forensics/darts_bank/)
- [ ] [Vaut mieux sécuriser que guérir](./forensics/vaut_mieux_securiser_que_guerir/)

## OSINT
### Introduction
- [x] Légende (Author: **@Izipak (_hdrien)**)
    > Sur cette photo, une des premières légendes du ski français s'apprête à franchir la ligne d'arrivée et remporter son troisième titre de champion du monde cette année. Saurez-vous retrouver son nom et prénom ainsi que le nom de la ville dans laquelle ces compétitions ont eu lieu ?
    - I asked ChatGPT :)
    > Moi: Trouve qui c'est : une des premières légendes du ski français s'apprête à franchir la ligne d'arrivée et remporter son troisième titre de champion du monde cette année
    > ChatGPT: Cela ressemble beaucoup à Jean-Claude Killy, une véritable légende du ski français. Il a remporté trois titres de champion du monde de ski alpin au cours de sa carrière.
    > Moi: Y a-til d'autre triple champion du monde de ski francais ?
    > ChatGPT: Oui, en effet ! Un autre triple champion du monde français en ski alpin est Emile Allais. Il a remporté ses titres dans les années 1930 et 1940.
    - After that I made a research on Emile Allais and discover (on wikipedia) he get his third title at **Chamonix**
    - The flag is : `404CTF{Emile-Allais_Chamonix}`
- [x] Not on my watch (Author: **@HgAt**)
    > Vous êtes arbitre pour l'épreuve de ski de fond et vous accordez une attention particulière à tout ce qui touche au temps.
    > Cependant, en vous réveillant le matin de la compétition, vous vous rendez compte que votre belle montre de poche s'est arrêtée pendant la nuit. Vous la démontez et vous rendez compte que le mécanisme a l'air endommagé. 
    > Sous le coup de la déception, vous entreprenez de trouver un nouveau mécanisme pour celle-ci. Vous vous renseignez donc sur le nombre de mécanismes qui ont été produits.
    >  Si 1,000,387 mécanismes ont été produits, le format du flag sera: 404CTF{1,000,387}
    - By looking at the picture we can see it's a **Waltham Watch Co.**
    - We also get the model **15 Jewels** and the serial number : **15404141**
    - This site will help us getting more info on this watch : https://pocketwatchdatabase.com/
    - We can find a lot of info and we have **Grade/Model Total Production:	197,100**
    - So the flag is : 404CTF{197,100}

### Easy
- [ ] Coup de circuit 2/3 (Author: @Smyler)
    > Le challenge suivant sera disponible dans la catégorie Divers une fois que vous aurez validé celui-ci.
    > Super ! Grace à vous j'ai pu retirer le fichier de mon PC, mais pensez-vous qu'il serait possible d'en savoir un peu plus sur ce malware ?
    > Retrouvez l'interface web du panneau de Command & Control du malware. Le flag y sera reconnaissable.
    - Go on VirusTotal
    - We can see this domain : takemeouttotheballgame.space which look suspicious because created in 2024 and the name is suspicious
    - Searching the domain on google give us that : `https://nmap.online/result/a572cd2d3b48303461ec4c147ffa1fa640afae0d/panel-5d4213f3bf078fb1656a3db8348282f482601690takemeouttotheballgamespace2`
    ```
    Online Nmap scanner
    https://nmap.online › result › panel-5d4213f3bf078fb1...
    5 days ago — Scan report for "panel-5d4213f3bf078fb1656a3db8348282f482601690.takemeouttotheballgame.space" ... Enter 
    ```
    - By going on the link tested by this nmap we get the flag : `404CTF{5up3r_b13n_c4Ch3_gr@cE_Au_n0M_@_r4lOngE}`

## Steg
### Introduction
- [x] L'absence (Author: **@Crevette et Ceriseuh**)
    > Hier, Francis n'était pas là à son épreuve de barres asymétriques, il nous a envoyé une lettre d'excuse. Malheureusement, la fin de sa lettre est illisible.
    > Déchiffrez la fin de ses excuses.
    - We dl the **lettre.txt** and we cat it
    - We notice multiple things, first the 3 first line are normal
    - Only the last line need to be decoded
    - We see (in the first three lines) some Upper case letter
    - The name of the Author : franciS vigenere
    - We have everything, the name indicate a vigenere encoding, the upper case letter are the letters of the key
    - We have the key : GYMNASTIQUES (we put it in cyberchef with the encoded code and with a vigenere decode recipe)
    - We get the flag : **404CTF{NeVolezPasLesDrapeauxSvp}**
