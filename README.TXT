Jenny Diep 20036864
Charbel Machaalani 20204556

-- REPO LINK -- 
https://github.com/jenoschan/TP1_IFT3913 

-- DOCUMENTATION --
-------------------------------------------------------------------------------------------------------------
pour utiliser jls.exe: 

rouler le programme avec le dossier contenant les fichiers code comme entrée.

exemple de commande : start jls.exe java
-------------------------------------------------------------------------------------------------------------
pour utiliser nvloc.exe:

Assurez-vous d'avoir roulé le programme jls.exe avant nvloc pour avoir le fichié tp_1.csv que nvloc doit utiliser.
roulez nvloc.exe en fournissant comme seule commande un fichier .java dans le dossier que vous désirez. le programme écrira
le nvloc pour chaque fichier .java dans le dossier dans la colonne nvloc de tp_1.csv en même temps d'imprimer le nvloc pour le fichier
fournie comme argument dans le terminal. (la colonne nvloc est écrite dans le tp_1.csv pour ensuite être utilisée par egon.exe.

exemple de commande: start nvloc.exe "C:\Users\charb\OneDrive\Desktop\qualite\Tp1_final\TP1_IFT3913-main\final\java\org\jfree\chart\annotations\AbstractAnnotation.java"

!! ATTENTION !! toujours rouler nvloc.exe avant lcsec.exe pour avoir les bonnes titres de colonnes pour les fichier csv générés par egon.exe
-------------------------------------------------------------------------------------------------------------------------------
pour utiliser lcsec.exe:

rouler le programme avec le dossier contenant les ficheirs java comme premier argument puis le fichier tp_1.csv généré par jls.exe comme deuxième argument

esemple de commande: start lcsec.exe java tp_1.csv

!! ATTENTION !! lcsec.exe prend du temps pour rouler. SVP attendre environ 3 minutes avant d'ouvrir tp_1.csv pour voir la colonne csec s'ajouter
--------------------------------------------------------------------------------------------------------------------------------------------------
pour utiliser egon.exe:

assurez vous d'avoir roulé les programmes dans l'ordre suivant: jls.exe, nvloc.exe, lcsec.exe

executez egon.exe avec le folder avec toutes les fichier java comme premier argument puis le seuil % comme deusieme argument

egon.exe va générer le fichier tp_1B qui va contenir les classes supérieures au seuil entré en parametre
