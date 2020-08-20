empleado = {
    'Gabriela': 'DBA',
    'Carlos': 'Marketing',
    'Jorge': 'Developer Senior',
    'Maria': 'Seguridad'
}

valor = 0

print('\n****Bienvenido al menu de empleado****\n')

while valor == 0 :
    nombre = input('\nIngrese nombre de empleado\n -> ')
    print('\n ****Departamento****\n')
    buscar = 0

    for emp,depart in empleado.items():
        if emp == nombre:
            print('--> '+depart)
            buscar = 1

    if buscar == 0:
        print('--> No Existe empledo..!!')
        valor=1


'''
print('\n ****.empleado****')
for e in empleado :
    print(e)

print('\n ****empleado.keys()****')

for k in empleado.keys():
    print(k)

print('\n ****empleado.items()****')

for i,numero in empleado.items():
    print(i,' ',numero)
'''