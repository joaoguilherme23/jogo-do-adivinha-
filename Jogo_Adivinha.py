# ESTE É O JOGO DO ADIVINHA, INICIANDO NA PROGRAMAÇÃO  

import random

numberSecret = random.randint(1,10)

print('ESTE É O JOGO DO ADIVINHA\nVOCE TEM 6 CHANCES PARA TENTAR ACERTAR O NÚMERO QUE ESTOU PENSANDO de 1 a 10.')
print('VOU PENSAR EM UM NÚMERO SÓ UM MOMENTO..')

while True:
    for i in range(6):
        print(str(i)+'...')

    for numberSecret in range(1,7):
        number = int(input('informe o numero: '))

        if number == numberSecret:
            print('VOCÊ ACERTOU, O NUMERO QUE ESTAVA PENSADO É: ' + str(numberSecret))

        if number > numberSecret:
            print('TENTE NOVAMENTE, COM UM VALOR MENOR')

        elif number < numberSecret:
            print('TENTE NOVAMENTE, COM UM NUMERO MAIOR')

        else:
         break
