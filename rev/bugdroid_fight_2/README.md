# Bugdroid Fight 2/2

## Speech
```
Vous venez de consulter le message du Bugdroid...
Dans son message, il explique que le combat ne peut être gagné à la seule force des poings... À moins que vous ne soyez aidé d'une force divine : une formule magique se cache ici, elle vous permettra de gagner le duel.
Format de flag : 404CTF{formule_magique}
```

## Author
@Whiplash

## MD5
Bugdroid_Fight_-_Part_2.aab = 32a91993315d3616669644532fb9dc0c

## Analysis
1. It's an AAB file which is a new way of distributing android app (cf. resource 1)
2. Let's transform this AAB to APKS (APKS is an archive containing apk) I used this command : `java -jar bundletool-all-1.11.0.jar build-apks --bundle=/MyApp/my_app.aab --output=/MyApp/my_app.apks --mode=universal` (cf. resource 2)
3. After creating this *apks* file we can extract his content `7z x Bugdroid_Fight_-_Part_2.apks`
4. We get an application named *universal.apk* which we can work on

## Resources
1. [What is an AAB file ?](https://www.nextpit.com/what-is-aab-file-android)
2. [How to get an apk from aab](https://docs.catappult.io/docs/extract-your-apps-apks-from-aab-file)