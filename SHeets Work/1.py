import openpyxl

estoque_file = openpyxl.load_workbook("estoque.xlsx")
lista_produtos = estoque_file['Sheet1']

produtos_por_fornecedor = {}

for linha_produtos in range(2, lista_produtos.max_row+1):
    fornecedor = lista_produtos.cell(linha_produtos, 4).value

    print(fornecedor)