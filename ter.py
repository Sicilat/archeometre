import keyboard
import os
import time

x_ref = 0
y_ref = 0
z_ref = 0
cap_a = 1
cap_b = 2
cap_c = 3
x_pos = 0
y_pos = 0
z_pos = 0

def clear():
	os.system('clear||cls')

def menu(x_ref, y_ref, z_ref, cap_a, cap_b, cap_c, x_pos, y_pos, z_pos):
	clear()
	print('Archeometre V0.1')
	print(' ')
	print('Référentiel : ')
	print(' ')
	print('X = ', end='')
	print(x_ref)
	print('Y = ', end='')
	print(y_ref)
	print('Z = ', end='')
	print(z_ref)
	print(' ')
	print('Valeurs des capteurs : ')
	print(' ')
	print('Capteur A : ', end='')
	print(cap_a)
	print('Capteur B : ', end='')
	print(cap_b)
	print('Capteur C : ', end='')
	print(cap_c)
	print(' ')
	print('Positions calculées : ')
	print(' ')
	print('X = ', end='')
	print(x_pos)
	print('Y = ', end='')
	print(y_pos)
	print('Z = ', end='')
	print(z_pos)
	print(' ')
	print('Commandes : ')
	print(' ')
	print('A -> Changer le référentiel sur X')
	print('Z -> Changer le référentiel sur Y')
	print('E -> Changer le référentiel sur Z')
	print('Q -> Calculer')
	print('S -> Reset des capteurs')
	print('F -> Copier les valuers dans un .txt')
	print('D -> Copier les valeurs dans le presse-papier')
	print('R -> Quitter l\'interface')

def calcul(x_ref, y_ref, z_ref, cap_a, cap_b, cap_c, x_pos, y_pos, z_pos):
	x_pos = 1
	y_pos = 1
	z_pos = 1
	return x_pos, y_pos, z_pos

while True:
	menu(x_ref, y_ref, z_ref, cap_a, cap_b, cap_c, x_pos, y_pos, z_pos)
	if keyboard.is_pressed('r'):
		clear()
		exit()
	elif keyboard.is_pressed('s'):
		cap_a = 0
		cap_b = 0
		cap_c = 0
	elif keyboard.is_pressed('f'):
		f = open('./log.txt', "w+")
		print(cap_a, file=f)
		print(cap_b, file=f)
		print(cap_c, file=f)
		f.close()
	elif keyboard.is_pressed('q'):
		x_pos, y_pos, z_pos = calcul(x_ref, y_ref, z_ref, cap_a, cap_b, cap_c, x_pos, y_pos, z_pos)
	time.sleep(0.1)

