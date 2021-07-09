import logging

### Ativar log em modo debug

#logging.basicConfig(level=logging.DEBUG)

### Ativar logging em arquivo

logging.basicConfig(filename='arquivo.log',filemode='a',level=logging.DEBUG,
format='%(asctime)s:%(levelname)s:%(message)s')


## Configurar a mensagem de debug

logging.debug("Mensagem de debug")


num1 = 5
num2 = 6
def soma(x,y):
    return x + y

faz_soma = soma(num1,num2)

logging.debug("{}+{}={}".format(num1,num2,faz_soma))