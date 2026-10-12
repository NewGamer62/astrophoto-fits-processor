# 🌟 AstroPhoto FITS Processor

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
  <img src="https://img.shields.io/badge/OpenCV-Computer%20Vision-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white" alt="OpenCV" />
  <img src="https://img.shields.io/badge/Astropy-Astronomy-FF6F00?style=for-the-badge" alt="Astropy" />
  <img src="https://img.shields.io/badge/Interface-Tkinter%20%2F%20Matplotlib-3776AB?style=for-the-badge" alt="GUI" />
  <img src="https://img.shields.io/badge/Licence-MIT-green?style=for-the-badge" alt="Licence" />
</p>

---

## 📌 Présentation

**AstroPhoto FITS Processor** est un outil scientifique en Python dédié au traitement d'astrophotographies au format FITS (*Flexible Image Transport System*). Conçu pour l'imagerie du ciel profond (nébuleuses, galaxies), il permet d'atténuer sélectivement le champ d'étoiles au premier plan afin de réhausser le contraste et les détails des structures gazeuses et des poussières interstellaires sans altérer le fond nébulaire.

L'application allie la précision des calculs astrophysiques (`astropy`, `photutils`) aux algorithmes de morphologie mathématique (`opencv-python`), complétée par une interface graphique interactive en temps réel (`tkinter`, `matplotlib`).

---

## ✨ Fonctionnalités Clés

- **Détection d'Étoiles par Modélisation Gaussienne** :
  - Détection automatique via l'algorithme `DAOStarFinder` (`photutils`).
  - Estimation robuste du fond de ciel et de son écart-type ($\sigma$) par *sigma-clipping*.
  - Mécanisme de *fallback* adaptatif par seuillage de percentiles en cas de gradients de luminosité complexes.
- **Réduction Morphologique Sélective** :
  - Génération dynamique de masques binaires centrés sur les coordonnées stellaires.
  - Adoucissement des contours par filtre gaussien ($\sigma=2.0$) pour éliminer les artéfacts de bordure.
  - Érosion morphologique sélective (noyaux configurables) et recombinaison linéaire pondérée :
    $$\mathcal{I}_{\text{finale}} = \mathcal{M} \odot \mathcal{I}_{\text{érodée}} + (1 - \mathcal{M}) \odot \mathcal{I}_{\text{originale}}$$
- **Interface Graphique Interactive & Comparateur Avancé** :
  - Ajustement dynamique de 6 paramètres (seuil $\sigma$, rayon stellaire, flou gaussien, taille du noyau, itérations).
  - Mode **Blink Comparator** (alternance automatique avant/après toutes les 500ms).
  - Slider de fondu continu (0 à 100%) pour doser précisément la réduction.
  - Cartographie thermique des résidus (Heatmap différentielle) visualisant les zones érodées.

---

## 🛠️ Architecture Technique

```
astrophoto-fits-processor/
├── phase1/              # Prototypes d'érosion morphologique globale
├── phase2/              # Pipeline de détection DAOStarFinder & masquage sélectif
├── phase3/              # Application finale avec interface graphique interactive
│   └── app_interactive.py
├── examples/            # Jeux de données astronomiques de test (.fits)
│   ├── test_M31_linear.fits
│   └── HorseHead.fits
├── png/                 # Exports et rendus graphiques comparatifs
├── requirements.txt     # Dépendances du projet
└── README.md
```

---

## 👨‍💻 Rôle & Contributions Personnelles (Noa Gaillard)

Dans le cadre de ce projet mené en équipe :
- **Architecture & Conception de l'IHM (Phase 3)** : Conception et implémentation complète de l'application interactive sous Tkinter et Matplotlib (`app_interactive.py`).
- **Pipeline de Comparaison Visuelle** : Développement du moteur de *Blink Comparison*, du slider d'opacité en temps réel et du rendu différentiel par carte de chaleur.
- **Optimisation des Performances de Rendu** : Découplage du calcul de détection d'étoiles (coûteux) et de la boucle de rendu morphologique pour garantir une interface fluide et sans freeze lors de la manipulation des curseurs.
- **Robustesse & Précision Numérique** : Transition du pipeline de traitement vers `float64` pour éliminer les pertes de dynamique et artefacts de quantification inhérents au `uint8`.

---

## 🚀 Démarrage Rapide

### Prérequis
- Python 3.10 ou supérieur
- Environnement virtuel recommandé

### Installation

```bash
# 1. Cloner le dépôt
git clone https://github.com/NewGamer62/astrophoto-fits-processor.git
cd astrophoto-fits-processor

# 2. Créer et activer un environnement virtuel
python -m venv venv
# Windows :
.\venv\Scripts\activate
# Linux/macOS :
source venv/bin/activate

# 3. Installer les dépendances
pip install -r requirements.txt
```

### Lancement de l'Application

```bash
python phase3/app_interactive.py
```
Chargez un fichier FITS d'exemple (disponible dans `examples/HorseHead.fits` ou `test_M31_linear.fits`) et ajustez les paramètres d'érosion en temps réel.
