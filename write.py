import h5py
import numpy as np


f = h5py.File("mytestfile.h5", "w")
grp = f.create_group("subgroup")
grp2 = grp.create_group("subsubgroup")
dset2 = grp.create_dataset("another_dataset", (50,), dtype='i', data=range(0,50))
dset3 = f.create_dataset('subgroup2/dataset_three', (10,), dtype='i')
dset4 = grp2.create_dataset("yet_another_dataset", (20,), dtype='f')
print(dset2.name)
print(dset3.name)
print(dset4.name)
