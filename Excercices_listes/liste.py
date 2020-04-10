#liste


import random

liste1 = []

rept = True

while rept == True :
	nbr =input ("Entrez un chiffre ou taper T pour terminer : ")
	if nbr =="T" or nbr == "t":
		rept = False 
	else :
		try :
			nbr =int(nbr)
		except ValueError :
			print ("Merci de saisir un chiffre ")
			rept = True
		else :
			liste1.append(nbr)
			rept = True	



print ("\nles chiffre entrer sont :")
for i in liste1 :
	print (" - {}".format(i))

print ("\nle nombre d'élément dans la liste est : {} ".format(len(liste1)))

print ("\nle chiffre max dans la liste est : {}".format(max(liste1)))

print ("\nle chiffre min dans la liste est : {}".format(min(liste1)))

print (" \nla somme de la liste est : {} \n".format(sum(liste1)))

print ("\n chiffre aléatoir de la liste avec choice: {}".format(random.choice(liste1)))

print ("\n chiffre aléatoir de la liste avec randint: {}".format(random.randint(0,len(liste1)-1)))

random.shuffle(liste1)
print ("\n élément de liste mélanger avec shuffle : {}".format(liste1))


print ("\n échantillon de 2 élément de la liste: {}".format(random.sample(liste1,2)))