from pathlib import Path
import pandas as pd

DATA_DIR = Path("data")

def read_incendies(path, sep=";"):
    lines = [l for l in path.read_text(encoding="utf-8", errors="replace").splitlines() if l.strip()]
    counts = [len(l.split(sep)) for l in lines[:40]]
    n_cols = max(set(counts), key=counts.count)
    header_row = next(i for i, c in enumerate(counts) if c == n_cols)
    return pd.read_csv(path, sep=sep, skiprows=header_row)

for f in DATA_DIR.glob("Incendies_*.csv"):
    df = read_incendies(f)
    df.to_csv(f, sep=",", index=False)