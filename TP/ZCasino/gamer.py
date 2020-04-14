
import pickle
import pdb


#recup nombre dicto in file 
with open("gamer.txt","rb") as fichier :
	mpick = pickle.Unpickler(fichier)

	 
	rept = True
	i=0
	while rept == True :	
		try : 
			mpick.load()
		except EOFError:
			rept = False
		else :
			i +=1
			rept = True	



#print dicto in file
with open("gamer.txt","rb") as fichier :
	mpick = pickle.Unpickler(fichier)
	n=1			
	while n<=i:

		try:
			recup = mpick.load()
		except EOFError:
			break
		else :
			for k,v in recup.items() :
				print (k,v)	
			pass
			
		
