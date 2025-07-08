from exibicao import mostrar_tabuleiro, exibir_pontuacao
from colorama import init, Fore, Style
init(autoreset=True)

def mostrar_menu():
    """Exibe o menu principal com as opções de entrada do jogador"""

    while True:
        #exibe o menu principal
        print(f"\n-------------------- {Fore.BLUE}BATALHA NAVAL{Style.RESET_ALL} --------------------\n")
        print("1 - Jogar")
        print("2 - Ver melhores pontuações")
        print("3 - Sair")
        opcao = (input("Digite uma opção: "))

        if opcao == "1":
            mostrar_tabuleiro()
        elif opcao == "2":
            exibir_pontuacao()
        elif opcao == "3":
            print(f"{Fore.LIGHTCYAN_EX}\nFinalizando programa... Até a pŕoxima!{Style.RESET_ALL}")
            break
          

def input_jogador():
    """Cria entrada das coordenadas"""
    
    #print da entrada do jogador
    print(f"\nDigite a posição para tentar (formato linha e coluna. {Fore.LIGHTYELLOW_EX}Ex.: A 1{Style.RESET_ALL})")
    entrada = input("Se quiser desistir digite -1: ").strip().upper()
    print("\n-------------------------------------------------------------")
    
    
    #se o jogador desistir do jogo retorna none
    if entrada == "-1": 
        return None
    
    #transforma a entrada do usuário NUMA lista e verifica se tem 2 valores
    partes = entrada.split()
    if len(partes) != 2:
        print(f"{Fore.LIGHTMAGENTA_EX}Formato inválido.{Style.RESET_ALL}")
        return input_jogador()

    #confere se a entrada do jogador é válida 
    jogada_valida = verifica_movimento(partes)
    if jogada_valida:
        return jogada_valida
    else:
        return input_jogador()
      

def verifica_movimento(partes):
    """
    Confere se a entrada do jogador está dentro é compatível com as coordenadas do tabuleiro.
    Faz a tradução as letras (linhas) para os números das coordenadas.
    """

    #associa cada letra a um número
    partes_0 = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5}

    #confere se a letra digitada é válida
    linha = partes[0]
    if linha not in partes_0:
        print(f"{Fore.LIGHTMAGENTA_EX}Letra inválida!{Style.RESET_ALL}")
        return None
    
    linha =  partes_0[partes[0]]
    
    #confere se o numero digitado é valido e trata o erro
    try:
        coluna = int(partes[1]) - 1
        if coluna < 0 or coluna > 5:
            print(f"{Fore.LIGHTMAGENTA_EX}Número inválido!{Style.RESET_ALL}")
            return None
    except ValueError:
        print(f"{Fore.LIGHTMAGENTA_EX}Número inválido!{Style.RESET_ALL}")
        return None
    
    #se letra e numero estiverem corretos, retorna uma lista de coordenadas
    return [linha, coluna]
