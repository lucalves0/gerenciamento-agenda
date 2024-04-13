def salvarContato(contatos, nomeContato, telefone, email):
    contato = {"nome": nomeContato, "telefone": telefone, "email": email, "favorito": False}   # dicionário
    contatos.append(contato)
    print(f"Contato  de {nomeContato} foi adicionado com sucesso !") 
    return

def editarContato(contatos, indiceContato):
    indice_contato_ajustado = int(indiceContato ) - 1

    nome = input("Adicione um novo nome: ")
    telefone = input("Adicione um novo telefone: ")
    email = input("Adicione um novo email: ")

    if indice_contato_ajustado >= 0 and indice_contato_ajustado < len(contatos):
        contatos[indice_contato_ajustado]["nome"] = nome
        contatos[indice_contato_ajustado]["telefone"] = telefone
        contatos[indice_contato_ajustado]["email"] = email
        print(f"\nContato de {nome} atualizada !")
    else:
        print("Contato invalido. ")
    return 

def visualizaContatos(contatos):
    print("\nLista de contatos :")
    status = "✓" if contato["favorito"] else " "
    print(f"\nContatos com o [{status}] indica que está como contato favorito na agenda. ")
    for indice, contato in enumerate(contatos, start=1):  # o start permite nós começar de onde nós quiser
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
    
        print(f"\n{indice}. [{status}] {nome_contato} || Telefone: {telefone_contato} || Email: {email_contato}")
    return 

def deletarContato(contatos, nomeContato):
    for contato in contatos: 
        if contato["nome"] == nomeContato:
            contatos.remove(contato)

    print("O contato foi deletadas!")
    return

def favoritarContato(contatos, contato_indice):
    indice_contato_ajustado = int(contato_indice) - 1
    contatos[indice_contato_ajustado]["favorito"] = True
    print(f"Contato {contato_indice} marcada como favorito")
    return 

contatos = []
contatosFavoritos = []
nomeUsuario = input("Por gentileza nos forneça seu nome: ")

while True:

    print(f"\nBem vindo {nomeUsuario} ! Sua agenda está inicializando, aguarde um instante..")
    print("\n1. Salvar contato")
    print("2. Editar contato")
    print("3. Deletar contato")
    print("4. Marca contato como favorito")
    print("5. Visualizar contatos salvos")
    print("6. Sair")

    escolha = input("\nQual opção você deseja realizar ?")

    if (escolha == "1"):
        nomeContato = input("\nQual o nome do contato ? ")
        telefone = input(f"Qual o telefone de {nomeContato} ? ")
        email = input(f"Qual é o email do {nomeContato} ? ")
        salvarContato(contatos, nomeContato, telefone, email)
    
    elif(escolha == "2"):
        visualizaContatos(contatos)
        indice = input("Adicione o indice do contato que deseja editar: ")
        editarContato(contatos, indice)

    elif (escolha == "3"):
        visualizaContatos(contatos)
        nome = input("Qual é o nome do contato que voçê deseja deletar: ")
        deletarContato(contatos, nome)
    
    elif (escolha == "4"):
        visualizaContatos(contatos)
        indiceContato = input("Indique o indice do contato que deseja marca como favorito: ")
        favoritarContato(contatos, indiceContato)

    elif (escolha == "5"): 
        visualizaContatos(contatos)
    
    elif(escolha == "6"):
        break
