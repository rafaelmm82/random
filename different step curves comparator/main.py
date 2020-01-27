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

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(pn1[:, 0], pn1[:, 1], 'C1', label='Original')
ax.plot(nc1[0, :], nc1[1, :], 'C5', label='Approximate')
ax.legend()
plt.show()



# %%


# Before

# fig, ax = plt.subplots(figsize=(12, 6))
fig, ax = plt.subplots()
plt.gca().set_aspect('equal', adjustable='box')
plt.ylim(-1, 6)
ax.plot(nc1[0, :2500], nc1[1, :2500], 'C1', label='C1')
ax.plot(nc1[0, :2500], nc2[1, :2500], 'C2', label='C2')
ax.plot(nc1[0, :2500], nc3[1, :2500], 'C3', label='C3')
ax.plot(nc1[0, :2500], nc4[1, :2500], 'C4', label='C4')
ax.plot(nc1[0, :2500], nc5[1, :2500], 'C5', label='C5')
ax.legend()
plt.show()

# %%
# After
all_curves = np.array([nc1[1, :2500],
                       nc2[1, :2500],
                       nc3[1, :2500],
                       nc4[1, :2500],
                       nc5[1, :2500]])

all_mean = all_curves.mean(axis=0)
all_std = all_curves.std(axis=0)
over_line = all_mean + all_std
under_line = all_mean - all_std

# %%
# plot after
# fig, ax = plt.subplots(figsize=(200, 6))
# plt.axis('equal')
plt.gca().set_aspect('equal', adjustable='box')
plt.ylim(-1, 6)
plt.plot(nc1[0, :2500], nc1[1, :2500], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :2500], nc2[1, :2500], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :2500], nc3[1, :2500], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :2500], nc4[1, :2500], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :2500], nc5[1, :2500], color='gray', linewidth=0.5, alpha=0.8)
plt.plot(nc1[0, :2500], all_mean, linewidth=2) #mean curve.
plt.fill_between(nc1[0, :2500], under_line, over_line, color='b', alpha=.1) #std curves.

plt.show()

