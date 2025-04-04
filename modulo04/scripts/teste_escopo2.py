"""
Programa de teste de escopo de variavéis -2
Author: Izabela lima 
Version: 2025-04-03
"""
from click import clear
def calculo():
    global c, d # nesse codigo vou usar uma variavel global chamada c 
    a = 5
    b = a + c
    c = 30
    d = 50
    return b
# promagrama principal
c = 10
print(calculo())
print("valor de c=",c, "valor de d=",d)
