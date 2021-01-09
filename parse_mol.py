
def mol_counter(formula, i):
    
    i = i
    last = ''
    mol = {}
    number = ''
  
    while i < len(formula):
        # print(formula[i])
        if formula[i] in ('(', '[', '}'):
          
            second, i = mol_counter(formula, i+1)
            for idx in second:
                if mol.get(idx) != None:
                    mol[idx] += second[idx]
                    print(mol)
                else:
                    mol[idx] = second[idx]
                    print('mol idx', mol[idx], idx)
            print('i', i, 'len', len(formula))

        elif formula[i] in (')','}',']'):
            try:
                if formula[i+1].isdigit():
                    number = int(formula[i+1])
                    for idx in mol:
                        mol[idx] *= number
                    return mol , i 
                else:
                    return mol , i 
            except IndexError:
                return mol , i
                
        elif formula[i].isdigit():
            if name != "":
                name += formula[i]
            else:
                name = formula[i]

            mol[last] = int(name)
            i += 1
            continue

        elif not formula[i].islower() and mol.get(formula[i]) == None:
            mol[formula[i]] = 1
            last = formula[i]
        else:
            if mol.get(last):
                del mol[last]
            
            mol[last + formula[i]] = 1
            last = last + formula[i]

        i += 1
        name = ""

    return mol , i


def parse_molecule (formula):
    # detectar cuandXo estan encerradas en parentesis
    # multiplicar 
    mol, _ = mol_counter(formula, 0)

    return mol
        
        
        


if __name__ == '__main__':
    formula = input('Ingrese formula: ')
    a = parse_molecule(formula)

    print('formula: ' + str(a))
