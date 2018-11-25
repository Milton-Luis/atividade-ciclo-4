# coding: utf-8

from tkinter import *
from Registro import Paciente
from CalcIMC import IMC
from JanelaConsulta import *

class JanelaTK:
    def __init__(self, janela):

        self.fonte = ("Times New Roman", "12")

        self.janela = janela
        self.janela.geometry("700x400+300+100")
        self.janela.title("Cálculo de IMC - Indice de massa corporal")

        self.lbNome = Label(janela, text="Nome do Paciente:")
        self.lbNome["font"] = self.fonte
        self.lbNome.place(x=10, y=10)

        self.nome = Entry(janela, width=60)
        self.nome["font"] = self.fonte
        self.nome.place(x=150, y=10)

        self.lbEnd = Label(janela, text="Endereço Completo: ")
        self.lbEnd["font"] = self.fonte
        self.lbEnd.place(x=10, y=70)

        self.end = Entry(janela, width=60)
        self.end["font"] = self.fonte
        self.end.place(x=150, y=70)

        self.lbAltura = Label(janela, text="Altura (M)")
        self.lbAltura["font"] = self.fonte
        self.lbAltura.place(x=10, y=130)

        self.altura = Entry(janela, width=20)
        self.altura["font"] = self.fonte
        self.altura.place(x=150, y=130)

        self.lbPeso = Label(janela, text="Peso (Kg)")
        self.lbPeso["font"] = self.fonte
        self.lbPeso.place(x=10, y=190)

        self.peso = Entry(janela, width=20)
        self.peso["font"] = self.fonte
        self.peso.place(x=150, y=190)

        self.txt = Text(janela, width=40, height=10)
        self.txt.place(x=330, y=130)

        self.btC = Button(janela, text="Calcular")
        self.btC["font"] = self.fonte
        self.btC["command"] = self.btCalcular
        self.btC["width"] = 15
        self.btC.place(x=10, y=260)

        self.btR = Button(janela, text="Reiniciar")
        self.btR["command"] = self.btReiniciar
        self.btR["font"] = self.fonte
        self.btR["width"] = 15
        self.btR.place(x=170, y=260)

        self.btS = Button(janela, text="Sair")
        self.btS["font"] = self.fonte
        self.btS["command"] = quit
        self.btS["width"] = 15
        self.btS.place(x=500, y=325)

        self.btV = Button(janela, text="Consultar Registro")
        self.btV["font"] = self.fonte
        self.btV["command"] = self.btConsultar
        self.btV["width"] = 20
        self.btV.place(x=150, y=325)


    def btCalcular(self):
        user = Paciente()

        user.nome = self.nome.get()
        user.end = self.end.get()
        user.altura = float(self.altura.get())
        user.peso = float(self.peso.get())
        
        calc = IMC(user.altura, user.peso)
        imc = calc.Calcula()

        user.result = imc

        self.txt.insert(INSERT, "{:^40}\n========================================\n"\
            .format(user.InserirRegistro()))
    
        self.txt.insert(INSERT, "Nome: {}\n".format(user.nome))
        self.txt.insert(INSERT, "Endereço: {}\n".format(user.end))
        self.txt.insert(INSERT, "Altura: {} m    Peso: {} Kg\n".format(user.altura, user.peso))
        self.txt.insert(INSERT, "Seu IMC é: %.2f\n" % user.result)
        
        self.txt.insert(INSERT, "{}".format(calc.VerificaIMC()))


    def btReiniciar(self):

        self.nome.delete(0, END)
        self.end.delete(0, END)
        self.altura.delete(0, END)
        self.peso.delete(0, END)
        self.txt.delete(1.0, END)
        return self.txt, self.nome, self.end, self.altura, self.peso

    def btConsultar(self):
        raiz=Tk()
        sub = SubJanela(raiz)
        
        sub.Exibir()
        raiz.mainloop()


tk = Tk()
JanelaTK(tk)
tk.mainloop()