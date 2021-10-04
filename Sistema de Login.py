import tkinter as tk
import Cadastro
import Validar
from functools import partial
import os

#Diretório atual
dir_name = os.path.dirname(__file__)

#Janela
janela = tk.Tk()
janela.title("Sistema de Login")
janela.geometry("275x180")
janela.configure(background = "#f03e44")

#Imagens
user_icon = tk.PhotoImage(file = f"{os.path.join(dir_name, './user_icon.png')}")
pass_icon = tk.PhotoImage(file = f"{os.path.join(dir_name, './pass_icon.png')}")

#Apaga um usuário cadastrado
def Apagar(nome, senha):
	arquivo = open(f"{os.path.join(dir_name, './Contas.txt')}", "r")
	linhas = arquivo.readlines()
	for e, c in enumerate(linhas):
		if nome.input.get() == c.split()[0] and senha.input.get() == c.split()[1]:
			del linhas[e]
			novo_arquivo = open(f"{os.path.join(dir_name, './Contas.txt')}", "w")
			for lines in linhas:
				novo_arquivo.write(lines)
			novo_arquivo.close()
			break
		else:
			pass
			
			
#Classe para os botões
class Botão:
	def __init__(self, x, y, texto, comando, fg, bg):
		self.botão = tk.Button(janela, text = texto, command = comando, fg = fg, bg = bg, border = 0, highlightbackground = "#f03e44")
		self.botão.place(x = x, y = y)


#Classe para os inputs
class Input:
	def __init__(self, x, y):
		self.input = tk.Entry(janela, border = 0, bg = "#f03e44", highlightbackground = "#f03e44", highlightthickness = 0, width = 20, fg = "white")
		self.input.place(x = x, y = y)


#Classe para os labels
class Caixa:
	def __init__(self, x, y, texto = None, fonte = "Arial", tam = 10):
		self.caixa = tk.Label(janela, text = texto, font = (fonte, tam), bg = "#f03e44")
		self.caixa.place(x = x, y = y)


#Inputs
i1 = Input(70, 30)

i2 = Input(70, 80)
i2.input["show"] = "*"

#Separator

separator1 = tk.Frame(janela, bg="white", height=2, width = 163, bd=0)
separator1.pack(fill="x")
separator1.place(x = 70, y = 50)

separator2 = tk.Frame(janela, bg="white", height=2, width = 163, bd=0)
separator2.pack(fill="x")
separator2.place(x = 70, y = 100)

#Caixas
c1 = Caixa(23, 20)
c1.caixa["image"] = user_icon
c2 = Caixa(23, 70)
c2.caixa["image"] = pass_icon
c3 = Caixa(10, 160, "", tam = 7, fonte = "Arial Black")
c3.caixa["fg"] = "#353738"

#Botões
b1 = Botão(20, 118, "Cadastrar", partial(Cadastro.Cadastrar, i1, i2, c3), "#353738", "#d9ddde")
b1.botão["activebackground"] = "#d9ddde"
b1.botão["activeforeground"] = "#f03e44"
b2 = Botão(120, 118, "Login", partial(Validar.Validar, i1, i2, c3), "#353738", "#d9ddde")
b2.botão["activebackground"] = "#d9ddde"
b2.botão["activeforeground"] = "#f03e44"
b3 = Botão(190, 118, "Apagar", partial(Apagar, i1, i2), "#353738", "#d9ddde")
b3.botão["activebackground"] = "#d9ddde"
b3.botão["activeforeground"] = "#f03e44"

janela.mainloop()


#Created by Darlys0nZ [19/08/2021 22:00]