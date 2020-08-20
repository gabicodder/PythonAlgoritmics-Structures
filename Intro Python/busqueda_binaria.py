objetivo = float(input('\nEscoge un numero\n --> '))
epsilon = 0.001
bajo = 0.0
alto = objetivo
respuesta = (alto + bajo) / 2

while abs(respuesta**2 - objetivo) >= epsilon:
    #print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
    if respuesta**2 < objetivo:
        bajo = respuesta
    else:
        alto = respuesta
    
    respuesta = (alto + bajo) / 2
    #break


print(f'--> La raiz cuadrada del {objetivo} es {respuesta}')