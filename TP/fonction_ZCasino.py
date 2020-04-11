import random


def paire_impaire (nbr):
	""" fonction for controle type nombre"""
	if (nbr %2 == 0) :
		nbr = True
	else :
		nbr = False
	return (nbr)

def randnbr(nbr) :
	"""Fonction for return a random nombre"""
	randnbr = random.randint(0,nbr)
	return randnbr

def controle_int(nbr):
	""" fonction for controle int """
	try :
		int (nbr)
	except ValueError: 
		print ("\nMerci de saisir un chiffre")		
	else : 
		return True	

def controle_nbruser(nbr):
	""" fonction for controle usernbr between 0 and 10 """
	try :
		 nbr > 0 and nbr <= 10
	except ValueError :
		print ("Merci de saisir un chiffre entre 0 et 10 ")
	else :
		return True