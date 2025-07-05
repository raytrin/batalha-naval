import random

class Tabuleiro:
    """Modela um tabuleiro de batalha naval, tamanho 6x6"""

    @staticmethod
    def criar_tabuleiro(): 
        """Cria um tabuleiro tamanho 6x6 e o retorna"""

        #variavel com o char padrao de posição nao escolhida
        char_tabuleiro = "\u2588"

        #lista das "linhas"
        board = []

        #laço que gera as colunas e adiciona à lista das linhas
        for _ in range(6):
            l = []
            for _ in range(6):
                l.append(char_tabuleiro)
            board.append(l)

        return board
    
    @staticmethod 
    def printar_tabuleiro(board):
        """Imprime o tabuleiro formatado"""

        letras = ['A', 'B', 'C', 'D', 'E', 'F']

        #colunas do tabuleiro com numeros
        print("\n   ", end="")
        for n in range(1, 7):
            print(f"{n:>2}", end=" ")
        print()
        
        #linhas do tabuleiro com letras
        for i in range(6):
            print(f"{letras[i]}| ", end="")
            for j in range(6):
                print(f"{board[i][j]:>2}", end=" ")
            print()
            print()


    @staticmethod
    def coordenadas():
        """Cria uma lista com todas as coordenadas do tabuleiro e as retorna"""
        
        #cria a lista com todas as coordenadas do tabuleiro
        coordenadas = []

        #gera todas as coordenadas do tabuleiro 
        for i in range(6):
            for j in range(6):
                c = [i, j]
                coordenadas.append(c)

        return coordenadas
    

    @staticmethod
    def posicionar_embarcacoes(coordenadas):
        """Gera aleatoriamente as posições das embarcações no tabuleiro e retorna as listas com essas posições"""

        #posiciona os navios
        navio = random.sample(coordenadas, 5) 
        
          
        #remove posições ocupadas pelos navios
        for c in navio:
            coordenadas.remove(c)
        #posiciona os submarinos
        submarino = random.sample(coordenadas, 3)
        
        return navio, submarino
    
    @staticmethod
    def processar_jogada(board, jogada, navio, submarino):
        """Altera o char no tabuleiro caso o jogador acerte embarcações ou água. Retorna os pontos pelo acerto das embracações"""

        #variavel que guarda os pontos da primeira jogada
        pts = 0

        #verifica se a posição já foi jogada
        if board[jogada[0]][jogada[1]] != "\u2588":
            print("\n==> Você já jogou nessa posição!")
            return -1

        #muda o char caso a coordenada escolhida seja a de um navio
        for pos in navio:
            if jogada == pos:
                board[jogada[0]][jogada[1]] = "X"
                pts +=1
               

        #muda o char caso a coordenada escolhida seja a de um submarino
        for pos in submarino:
            if jogada == pos:
                board[jogada[0]][jogada[1]] = "x"
                pts += 1
                

        #muda o char caso a coordenada nao seja navio nem sub, seja água
        if jogada not in navio and jogada not in submarino:
            board[jogada[0]][jogada[1]] = "_"
    
        return pts

  