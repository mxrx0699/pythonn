# Exercício
# 1: Escreva um arquivo chamado produtos.txt com os seguintes dados:

# Arroz,20


# Feijão,15


# Açúcar,10


# Exercício 2: Leia o conteúdo do arquivo produtos.txt e exiba no console.

# Exercício 3: Adicione um produto ao arquivo usando o código
# Python.

# Exercício 4: Calcule o preço médio dos produtos no arquivo.

with open('produtos.txt', 'w') as arquivo:
    arquivo.write('Arroz, 20\n')
    arquivo.write('Feijao, 15\n')
    arquivo.write('Acucar, 10')

with open('produtos.txt', 'r') as file:
    print(file.read())
    
with open('produtos.txt', 'a') as file:
    file.write('\nManteiga, 5')

preco = 20, 15, 10, 5
media = sum(preco)/len(preco)
print(f'A média dos valores é {media}')

# with open('produtos.txt', 'r') as arquivo:
#     produtos = arquivo.readline()
#     precos = [float(produtos.split(",")[1] for produtos in produtos)]
#     media = sum(precos)/len(precos)
#     print(f'Preço médio: {media:.2f}')

