# Classe ContaBancaria
class ContaBancaria:
    def __init__(self, numero, titular, saldo_inicial=0):
        self.numero = numero
        self.titular = titular
        # Atributo privado, a convenção em Python é usar um sublinhado
        self._saldo = saldo_inicial  

    def get_saldo(self):
        """Método getter para acessar o saldo."""
        return self._saldo

    def set_saldo(self, novo_saldo):
        """
        Método setter para modificar o saldo.
        A regra é que o saldo não pode ser negativo.
        """
        if novo_saldo >= 0:
            self._saldo = novo_saldo
            print("Saldo alterado com sucesso.")
        else:
            print("Erro: O saldo não pode ser um valor negativo.")

# ---

# Classe Pessoa
class Pessoa:
    def __init__(self, nome, data_nascimento, cpf, identidade):
        self.nome = nome
        self.data_nascimento = data_nascimento
        # Atributos privados
        self._cpf = cpf  
        self._identidade = identidade  

    # Métodos para o CPF
    def get_cpf(self):
        """Método getter para o CPF."""
        return self._cpf

    def set_cpf(self, novo_cpf):
        """Método setter para o CPF."""
        self._cpf = novo_cpf
        print("CPF alterado com sucesso.")

    # Métodos para a Identidade
    def get_identidade(self):
        """Método getter para a identidade."""
        return self._identidade

    def set_identidade(self, nova_identidade):
        """Método setter para a identidade."""
        self._identidade = nova_identidade
        print("Identidade alterada com sucesso.")

# ---

### **Exemplos de uso das classes**

print("### Exemplo de uso da ContaBancaria ###")
# Cria uma nova conta bancária
minha_conta = ContaBancaria("98765-4", "Walter Sobral", 500.0)
print(f"Número da Conta: {minha_conta.numero}")
print(f"Titular: {minha_conta.titular}")
print(f"Saldo atual: R$ {minha_conta.get_saldo()}")

# Tentando mudar o saldo para um valor válido
minha_conta.set_saldo(750.50)
print(f"Saldo após alteração: R$ {minha_conta.get_saldo()}")

# Tentando mudar o saldo para um valor inválido (negativo)
minha_conta.set_saldo(-100.0)
print(f"Saldo após tentativa de valor negativo: R$ {minha_conta.get_saldo()}")

print("\n" + "="*40 + "\n")

print("### Exemplo de uso da Pessoa ###")
# Cria um novo objeto da classe Pessoa
minha_pessoa = Pessoa("Rosângela Sobral", "05/03/1982", "111.222.333-44", "2345678-9")
print(f"Nome: {minha_pessoa.nome}")
print(f"Data de Nascimento: {minha_pessoa.data_nascimento}")
print(f"CPF: {minha_pessoa.get_cpf()}")
print(f"Identidade: {minha_pessoa.get_identidade()}")

# Alterando o CPF e a identidade
minha_pessoa.set_cpf("555.666.777-88")
minha_pessoa.set_identidade("9876543-2")
print(f"\nNovo CPF: {minha_pessoa.get_cpf()}")
print(f"Nova Identidade: {minha_pessoa.get_identidade()}")