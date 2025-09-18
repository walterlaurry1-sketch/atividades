# ====================================================================
# Passo 1: Herança Simples e Atributos
# ====================================================================

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    pass

print("--- Herança Simples ---")
cliente1 = Cliente("Walter Sobral", "walter.sobral@exemplo.com")
print(f"Nome do cliente: {cliente1.nome}")
print(f"E-mail do cliente: {cliente1.email}")
print("\n" + "="*50 + "\n")

# ====================================================================
# Passo 2: Herança de Métodos e Sobrescrita
# ====================================================================

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")

    def saudacao(self):
        return "Olá, usuário"

class Cliente(Usuario):
    def saudacao(self):
        return "Olá, cliente"

print("--- Herança e Sobrescrita de Métodos ---")
cliente2 = Cliente("Rosângela Sobral", "rosangela@exemplo.com")
print("Chamando o método herdado 'exibir_informacoes()':")
cliente2.exibir_informacoes()
print(f"Chamando o método sobrescrito 'saudacao()': {cliente2.saudacao()}")
print("\n" + "="*50 + "\n")

# ====================================================================
# Passo 3: Construtor em Classe Herdeira com super()
# ====================================================================

class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

class Cliente(Usuario):
    def __init__(self, nome, email, saldo):
        super().__init__(nome, email)
        self.saldo = saldo

print("--- Construtor com super() ---")
cliente3 = Cliente("Walter Sobral", "walter@exemplo.com", 1500.50)
print(f"Nome do cliente: {cliente3.nome}")
print(f"E-mail do cliente: {cliente3.email}")
print(f"Saldo do cliente: R$ {cliente3.saldo:.2f}")
print("\n" + "="*50 + "\n")

# ====================================================================
# Passo 4: Herança em Múltiplos Níveis
# ====================================================================

class Funcionario(Usuario):
    def __init__(self, nome, email, salario):
        super().__init__(nome, email)
        self.salario = salario

class Gerente(Funcionario):
    def __init__(self, nome, email, salario, departamento):
        super().__init__(nome, email, salario)
        self.departamento = departamento

print("--- Herança em Múltiplos Níveis ---")
gerente1 = Gerente("Leticia Sobral", "leticia@exemplo.com", 5000, "Administrativo")
print(f"Nome: {gerente1.nome}")
print(f"E-mail: {gerente1.email}")
print(f"Salário: {gerente1.salario}")
print(f"Departamento: {gerente1.departamento}")
print("\n" + "="*50 + "\n")

# ====================================================================
# Passo 5 e 6: Herança Múltipla e Ordem de Resolução
# ====================================================================

class Autenticacao:
    def login(self):
        return "Login realizado."

    def status(self):
        return "Status da Autenticação."

class Permissao:
    def verificar_permissao(self):
        return "Permissão verificada."
    
    def status(self):
        return "Status da Permissão."

class Administrador(Autenticacao, Permissao):
    pass

print("--- Herança Múltipla e MRO ---")
admin1 = Administrador()
print(f"Método 'login()' da classe Autenticacao: {admin1.login()}")
print(f"Método 'verificar_permissao()' da classe Permissao: {admin1.verificar_permissao()}")

print(f"\nChamando o método 'status()' de Administrador: {admin1.status()}")

print("\nOrdem de Resolução de Métodos (MRO):")
print(Administrador.__mro__)
print("\n" + "="*50 + "\n")