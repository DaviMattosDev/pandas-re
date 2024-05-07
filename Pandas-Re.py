import pandas as pd
import csv
import re

# Função para substituir caracteres especiais


def substituir_caracteres_especiais(texto):
    return re.sub(r'[^\x00-\x7F]+', '', texto)


# Lista para armazenar os dados
dados = []

# Abrir o arquivo CSV e ler os dados
with open('dados.csv', newline='', encoding='latin1') as csvfile:
    # Ler o CSV usando o delimitador ","
    leitor_csv = csv.reader(csvfile, delimiter=',')
    # Iterar sobre as linhas do CSV
    for linha in leitor_csv:
        # Substituir caracteres especiais e remover aspas extras
        linha = [substituir_caracteres_especiais(
            valor.strip('\"')) for valor in linha]
        # Adicionar a linha à lista de dados
        dados.append(linha)

# Criar DataFrame com os dados
df = pd.DataFrame(dados[1:], columns=dados[0])

# Renomear colunas
df.columns = ['Nome', 'E-mail', 'Telefone', 'Endereço', 'Cidade', 'Estado', 'CEP',
              'Idade', 'Sexo', 'Profissão', 'Interesse', 'Última Compra', 'Valor Última Compra']

# Funções para extrair informações com expressões regulares


def extrair_nome_completo(nome):
    match = re.search(r"(\w+\s?\w+)", nome)
    if match:
        return match.group(0)
    else:
        return ""


def validar_email(email):
    match = re.search(
        r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)", email)
    return bool(match)


def formatar_telefone(telefone):
    match = re.search(
        r"(\+?\d{2,3}\s?\(?\d{2,3}\)?\s?\d{3,5}-\d{3,5})", telefone)
    if match:
        return match.group(0)
    else:
        return ""


def extrair_cep(cep):
    match = re.search(r"(\d{5}-\d{3})", cep)
    if match:
        return match.group(0)
    else:
        return ""


def validar_idade(idade):
    try:
        idade = int(idade)
        if idade > 0:
            return True
        else:
            return False
    except ValueError:
        return False


def validar_sexo(sexo):
    return sexo in ["Masculino", "Feminino"]


def extrair_profissao(profissao):
    match = re.search(r"(.+)", profissao)
    if match:
        return match.group(0)
    else:
        return ""


def extrair_interesse(interesse):
    match = re.search(r"(.+)", interesse)
    if match:
        return match.group(0)
    else:
        return ""


def extrair_data_ultima_compra(data):
    match = re.search(r"(\d{4}-\d{2}-\d{2})", data)
    if match:
        return match.group(0)
    else:
        return ""


def extrair_valor_ultima_compra(valor):
    try:
        valor = float(valor.replace(',', '.'))
        if valor >= 0:
            return valor
        else:
            return None
    except ValueError:
        return None


# Aplicar funções em cada coluna
df['Nome'] = df['Nome'].apply(extrair_nome_completo)
df['E-mail'] = df['E-mail'].apply(validar_email)
df['Telefone'] = df['Telefone'].apply(formatar_telefone)
df['CEP'] = df['CEP'].apply(extrair_cep)
df['Idade'] = df['Idade'].apply(validar_idade)
df['Sexo'] = df['Sexo'].apply(validar_sexo)
df['Profissão'] = df['Profissão'].apply(extrair_profissao)
df['Interesse'] = df['Interesse'].apply(extrair_interesse)
df['Última Compra'] = df['Última Compra'].apply(extrair_data_ultima_compra)
df['Valor Última Compra'] = df['Valor Última Compra'].apply(
    extrair_valor_ultima_compra)

# Analisar e salvar dados
print("Primeiras linhas do DataFrame:")
print(df.head())

print("\nInformações sobre o DataFrame:")
print(df.info())

print("\nEstatísticas descritivas:")
print(df.describe())

print("\nContagem de valores únicos:")
print(df.nunique())

print("\nValores faltantes por coluna:")
print(df.isnull().sum())

df.to_csv('dados_com_informacoes_adicionais.csv', index=False)
