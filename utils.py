import pandas as pd
import os

def export_terrain_to_csv(terrain, filename="terreno_erosao.csv", folder="dados"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    df = pd.DataFrame(terrain)
    df.to_csv(path, index=False)
    print(f"Terreno exportado para: {path}")

def export_terrain_stats(terrain, filename="estatisticas_terreno.txt", folder="dados"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)

    minimo = terrain.min()
    maximo = terrain.max()
    media = terrain.mean()
    desvio = terrain.std()

    texto = (
        "Estatísticas do Terreno após Erosão\n"
        f"→ Altura mínima: {minimo:.2f} m\n"
        f"→ Altura máxima: {maximo:.2f} m\n"
        f"→ Altura média : {media:.2f} m\n"
        f"→ Desvio padrão: {desvio:.2f} m\n"
    )

    with open(path, "w", encoding="utf-8") as f:
        f.write(texto)

    print(f"Estatísticas salvas em: {path}")

