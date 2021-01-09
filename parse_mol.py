
def mol_counter(formula, i):
    last_integer = None
    mol = {}

    while i < len(formula):
        it = formula[i]

        if it.isdigit():
            if flast_integer == None:
                last_integer = it
            else:
                last_integer += it
            mol[it] = int(last_integer)
            
        elif it.isupper() and mol.get(it) == None:
            mol[it] = 1
        elif it.islower():
            if i - 1 > -1:
                del mol[formula[i-1]]
                mol[formula[i - 1] + it] = 1
            
        i += 1
             
            


def parse_molecule (formula):
    # detectar cuandXo estan encerradas en parentesis
    # multiplicar 
    mol = mol_counter(formula, 0)

    return mol
        
        
        


if __name__ == '__main__':
    formula = input('Ingrese formula: ')
    a = parse_molecule(formula)

    print('formula: ' + str(a))
