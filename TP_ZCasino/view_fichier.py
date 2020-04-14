import pickle

#recup nombre dicto in file 
with open("gamer.txt","rb") as fichier :
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
			rept = True	

			
with open("gamer.txt","rb") as fichier :
		mpick = pickle.Unpickler(fichier)
		n=1			
		while n<=nbrdict:

			try:
				recup = mpick.load()
			except EOFError:
				break
			else :
				for k,v in recup.items() :
					print (k,v)	
				pass
				
		
