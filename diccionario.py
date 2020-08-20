def run():
    mi_diccionario = {
        'Ecuador': 'Latinos',
        'EEUU': 'Gringos',
        'España': 'Hostia joder!'
    }
    for i,valor in mi_diccionario.items():
        print(f'{i} - {valor}')
    # for i in mi_diccionario.keys():
    #     print(f'\n{i}')
    # for i in mi_diccionario.values():
    #     print(f'\n{i}')
    

if __name__ == "__main__":
    run()