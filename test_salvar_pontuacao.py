from exibicao import salvar_pontuacao

def test_salvar_pontuacao():
    jogadores = {
        'luis': 3,
        'lucas': 4
    }
    nome = 'rayssa'
    pontos = 2

    salvar_pontuacao(nome, pontos, jogadores)

    assert jogadores['rayssa'] == 2


    
