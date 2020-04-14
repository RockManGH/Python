# -*- coding: utf8 -*-
# Jeu ZCasino

import os
import time
import fonction_ZCasino
import fonction_gamer
import fonction_history

from datetime import datetime


# message for welcome
print ("\n 		 jeu ZCasino \n")
print ("   le Random magic en 0 et 5 :) ")

# identification gamer
rept=True
while rept == True :
	cg= input ("Vous avez déjà un compte, entrer 1 si non 0 pour créer un nouveau :")
	
	if fonction_ZCasino.controle_int(cg) == True :
		cg=int(cg)
		if cg == 1 :
			player =fonction_gamer.connexion_gamer()
			# show stat last play
			print(" hisotique de votre dernier jeu : \n")
			print ("date :{}\n".format(player["lasteplay"]))
			print ("vous aviez misé(e) :{}€\n".format(player["bet"]))
			print ("votre solde :{}\n".format(player["balance"]))
			rept =False
		elif cg ==0 :
			player=fonction_gamer.new_gamer()
			print("\n bienvenue au jeu ZCasino")
			rept= False
		else :
			print ("Merci de saisir 1 ou 0 ")		
			pass
	else :
		rept = True


rept = True
while rept == True:
	ch=input ("voulez vous commencer une nouvelle partie tapez 'N' si non 'H' pour tous vos hisotiques :")
	if ch.lower() == 'n': 
		rept =False
	elif ch.lower() == 'h':
		fonction_history.history_play(player)
		rept=False
	else:
		print ("Merci de faire le bon choix")
		rept = True

#inint calc nombre play
nbrg=1
# boucle for repet play
jouer = True
while jouer  :
	if player ["balance"] == 0:
		rept = True
		while rept == True: 
			nbr = input ("\nentre votre mise en €:")
			if fonction_ZCasino.controle_int(nbr) == True :
				player ["bet"]+=int(nbr)
				player["balance"]=int(nbr)
				rept = False
			else :
				rept = True
	rept = True

	while rept == True: 
		nbr = input ("Merci de saisir un chiffre en 0 et 5 :")
		if fonction_ZCasino.controle_int(nbr) == True :
			nbr = int(nbr)
			if fonction_ZCasino.controle_nbruser(nbr) == True:
				nbruser=int(nbr)
				rept = False
		else :
			rept = True

	randnbr = fonction_ZCasino.randnbr()
	print ("\n Suspense... Recherche du chiffre gagnant en cours ... ")
	time.sleep(1)
	print (" \nle chiffre gagnant est : {}".format(randnbr))

	#appel de la fonction pour contrler le type du chiffre	
	npoim = fonction_ZCasino.paire_impaire(nbruser)	
	rpoim = fonction_ZCasino.paire_impaire(randnbr)	

	# indiquer que le choix random est le gagnon
	if randnbr == nbruser :
		player["balance"] = int(player["balance"]) * 3

		print (" \nvous venez de gagner : {} €".format(player["balance"]))

	elif npoim == rpoim:		
		#si oui rendre 50% de la somme misé 
		player["balance"] = int(player["balance"]) /2

		if npoim == True and rpoim == True :
			print("\n le chiffre gagant est raté ")
			print ("\nMais puisque les chiffres sont du même type paire, vous garder 50% de votre mise")
		else :
			print("\n le chiffre gagant est raté ")
			print ("\nMais puisque les chiffres sont du même type paire, vous garder 50% de votre mise")

	#si non solde misée est perdu 
	else :
		print ("\nle chiffre entrer et le chiffre gagant sont des types différents, vous avez tout perdu ")
		player["balance"] =0

	#afficher le solde du joueur 
	print (" \nvotre solde actuelle est: ",player["balance"],"$")

	# proposer de jouer à nouveau ou quitter 
	jouer = input ("\n pour jouer à nouveau taper entrer si non Q pour quitter :")
	if jouer.lower() == 'q': 		
		jouer = False
		player["lasteplay"]=datetime.now().isoformat(timespec='minutes')
		player["nbrg"] =player["nbrg"]+ nbrg

		print (" Au revoir {} \n vous avez jouer en total {} fois \n vous avez misé(e) un total de : {}€ \n vos parter avec un solde de :{}€ "
			.format(player["login"],player["nbrg"],player["bet"],player["balance"]))

		# save information user in file gamer.txt
		fonction_gamer.save_play_gamer(player)
	else :
		jouer = True
		nbrg += 1


