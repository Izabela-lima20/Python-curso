"""
Arquivo que conterá funções úteis ao sistema
Author: Izabela lima 
Version: 2025-04-03
"""

def cabecalho(titulo="Olá", colunas=60):
    #colunas = 60
    espacos = (colunas-len(titulo))//2
    texto = " " * espacos + titulo + " " * espacos
    print(texto)
def fatorial(valor):
    ret = 1
    for i in range(valor,1,-1):
        ret *= i
        return ret #retona o valor
def fatorial_rec(valor): # fatorial usando recursividade
    if valor == 1: return 1
    return valor * fatorial_rec(valor - 1)



if __name__ == "__main__": # so executa quando eu chamar o funcoes.py
   cabecalho("Olá turma!",20)
   