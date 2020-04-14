import pickle
import os



def history_play(dictplayer) :
	#recup nombre dicto in file 
	with open("{}".format(dictplayer["path"]),"rb") as fichier :
		mpick = pickle.Unpickler(fichier)

		rept = True
		nbrdict=0
		while rept == True :	
			try : 
				mpick.load()
			except EOFError:
				rept = False
			else :
				nbrdict +=1		

	with open("{}".format(dictplayer["path"]),"rb") as fichier :
			mpick = pickle.Unpickler(fichier)
			n=1			
			while n<=nbrdict:

				try:
					recup = mpick.load()
				except EOFError:
					break
				else :
					#for k,v in recup.items() :
					#	print (k,v)
					print ("date :{}".format(recup["lasteplay"]))
					print ("cumul de ce que vous aviez misé :{}€".format(recup["bet"]))
					print ("votre solde :{}".format(recup["balance"]))	
					print ("")
		
					n +=1			
				

def last_play(dictplayer):
	#recup nombre dicto in file 
	with open("{}".format(dictplayer["path"]),"rb") as fichier :
		mpick = pickle.Unpickler(fichier)

		rept = True
		nbrdict=0
		while rept == True :	
			try : 
				mpick.load()
			except EOFError:
				rept = False
			else :
				nbrdict +=1		

	with open("{}".format(dictplayer["path"]),"rb") as fichier :
		mpick = pickle.Unpickler(fichier)
		n=1			
		while n<=nbrdict:
			try:
				recup = mpick.load()
			except EOFError:
				break
			else :
				last_play=recup

	return last_play