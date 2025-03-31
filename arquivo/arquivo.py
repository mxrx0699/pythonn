file = open('dados.txt', 'rb')

print(file.read())

file.close()

with open('dados.txt', 'w') as file:
    file.write('Hello World')
    
with open('dados.txt','r') as file:
    conteudo = file.read()
print(conteudo)