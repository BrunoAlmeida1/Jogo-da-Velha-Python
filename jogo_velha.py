# Minha Melhor Versão do Jogo da Velha

from random import randint
from time import sleep

veia = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

# Função que altera os valores da matriz conforme o valor digitado no teclado, ou o valor sorteado pelo computador


def posiçao(p, l):
    x = 0
    while x == 0:
        for i in range(3):
            l1 = 7
            l2 = 4
            l3 = 1
            for k in range(3):
                if i == 0:
                    if p == l1 and veia[i][k] == ' ':
                        veia[i][k] = l
                        x = 1
                        break
                elif i == 1:
                    if p == l2 and veia[i][k] == ' ':
                        veia[i][k] = l
                        x = 1
                        break
                elif i == 2:
                    if p == l3 and veia[i][k] == ' ':
                        veia[i][k] = l
                        x = 1
                        break
                l1 += 1
                l2 += 1
                l3 += 1
        if i == 2 and x == 0:
            if jogo == 2 or player % 2 != 0:
                print('Posição Ocupada! Tente em outra posição.')
                p = int(input('Digite a posição: '))
            else:
                p = randint(1, 9)


print('                  JOGO DA VELHA              \n')
print('Para jogar digite a posição de acordo com o\n'
      'seu teclado númerico, sendo 7-8-9 a primeira\n'
      'linha, 4-5-6 a segunda linha e 1-2-3 a terceira.\n')

print(' 7 | 8 | 9 ')
print('---+---+---')
print(' 4 | 5 | 6 ')
print('---+---+---')
print(' 1 | 2 | 3 ')
print('---+---+---\n')

msg = 'Se deseja jogar contra a máquina digite (1), \nmas se deseja jogar contra outro jogador digite (2): '
while (jogo := int(input(msg))) not in (1, 2):
    print('Opção Inválida!')

# Neste trecho do código é sorteado o jogador que irá iniciar o jogo. Além disso, é nesse trecho que possibilita os jogadores ou a máquina fazer a jogada.

turno = 0
player = randint(0, 1)
while True:
    turno += 1
    if player % 2 != 0:
        print('\nJogador 1, sua vez!')
        pos = int(input('Jogador 1 faça sua jogada: '))
        let = 'X'
        posiçao(pos, let)
        player += 1

        print(f' {veia[0][0]} | {veia[0][1]} | {veia[0][2]} ')
        print('---+---+---')
        print(f' {veia[1][0]} | {veia[1][1]} | {veia[1][2]} ')
        print('---+---+---')
        print(f' {veia[2][0]} | {veia[2][1]} | {veia[2][2]} ')
        print('---+---+---\n')

    else:
        if jogo == 1:
            print('Deixe-me pensar na minha jogada...')
            sleep(1.5)
        else:
            print('Jogador 2, sua vez!')

        if jogo == 1:
            pos = randint(1, 9)
            let = 'O'
            posiçao(pos, let)
            player += 1
        else:
            pos = int(input('Jogador 2 faça sua jogada: '))
            let = 'O'
            posiçao(pos, let)
            player += 1

        print(f' {veia[0][0]} | {veia[0][1]} | {veia[0][2]} ')
        print('---+---+---')
        print(f' {veia[1][0]} | {veia[1][1]} | {veia[1][2]} ')
        print('---+---+---')
        print(f' {veia[2][0]} | {veia[2][1]} | {veia[2][2]} ')
        print('---+---+---')

    # Enfim, é aqui onde o programa calcula se houve um vencedor ou se o jogo deu empate

    fim = False
    win = 0
    for x in range(3):
        if veia[x][0] != ' ' and veia[x][0] == veia[x][1] == veia[x][2]:
            win = 1
    for x in range(3):
        if veia[0][x] != ' ' and veia[0][x] == veia[1][x] == veia[2][x]:
            win = 1
    if veia[0][2] != ' ' and ((veia[0][2] == veia[1][1] == veia[2][0]) or (veia[0][0] == veia[1][1] == veia[2][2])):
        win = 1
    if win == 1:
        break
    if turno == 9:
        fim = True
        print('Fim de Jogo! Deu Velha!')
        break
if not fim:
    if player % 2 == 0:
        print('Fim de Jogo. Jogador 1 ganhou!')
    elif jogo == 2:
        print('Fim de Jogo. Jogador 2 ganhou!')
    else:
        print('Fim de jogo. Eu ganhei!')
