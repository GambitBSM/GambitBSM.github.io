---
title: 'namespace hdf5tools'

description: "[No description available]"

---

# hdf5tools



[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| def | **[get_dset_lengths](/documentation/code/namespaces/namespacehdf5tools/#function-get-dset-lengths)**(d d, group group, dsets dsets) |
| def | **[check_lengths](/documentation/code/namespaces/namespacehdf5tools/#function-check-lengths)**(d d) |
| def | **[copy_dset](/documentation/code/namespaces/namespacehdf5tools/#function-copy-dset)**(indset indset, outdset outdset, nextempty nextempty, basemsg basemsg ="") |
| def | **[copy_dset_whole](/documentation/code/namespaces/namespacehdf5tools/#function-copy-dset-whole)**(indset indset, outdset outdset, nextempty nextempty, basemsg basemsg ="") |
| def | **[cantor_pairing](/documentation/code/namespaces/namespacehdf5tools/#function-cantor-pairing)**(x x, y y) |
| def | **[check_for_duplicates](/documentation/code/namespaces/namespacehdf5tools/#function-check-for-duplicates)**(fout fout, group group) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[chunksize](/documentation/code/namespaces/namespacehdf5tools/#variable-chunksize)**  |
| int | **[bufferlength](/documentation/code/namespaces/namespacehdf5tools/#variable-bufferlength)**  |
| int | **[max_ppidpairs](/documentation/code/namespaces/namespacehdf5tools/#variable-max-ppidpairs)**  |

## Detailed Description




```
Tools for reading/writing data from HDF5 files```


## Functions Documentation

### function get_dset_lengths

```
def get_dset_lengths(
    d d,
    group group,
    dsets dsets
)
```


### function check_lengths

```
def check_lengths(
    d d
)
```


### function copy_dset

```
def copy_dset(
    indset indset,
    outdset outdset,
    nextempty nextempty,
    basemsg basemsg =""
)
```


### function copy_dset_whole

```
def copy_dset_whole(
    indset indset,
    outdset outdset,
    nextempty nextempty,
    basemsg basemsg =""
)
```


### function cantor_pairing

```
def cantor_pairing(
    x x,
    y y
)
```


### function check_for_duplicates

```
def check_for_duplicates(
    fout fout,
    group group
)
```



## Attributes Documentation

### variable chunksize

```
int chunksize =  1000;
```


### variable bufferlength

```
int bufferlength =  100;
```


### variable max_ppidpairs

```
int max_ppidpairs =  10*bufferlength;
```





-------------------------------

Updated on 2022-09-07 at 13:49:48 +0000