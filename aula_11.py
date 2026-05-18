class Pessoa:
    def __init__(self, nome, idade, altura):
        self._nome = nome  #encapsulamento
        self.idade = idade
        self.altura = altura

    def apresentar(self):
        print('Olá, meu nome é:', self._nome, ', tenho ', self.idade, 'anos e ', self.altura, 'de altura')

    def get_nme(self):
        return self._nome

p1 = Pessoa("João", 33, "1,80")
p2 = Pessoa("Karina", 28, "1,70")

p1.apresentar()
p2.apresentar()

print(p1._nome)
print(p1.get_nme())
print(p2.idade)

class Aluno(Pessoa):
    def __init__(self, nome, idade, altura, matricula):
        super().__init__(nome, idade, altura)
        self.matricula = matricula

    def estudante(self):
        print('A matricula do aluno é', self.matricula)

    def apresentar(self):
        # Correção: Adicionados os parênteses em get_nome()
        print('Olá, meu nome é:', super().get_nme(), 'e minha matricula é:', self.matricula)


aluno1 = Aluno('Pedro', 30, '1,90', '000678908')

aluno1.estudante()
aluno1.apresentar()

## -- ##

class Carro:
    def __init__(self, modelo, placa, ano):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano

    def mostrarPlaca(self):
        print("Placa do veículo:", self.placa)

# Exemplo de uso
meu_carro = Carro("Gol", "ABC-1234", 2015)
meu_carro.mostrarPlaca()
