import numpy as np
import illustris_python as il
import pickle as pkl
import pandas as pd

sim = 'TNG300-1'
dmo = False

if dmo:
    sim = sim+'-Dark'

unpickled_df = pd.read_pickle("./"+sim+"_catalogue.pkl")

SubhaloMass = unpickled_df["SubhaloMass"]
