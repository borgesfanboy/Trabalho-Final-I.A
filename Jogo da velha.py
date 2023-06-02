import pygame
import random


pygame.init()


largura = 300
altura = 300
tamanho_celula = 100
cor_fundo = (255, 255, 255)
cor_linhas = (0, 0, 0)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Jogo da Velha')


vazio = ' '
jogador = 'X'
ia = 'O'


def criar_tabuleiro():
    tabuleiro = []
    for _ in range(3):
        linha = [vazio] * 3
        tabuleiro.append(linha)
    return tabuleiro

def desenhar_tabuleiro(tabuleiro):
    tela.fill(cor_fundo)
    for linha in range(3):
        for coluna in range(3):
            pygame.draw.rect(tela, cor_linhas, (coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula), 1)
            if tabuleiro[linha][coluna] != vazio:
                fonte = pygame.font.Font(None, 80)
                texto = fonte.render(tabuleiro[linha][coluna], True, cor_linhas)
                pos_x = coluna * tamanho_celula + tamanho_celula // 2 - texto.get_width() // 2
                pos_y = linha * tamanho_celula + tamanho_celula // 2 - texto.get_height() // 2
                tela.blit(texto, (pos_x, pos_y))
    pygame.display.flip()


def verificar_vencedor(tabuleiro):
    
    for linha in range(3):
        if tabuleiro[linha][0] == tabuleiro[linha][1] == tabuleiro[linha][2] != vazio:
            return tabuleiro[linha][0]

    for coluna in range(3):
        if tabuleiro[0][coluna] == tabuleiro[1][coluna] == tabuleiro[2][coluna] != vazio:
            return tabuleiro[0][coluna]

  
    if tabuleiro[0][0] == tabuleiro[1][1] == tabuleiro[2][2] != vazio:
        return tabuleiro[0][0]
    if tabuleiro[0][2] == tabuleiro[1][1] == tabuleiro[2][0] != vazio:
        return tabuleiro[0][2]

    
    if not any(vazio in linha for linha in tabuleiro):
        return 'Empate'

    return None


def jogada_ia(tabuleiro):
    
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == vazio:
                tabuleiro[linha][coluna] = ia
                if verificar_vencedor(tabuleiro) == ia:
                    return

                tabuleiro[linha][coluna] = vazio

    
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == vazio:
                tabuleiro[linha][coluna] = jogador
                if verificar_vencedor(tabuleiro) == jogador:
                    tabuleiro[linha][coluna] = ia
                    return

                tabuleiro[linha][coluna] = vazio


    jogadas_disponiveis = []
    for linha in range(3):
        for coluna in range(3):
            if tabuleiro[linha][coluna] == vazio:
                jogadas_disponiveis.append((linha, coluna))

    if jogadas_disponiveis:
        linha, coluna = random.choice(jogadas_disponiveis)
        tabuleiro[linha][coluna] = ia


def jogo_da_velha():
    tabuleiro = criar_tabuleiro()
    jogador_atual = jogador
    jogo_terminado = False

    desenhar_tabuleiro(tabuleiro)
    while not jogo_terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN and jogador_atual == jogador:
                pos = pygame.mouse.get_pos()
                coluna = pos[0] // tamanho_celula
                linha = pos[1] // tamanho_celula

                if tabuleiro[linha][coluna] == vazio:
                    tabuleiro[linha][coluna] = jogador_atual
                    jogador_atual = ia
                    desenhar_tabuleiro(tabuleiro)

                    vencedor = verificar_vencedor(tabuleiro)
                    if vencedor:
                        mensagem = f'O vencedor é: {vencedor}'
                        if vencedor == 'Empate':
                            mensagem = 'Empate!'
                        print(mensagem)
                        jogo_terminado = True
                        break

        if jogador_atual == ia and not jogo_terminado:
            jogada_ia(tabuleiro)
            jogador_atual = jogador
            desenhar_tabuleiro(tabuleiro)

            vencedor = verificar_vencedor(tabuleiro)
            if vencedor:
                mensagem = f'O vencedor é: {vencedor}'
                if vencedor == 'Empate':
                    mensagem = 'Empate!'
                print(mensagem)
                jogo_terminado = True

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

jogo_da_velha()
