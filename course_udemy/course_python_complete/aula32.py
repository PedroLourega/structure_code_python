"""
Faça um programa que peça ao usuário para digitar um número inteiro, informe se este numero é par ou impar. Caso o usuário não digite um número inteiro, informe que não é um númer inteiro.
"""

entrada = input('Digite um número:')

# if entrada.isdigit():
#     entrada_int = int(entrada)
#     par_impar = entrada_int % 2 == 0 
#     par_impar_texto = 'ímpar'

#     if par_impar:
#         par_impar_texto = 'par'


#     print(f'O número {entrada_int} é {par_impar_texto}')
# else:
#     print('Você nao digitou um numero inteiro')

try:
    entrada_int = int(entrada)
    par_impar = entrada_int % 2 == 0
    par_impar_texto = 'ínpar'

    if par_impar:
        par_impar_texto = 'par'

        print(f'O número {entrada_int} é {par_impar_texto}')

except:
    print("Você não digitou um numero inteiro.")