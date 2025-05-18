sair_2 = None

while True:
    if sair_2 == 's':
        break
    
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    tipo_de_conta = input('Que tipo de conta você deseja realizar (+-*/)?: ')
    operadores_permitidos = '+-*/'

    if numero_1.isdigit() and numero_2.isdigit():
        numero_1 = int(numero_1)
        numero_2 = int(numero_2)
    else:
        print('Digite apenas números.')

    if tipo_de_conta not in operadores_permitidos:
        print('Um ou ambos os operadores digitados são inválidos.')
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
        sair = input('Você deseja sair? digite [s] para sair e [n] para não sair: ')
        if sair == 's':
            print('Você saiu.')
            sair_2 = sair
            break
        if sair == 'n':
            break
        else:
            print('Apenas s e n são válidos')
            continue