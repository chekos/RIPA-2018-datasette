import pandas as pd
import numpy as np
from pathlib import Path

THIS_FILE = Path(__file__)
THIS_DIR = THIS_FILE.parent
EXTERNAL_DATA = THIS_DIR.joinpath("./../../data/external/")
INTERIM_DATA = THIS_DIR.joinpath("./../../data/interim/")

FULL_DB = "RIPA Stop Data 2018.csv"
data = pd.read_csv(EXTERNAL_DATA.joinpath(FULL_DB))

dfs = np.array_split(data, 15)
for idx,df in enumerate(dfs):
    print(f"Saving dataset #{idx}")
    df.to_csv(INTERIM_DATA.joinpath(f"ripa-2018-part-{idx}.csv"), index = False)
    