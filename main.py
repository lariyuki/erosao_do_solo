import numpy as np
from models import simulate_erosion
from plot import plot_terrain
from utils import export_terrain_to_csv, export_terrain_stats

def main():
    print("Simulador de Erosão de Solo")
    tamanho = int(input("Tamanho do terreno (NxN): "))
    intensidade = float(input("Intensidade da chuva (0 a 1): "))
    passos = int(input("Quantos ciclos de chuva (ex: 100): "))

    # Terreno inicial aleatório
    terreno = np.random.rand(tamanho, tamanho) * 100

    # Mostrar imagem antes da erosão
    plot_terrain(terreno, "Terreno original (antes da erosão)")

    # Aplicar simulação de erosão
    print("\nSimulando erosão...")
    resultado = simulate_erosion(terreno.copy(), intensidade, passos)

    # Mostrar imagem depois da erosão
    plot_terrain(resultado, "Terreno após erosão")

    # Exportar CSV e estatísticas
    export_terrain_to_csv(resultado, "terreno_erosao.csv")
    export_terrain_stats(resultado, "estatisticas_terreno.txt")

    print("Simulação concluída.")

if __name__ == "__main__":
    main()



