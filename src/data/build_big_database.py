import pandas as pd
import numpy as np
from pathlib import Path

THIS_FILE = Path(__file__)
THIS_DIR = THIS_FILE.parent
INTERIM_DATA = THIS_DIR.joinpath("./../../data/interim/")

FULL_DB = "ripa-2018.csv"
datasets = []
for csv in INTERIM_DATA.glob("*-part-*.csv"):
    print(f"Reading dataset: {csv.name}")
    datasets.append(pd.read_csv(csv))

big_dataset = pd.concat(datasets, ignore_index=True)
print("Saving dataset...")
big_dataset.to_csv(INTERIM_DATA.joinpath(FULL_DB), index = False)
