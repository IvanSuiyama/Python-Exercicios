exp = str(input('Digite uma expressão'))
parenteses = []
for s in exp:
    if s == '(':
        parenteses.append('(')
    elif s == ')':
        if len(parenteses) > 0:
            parenteses.pop()
        else:
            parenteses.append(')')
            break
if len(parenteses) == 0:
    print('Expressão Valida')
else:
    print('Expressão Invalida')
