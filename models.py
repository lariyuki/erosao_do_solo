import numpy as np
from scipy.ndimage import gaussian_filter
from tqdm import trange  # barra de progresso

def simulate_erosion(terrain, rain_intensity, steps):
    erosion_rate = 0.1 * rain_intensity

    for _ in trange(steps, desc="Simulando erosão"):
        dx, dy = np.gradient(terrain)
        slope = dx**2 + dy**2

        erosion = erosion_rate * slope
        terrain -= erosion

        terrain = gaussian_filter(terrain, sigma=1)
        terrain = np.nan_to_num(terrain, nan=0.0, posinf=100.0, neginf=0.0)
        terrain = np.clip(terrain, 0, 100)

    return terrain
