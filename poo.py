# -----------------------------------------------------------------------------------------Aula - 31/03------------------------------------------------------------------------------------------------------------------

# class Pessoa:
#     def __init__(self, nome, idade):
#         self.nome = nome
#         self.idade = idade
        
# def apresentar(self):
#     print(f'Oi, eu sou {self.nome} e tenho {self.idade} anos.')
    
# pessoa1 = Pessoa('Mariana', 21)
# apresentar(pessoa1)
# ----------------------------------------------------------------------------------
# class Carro:
#     def __init__(self, modelo, placa, ano):
#         self.modelo = modelo
#         self.placa = placa
#         self.ano = ano 
    
#     def apresentar(self):
#         print(f'O modelo do carro é {self.modelo}, placa {self.placa}, ano {self.ano}')
        
#     def ligar(self):
#         print('O carro está ligando.')
    
#     def parar(self):
#         print('O carro está parando.')
        
# car = Carro('Ford Fusion','CFG-84-989489', 2025)
# car.apresentar()
# car.ligar()
# car.parar()

# --------------------------------------------------------------------------------
# class Aluno:
#     def __init__(self, nome, curso):
#         self.nome = nome
#         self.curso = curso
#         self.tempoSemDormir = 9
    
#     def estudar(self, horas):
#         if horas > 0:
#             self.tempoSemDormir += horas
#             print(f'{self.nome} estudou por {horas} horas.\nTempo sem dormir: {self.tempoSemDormir} horas')
#         else:
#             print('O tempo de estudo deve ser positivo!')

# aluno1 = Aluno('Mariana', 'Matemática')
# aluno1.estudar(5)

# correção professora -------------------
class Aluno:
    def __init__(self, nome, curso, tempoSemDormir=0):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir
        
    def estudar(self, horas):
        self.tempoSemDormir += horas
    
    def dormir(self, horas):
        self.tempoSemDormir -= horas
        if self.tempoSemDormir < 0:
            self.tempoSemDormir = 0
    
    def mostrar(self):
        print(f'Nome: {self.nome}, curso: {self.curso}, tempo sem dormir: {self.tempoSemDormir}')

aluno1 = Aluno('Mariana', 'Matemática', 8)    
aluno1.Aluno.mostrar()

 
        
        
        
        
        
        