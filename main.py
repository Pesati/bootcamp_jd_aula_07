from etl import ler_csv, produtos_eletronicos , somatorio_vendas

arquivo_csv = "vendas.csv"

ler_arquivo_csv = ler_csv(arquivo_csv)
somente_eletronicos = produtos_eletronicos(ler_arquivo_csv)
valor_venda_eletronicos = somatorio_vendas(somente_eletronicos)

print(somente_eletronicos)
print(valor_venda_eletronicos)