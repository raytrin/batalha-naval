import json

#variavel do arquivo json
arquivo_jogadores = "jogadores.json"

def carregar_jogadores():
    """Recebe os dados do arquivo e carrega em um dicionário"""

    #tratamento de erro caso não encontre o arquivo
    try:
        #recebe o arquivo json e retorna um dicionário com os dados
        with open(arquivo_jogadores, "r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}

def salvar_jogadores(dados_jogador):
    """Salva os novos dados em no arquivo json"""

    #recebe os dados dos jogadores e salva em um arquivo json
    with open(arquivo_jogadores, "w", encoding="utf-8") as arquivo:
        json.dump(dados_jogador, arquivo, indent=2)

