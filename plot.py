import matplotlib.pyplot as plt
import os

def plot_terrain(terrain, title="", save_path=None):
    plt.figure(figsize=(8, 6))
    plt.imshow(terrain, cmap='terrain')
    plt.colorbar(label='Altura (m)')
    plt.title(title)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.tight_layout()

    # salva a imagem se um caminho for fornecido
    if save_path:
        folder = os.path.dirname(save_path)
        if folder:
            os.makedirs(folder, exist_ok=True)
        plt.savefig(save_path, dpi=300)
        print(f"Imagem salva em: {save_path}")

    plt.show()
