### Erro

###print("João)

###Exceção 

#print(2/0)

from typing import overload


#entrada = int(input("Digite um valor numérico: "))

###Podemos tratar as exceções com as funções try e except

try:
    print("Olá")
    print("olá")
except:
    print("Escreva corretamente") 

try:
    print(2/1)
except NameError:
    print("não divida por zero")

try:
    print(2 + ("a"))
except:
    print("não pode somar assim")

try:
    div=(2/0)
    print(div)
except ZeroDivisionError:
    print("Número não pode ser dividido por zero")

### Tratar exceções com condicionais e loops

def perguntaint():
    while True:
        try:
            numint = int(input("Digite um número inteiro: "))
        except:
            print("Digite certo")
            continue
        else:
            print("Ok registrado")
            break
        finally:
            print("Fim do programa")

perguntaint()

### Criar a própria exceção com a função raise

#def divisao(x,y):
#    if y ==0:
#        raise ValueError("Segundo valor não pode ser 0")
#    return x /y

#print(divisao(2,0))

print("planta")
