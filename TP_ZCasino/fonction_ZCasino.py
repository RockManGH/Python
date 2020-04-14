import random
import pickle
import fonction_history



def paire_impaire (nbr):
	""" fonction for controle type nombre"""
	if (nbr %2 == 0) :
		nbr = True
	else :
		nbr = False
	return (nbr)

def randnbr() :
	"""Fonction for return a random nombre"""
	randnbr = random.randint(0,5)
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
	""" fonction for controle usernbr between 0 and 5 """
	if nbr < 0 or nbr > 5 :
		print ("\nMerci de saisir un chiffre entre 0 et 5\n ")
	else :
		return True

