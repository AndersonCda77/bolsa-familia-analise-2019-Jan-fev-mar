#!/usr/bin/env python3
import sys

# Ignora a linha de cabeçalho
first_line = True

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    if first_line:
        first_line = False
        continue

    try:
        columns = line.split(';')
        uf = columns[2].strip()  # Coluna 2: UF
        valor_parcela = float(columns[8].replace(',', '.'))  # Coluna 8: Valor Parcela
        print(f"{uf}\t{valor_parcela}")
    except (IndexError, ValueError):
        continue
