#----------------------------------------------------
# 1. Tratar erro de número inteiro
#----------------------------------------------------
print("--- Exercício 1 ---")
try:
    numero = int(input("Digite um número inteiro: "))
    print(f"O número digitado é: {numero}")
except ValueError:
    print("Erro: Você não digitou um número inteiro válido.")
print("--- Fim do Exercício 1 ---\n")

#----------------------------------------------------
# 2. Multiplicar dois números com tratamento de erro
#----------------------------------------------------
print("--- Exercício 2 ---")
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
except ValueError:
    print("Erro: Entrada inválida. Por favor, digite apenas números.")
print("--- Fim do Exercício 2 ---\n")

#----------------------------------------------------
# 3. Usar 'else' com 'try' para conversão
#----------------------------------------------------
print("--- Exercício 3 ---")
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: A entrada não é um número inteiro.")
else:
    print(f"A conversão foi bem-sucedida! O número é: {numero}")
print("--- Fim do Exercício 3 ---\n")

#----------------------------------------------------
# 4. Usar 'try' e 'finally' com arquivo
#----------------------------------------------------
print("--- Exercício 4 ---")
try:
    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)
except FileNotFoundError:
    print("Aviso: O arquivo 'dados.txt' não foi encontrado.")
finally:
    print("Encerrando programa.")
print("--- Fim do Exercício 4 ---\n")

#----------------------------------------------------
# 5. Função 'dividir' que lança ZeroDivisionError
#----------------------------------------------------
print("--- Exercício 5 ---")
def dividir(a, b):
    if b == 0:
        raise ZeroDivisionError("Não é possível dividir por zero.")
    return a / b

try:
    resultado = dividir(10, 2)
    print(f"Resultado da divisão: {resultado}")
    
    # Esta linha vai gerar a exceção
    # resultado_erro = dividir(5, 0)
    # print(resultado_erro) 
except ZeroDivisionError as e:
    print(f"Ocorreu um erro: {e}")
print("--- Fim do Exercício 5 ---\n")

#----------------------------------------------------
# 6. Exceção personalizada IdadeInvalidaError
#----------------------------------------------------
print("--- Exercício 6 ---")
class IdadeInvalidaError(Exception):
    """Exceção personalizada para idade negativa."""
    pass

def cadastrar_idade(idade):
    if idade < 0:
        raise IdadeInvalidaError("A idade não pode ser um valor negativo.")
    print(f"Idade cadastrada com sucesso: {idade} anos.")

try:
    cadastrar_idade(30)
    # Esta linha vai gerar a exceção
    # cadastrar_idade(-5) 
except IdadeInvalidaError as e:
    print(f"Erro: {e}")
print("--- Fim do Exercício 6 ---\n")

#----------------------------------------------------
# 7. Tratar múltiplos tipos de erro
#----------------------------------------------------
print("--- Exercício 7 ---")
try:
    num1_str = input("Digite o primeiro número: ")
    num2_str = input("Digite o segundo número: ")
    
    num1 = float(num1_str)
    num2 = float(num2_str)
    
    resultado = num1 / num2
    print(f"O resultado da divisão é: {resultado}")

except ValueError:
    print("Erro: Por favor, digite apenas números válidos.")
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero.")
print("--- Fim do Exercício 7 ---\n")

#----------------------------------------------------
# 8. 'try', 'else' e 'finally' para verificar par/ímpar
#----------------------------------------------------
print("--- Exercício 8 ---")
try:
    numero = int(input("Digite um número inteiro: "))
except ValueError:
    print("Erro: A entrada não é um número inteiro.")
else:
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")
finally:
    print("Fim do programa.")
print("--- Fim do Exercício 8 ---\n")

#----------------------------------------------------
# 9. Função 'sacar' com exceção personalizada
#----------------------------------------------------
print("--- Exercício 9 ---")
class SaldoInsuficienteError(Exception):
    """Exceção personalizada para saldo insuficiente."""
    pass

def sacar(saldo, valor):
    if valor > saldo:
        raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
    return saldo - valor

try:
    saldo_atual = 1500
    print(f"Saldo inicial: R${saldo_atual}")
    
    novo_saldo = sacar(saldo_atual, 500)
    print(f"Saque de R$500 realizado. Novo saldo: R${novo_saldo}")
    
    # Esta linha vai gerar a exceção
    # novo_saldo_erro = sacar(novo_saldo, 1500)
    # print(novo_saldo_erro)
except SaldoInsuficienteError as e:
    print(f"Erro: {e}")
print("--- Fim do Exercício 9 ---")