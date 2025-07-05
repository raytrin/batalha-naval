from tabuleiro import Tabuleiro

def test_atinge_navio():
    board = Tabuleiro.criar_tabuleiro()
    navio = [[1, 1]]
    submarino = []
    entrada = [1, 1]

    pontos = Tabuleiro.processar_jogada(board, entrada, navio, submarino)
    assert pontos == 1
    assert board[1][1] == "X"

def test_atinge_submarino():
    board = Tabuleiro.criar_tabuleiro()
    submarino = [[5, 5]]
    navio = []
    entrada = [5, 5]

    pontos = Tabuleiro.processar_jogada(board, entrada, navio, submarino)
    assert pontos == 1
    assert board[5][5] == "x"

def test_nao_atinge_nada():
    board = Tabuleiro.criar_tabuleiro()
    navio = [[1, 1]]
    submarino = [[5, 5]]
    entrada = [3, 3]

    pontos = Tabuleiro.processar_jogada(board, entrada, navio, submarino)
    assert pontos == 0
    assert board[3][3] == "_"
    