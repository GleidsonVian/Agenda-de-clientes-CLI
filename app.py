import pandas as pd

# Função para adicionar um novo cliente
def adicionar_cliente(nome, telefone, servico, descricao, arquivo_excel='agenda_clientes.xlsx'):
    # Criar um dicionário com os dados do cliente
    novo_cliente = {
        'Nome': nome,
        'Telefone': telefone,
        'Serviço': servico,
        'Descrição': descricao
    }
    
    try:
        # Tentar ler o arquivo existente
        df = pd.read_excel(arquivo_excel)
    except FileNotFoundError:
        # Se o arquivo não existir, criar um novo DataFrame
        df = pd.DataFrame(columns=['Nome', 'Telefone', 'Serviço', 'Descrição'])
    
    # Adicionar o novo cliente ao DataFrame
    df = df._append(novo_cliente, ignore_index=True)
    
    # Salvar o DataFrame atualizado no arquivo Excel
    df.to_excel(arquivo_excel, index=False)

# Função para listar todos os clientes
def listar_clientes(arquivo_excel='agenda_clientes.xlsx'):
    try:
        df = pd.read_excel(arquivo_excel)
        return df
    except FileNotFoundError:
        return pd.DataFrame(columns=['Nome', 'Telefone', 'Serviço', 'Descrição'])


while True:

    resposta = input('Deseja adicionar outro registro? (n) para sair: ')
    if resposta == 'n':
        break
    nome = input('Nome: ')
    telefone = input('Telefone: ')
    servico = input('Serviço realizado: ')
    descricao = input('Descrição do serviço: ')
    adicionar_cliente(nome, telefone, servico, descricao)


clientes = listar_clientes()

