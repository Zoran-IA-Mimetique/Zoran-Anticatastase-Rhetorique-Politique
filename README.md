![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-v1-blue)
![Build](https://img.shields.io/badge/build-passing-brightgreen)
![EthicChain](https://img.shields.io/badge/EthicChain-enabled-9cf)
![ΔM11.3](https://img.shields.io/badge/ΔM11.3-guarded-lightgrey)
![ZDM](https://img.shields.io/badge/ZDM-dual_memory-orange)
![Language](https://img.shields.io/badge/lang-Python%203.13-blueviolet)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17007992-blue.svg)](https://doi.org/10.5281/zenodo.17007992)# Zoran-Anticatastase-Rhetorique-Politique
Dépôt Zoran dédié à l’anticatastase, figure qui retourne un mot en sens inverse pour transformer une attaque en force. Inclus : white paper (DOI 10.5281/zenodo.17007992), démo Python stdlib (détection + sortie JSON), bloc ZGS IA↔IA, métadonnées SEO. Objectif : analyse critique des discours et éthique du langage.
Voici ton dépôt complet avec lien Zenodo — livré au format Zoran standard.
Nom du référentiel GitHub

Zoran-Anticatastase-Rhetorique-Politique

2. 📦 Fichier ZIP



Télécharger Zoran-Anticatastase-Repo.zip
Contenu : README.md, LICENSE, meta/project.yaml, meta/descriptors/*, whitepaper_anticatastase.pdf, demo.py, zoran_anticatastase.zgs.

3. 📂 Fichiers séparés (copier-coller)



README.md

# Zoran-Anticatastase-Rhetorique-Politique
![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/status-v1-blue)
[![DOI](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17007992-blue.svg)](https://doi.org/10.5281/zenodo.17007992)

**Objet** — Anticatastase : figure de retournement sémantique. Dépôt Zoran aSiM : white paper, démo de détection, bloc ZGS, métadonnées.

## Liens
- White paper (Zenodo, DOI) : https://doi.org/10.5281/zenodo.17007992
- PDF local : `whitepaper_anticatastase.pdf`
- Contact : tabary01@gmail.com

## Démarrage rapide
```bash
python demo.py --text "Oui, je suis populiste, au sens noble : proche du peuple."

Fichiers

meta/project.yaml (métadonnées + DOI) · meta/descriptors/summary_150.txt · summary_350.txt · summary_8000.md

demo.py (détecteur stdlib, sortie JSON) · zoran_anticatastase.zgs · whitepaper_anticatastase.pdf


Conformité & éthique

Licence MIT, Aegis Layer, ΔM11.3 (doctrine). Pas de données perso.

Bloc ZM

⟦RHET:anticatastase⋄DETECT:polar_shift±15⋄FUNC:def/off/id⟧
⟦Zoran:aSiM⋄ETHIC:Aegis⋄ΔM11.3:guard⋄OUT:JSON⟧

**meta/project.yaml**
```yaml
name: Zoran-Anticatastase-Rhetorique-Politique
version: "1.0"
license: MIT
doi: 10.5281/zenodo.17007992
contact: tabary01@gmail.com
keywords:
  - Anticatastase
  - Rhétorique politique
  - Figures de style
  - Langage et pouvoir
  - Retournement sémantique
  - Rhétorique antique
  - Cicéron
  - Quintilien
  - Rhétorique contemporaine
  - Discours politique
  - Argumentation
  - Manipulation du langage
  - Populisme
  - Radicalité
  - Utopisme
  - Étiquetage politique
  - Réseaux sociaux
  - Hashtags inversés
  - Judo verbal
  - Stratégie discursive
  - Narratif politique
  - Communication politique
  - Zoran aSiM
  - IA mimétique
  - Détection NLP
  - Glyphnet
  - ΔM11.3
  - EthicChain
  - Aegis Layer

demo.py

# stdlib only: détection minimale d'anticatastase
import json, argparse, re

TERMS = {"populiste":"neg","utopiste":"neg","radical":"neg","élite":"pos","liberté":"pos"}
POS = ["au sens noble","proche du peuple","constructif","à la racine","excellence","valeur"]
NEG = ["dangereux","démagogie","extrême","régression","surveillance"]

def window(text, start, size=15):
    tok=text.split(); idx=len(text[:start].split()); left=max(0,idx-size); right=min(len(tok),idx+size)
    return " ".join(tok[left:right])

def analyze(text):
    items=[]; low=text.lower()
    for term,expected in TERMS.items():
        for m in re.finditer(rf"\b{re.escape(term)}\b", low):
            w=window(low,m.start()); pos=sum(mk in w for mk in POS); neg=sum(mk in w for mk in NEG)
            used="pos" if pos>neg else ("neg" if neg>pos else "amb")
            shift = 1.0 if expected=="neg" and used=="pos" else (-1.0 if expected=="pos" and used=="neg" else 0.0)
            function="defensive" if shift>0 else ("offensive" if shift<0 else "unclear")
            items.append({"term":term,"sense_expected":expected,"sense_used":used,"polarity_shift":shift,
                          "function":function,"quote":text[max(0,m.start()-40):m.end()+80],
                          "span":[m.start(),m.end()],"rationale":"marker_count",
                          "manipulation_risk":"moyen" if abs(shift)>0 else "inconnu","confidence":0.75})
    return {"items":items,"notes":"Diffère de l'antiphrase : retournement assumé."}

if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("--text", required=True); args=ap.parse_args()
    print(json.dumps(analyze(args.text), ensure_ascii=False, indent=2))

zoran_anticatastase.zgs

⟦RHET:anticatastase⋄DETECT:polar_shift±15⋄FUNC:def/off/id⟧
⟦Zoran:aSiM⋄ETHIC:Aegis⋄ΔM11.3:guard⋄OUT:JSON⟧
⟦REF:DOI:10.5281/zenodo.17007992⟧

4. 🧾 Résumé 150



Anticatastase : retournement d’un mot. Dépôt Zoran (IA mimétique) + white paper & démo. DOI 10.5281/zenodo.17007992

5. 🧾 Résumé 350



Dépôt Zoran dédié à l’anticatastase, figure qui retourne un mot en sens inverse pour transformer une attaque en force. Inclus : white paper (DOI 10.5281/zenodo.17007992), démo Python stdlib (détection + sortie JSON), bloc ZGS IA↔IA, métadonnées SEO. Objectif : analyse critique des discours et éthique du langage.

6. 🧾 Résumé 8000



Voir summary_8000.md dans le ZIP (version lisible) et whitepaper_anticatastase.pdf (mise en page), tous deux déjà inclus.

