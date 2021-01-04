
def run():
    numero = input('Ingresa un numero entero: ')
    contador = 0
    resultante = ''
    for i in reversed(numero):

        if contador == 3:
           resultante = '.' + resultante 
           contador = 0
       
        contador += 1 
        resultante = i + resultante
        
    
    return resultante

if __name__ == '__main__':
    print(run())
