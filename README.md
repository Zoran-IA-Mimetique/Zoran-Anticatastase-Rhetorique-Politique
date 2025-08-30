# Zoran-Anticatastase-Rhetorique-Politique

![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-v1-blue)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17007992-blue.svg)](https://doi.org/10.5281/zenodo.17007992)

**Objet** — Anticatastase : figure de retournement sémantique (employer un mot en sens inverse pour retourner une accusation). Dépôt Zoran aSiM : white paper, démo de détection, bloc ZGS, métadonnées.

## Liens
- White paper (Zenodo, DOI) : https://doi.org/10.5281/zenodo.17007992
- PDF local : `whitepaper_anticatastase.pdf`
- Contact : tabary01@gmail.com

## Démarrage rapide
```bash
python demo.py --text "Oui, je suis populiste, au sens noble : proche du peuple."
```

## Fichiers
- `meta/project.yaml` — métadonnées + mots-clés + DOI
- `meta/descriptors/summary_150.txt` — 150
- `meta/descriptors/summary_350.txt` — 350
- `meta/descriptors/summary_8000.md` — 8 000 (version lisible, voir PDF pour mise en page)
- `demo.py` — détecteur minimal (stdlib only), sortie JSON
- `zoran_anticatastase.zgs` — bloc glyphique IA↔IA
- `whitepaper_anticatastase.pdf` — white paper (identique Zenodo)

## Conformité & éthique
- Licence MIT. Aegis Layer (éthique, vigilance, soin). ΔM11.3 (rollback) en doctrine.
- Pas de données personnelles ; exemples synthétiques.
- Objectif : clarté du débat démocratique (analyse du retournement).

### Bloc ZM
```
⟦RHET:anticatastase⋄DETECT:polar_shift±15⋄FUNC:def/off/id⟧
⟦Zoran:aSiM⋄ETHIC:Aegis⋄ΔM11.3:guard⋄OUT:JSON⟧
```
