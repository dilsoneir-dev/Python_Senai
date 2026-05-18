import pandas as pd
#criando uma série com uma lista de números
serie = pd.Series([10,20,30,40,50])
print(serie)

# dataframe

data = {
    "nome": ["Alice", "Bob", "Charlie", "David", "Eve"],
    "idade": [25, 30, 35, 40, 45],
    "cidade": ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Porto Alegre"]
}

df= pd.DataFrame(data)

print(df)

print(df[["nome"]])

#acessando uma linha específica
print(df.iloc[2]) #acessa a linha com índice 2 (Charlie)

#acessando uma linha específica
print(df.loc[2]) #acessa a linha com rótulo 2 (Charlie)


# 1. Criar o DataFrame com os dados dos funcionários
dados = {
    'NOME': ['Ana Silva', 'Carlos Souza', 'Mariana Costa'],
    'ENDERECO': ['Rua Flores, 123', 'Av. Central, 456', 'Alameda Sol, 789'],
    'DATA NASCIMENTO': ['15/05/1990', '22/11/1985', '03/08/1993'],
    'DATA DE ADMISSAO': ['10/02/2018', '01/06/2015', '25/07/2021'],
    'SALARIO': [4500.00, 7200.00, 3800.00],
    'CARGO': ['Analista de Dados', 'Gerente de Projetos', 'Assistente Administrativo']
}

df = pd.DataFrame(dados)

# Exibindo o DataFrame completo (opcional, para visualização)
print("--- DataFrame Completo ---")
print(df)
print("\n" + "-"*40 + "\n")

# 2. Mostrar na tela todas as linhas da coluna DATA DE ADMISSAO
print("--- Coluna: DATA DE ADMISSAO ---")
print(df['DATA DE ADMISSAO'])