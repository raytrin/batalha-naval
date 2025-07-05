from frontend import verifica_movimento

def test_jogada_valida():
    assert verifica_movimento(['A', '3']) == [0, 2]

def test_letra_invalida():
    assert verifica_movimento(['Z', '3']) is None

def test_numero_invalido():
    assert verifica_movimento(['C', '9']) is None

def test_entrada_nao_numerica():
    assert verifica_movimento(['B', 'abc']) is None
