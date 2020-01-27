import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# %%
# loading points for initial tests
pn1 = pd.read_csv('different step curves comparator/data_samples/section_1.tsv', sep='\t').to_numpy()
pn2 = pd.read_csv('different step curves comparator/data_samples/section_2.tsv', sep='\t').to_numpy()
pn3 = pd.read_csv('different step curves comparator/data_samples/section_3.tsv', sep='\t').to_numpy()
pn4 = pd.read_csv('different step curves comparator/data_samples/section_4.tsv', sep='\t').to_numpy()
pn5 = pd.read_csv('different step curves comparator/data_samples/section_5.tsv', sep='\t').to_numpy()


# %%

nc1 = curve_fit(pn1, start=0, end=40, step=3000)
nc2 = curve_fit(pn2, start=0, end=40, step=3000)
nc3 = curve_fit(pn3, start=0, end=40, step=3000)
nc4 = curve_fit(pn4, start=0, end=40, step=3000)
nc5 = curve_fit(pn5, start=0, end=40, step=3000)


# %%


# Before

fig, ax = plt.subplots(figsize=(6, 3))
ax.plot(nc1[0, :], nc1[1, :], 'C1', label='C1')
ax.plot(nc1[0, :], nc2[1, :], 'C2', label='C2')
ax.plot(nc1[0, :], nc3[1, :], 'C3', label='C3')
ax.plot(nc1[0, :], nc4[1, :], 'C4', label='C4')
ax.plot(nc1[0, :], nc5[1, :], 'C5', label='C5')
ax.legend()
plt.show()

# %%
# After
all_curves = np.array([nc1[1, :],
                       nc2[1, :],
                       nc3[1, :],
                       nc4[1, :],
                       nc5[1, :]])

all_mean = all_curves.mean(axis=0)
all_std = all_curves.std(axis=0)
over_line = all_mean + all_std
under_line = all_mean - all_std

# %%
# plot after

plt.plot(nc1[0, :], nc1[1, :], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :], nc2[1, :], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :], nc3[1, :], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :], nc4[1, :], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :], nc5[1, :], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :], all_mean, linewidth=2) #mean curve.
plt.fill_between(nc1[0, :], under_line, over_line, color='b', alpha=.1) #std curves.

plt.show()
