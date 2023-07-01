"""
while <condição>:
    <codigo>

Incremento
> Adicionar uma unidade ao valor de uma variavel

var = var + 1
or
var += 1
"""

"""
count = 0
while count < 5:
    print("Valor de count =", count)
    #Realizando o Incremento da variavel count
    count +=1

"""

"""
count = 0
while count < 5:
    jogador = input ('Digite o nome do jogador:')
    count +=1
"""



"""
1. Utilize laço de repetição para imprimir 10 vezes a mensagem "hello world" na tela

count = 0
while count < 10:
    print("Hello Word")
    count +=1
"""

"""
2. Utilize laço de repetição para imprimir uma sequencia de 0 a 100

count = 0
while count <= 100:
    print(count)
    count += 1
"""

"""
3. Utilize laço de repetição para imprimir uma sequencia de 0 até um numero digitado pelo usuário 

count = 0 
num = int(input("Digite o numero desejado para a sequencia:"))
while count <= num:
    print(count)
    count += 1
    
"""


"""
4. Utilize laço de repetição para imprimir todos os pares entre 0 e 100

count = 0
while count <= 100:
    count += 1
    if count % 2 == 0:
        print(count)

"""

"""
5. Utilize laço de repetição para imprimir todos os pares entre 0 e o numero digitado pelo usuário 

count = 0
num = int(input("Digite o numero desejado para a sequencia:"))

while count < num:
    count += 1
    if count % 2 == 0:
        print(count)
"""

"""
Desafio. Utilize laço de repetição para imprimir a seguinte sequencia
I = 1 J = 3
I = 2 J = 5
I = 3 J = 7
...
...
I = 9 J = 19

Resolução:

I = 1
J = 3
while I <= 9:
    print("I = ",I, " J =",J)
    I = I + 1
    J = J + 2

"""


"""
6. Leia 10 números utilizando laços de repetição e sempre que o número digitado for par, imprima a mensagem "Este número
 é par" 
 
 count = 0
while count < 10:
    count +=1
    num = int(input("Digite um numero:"))
    if num % 2 == 0:
        print("Esse numero é par")



"""

"""
7. Leia 10 números utilizando laços de repetição e sempre que o número for entre 60 e 100, imprimir a mensagem 
"Este número esta dentro do intervalo" 

count = 0
while count < 10:
   
    num = int(input("Digite um numero:"))
    if 60 <= num <= 100:
        print("Este numero esta dentro do intervalo")
    count += 1

"""

"""
8. Leia 10 números utilizando laços de repetição e ao final do laço informe a quantidade de números pares digitados

count = 0
# Contador que ira armazenar a quantidade de numeros pares
pares = 0
while count < 10:
    num = int(input("Digite um numero:"))
    if num % 2 == 0:
        pares += 1
    count += 1
print("A quantidade de numeros pares", pares)
"""



