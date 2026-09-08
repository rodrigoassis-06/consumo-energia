# Calculadora de Consumo Elétrico Inteligente

def calcular_consumo():
    print("=== CALCULADORA DE CONSUMO ELÉTRICO ===\n")
    
    aparelho = input("Digite o nome do aparelho (ex: Geladeira): ")
    potencia = float(input("Digite a potência do aparelho em Watts (W): "))
    horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))
    
    consumo_mensal = (potencia * horas_dia * 30) / 1000
    
    tarifa_kwh = 0.75
    custo_estimado = consumo_mensal * tarifa_kwh
    
    print("\n----------------------------------")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo estimado: {consumo_mensal:.1f} kWh/mês")
    print(f"Custo estimado: R$ {custo_estimado:.2f}/mês")
    print("----------------------------------")

if __name__ == "__main__":
    calcular_consumo()