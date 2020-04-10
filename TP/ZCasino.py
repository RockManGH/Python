# -*- coding: utf8 -*-
# Jeu ZCasino

import os
import random


# boucle pour choix du numéro
print ("\n Bienvenue au jeu ZCasino \n")

jouer = True
while jouer  :
	
	nbruser = -1
	while nbruser <0 or nbruser > 49: 
		
		nbruser = input("\n Merci de choisir un numero entre 0 et 49 :")
		
		try :
			#controle la saisie est bien un int 
			int (nbruser)
			# controle des chiffres négatif
			assert int(nbruser) >= 0 
			assert int (nbruser) <=49
		except ValueError: 
			print ("\nMerci de saisir un chiffre")	
			nbruser = -1
		except AssertionError :
			print ("\nle chiffre choisi est invalide")
			nbruser =-1
		else : nbruser = int(nbruser)		


	print ("\n vous avez choisi le numéro :", nbruser)

	# le joueur doit saisir le somme à miser
	bouvleremise = True
	while bouvleremise  : 
		
		nbrmise = input("\nMerci de choisir la somme que vous voulez miser en $ :")
		
		try : 
			int (nbrmise)
			assert int (nbrmise) > 0
		except ValueError: 
			print ("\nMerci de saisir un chiffre")
				
		except AssertionError 	:
			print ("\nMerci de saisir une somme supérieur à 0$: ")
			
		else : 
			nbrmise = int(nbrmise)		
			bouvleremise = False


	print ("\nvous avez miser la somme de :", nbrmise)


	# choix random d'un chiffre entre 0 et 49
	randnbr = random.randint(0,49)
	print (" \nle chiffre gagnant est : ",randnbr)

	# indiquer que le choix random est le gagnon
	if randnbr == nbruser :
		gain = nbrmise * 3
		print (" \nvous avez gagner : ",gain,"$")
		
	else : 
		print ("\n vous avez perdu")

	# vérifier si le n° choisi fait parti des pairs ou impaire 
	if (nbruser %2 == 0) :
		npoim = True
	else :
		npoim = False

	# verifier le n° random est paire ou impaire 
	if (randnbr %2 == 0) :
		rpoim = True
	else :
		rpoim = False

	# controler si le n° choisi et le random sont tous les deux paire ou impaire
	if npoim == rpoim :

		#si oui rendre 50% de la somme misé 
		nbrmise = nbrmise /2
		#si non solde misée est perdu 
	else :
		nbrmise =0
	#afficher le solde du joueur 

	print (" \nvotre solde actuelle est: ",nbrmise,"$")

	# proposer de jouer à nouveau ou quitter 
	jouer = input ("\n pour jouer à nouveau taper entrer si non Q pour quitter :")
	if jouer.lower() == 'q': 		jouer = False
	else : jouer = True


