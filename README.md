# 🚢 Batalha Naval

Jogo de Batalha Naval desenvolvido em Python como projeto final da disciplina Introdução à Programação.

## 📺 Demonstração

[![Demonstração Batalha Naval](https://img.youtube.com/vi/x5AUvN5W85Q/0.jpg)](https://youtu.be/x5AUvN5W85Q)

## 🎮 Como Jogar

- **Objetivo**: Encontrar todas as 8 embarcações no tabuleiro 6x6
- **Embarcações**: 5 navios (X) + 3 submarinos (x)
- **Tentativas**: Máximo 15 por jogo
- **Formato**: Digite coordenadas como "A 1" (letra + número)
- **Desistir**: Digite "-1" para sair da partida atual

### Símbolos
- `█` - Posição não selecionada
- `X` - Navio atingido
- `x` - Submarino atingido  
- `_` - Água

## 🚀 Como Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/raytrin/batalha-naval.git
   cd batalha-naval
   ```

2. **Instale a dependência**
   ```bash
   pip install colorama
   ```

3. **Execute o jogo**
   ```bash
   python main.py
   ```

## 📁 Estrutura

```
├── main.py                    # Arquivo principal para executar o jogo
├── frontend.py               # Interface do usuário
├── exibicao.py              # Controle do jogo
├── tabuleiro.py             # Lógica do tabuleiro 
├── persistencia.py          # Salvar/carregar dados
├── jogadores.json           # Arquivo de dados dos jogadores
├── test_frontend.py         # Testes do frontend
├── test_salvar_pontuacao.py # Testes de persistência
├── test_tabuleito.py        # Testes do tabuleiro
└── README.md               # Documentação
```

## 🧪 Testes

```bash
# Instalar pytest (se não tiver)
pip install pytest

# Executar todos os testes
pytest

# Ou executar individualmente
python test_frontend.py
python test_salvar_pontuacao.py
python test_tabuleito.py
```
---
## ✨ Funcionalidades

- ✅ Validação de entradas (coordenadas inválidas, formato incorreto)
- ✅ Sistema de pontuação e ranking
- ✅ Persistência de dados (salva jogadores e pontuações)
- ✅ Interface colorida no terminal
- ✅ Opção de desistir da partida
- ✅ Testes unitários implementados

---
## 💡 Tecnologias

- Python 3.x
- Colorama (cores no terminal)
- JSON (persistência)
- Pytest (testes)

---
**Desenvolvido por**: Rayssa Trindade  
**Contato**: rayytrindade@gmail.com