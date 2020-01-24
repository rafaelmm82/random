import pandas as pd
import numpy as np

# %%
# loading points for initial tests
pn1 = pd.read_csv('different step curves comparator/data_samples/section_1.tsv', sep='\t').to_numpy()
pn2 = pd.read_csv('different step curves comparator/data_samples/section_2.tsv', sep='\t').to_numpy()
pn3 = pd.read_csv('different step curves comparator/data_samples/section_3.tsv', sep='\t').to_numpy()
pn4 = pd.read_csv('different step curves comparator/data_samples/section_4.tsv', sep='\t').to_numpy()
pn5 = pd.read_csv('different step curves comparator/data_samples/section_5.tsv', sep='\t').to_numpy()

# %%
len(pn1)
min(pn1[0,:])


dpn1 = [pn1[i+1][0] - pn1[i][0] for i in range(pn1.shape[0] - 1)]
dpn1.remove(0.0)
min(dpn1)
