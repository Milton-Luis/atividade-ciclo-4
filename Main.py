# coding: utf-8

from Registro import Paciente
from CalcIMC import *


class Control():
	def __init__(self):
		user = Paciente()
		

		user.nome = input("Digite um nome: ")
		user.end = input("Digite um endereço: ")
		
		user.altura = float(input("Digite um altura: "))
		user.peso = float(input("Digite um peso: "))

		calc = IMC(user.altura, user.peso)
		imc = calc.Calcula()

		user.result = imc
		print()
		print(user.InserirRegistro())
		print(calc.VerificaIMC())
		print()
		print("Id\tNome\t\tEndereço\tAltura\tPeso\tIMC\n")
		print(user.Exibir_registro())


ctrl = Control()