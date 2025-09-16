class Pessoa:
    def __init__(self, nome, idade, cpf):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

    def eh_maior_de_idade(self):
        return self.idade >= 18

pessoa1 = Pessoa("Alice", 20 , "123.456.789-00")
pessoa2 = Pessoa("Bob", 16 , "987.654.321-00")
print(pessoa1.nome)
print(pessoa2.nome)
if pessoa1.eh_maior_de_idade():
    print(f"{pessoa1.nome} é maior de idade.")
else:
    print(f"{pessoa1.nome} é menor de idade.")
