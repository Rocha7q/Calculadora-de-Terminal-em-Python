sair = None

while True:

    if sair == 's':
        break

    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    tipo_de_conta = input('Que tipo de conta você quer realizar (+-*/)?: ')

    if numero_1.isdigit() and numero_2.isdigit():
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    
    operadores_permitidos = '+-*/'

    if tipo_de_conta not in operadores_permitidos:
        print('Um ou ambos os operadores digitados não são válidos')
        continue

    if numero_1 and numero_2 is int:
        ...

    elif tipo_de_conta == '+':
        print(numero_1 + numero_2)

    elif tipo_de_conta == '-':
        print(numero_1 - numero_2)

    elif tipo_de_conta == '*':
        print(numero_1 * numero_2)
    
    elif tipo_de_conta == '/':
        print(numero_1 / numero_2)

    while True:
        sair = input('Você quer sair? Digite [s] para sim e [n] para não: ')

        if sair == 's':
            print('Você saiu.')
            break
        
        elif sair == 'n':
            break
        
        else:
            print('Apenas s e n são válidos.')
            continue
