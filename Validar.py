import os

file = os.path.dirname(__file__)

def Validar(nome, senha, caixa):
	arquivo = open(f"{os.path.join(file, './Contas.txt')}", "r")
	for line in arquivo:
		if nome.input.get() == line.split()[0] and senha.input.get() == line.split()[1]:
			a = True
			break
		else:
			a = False
	try:
		if a == True:
			caixa.caixa["text"] = "Usuário Autenticado"

		else:
			caixa.caixa["text"] = "Usuário Não Autenticado"
	except:
		print ("ERRO! Nenhum usuário foi cadastrado!")

