from math import *

while True:
	capA = int(input('Capteur A > '))
	capB = int(input('Capteur B > '))
	capC = int(input('Capteur B > '))
	print('Lancement des calculs...')
	Z = ((capB * capB) - (capC * capC) + 1) / 2
	X = ((capA * capA) - (capB * capB) - 1) / (-2)
	if (capB * capB) - (X * X) - (Z * Z) < 0:
		print('Point introuvable !')
		print('Valeurs incorrectes !')
		print('Calcul de la position arrétée')
	else:
		Y = sqrt((capB * capB) - (X * X) - (Z * Z)) * -1
		print('X = ' + str(X))
		print('Y = ' + str(Y))
		print('Z = ' + str(Z))
		print('')