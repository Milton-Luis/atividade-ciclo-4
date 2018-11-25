#coding: utf-8

class IMC():
	
	def __init__(self, a, p):
		self.altura = a
		self.peso = p


	def Calcula(self):
		self.result = float(self.peso/(self.altura * self.altura))
		return self.result
		print(self.result)

	def VerificaIMC(self):
		# print usado caso exibir no teminal

		if self.result < 16:
		   return "Situação: Magreza grave"
		   print("Situação: Magreza grave")

		if self.result >= 16 < 17:
		   return "Situação: Magreza Moderada"
		   print("Situação: Magreza Moderada")


		elif self.result >= 17 < 18.5:
		   return "Situação: Magreza Leve"
		   print("Situação: Magreza Leve")


		elif self.result >= 18.25 < 25:
		   return "Situação: Saudável"
		   print("Situação: Saudável")


		elif self.result > 25 < 30:
		   return "Situação: Sobrepeso"
		   print("Situação: Sobrepeso")

		elif self.result >= 30 < 35:
		   return "Situação: Obesidade - Grau I"
		   print("Situação: Obesidade - Grau I")

		elif self.result >= 35 < 40:
		   return "Situação: Obesidade - Grau II (Severa)"
		   print("Situação: Obesidade - Grau II - (Severa)")

		else:
		   return "Situação: Obesidade - Grau III (Morbida)"
		   print("Situação: Obesidade - Grau III - (Morbida)")
