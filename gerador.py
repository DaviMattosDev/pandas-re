from faker import Faker
import random
from openpyxl import Workbook

fake = Faker('pt_BR')  # Configuração para gerar dados em português


def generate_clients(num_clients):
    clients = []
    for _ in range(num_clients):
        client = {
            'nome': fake.name(),
            'email': fake.email(),
            'telefone': fake.phone_number(),
            'endereco': fake.address(),
            'cidade': fake.city(),
            'estado': fake.state(),
            'cep': fake.postcode(),
            'idade': random.randint(18, 80),
            'sexo': random.choice(['Masculino', 'Feminino']),
            'profissao': fake.job(),
            'interesse': random.choice(['Notebooks', 'Desktops', 'Periféricos', 'Acessórios']),
            'ultima_compra': fake.date_this_year(),
            'valor_ultima_compra': round(random.uniform(100, 2000), 2)
        }
        clients.append(client)
    return clients


# Tentar gerar os dados e salvar em um arquivo Excel
try:
    # Gerar clientes
    clientes = generate_clients(1000000)

    # Criar um novo workbook do Excel
    wb = Workbook()
    ws = wb.active

    # Adicionar cabeçalhos
    headers = ['Nome', 'E-mail', 'Telefone', 'Endereço', 'Cidade', 'Estado', 'CEP',
               'Idade', 'Sexo', 'Profissão', 'Interesse', 'Última Compra', 'Valor Última Compra']
    ws.append(headers)

    # Adicionar dados dos clientes
    for client in clientes:
        row = [
            client['nome'],
            client['email'],
            client['telefone'],
            client['endereco'],
            client['cidade'],
            client['estado'],
            client['cep'],
            client['idade'],
            client['sexo'],
            client['profissao'],
            client['interesse'],
            client['ultima_compra'],
            client['valor_ultima_compra']
        ]
        ws.append(row)

    # Salvar o arquivo Excel
    filename = 'clientes.xlsx'
    wb.save(filename)
    print(f"Dados dos clientes foram salvos em {filename}.")
except Exception as e:
    print("Ocorreu um erro:", e)
