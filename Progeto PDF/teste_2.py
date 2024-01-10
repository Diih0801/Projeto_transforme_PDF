import tabula
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import NamedStyle

# Especifique o caminho para o arquivo PDF
caminho_pdf = "C:\\Users\\paaml\\OneDrive\\Área de Trabalho\\Progeto Marcelo\\4500368508.pdf"

# Use tabula para extrair a tabela do PDF
tabelas = tabula.read_pdf(caminho_pdf, pages='all')

# Supondo que você queira trabalhar com a primeira tabela extraída
tabela = tabelas[0]

# Crie um DataFrame do pandas com a tabela extraída
df = pd.DataFrame(tabela)

# Crie um novo arquivo Excel e escreva o DataFrame nele
excel_path = "C:\\Users\\paaml\\OneDrive\\Área de Trabalho\\Progeto Marcelo\\4500368508.xlsx"
df.to_excel(excel_path, index=False, header=False)

# Carregue o arquivo Excel usando openpyxl para formatar as colunas
workbook = Workbook()
sheet = workbook.active
df_excel = pd.read_excel(excel_path, header=None)

# Defina estilos específicos para as colunas conforme necessário
style_header = NamedStyle(name="header_style", font="Bold")
sheet.append(list(df_excel.columns))
for header_cell in sheet[3]:
    header_cell.style = style_header

# Salve as alterações no arquivo Excel
workbook.save(excel_path)