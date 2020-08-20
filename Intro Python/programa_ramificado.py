nom_1 = input('Ingresa tu nombre:\n')
num_1 = int(input('Ingresa tu edad: \n'))
nom_2 = input('Ingresa el nombre de tu amigo: \n')
num_2 = int(input('Ingresa la edad de tu amigo: \n'))

rest = int(num_1 - num_2)

if num_1 > num_2:
    print(f'{nom_1} es mayor a {nom_2} por {rest} años')
elif num_1 < num_2 :
    
    print(f'{nom_1} es menor a {nom_2} por {rest*-1} años')
else:
    print(f'{nom_1} y {nom_2} tienen la misma edad')