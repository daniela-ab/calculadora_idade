from datetime import datetime

# Solicitar a data de nascimento do usuário
data_nascimento_str = input("Digite sua data de nascimento (no formato DD/MM/AAAA): ")

# Converter a data de nascimento para um objeto datetime
data_nascimento = datetime.strptime(data_nascimento_str, "%d/%m/%Y")

# Obter a data atual
data_atual = datetime.now()

# Calcular a diferença entre as datas
diferenca = data_atual - data_nascimento

# Calcular a idade em anos, meses, dias, semanas, horas e segundos
idade_anos = diferenca.days // 365
idade_meses = diferenca.days // 30
idade_dias = diferenca.days
idade_semanas = diferenca.days // 7
idade_horas = diferenca.days * 24
idade_segundos = diferenca.total_seconds()

# Exibir a idade nos seis formatos diferentes
print(f"Idade em anos: {idade_anos} anos")
print(f"Idade em meses: {idade_meses} meses")
print(f"Idade em semanas: {idade_semanas} semanas")
print(f"Idade em dias: {idade_dias} dias")
print(f"Idade em horas: {idade_horas} horas")
print(f"Idade em segundos: {idade_segundos} segundos")