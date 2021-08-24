import tkinter as tk
import Cadastro
import Validar
from functools import partial

#Janela
janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("275x180")


#Apaga um usuário cadastrado
def Apagar(nome, senha):
	arquivo = open("Contas.txt", "r")
	linhas = arquivo.readlines()
	for e, c in enumerate(linhas):
		if nome.input.get() == c.split()[0] and senha.input.get() == c.split()[1]:
			del linhas[e]
			novo_arquivo = open("Contas.txt", "w")
			for lines in linhas:
				novo_arquivo.write(lines)
			novo_arquivo.close()
			break
		else:
			pass
			
			
#Classe para os botões
class Botão:
	def __init__(self, x, y, texto, comando, fg, bg):
		self.botão = tk.Button(janela, text = texto, command = comando, fg = fg, bg = bg)
		self.botão.place(x = x, y = y)


#Classe para os inputs
class Input:
	def __init__(self, x, y):
		self.input = tk.Entry(janela)
		self.input.place(x = x, y = y)


#Classe para os labels
class Caixa:
	def __init__(self, x, y, texto, fonte = "Arial", tam = 10):
		self.caixa = tk.Label(janela, text = texto, font = (fonte, tam))
		self.caixa.place(x = x, y = y)


#Inputs
i1 = Input(70, 30)
i1.input["relief"] = "sunken"
i1.input["border"] = 2
i2 = Input(70, 70)
i2.input["relief"] = "sunken"
i2.input["border"] = 2

#Caixas
c1 = Caixa(10, 30, "Usuário")
c2 = Caixa(10, 70, "Senha")
c3 = Caixa(10, 150, "", tam = 7, fonte = "Arial Black")
c3.caixa["fg"] = "Red"

#Botões
b1 = Botão(20, 108, "Cadastrar", partial(Cadastro.Cadastrar, i1, i2, c3), "White", "Red")
b1.botão["activebackground"] = "White"
b1.botão["activeforeground"] = "Red"
b2 = Botão(120, 108, "Login", partial(Validar.Validar, i1, i2, c3), "White", "Red")
b2.botão["activebackground"] = "White"
b2.botão["activeforeground"] = "Red"
b3 = Botão(190, 108, "Apagar", partial(Apagar, i1, i2), "White", "Red")
b3.botão["activebackground"] = "White"
b3.botão["activeforeground"] = "Red"

janela.mainloop()


#Created by Darlys0nZ [19/08/2021 22:00]