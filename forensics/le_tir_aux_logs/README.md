# Le tir aux logs

## Speech
```
Il semblerait qu'une personne malveillante ait réussi à se connecter sur le site d'inscription d'une compétition de tir à l'arc.
Aidez-nous à investiguer sur cette attaque via le fichier de logs de notre serveur. Quel est l'URL complète qui a permis de se connecter de manière frauduleuse ?

Le flag attendu est l'URL utilisée par l'attaquant pour exploiter une vulnérabilité du site avec succès, entouré du format habituel.
Par exemple, si l'attaquant se rend sur la page https://example.com?authenticated=1 pour se connecter de manière frauduleuse, le flag sera 404CTF{https://example.com?authenticated=1}.
Par ailleurs, toutes les IP utilisées sont fictives et non pertinentes.
```

## Analysis
1. Only 56 lines, we can see SQLi atline 32/33
2. The good one : 404CTF{http://www.inscription_tir_arc.com/index.php?username=admin%27%23&password=test}

Why ? Because the response is a 302 and the size of the response is 784, just like all other good connection