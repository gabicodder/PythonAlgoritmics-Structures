print('\n\n****--FACTORIAL DE UN NUMERO--****')
numero = int(input('\nIngresa un numero \n--> '))

def menu():
    print(factorial(numero))
    
def factorial(n):
    '''Calcula el factorial de n.

    n int > 0
    returns n!
    '''
    #print(f'{n} * {n - 1} = {n * (n-1)}')
    if n == 1:
        return 1
    return n * factorial(n - 1)
    
            
menu()