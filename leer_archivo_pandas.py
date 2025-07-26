import pandas as pd


df = pd.read_excel("./music.xlsx")

print(df)
# import openpyxl
# from openpyxl import load_workbook

# xls = load_workbook("./music.xlsx")

# # ingresar a la hoja de excel deseada
# sheet = xls['PXNDX']

# print(f"numero de filas: {sheet.max_row} \nnumero de columnas: {sheet.max_column}")

# sheet.columns