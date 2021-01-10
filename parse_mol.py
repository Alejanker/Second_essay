def parse_mol(formula, i=0):
    number = None

    name = ''
    mol = {}

    temporal = 0

    while i < len(formula):
        it = formula[i]

        if it in (')', ']', '}'):
            if i + 1 < len(formula):
                for idx in formula[i+1:]:
                    if idx.isdigit():
                        if number == None:
                            number = idx
                        else:
                            number += idx
                        i += 1
                    else:
                        break
                
            if number == None:
                return mol, i 
            else:
                number = int(number)

                for idx in mol:
                    mol[idx] *= number
                
                return mol, i

        elif it in ('(' , '[', '{'):
            second , i = parse_mol(formula, i+1)

            for idx in second:
                if idx in mol:
                    mol[idx] += second[idx]
                else:
                    mol[idx] = second[idx]

        elif it.isdigit():
            number = ''
            for idx in formula[i:]:
                if idx.isdigit():
                    number += idx
                    i += 1
                else:
                    break
            
            number = int(number)
            valor = number + (mol[name] if name in mol else 0)
            
            if temporal == 1:
                valor -= 1

            mol[name] = valor

            number = None
            temporal = 0
            continue
            
        else:
            valor = 1
            for idx in formula[i:]:
                if idx.isupper() and valor:
                    name = idx
                    valor -= 1
                elif idx.islower():
                    name += idx
                    i += 1
                else:
                    break

            mol[name] = (mol[name] if name in mol else 0) + 1
            temporal = 1  
    
        i += 1

    return mol, i


if __name__ == '__main__':
    formula = input('Mol: ')

    a, _ = parse_mol(formula)

    print(a)