# -*- coding: utf8 -*-
# Jeu ZCasino

import os
import time
import fonction_ZCasino

gamer = {"name":"", "bet":0,"nbrg":1,"balance":0}


print ("\n 		 jeu ZCasino \n")
print (" le Random magic en 0 et 10 :) ")

gamer["name"] = input ("entrer votre nom :") 

# boucle pour choix du numéro
jouer = True
while jouer  :
	if gamer ["balance"] == 0:
		rept = True
		while rept == True: 
			nbr = input ("entre votre mise en €:")
			if fonction_ZCasino.controle_int(nbr) == True :
				gamer ["bet"]+=int(nbr)
				gamer["balance"]=int(nbr)
				rept = False
			else :
				rept = True

	rept = True
	while rept == True: 
		nbr = input ("Merci de saisir un chiffre en 0 et 10 :")
		if fonction_ZCasino.controle_int(nbr) == True :
			nbr = int(nbr)
			if fonction_ZCasino.controle_nbruser(nbr) == True:
				nbruser=int(nbr)
				rept = False
		else :
			rept = True

	randnbr = fonction_ZCasino.randnbr(nbruser)
	print ("\n Suspense... Recherche du chiffre gagnant en cours ... ")
	time.sleep(1)
	print (" \nle chiffre gagnant est : {}".format(randnbr))

	#appel de la fonction pour contrler le type du chiffre	
	npoim = fonction_ZCasino.paire_impaire(nbruser)	
	rpoim = fonction_ZCasino.paire_impaire(randnbr)	

	# indiquer que le choix random est le gagnon
	if randnbr == nbruser :
		gamer["balance"] = int(gamer["balance"]) * 3

		print (" \nvous venez de gagner : {} €".format(gamer["balance"]))

	elif npoim == rpoim:		
		#si oui rendre 50% de la somme misé 
		gamer["balance"] = int(gamer["balance"]) /2

		if npoim == True and rpoim == True :
			print("\n le chiffre gagant est raté ")
			print ("\nMais puisque les chiffres sont du même type paire, vous garder 50% de votre mise")
		else :
			print("\n le chiffre gagant est raté ")
			print ("\nMais puisque les chiffres sont du même type paire, vous garder 50% de votre mise")

	#si non solde misée est perdu 
	else :
		print ("\nle chiffre entrer et le chiffre gagant sont des types différents, vous avez tout perdu ")
		gamer["balance"] =0

	#afficher le solde du joueur 
	print (" \nvotre solde actuelle est: ",gamer["balance"],"$")

	# proposer de jouer à nouveau ou quitter 
	jouer = input ("\n pour jouer à nouveau taper entrer si non Q pour quitter :")
	if jouer.lower() == 'q': 		
		jouer = False
		print (" Au revoir {} \n vous avez jouer {} fois \n vous avez miser un total de : {}€ \n vos parter avec un solde de :{}€ "
			.format(gamer["name"],gamer["nbrg"],gamer["bet"],gamer["balance"]))
	else :
		jouer = True
		gamer["nbrg"]+=1


