from datetime import datetime
import pickle
import fonction_ZCasino
import pathlib
import fonction_history


#recup nombre players in file ./gamers/nombre_players.txt
with open ('./gamers/nombre_players.txt','r') as fichier :
	nbrp=int(fichier.read())


def new_gamer():
	"""  save new gamer in the file gamer.txt"""
	print ("\n Création de nouvelle fiche gamer ")
	gamer = {}

	gamer["id"] = nbrp + 1
	gamer["DateCreat"] = datetime.now().isoformat(timespec='minutes')
	gamer["login"]=input ("entre votre login :")
	gamer["passw"]= input("entre votre mot de passe :")
	gamer["bet"]=0
	gamer["nbrg"]=0
	gamer["balance"]=0
	gamer["lasteplay"]=datetime.now().isoformat(timespec='minutes')
	gamer["path"] = "./gamers/player{}.txt".format(nbrp)

	with open('./gamers/player{}.txt'.format(nbrp),'ab') as fichier :
		mpick = pickle.Pickler(fichier)
		mpick.dump(gamer)

	with open ('./gamers/nombre_players.txt','w') as fichier :
		fichier.write(str(nbrp+1))

	return gamer


def connexion_gamer():

	rept = True
	while rept == True:
		
		login = input("entrer votre login :")
		feed =1
		while feed < nbrp:
			# read content file
			with open('./gamers/player{}.txt'.format(feed),"rb") as text :
				mpick = pickle.Unpickler(text)
				dictplayer = mpick.load()

				#feed login in dict player
				for k,v in dictplayer.items() :
					if k == "login" and v == login :
						#init true login for control passw
						login = True	
						
			feed += 1
				
		if login != True :
			print("votre login est inconnu")
			rept = input (" Pour réessayer taper Entrer, si non 'N' pour créer un nouveau profil :")
			if rept.lower() == "n" :
				new_gamer()
				rept = False
			else :
				rept = True	


		# control password gamer 					
		if login == True :	
	
			rept = True		
			while rept == True :
				passw = input("entrer votre mot de passe :")

				for k,v in dictplayer.items():
					if k == "passw" and v == passw :
						passw = True	

				if passw == True :
					print ("\nconnexion réussi ")
					history=fonction_history.last_play(dictplayer)
					rept = False
				else :	
					print (" \n mot de passe incorrect , réessayez à nouveau")		
					rept = True	

	return history										
					


def save_play_gamer(player):

	with open("{}".format(player["path"]),"ab") as fichier :
		mpick = pickle.Pickler(fichier)
		mpick.dump(player)	

					 



			

	


