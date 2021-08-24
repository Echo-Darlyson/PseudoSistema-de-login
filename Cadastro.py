def Cadastrar(i1, i2, c3):
	arquivo = open("Contas.txt", "a")
	nome = i1.input.get().strip()
	senha = i2.input.get().strip()
	if senha == "" and nome == "":
		c3.caixa["text"] = "Os campos Usuário e Senha devem ser preenchidos"
	elif senha == "" and nome != "":
		c3.caixa["text"] = "O campo Senha deve ser preenchido"
	elif senha != "" and nome == "":
		c3.caixa["text"] = "O campo Nome deve ser preenchido"
	else:
		arquivo.write(f"{nome} {senha}\n")
		arquivo.close()
