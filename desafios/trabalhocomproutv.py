
# Desafio Operadores Lógicos

# Os Trabalhos
trabalho_terca = False
trabalho_quinta = False

"""
-Confirmando os 2: tv 50" + Sorvete
-Confirmando apenas 1: TV 32" + Sorvete
-Nehum confirmado: Fica em casa
"""

if (trabalho_terca and trabalho_quinta):
    print('Vai comprar a tv 50" mais o sorvete')
elif (trabalho_terca or trabalho_quinta):
    print('Vai comprar a tv 32" mais o sorverte')
else:
    print("Não vai ter nem tv e nem sorte, com isso ganhou Saude")
