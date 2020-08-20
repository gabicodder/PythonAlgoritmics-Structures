import random


def run():
    numero_aleatorio = random.randint(1,100) 
    numero = int(input('\nEscribe un numero del 1 al 100: '))
    while numero_aleatorio != numero:
          if numero < numero_aleatorio:
              print('\n\tBusca un numero más grande')
          else:
              print('\n\tBusca un numero más pequeño')

          numero = int(input('\t::::Elige otro número: '))

    print('\n\n\t\t*****:::::You WIN..!! =):::::*****')    



if __name__ == "__main__":
    run()