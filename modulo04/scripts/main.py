"""
Programa principal
Author: Izabela lima 
Version: 2025-04-03
"""
# (pip install click) para importar a função clera 
import funcoes
from click import clear # importando somente a função clear
clear() # limpa o console (terminal)
funcoes.cabecalho(colunas =50,titulo="Bem vindo!")
funcoes.cabecalho("Olá turma, boa noite!",30)
funcoes.cabecalho()
funcoes.cabecalho(colunas=15)
print("fatorial de 5=" ,funcoes.fatorial(5))
print("fatorial de 5=", funcoes.fatorial_rec(5))