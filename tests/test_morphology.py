import numpy as np
import cv2 as cv
from astropy.stats import sigma_clipped_stats


def test_sigma_clipped_stats_synthetic():
    # Création d'une image synthétique 100x100 avec fond uniforme bruité
    np.random.seed(42)
    background = np.random.normal(loc=100.0, scale=5.0, size=(100, 100))
    # Ajout d'étoiles saturées
    background[20, 20] = 500.0
    background[50, 50] = 600.0
    background[80, 80] = 750.0

    mean, median, std = sigma_clipped_stats(background, sigma=3.0)

    # La médiane et la moyenne doivent être très proches de 100 malgré les étoiles aberrantes
    assert 98.0 < median < 102.0
    assert 4.0 < std < 6.0


def test_morphological_erosion_and_blending():
    # Image synthétique flottante normalisée [0, 1]
    image = np.zeros((50, 50), dtype=np.float64)
    # Disque lumineux simulant une étoile
    cv.circle(image, (25, 25), 5, 1.0, -1)

    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3, 3))
    eroded = cv.erode(image, kernel, iterations=1)

    # L'érosion doit réduire la somme totale d'intensité de l'étoile
    assert np.sum(eroded) < np.sum(image)

    # Masque binaire lissé
    mask = (image > 0.1).astype(np.float64)
    blurred_mask = cv.GaussianBlur(mask, (5, 5), sigmaX=1.5)

    # Recombinaison pondérée : M * I_erodee + (1 - M) * I_originale
    blended = blurred_mask * eroded + (1.0 - blurred_mask) * image

    assert blended.shape == (50, 50)
    assert blended.dtype == np.float64
    assert np.all(blended >= 0.0) and np.all(blended <= 1.0)
