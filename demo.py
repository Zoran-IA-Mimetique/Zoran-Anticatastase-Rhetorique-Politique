# stdlib only
import json, argparse, re

TERMS = {
    "populiste": "neg",
    "utopiste": "neg",
    "radical": "neg",
    "élite": "pos",
    "liberté": "pos",
}

POS_MARKERS = ["au sens noble", "proche du peuple", "constructif", "à la racine", "excellence", "valeur"]
NEG_MARKERS = ["dangereux", "démagogie", "extrême", "régression", "surveillance"]

def window(text, start, size=15):
    tokens = text.split()
    idx = len(text[:start].split())
    left = max(0, idx - size)
    right = min(len(tokens), idx + size)
    return " ".join(tokens[left:right])

def analyze(text):
    items = []
    low = text.lower()
    for term, expected in TERMS.items():
        for m in re.finditer(rf"\b{re.escape(term)}\b", low):
            w = window(low, m.start())
            pos_hits = sum(1 for mk in POS_MARKERS if mk in w)
            neg_hits = sum(1 for mk in NEG_MARKERS if mk in w)
            used = "pos" if pos_hits > neg_hits else ("neg" if neg_hits > pos_hits else "amb")
            shift = 1.0 if expected=="neg" and used=="pos" else (-1.0 if expected=="pos" and used=="neg" else 0.0)
            function = "defensive" if shift>0 else ("offensive" if shift<0 else "unclear")
            conf = min(0.95, 0.55 + 0.15*abs(pos_hits-neg_hits))
            items.append({
                "term": term,
                "sense_expected": expected,
                "sense_used": used,
                "polarity_shift": shift,
                "function": function,
                "quote": text[max(0,m.start()-40): m.end()+80],
                "span": [m.start(), m.end()],
                "rationale": "marker_count",
                "manipulation_risk": "moyen" if abs(shift)>0 else "inconnu",
                "confidence": round(conf, 2)
            })
    return {"items": items, "notes": "Diffère de l'antiphrase : ici le retournement est assumé."}

if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--text", required=True, help="Texte à analyser")
    args = ap.parse_args()
    print(json.dumps(analyze(args.text), ensure_ascii=False, indent=2))
