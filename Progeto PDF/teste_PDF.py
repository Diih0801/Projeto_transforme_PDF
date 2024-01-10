import tabula

# Caminho do Arquivo PDF
caminho_pdf = "C:\\Users\\paaml\\OneDrive\\Área de Trabalho\\Progeto Marcelo\\Pedidos\\4500368508.pdf"

# Use a funcão read_pdf para extrair as tabelas do PDF
tabelas = tabula.read_pdf(caminho_pdf, pages='all', multiple_tables=True)

# Salvar a tabela no formato da sua escolha
for i, tabela in enumerate(tabelas):
   tabela.to_csv(f'Pedido_{i + 1}.csv', index=False)

#print(tabelas)