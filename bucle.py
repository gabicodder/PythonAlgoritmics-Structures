def potencia(numero,potencia):
    return numero**potencia


def run():
    numero = int(input('Escribe un numero: '))
    limite = 1000
    cont = 0
    resultado = potencia(numero,cont)
    while resultado < limite:
        print(f'{numero} elevado a {cont} es igual a: {resultado}')
        cont = cont + 1
        resultado = potencia(numero,cont)

    print('Fin del bucle.!')

if __name__ == "__main__":
    run()