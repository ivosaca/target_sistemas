# juros simples, aplicado dia a dia mas sem ser juros sobre juros. Portando equação:
# Valor Final=Principal×(1+0.025×dias_de_atraso)


valor_inicial = float(input("Digite o valor inicial: "))
dias_atraso = int(input("Digite a quantidade de dias em atraso: "))
valor_final_simples = valor_inicial * (1 + 0.025 * dias_atraso)

print(f"Valor final com juros simples: R$ {valor_final_simples:.2f}")
