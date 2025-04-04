"""
Codigo para demostrar escopo de variavel no python
Author: Izabela lima 
Version: 2025-04-03
"""
from click import clear
#definindo uma função
def calculo():
    a = 5 # criação da variavel a 
    b = a + c
    # c = 30 # isso via dar erro, pq a variavel C passa a ser local
    return b
#programa principal
c = 10 
clear()
print(calculo())
