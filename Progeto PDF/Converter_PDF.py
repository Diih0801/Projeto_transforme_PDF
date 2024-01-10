import tabula
import pandas as pd

def pdf_para_dataframe(rota_arquivo):
    # Extrair tabela do arquivo PDF
    tabela = tabula.read_pdf(rota_arquivo, pages='all',multiple_tables=True)

    # Inicializando um DataFrame vazio para armazenar as tabelas combinadas
    dataframe_combinado = pd.DataFrame()

    # Combinar todas as tabelas em um unico DataFrame
    for tabela in tabela:
        df = tabela.copy()
        dataframe_combinado = pd.concat([dataframe_combinado, df], ignore_index=True)

    return dataframe_combinado

# Rota do arquivo PDF no seu computador
rota_pdf = ("C:\\Users\\paaml\\OneDrive\\Área de Trabalho\\Progeto Marcelo\\Pedidos\\4500368508.pdf")

# Chamar função para converter o PDF em um DataFrame único.
dataframe_unico = pdf_para_dataframe(rota_pdf)

# Transformar para Excel
dataframe_unico.to_excel('Pedido_08_excel.xlsx',index=False)
