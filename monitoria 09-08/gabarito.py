"""
    Gabarito de exercícios até o dia 09/08/2021
"""

## Exercícios Aula 1

# Fibonnaci iterativo

# versão 1
def fib1(n):
    f1 = 0
    f2 = 1

    for i in range(n):

        temp = f1
        f1 = f2
        f2 = temp + f2

        print(f"O {i + 1}-ésimo termo é {f1}")

# versão 2
def fib2(n):

    f1, f2 = 0, 1

    for i in range(n):

        f1, f2 = f2, f1 + f2

        print(f"O {i + 1}-ésimo termo é {f1}")

def troca_lista(list):
    list[0], list[-1]

# Classificação de notas

def classifica_nota(nota):
    if nota >= 80:
        return "A"
    elif nota >= 65:
        return "B"
    elif nota >= 40:
        return "C"
    elif nota >= 30:
        return "D"
    else:
        return "F"

# Hello World infinito

def infinity_hello_world():
    while True:
        entrada = input("Digite uma letra: ")

        if entrada == "a":
            print("Hello")
        elif entrada == "b":
            print("world!")
        elif entrada == "q":
            break
        else:
            print("Entrada inválida")

## Exercícios Funções

# Função que exibe informações

def exibir_info(nome="", idade="", cidade=""):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")

# Função que calcula a média

def cumprimentar_usuario(nome="Usuário"):
    print(f"Olá, {nome}!")

# Função que calcula a média

def formatar_pedido(item, quantidade=1, preco_por_unidade=0):
    preco_total = quantidade * preco_por_unidade
    print(f"Pedido: {quantidade} x {item} a R${preco_por_unidade} cada. Total: R${preco_total}")


"""
Questão 4)

    a. É esperado que a palavra "algoritmo" não seja trocada por "funcao" após a chamada da função trocar_palavra, já que a variável palavra é passada é trocada localmente na função, não globalmente.
    b. Nenhum impacto é gerado na variável palavra após a chamada da função trocar_palavra.
    c. Tipos de dados imutáveis possuem um comportamento similar, como inteiros, floats e tuplas. Tipos de dados mutáveis possuem um comportamento diferente, como listas e dicionários.
"""

# Nota, a resposta acima foi enviesada, não existe resposta certa para o item (a).

## Exercícios Args e Kwargs (pulado momentaneamente)

# resto será feito depois
