'''Neste módulo, você aprendeu sobre a recursividade, técnica poderosa e extremamente útil para a construção de algoritmos. Aprendeu também como identificar a complexidade de um determinado algoritmo e compará-lo com outros.

A recursão é um conceito de programação poderoso, pois permite dividir os problemas em partes mais simples, além de ajudar a desenvolver um forte pensamento algorítmico no programador.

Sua tarefa é criar um programa em Python que implemente recursividade para somar os N primeiros números naturais.

Orientações para elaboração e entrega da atividade:

Crie um novo script em Python.
Solicite ao usuário que digite um número natural qualquer (inteiro e positivo).
Implemente uma função recursiva que seja capaz de somar todos os números até o número que foi digitado pelo usuário.
Importante: não utilize nenhum laço (estrutura de repetição) no programa!
Exiba em tela o resultado da soma desses números.
Envie o código Python (.py) desenvolvido por você pelo AVA.
Bons estudos!

Prof. Rafael Canteri.'''

def soma_recursiva(n):
    """Função recursiva que calcula a soma de 1 até n.

    Caso Base: Se n for igual a 1 ou 0, retorna o próprio valor.
    Caso Recursivo: Retorna n somado com o resultado da chamada para (n - 1).
    """
    if n <= 1:
        return n
    return n + soma_recursiva(n - 1)


def main():
    try:
        # Solicitando o número natural ao usuário
        numero = int(
            input("Digite um número natural (inteiro positivo): ").strip()
        )

        # Validação para garantir que o número é positivo/natural
        if numero < 0:
            print("Por favor, digite um número inteiro maior ou igual a zero.")
        else:
            resultado = soma_recursiva(numero)
            print(f"A soma de todos os números naturais até {numero} é: {resultado}")

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")


if __name__ == "__main__":
    main()