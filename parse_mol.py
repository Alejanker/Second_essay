
def mol_counter(formula, i):
    
    number = ''
    mol = {}

    while i < len(formula):
        if formula[i].isdigit():
            if number == '':
                number = formula[i]
            else:
                number += formula[i]
            print(number)
            mol[ formula[i-1] ] = int(number)
        
        elif formula[i].isupper() and mol.get(formula[i]) == None:
            mol[ formula[i] ] = 1
        
        else:
            if i-1 > -1 and i -1 < len(formula):
                del mol[ formula[i-1]]

                mol[formula[i-1] + formula[i] ] = 1

        i += 1

    return mol

def parse_molecule (formula):
    # detectar cuandXo estan encerradas en parentesis
    # multiplicar 
    mol = mol_counter(formula, 0)

    return mol
        
        
        


if __name__ == '__main__':
    formula = input('Ingrese formula: ')
    a = parse_molecule(formula)

    print('formula: ' + str(a))
