
def run():
    numero = input('Ingresa un numero: ')

    resultante = ''

    for i, l in enumerate(reversed(numero)):
        if i % 3 == 0 and i != 0:
            resultante = '.' + resultante
        
        resultante = l + resultante        
    
    return resultante

if __name__ == '__main__':
    print(run())
