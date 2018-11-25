#coding: utf-8

from tkinter import *
from tkinter import ttk

from Registro import Paciente

class SubJanela():
	
	def __init__(self, subJanela):
		self.fonte = ("Times New Roman", "12")

		self.subJanela = subJanela

		self.subJanela.geometry("800x400+300+100")
		self.subJanela.title("Consulta de Valores do DB imc")

		
		self.btS = Button(subJanela, text="Sair")
		self.btS["font"] = self.fonte
		self.btS["command"] = quit
		self.btS["width"] = 15
		self.btS.place(x=500, y=325)

		self.txt = Text(subJanela, width=95, height=15)
		self.txt["font"] = self.fonte
		self.txt.place(x=20, y=10)



	def Exibir(self):
		ex = Paciente()
		self.txt.insert(INSERT, "Id\tNome\t\tEndereço\t\t\tAltura\t\tPeso\t\tIMC\n")

		self.txt.insert(INSERT, ex.Exibir_registro())



