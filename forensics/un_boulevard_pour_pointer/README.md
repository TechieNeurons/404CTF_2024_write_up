# Un boulevard pour pointer

## Speech
```
Un script malveillant est présent dans le challenge. La protection de vos données est à votre charge.

Eh petit.e, c'est à toi de jouer. J'ai jeté toutes mes boules et aucune n'est proche du cochonnet. Par contre, tu peux peut-être t'appuyer sur elles pour pointer.

Trouvez le flag. Le fichier une fois décompressé fait 6GO
```

## Author

**@OwlyDuck**

## MD5

challenge.7z --> bf2907105d544d4d0adca7d3cf5eb942

## Analysis
1. Let's begin by analysing the image file `fdisk -lu image.img`
2. mount every partition as a loop device `sudo losetup -fP image.img`
3. Mount the second partition (the bigger and also the filesystem) `sudo mount /dev/loop0 /mnt/img2`
4. in `/root` we find **boule-3.pdf** which tell us it's an XFS filesystem
5. Let's find the file linked to the XFS filesystem `find /mnt/img2 -name *xfs* 2>/dev/null`
    - We have an xfsdump
6. We need some tool to recover this dump `apt-get install xfsdump -y`
    - And restore : `xfsrestore -f /mnt/img2/var/backup/backup_home.xfsdump home`
    - Then we analyse what we recover:
```bash
/mnt/img2/home/nicochonnet # tree
.
├── bin
├── Desktop
├── Documents
│   └── cochonnet.pdf
├── Downloads
├── Music
├── Pictures
├── Public
├── Templates
└── Videos
```
7. We have the flag in the pdf file : `404CTF{bi1_joué_br4vo_c_le_fl4g}`