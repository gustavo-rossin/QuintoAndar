import pandas as pd

excel_file = "Capital_share_bike__1___1_.xlsx"
output_csv_file = "capital_share_bike.csv"

# Carregar a planilha
df = pd.read_excel(excel_file)

# testa se o arquivo foi carregado corretamente
print(df.head())

# Salvar como CSV
df.to_csv(output_csv_file, index=False)  # index=False para não salvar o índice
print(f"Arquivo convertido com sucesso: {output_csv_file}")
