# Exercícios Aula 1

1. Escreva um programa que gere os primeiros $N$ números da sequência de Fibonacci, onde $N$ é fornecido pelo usuário.

2. Crie um programa que solicita ao usuário uma nota de 0 a 100 e converte essa nota para uma classificação em letras.
As classificações são:
    * A: 80 a 100
    * B: 65 a 79
    * C: 40 a 64
    * D: 30 a 39
    * F: 0 a 29

3. Escreva um programa que leia repetidamente um input do usuário.
Se o usuário digitar:
    * 'a', exibir "Hello". 
    * 'b', exibir "world!".
    * 'q', o programa deve sair.
    * Caso contrário, dizer que entrada é invalida.

# Exercícios Funções 1

1. Escreva uma função chamada ```exibir_info``` que recebe três parâmetros: ```nome```, ```idade``` e ```cidade```.
Esses parâmetros devem ter valores padrão de uma string vazia.
Dentro da função, imprima as informações no formato ```"Nome: [nome], Idade: [idade], Cidade: [cidade]"```.

2. Escreva uma função chamada ```cumprimentar_usuario``` que recebe um parâmetro ```nome```.
A função deve imprimir uma mensagem de saudação usando o nome fornecido.
Se nenhum nome for fornecido, ele deve ser padrão para "Usuário".

3. Escreva uma função chamada ```formatar_pedido``` que recebe parâmetros nomeados ```item```, ```quantidade``` e ```preco_por_unidade```, com valores padrão para ```quantidade``` $= 1$ e ```preco_por_unidade``` $= 0$. Dentro da função, calcule o preço total multiplicando a quantidade pelo preco_por_unidade. Exiba um texto que formate as informações do pedido no formato: ```"Pedido: [quantidade] x [item] a R$[preco_por_unidade] cada. Total: $[preco_total]"```.

4. Considere a seguinte função:

    ```python
    def trocar_palavra(palavra):
        palavra = "funcao"

    palavra = "algoritmo"
    trocar_palavra(palavra)
    print(palavra)
    ```

    a. Antes de executar o código, o que você espera que seja impresso após a chamada da função ```trocar_palavra```?\
    b. Qual é o impacto da chamada da função ```trocar_palavra``` na variavel ```palavra```?\
    c. Quais outros tipos de dados possuem um comportamento similar? e quais possuem um comportamento diferente?

# Exercícios Funções 2

1. Escreva uma função chamada ```calcular_media``` que recebe o nome do aluno e uma quantidade arbitrária de notas.
Dentro da função, calcule a média das notas passadas.
Exiba um texto que formate o resultado no formato: ```"O aluno [nome] teve média final [média]"```.

2. Escreva uma função chamada ```criar_perfil``` que recebe o nome de uma pessoa como primeiro argumento e argumentos de palavra-chave arbitrários representando vários aspectos de seu perfil (por exemplo, idade, cidade, ocupação, etc.).
Dentro da função, construa um dicionário onde as chaves são os nomes dos argumentos e os valores são os valores correspondentes passados para a função. 
Exiba este dicionário ao final da função.

# Exercícios Funções 3

1. Escreva uma função chamada ```calcular_quadrado``` que recebe um único parâmetro ```num```.
Dentro da função, calcule o quadrado de num e retorne-o.

2. Escreva uma função chamada ```calcular_propriedades_retângulo``` que recebe dois parâmetros: ```comprimento``` e ```largura```.
Dentro da função, calcule tanto a área quanto o perímetro do retângulo definido por estas dimensões.
Retorne estes valores como uma tupla (área, perímetro).

3. Escreva uma função chamada ```verificar_par_impar``` que recebe um parâmetro inteiro ```num```.
Dentro da função, verifique se o número é par ou ímpar.
Se for par, retorne a string "Par", caso contrário, retorne "Ímpar".

# Exercícios Funções 4

1. Escreva um programa que contenha uma função chamada ```contar_chamadas``` que incrementa um contador global a cada vez que é chamada.
Em seguida, chame a função várias vezes e imprima o valor do contador.

2. Considere a seguinte função em Python: 

    ```python
    def scope_test():
        def do_local():
            spam = "local spam"
            
        def do_global():
            global spam
            spam = "global spam"
            
        spam = "test spam"
        do_local()

        print("After local assignment:", spam)
        do_global()
        print("After global assignment:", spam)

    scope_test()
    print("In global scope:", spam)
    ```

    o que você espera que seja impresso após cada chamada de função e na linha final?

# Exercícios Módulos

## Módulo de Operações Matemáticas

Crie um módulo chamado operacoes_matematicas.py que contenha as seguintes funções:
* adicionar(a, b): Retorna a soma de a e b.
* subtrair(a, b): Retorna a subtração de b de a.
* multiplicar(a, b): Retorna a multiplicação de a por b.
* dividir(a, b): Retorna a divisão de a por b, tratando a divisão por zero.

Crie um script separado main.py que importe o módulo operacoes_matematicas e teste todas as funções com diferentes valores.