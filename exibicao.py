from tabuleiro import Tabuleiro
from persistencia import salvar_jogadores, carregar_jogadores
from colorama import init, Fore, Style
init(autoreset=True)

def mostrar_tabuleiro():
    """Exibe o tabuleiro"""
    from frontend import input_jogador

    #variaveis de controle
    tentativas = 0
    pontos_totais = 0
    board = Tabuleiro.criar_tabuleiro()
    coordenadas = Tabuleiro.coordenadas() 
    navio, submarino = Tabuleiro.posicionar_embarcacoes(coordenadas)
    nome = input("\nNome: ")
    print("\n-------------------------------------------------------")

    #carrega os dados dos jogadores
    jogadores = carregar_jogadores()

    while True:
        
        print(f"\n=== {Fore.MAGENTA}EMBARCAÇÕES{Style.RESET_ALL}: {pontos_totais}/8 | {Fore.MAGENTA}TENTATIVAS{Style.RESET_ALL}: {tentativas}/15 ===")

        #printa o tabuleiro
        Tabuleiro.printar_tabuleiro(board)

        #recebe a entrada do jogador
        entrada = input_jogador()

        # encerra o jogo
        if entrada == None:
            print(f"{Fore.LIGHTBLUE_EX}\nObrigada por jogar, {nome}. Até a próxima!{Style.RESET_ALL}")
            break

        #verifia se a posicao já foi jogada
        if board[entrada[0]][entrada[1]] != "\u2588":
            print(F"\n{Fore.LIGHTRED_EX} Você já jogou nessa posição! Tente novamente.{Style.RESET_ALL}")
            continue

        
        #confere se o jogador já esgotou as tentativas
        if entrada:
            tentativas += 1
        if tentativas >= 15:
           print(f"\n{Fore.LIGHTMAGENTA_EX}{nome}, você esgotou as tentativas!{Style.RESET_ALL}")
           print(f"\nVocê fez {pontos_totais} pontos!")
           #salva a pontuação no arquivo antes de sair
           salvar_pontuacao(nome, pontos_totais, jogadores)
           break
        
        #recebe os pontos e modifica o char no tabuleiro
        pontos = Tabuleiro.processar_jogada(board, entrada, navio, submarino)

        #confere e printa se o jogador atingiu uma embarcação ou a água
        if pontos > 0:
           print(f"\n{Fore.GREEN}==> Você atingiu uma embarcação!{Style.RESET_ALL}")
        else:
           print(f"\n{Fore.RED}==> Água!{Style.RESET_ALL}")

        #confere e printa quantos pontos o jogador fez
        pontos_totais += pontos    
        if pontos_totais == len(navio) + len(submarino):
          print(f"{Fore.CYAN}PARABÉNS, {nome}! Você ganhou!{Style.RESET_ALL}")
          print(f"\nVocê fez {pontos_totais} pontos!")
          #salva a pontuação da vitória 
          salvar_pontuacao(nome, pontos_totais, jogadores)
          break
        
               
def salvar_pontuacao(nome, pontos, jogadores):
    """Salva a pontuação dos jogadores"""

    #atribui os pontos aos nomes dos jogadores
    jogadores[nome] = pontos

    #salva os novos dados em json
    salvar_jogadores(jogadores)
    
        
def exibir_pontuacao():
    """Exibe um ranking com as melhores pontuações"""

    #variavel que recebe o dicionário com os dados dos jogadores
    jogadores = carregar_jogadores()
    
    #cria uma lista de tuplas contendo nome e pontuação em ordem decrescente
    jogadores_ordenado = sorted(jogadores.items(), key=lambda item: item[1], reverse=True)
    
    print(f"\n-------------- {Fore.GREEN}RANKING{Style.RESET_ALL} --------------")
    print(f"{'Lugar'} {str('Nome'):>9} {str('Pontos'):>10}")
    print("-------------------------------------")

    #exibe o ranking em ordem decrescente  
    for i, (nome, pontos) in enumerate(jogadores_ordenado):
        print(f"\n{i+1}º  {nome:>11} {pontos:>8}")



    