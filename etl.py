import csv

arquivo_csv = 'vendas.csv'

def ler_csv(nome_arquivo: str) -> list[dict]:
    
    """Lê um arquivo CSV e retorna uma lista de dicionários."""
    
    with open(nome_arquivo) as csvfile:
        reader = csv.DictReader(csvfile)
        return list(reader)
 
def produtos_eletronicos(lista: list) -> list[dict]:
    
    arquivos_eletronicos = []
    for eletronico in lista:
        if eletronico['Categoria'] == 'Electronics':
            arquivos_eletronicos.append(eletronico)
    return arquivos_eletronicos

def somatorio_vendas(produtos_eletronicos: list) -> int:
    
    valor_total = 0
    for produto in produtos_eletronicos:
        valor_total += int(produto.get("Venda"))
    return valor_total
    
