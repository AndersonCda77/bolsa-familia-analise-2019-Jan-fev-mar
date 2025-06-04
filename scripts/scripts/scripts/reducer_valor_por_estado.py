#!/usr/bin/env python3
import sys

current_uf = None
total_valor = 0.0

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        print(f"DEBUG: Linha recebida: {line}", file=sys.stderr)
        fields = line.split('\t')
        if len(fields) != 2:
            print(f"DEBUG: Formato inválido, esperado 2 campos, encontrado {len(fields)}: {line}", file=sys.stderr)
            continue

        uf, valor = fields
        valor = float(valor)
        print(f"DEBUG: UF={uf}, Valor={valor}", file=sys.stderr)

        if current_uf == uf:
            total_valor += valor
        else:
            if current_uf:
                print(f"{current_uf}\t{total_valor}")
                print(f"DEBUG: Saída gerada: {current_uf}\t{total_valor}", file=sys.stderr)
            current_uf = uf
            total_valor = valor
    except (ValueError, IndexError) as e:
        print(f"DEBUG: Erro ao processar linha: {line} | Erro: {e}", file=sys.stderr)
        continue

if current_uf:
    print(f"{current_uf}\t{total_valor}")
    print(f"DEBUG: Saída final gerada: {current_uf}\t{total_valor}", file=sys.stderr)
