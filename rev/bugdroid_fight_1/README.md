# Bugdroid Fight 1/2

## Speech
```
Un Bugdroid sauvage apparait !
Il est temps de mettre vos compétences de boxe en pratique, mais attention, cette fois il n'y a ni ring ni arbitre. Assurez-vous de bien observer autour de vous car, comme sur le ring, il est important de connaître les habitudes de son adversaire. Bon courage,
Retrouvez le message du Bugdroid.
Format de flag : 404CTF{message}
```

## Basic static
1. It's an APK, so lets install `sudo apt-get insatall jd-gui dex2jar`
2. Now transform the APK to JAR via dex2jar : `d2j-dex2jar Bugdroid_Fight_-_Part_1.apk`
3. Now fire up jd-gui
![Overview](./img/00_overview.png)
4. We see an airbnb.lottie and they are a lot of thing in it, it might be a rabbit hole, I think they used a real app and add some malicious things. We are looking for a message, so I go in the *MainActivity.class* of  *example.reverseintro* but nothing very interesting but we have the *MainActivityKt.class* to look at
5. The code is obfuscated and long, but after a little bit of reading I get that :
![MainActivityKt.class](./img/01_main_activity_kt.png)
6. The message is : `"Br4v0_tU_as_" + StringResources_androidKt.stringResource(R.string.attr_special, paramComposer, 0) + (new Utils()).lastPart)`
7. By clicking on `Utils().lastPart` I get this : 
```Java
public class Utils {
  String lastPart = "_m3S5ag3!";
}
```
8. Just to get the middle part : `StringResources_androidKt.stringResource(R.string.attr_special, paramComposer, 0)` I know `R.string.attr_special` is 2131492905
