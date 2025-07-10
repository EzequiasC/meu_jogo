from random import randint
from time import sleep

itens = ('Pedra', 'Papel', 'Tesoura', 'Lagarto', 'Spock') ### itens da minha lista
computador = randint(0,4) ### computador esolhendo um dos itens

print(''' REGRAS DO JOGO 
      
      As regras de Pedra-papel-tesoura-lagarto-Spock são:

- Tesoura corta papel
- Papel cobre pedra
- Pedra esmaga lagarto
- Lagarto envenena Spock
- Spock esmaga (ou derrete) tesoura
- Tesoura decapita lagarto
- Lagarto come papel
- Papel refuta Spock
- Spock vaporiza pedra
- Pedra amassa tesoura
      
 ''') ### REGRAS DO JOGO


print(''' Sua opções: 
[0] PEDRA 🪨
[1] PAPEL 🧻
[2] TESOURA ✂️
[3] LAGARTO 🦎
[4] SPOCK 🖖
      ''') ### OPÇÕES PARA A ESCOLHA DO JOGADOR

jogador = int(input('Qual a sua jogada? '))

print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PO')
sleep(1)

print('--' * 10)
print(f'O computador jogou {itens[computador]}') ## mostra na tela qual foi a escolha do computador
print(f'O jogador jogou {itens[jogador]}') ## mostra na tela qual foi a escolha do jogador 
print('--' * 10)

if computador == 0: ### COMPUTADOR JOGOU PEDRA
    if jogador == 0:
        print(f'EMPATE')
    elif jogador == 1:
        print(f'VOCÊ GANHOU..... ')
        print(f'Bora pra próxima ')
    elif jogador == 2:
        print(f'EU VENCI')
    elif jogador == 3:
        print('EU VENCI: PEDRA ESMAGA LAGARTO')
    elif jogador == 4:
        print('VOCÊ VENCEU: SPOCK VAPORIZA PEDRA')
    else:
        print(f'jogada invalida: ')
elif computador == 1: ### COMPUTADOR JOGOU PAPEL
    if jogador == 0:
        print(f'EU VENCI ')
    elif jogador == 1:
        print(f'EMPATE')
    elif jogador == 2:
        print(f'VOCÊ GANHOU..... ')
        print(f'Bora pra próxima ')
    elif jogador == 3:
        print('VOCÊ VENCEU: LAGARTO COME PAPEL')
    elif jogador == 4:
        print('EU VENCI: PAPEL REFUTA SPOCK')
    else:
        print(f'jogada invalida ')
elif computador == 2: ### COMPUTADOR JOGOU TESOURA
    if jogador == 0:
        print(f'VOCÊ GANHOU..... ')
        print(f'Bora pra próxima ')
    elif jogador == 1:
        print(f'EU VENCI ')
    elif jogador == 2:
        print(f'EMPATE')
    elif jogador == 3:
        print('EU VENCI: TESOURA DECAPITA LAGARTO')
    elif jogador == 4:
        print('VOCÊ VENCEU: SPOCK QUEBRA TESOURA')
        print(f'Bora pra próxima ')
    else:
        print(f'jogada invalida: ')
elif computador == 3: ### COMPUTADOR JOGOU LARGARTO
    if jogador == 0:
        print(f'VOCÊ GANHOU: PEDRA ESMAGA LARGARTO')
    elif jogador == 1:
        print('EU VENCI: LARGARTO COME PAPEL ')
    elif jogador == 2:
        print('VOCÊ GANHOU: TESOURA DECAPITA LARGARTO ')
        print(f'Bora pra próxima ')
    elif jogador == 3:
        print('EMPATE')
    elif jogador == 4:
        print('EU VENCI: LARGARTO ENVENENA SPOCK')
    else:
        print(f'jogada invalida: ')
elif computador == 4: ## COMPUTADOR SPOCK
    if jogador == 0:
        print(f'EU VENCI: SPOCK VAPORIZA PEDRA')
    elif jogador == 1:
        print(f'VOCÊ VENCEU: PAPEL REFUTA SPOCK')
        print(f'Bora pra próxima ')
    elif jogador == 2:
        print(f'EU VENCI: ESMAGA OU DERRETE Á TESOURA')
    elif jogador == 3:
        print(f'VOCÊ VENCEU: LARGARTO ENVENENA SPOCK ')
        print(f'Bora pra próxima ')
    elif jogador == 4:
        print('EMPATE')
    else:
        print(f'jogada invalida: ')