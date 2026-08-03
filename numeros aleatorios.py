'''Neste módulo, você aprendeu sobre as interações entre o software que o programador desenvolve e a memória principal. Aprendeu também sobre como criar listas na linguagem de programação Python.

Manipular listas é uma habilidade imprescindível para qualquer programador que utiliza linguagem Python, pois elas são estruturas de dados extremamente versáteis. Saber trabalhar com listas torna o código mais eficiente, legível e preparado para desafios mais complexos.

Sua tarefa é desenvolver um programa em Python que manipule uma lista de números aleatórios e os separe em outras duas listas.

Orientações para elaboração e entrega da atividade:

Crie um novo script em Python.
Importe o módulo “random” para poder trabalhar com números aleatórios.
Crie uma lista para ser preenchida com 100 números inteiros.
Preencha a lista criada com números gerados aleatoriamente. Dica: use a função randint() do módulo “random”.
Percorra novamente a lista preenchida e separe os números pares em uma lista e os números ímpares em outra.
Exiba na tela o conteúdo das três listas: a original, a lista de pares e a lista de ímpares.
Envie o código Python (.py) desenvolvido por você pelo AVA.
Bons estudos!'''



import random

# 1. Criação das listas vazias
numeros_originais = []
pares = []
impares = []

# 2. Preenchimento da lista com 100 números inteiros aleatórios (ex: entre 1 e 100)
for _ in range(100):
    numero = random.randint(1, 100)
    numeros_originais.append(numero)

# 3. Separação dos números em pares e ímpares
for numero in numeros_originais:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

# 4. Exibição dos resultados na tela
print("=== LISTA ORIGINAL (100 elementos) ===")
print(numeros_originais)

print("\n=== LISTA DE NÚMEROS PARES ===")
print(pares)

print("\n=== LISTA DE NÚMEROS ÍMPARES ===")
print(impares)