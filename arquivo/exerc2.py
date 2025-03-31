   # Função para exibir os dados
def exibir_dados():
    # Abrir o arquivo em modo de leitura
    with open("funcionarios.txt", "r") as arquivo:
        # Ler todas as linhas do arquivo
        conteudo = arquivo.readlines()
        # Imprimir o título
        print("Funcionários:")
        # Percorrer cada linha do conteúdo e imprimir, removendo o \n do final
        for linha in conteudo:
            print(linha.strip())

# Função para calcular a média das idades
def calcular_media():
    # Abrir o arquivo em modo de leitura
    with open("funcionarios.txt", "r") as arquivo:
        # Ler todas as linhas do arquivo
        conteudo = arquivo.readlines()
        # Criar uma lista com as idades
        idades = [int(linha.split(",")[1]) for linha in conteudo]
        # Calcular a média das idades
        media = sum(idades) / len(idades)
        # Imprimir a média com 2 casas decimais
        print(f"Média das idades: {media:.2f}")
        print(idades)
# Função para adicionar um funcionário
def adicionar_funcionario(nome, idade):
    # Abrir o arquivo em modo de adição
    with open("funcionarios.txt", "a") as arquivo:
        # Escrever no arquivo o nome e a idade separados por vírgula e com um \n no final
        arquivo.write(f"{nome},{idade}\n")
    # Imprimir a mensagem de sucesso
    print(f"Funcionário {nome} adicionado.")

# Função para excluir um funcionário
def excluir_funcionario(nome):
    # Abrir o arquivo em modo de leitura
    with open("funcionarios.txt", "r") as arquivo:
        # Ler todas as linhas do arquivo
        conteudo = arquivo.readlines()
    # Abrir o arquivo em modo de escrita
    with open("funcionarios.txt", "w") as arquivo:
        # Percorrer cada linha do conteúdo e escrever no arquivo apenas se o nome não estiver presente
        for linha in conteudo:
            if nome not in linha:
                arquivo.write(linha)
    # Imprimir a mensagem de sucesso
    print(f"Funcionário {nome} excluído.")

# Chamadas de teste
adicionar_funcionario("João", 35)
exibir_dados()
calcular_media()
excluir_funcionario("Carlos")
exibir_dados()