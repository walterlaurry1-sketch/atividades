# Lista de Exercícios - POO Classes e Objetos

# --- Exercício 1 e 2: Classe Pessoa com atributos e método ---
print("### Exercício 1 e 2: Classe Pessoa ###")
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

# Criando objetos e testando o método
pessoa1 = Pessoa("João", 25)
pessoa2 = Pessoa("Maria", 30)
pessoa1.apresentar()
pessoa2.apresentar()
print("-" * 20)

# --- Exercício 3 e 4: Classe Carro com __init__ e alteração de atributo ---
print("\n### Exercício 3 e 4: Classe Carro ###")
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

# Criando objetos e mostrando informações
carro1 = Carro("Ford", "Fusion", 2020)
print(f"Carro original: {carro1.marca} {carro1.modelo} ({carro1.ano})")

# Alterando um atributo
carro1.ano = 2023
print(f"Carro após a alteração: {carro1.marca} {carro1.modelo} ({carro1.ano})")
print("-" * 20)

# --- Exercício 5 e 6: Classe ContaBancaria com depósitos e saques ---
print("\n### Exercício 5 e 6: Classe ContaBancaria ###")
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Novo saldo: R${self.saldo:.2f}")
            return True
        else:
            print(f"Saldo insuficiente. Saldo atual: R${self.saldo:.2f}")
            return False

# Testando a classe
minha_conta = ContaBancaria("Walter Sobral", 1000)
minha_conta.depositar(500)
minha_conta.sacar(200)
minha_conta.sacar(2000) # Este saque deve falhar
print("-" * 20)

# --- Exercício 7 e 8: Classes Aluno e Turma com __str__ ---
print("\n### Exercício 7 e 8: Classes Aluno e Turma ###")
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota
    
    def __str__(self):
        return f"Aluno: {self.nome} - Nota: {self.nota}"

class Turma:
    def __init__(self):
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)
        print(f"Aluno {aluno.nome} adicionado à turma.")

# Criando e adicionando alunos
turma_a = Turma()
aluno1 = Aluno("Letícia", 9.5)
aluno2 = Aluno("Ricardo", 8.0)
turma_a.adicionar_aluno(aluno1)
turma_a.adicionar_aluno(aluno2)

# Imprimindo a lista de alunos, usando o método __str__
print("Lista de alunos na turma:")
for aluno in turma_a.alunos:
    print(aluno)
print("-" * 20)

# --- Exercício 9: Classe Cachorro com atributos de classe e instância ---
print("\n### Exercício 9: Classe Cachorro ###")
class Cachorro:
    especie = "Canis familiaris" # Atributo de classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Criando um objeto
meu_cachorro = Cachorro("Rex", 5)

# Acessando atributos
print(f"Acessando o atributo de classe pela INSTÂNCIA: {meu_cachorro.especie}")
print(f"Acessando o atributo de classe diretamente pela CLASSE: {Cachorro.especie}")
print(f"Atributo de instância (nome) do objeto: {meu_cachorro.nome}")
print(f"Atributo de instância (idade) do objeto: {meu_cachorro.idade}")