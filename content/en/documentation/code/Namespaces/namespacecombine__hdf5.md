---
title: "namespace combine_hdf5"

description: "[No description available]"

---

# namespace combine_hdf5

[No description available] [More...](#detailed-description)

## Functions

|                | Name           |
| -------------- | -------------- |
| def | **[sigint_handler](/documentation/code/namespaces/namespacecombine__hdf5/#function-sigint-handler)**(signum signum, frame frame) |
| def | **[usage](/documentation/code/namespaces/namespacecombine__hdf5/#function-usage)**() |

## Attributes

|                | Name           |
| -------------- | -------------- |
| int | **[chunksize](/documentation/code/namespaces/namespacecombine__hdf5/#variable-chunksize)**  |
| int | **[bufferlength](/documentation/code/namespaces/namespacecombine__hdf5/#variable-bufferlength)**  |
| int | **[max_ppidpairs](/documentation/code/namespaces/namespacecombine__hdf5/#variable-max-ppidpairs)**  |
| bool | **[runchecks](/documentation/code/namespaces/namespacecombine__hdf5/#variable-runchecks)**  |
| bool | **[delete_tmp](/documentation/code/namespaces/namespacecombine__hdf5/#variable-delete-tmp)**  |
| | **[outfname](/documentation/code/namespaces/namespacecombine__hdf5/#variable-outfname)**  |
| | **[group](/documentation/code/namespaces/namespacecombine__hdf5/#variable-group)**  |
| | **[tmp_files](/documentation/code/namespaces/namespacecombine__hdf5/#variable-tmp-files)**  |
| | **[N](/documentation/code/namespaces/namespacecombine__hdf5/#variable-n)**  |
| string | **[RA_group](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ra-group)**  |
| dictionary | **[files](/documentation/code/namespaces/namespacecombine__hdf5/#variable-files)**  |
| list | **[sync_dsets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-sync-dsets)**  |
| list | **[RA_dsets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ra-dsets)**  |
| | **[RA_dsets_exclude](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ra-dsets-exclude)**  |
| list | **[sync_lengths](/documentation/code/namespaces/namespacecombine__hdf5/#variable-sync-lengths)**  |
| list | **[RA_lengths](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ra-lengths)**  |
| | **[fnames](/documentation/code/namespaces/namespacecombine__hdf5/#variable-fnames)**  |
| | **[f](/documentation/code/namespaces/namespacecombine__hdf5/#variable-f)**  |
| list | **[datasets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-datasets)**  |
| dictionary | **[tmp_dset_metadata](/documentation/code/namespaces/namespacecombine__hdf5/#variable-tmp-dset-metadata)**  |
| dictionary | **[tmp_RA_dset_metadata](/documentation/code/namespaces/namespacecombine__hdf5/#variable-tmp-ra-dset-metadata)**  |
| | **[total_sync_length](/documentation/code/namespaces/namespacecombine__hdf5/#variable-total-sync-length)**  |
| | **[fout](/documentation/code/namespaces/namespacecombine__hdf5/#variable-fout)**  |
| | **[gout](/documentation/code/namespaces/namespacecombine__hdf5/#variable-gout)**  |
| dictionary | **[existing_dsets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-existing-dsets)**  |
| dictionary | **[dsetlengths](/documentation/code/namespaces/namespacecombine__hdf5/#variable-dsetlengths)**  |
| | **[init_output_length](/documentation/code/namespaces/namespacecombine__hdf5/#variable-init-output-length)**  |
| dictionary | **[target_dsets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-target-dsets)**  |
| | **[all_sync_dsets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-all-sync-dsets)**  |
| | **[all_RA_dsets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-all-ra-dsets)**  |
| | **[chunks](/documentation/code/namespaces/namespacecombine__hdf5/#variable-chunks)**  |
| | **[dtype](/documentation/code/namespaces/namespacecombine__hdf5/#variable-dtype)**  |
| | **[dt](/documentation/code/namespaces/namespacecombine__hdf5/#variable-dt)**  |
| | **[maxshape](/documentation/code/namespaces/namespacecombine__hdf5/#variable-maxshape)**  |
| | **[nextempty](/documentation/code/namespaces/namespacecombine__hdf5/#variable-nextempty)**  |
| dictionary | **[fin](/documentation/code/namespaces/namespacecombine__hdf5/#variable-fin)**  |
| | **[dset_length](/documentation/code/namespaces/namespacecombine__hdf5/#variable-dset-length)**  |
| dictionary | **[item](/documentation/code/namespaces/namespacecombine__hdf5/#variable-item)**  |
| | **[nchunks](/documentation/code/namespaces/namespacecombine__hdf5/#variable-nchunks)**  |
| int | **[imin](/documentation/code/namespaces/namespacecombine__hdf5/#variable-imin)**  |
| | **[imax](/documentation/code/namespaces/namespacecombine__hdf5/#variable-imax)**  |
| dictionary | **[pointIDs_in](/documentation/code/namespaces/namespacecombine__hdf5/#variable-pointids-in)**  |
| dictionary | **[mpiranks_in](/documentation/code/namespaces/namespacecombine__hdf5/#variable-mpiranks-in)**  |
| | **[pointIDs_isvalid_in](/documentation/code/namespaces/namespacecombine__hdf5/#variable-pointids-isvalid-in)**  |
| | **[mpiranks_isvalid_in](/documentation/code/namespaces/namespacecombine__hdf5/#variable-mpiranks-isvalid-in)**  |
| tuple | **[mask_in](/documentation/code/namespaces/namespacecombine__hdf5/#variable-mask-in)**  |
| | **[IDs_in](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ids-in)**  |
| | **[pointIDs_out](/documentation/code/namespaces/namespacecombine__hdf5/#variable-pointids-out)**  |
| | **[mpiranks_out](/documentation/code/namespaces/namespacecombine__hdf5/#variable-mpiranks-out)**  |
| | **[pointIDs_isvalid_out](/documentation/code/namespaces/namespacecombine__hdf5/#variable-pointids-isvalid-out)**  |
| | **[mpiranks_isvalid_out](/documentation/code/namespaces/namespacecombine__hdf5/#variable-mpiranks-isvalid-out)**  |
| tuple | **[mask_out](/documentation/code/namespaces/namespacecombine__hdf5/#variable-mask-out)**  |
| | **[IDs_out](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ids-out)**  |
| | **[ids](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ids)**  |
| | **[pid](/documentation/code/namespaces/namespacecombine__hdf5/#variable-pid)**  |
| | **[rank](/documentation/code/namespaces/namespacecombine__hdf5/#variable-rank)**  |
| | **[Nmatches](/documentation/code/namespaces/namespacecombine__hdf5/#variable-nmatches)**  |
| | **[Match](/documentation/code/namespaces/namespacecombine__hdf5/#variable-match)**  |
| | **[target_mask_small](/documentation/code/namespaces/namespacecombine__hdf5/#variable-target-mask-small)**  |
| | **[target_length](/documentation/code/namespaces/namespacecombine__hdf5/#variable-target-length)**  |
| | **[alltargetindices](/documentation/code/namespaces/namespacecombine__hdf5/#variable-alltargetindices)**  |
| | **[maskindices](/documentation/code/namespaces/namespacecombine__hdf5/#variable-maskindices)**  |
| | **[target_mask](/documentation/code/namespaces/namespacecombine__hdf5/#variable-target-mask)**  |
| | **[indexid](/documentation/code/namespaces/namespacecombine__hdf5/#variable-indexid)**  |
| | **[index](/documentation/code/namespaces/namespacecombine__hdf5/#variable-index)**  |
| | **[ntargets](/documentation/code/namespaces/namespacecombine__hdf5/#variable-ntargets)**  |
| | **[nsources](/documentation/code/namespaces/namespacecombine__hdf5/#variable-nsources)**  |
| | **[xsort](/documentation/code/namespaces/namespacecombine__hdf5/#variable-xsort)** <br>Just some test code which I decided to keep around since it is helpful for understand how the rearrangment of the input data to match the output selection works.  |
| | **[yindex](/documentation/code/namespaces/namespacecombine__hdf5/#variable-yindex)**  |
| | **[fancyindices](/documentation/code/namespaces/namespacecombine__hdf5/#variable-fancyindices)**  |
| dictionary | **[indset](/documentation/code/namespaces/namespacecombine__hdf5/#variable-indset)**  |
| | **[outdset](/documentation/code/namespaces/namespacecombine__hdf5/#variable-outdset)**  |

## Detailed Description




```
Combine data from several hdf5 files created by HDF5Printer into a single file```


## Functions Documentation

### function sigint_handler

```
def sigint_handler(
    signum signum,
    frame frame
)
```


### function usage

```
def usage()
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


### variable runchecks

```
bool runchecks = False;
```


### variable delete_tmp

```
bool delete_tmp = False;
```


### variable outfname

```
outfname =  sys.argv[1];
```


### variable group

```
group =  sys.argv[2];
```


### variable tmp_files

```
tmp_files =  sys.argv[3:];
```


### variable N

```
N =  len(tmp_files);
```


### variable RA_group

```
string RA_group =  group + "/RA";
```


### variable files

```
dictionary files =  {};
```


### variable sync_dsets

```
list sync_dsets =  [set([]) for i in range(N)];
```


### variable RA_dsets

```
list RA_dsets =  [set([]) for i in range(N)];
```


### variable RA_dsets_exclude

```
RA_dsets_exclude =  set(["RA_pointID","RA_pointID_isvalid","RA_MPIrank","RA_MPIrank_isvalid"]);
```


### variable sync_lengths

```
list sync_lengths =  [0 for i in range(N)];
```


### variable RA_lengths

```
list RA_lengths =  [0 for i in range(N)];
```


### variable fnames

```
fnames =  tmp_files;
```


### variable f

```
f =  h5py.File(fname,'r');
```


### variable datasets

```
list datasets =  [];
```


### variable tmp_dset_metadata

```
dictionary tmp_dset_metadata =  {};
```


### variable tmp_RA_dset_metadata

```
dictionary tmp_RA_dset_metadata =  {};
```


### variable total_sync_length

```
total_sync_length =  sum(sync_lengths);
```


### variable fout

```
fout =  h5py.File(outfname,'a');
```


### variable gout

```
gout =  fout.create_group(group);
```


### variable existing_dsets

```
dictionary existing_dsets =  {};
```


### variable dsetlengths

```
dictionary dsetlengths =  {};
```


### variable init_output_length

```
init_output_length =  check_lengths(dsetlengths);
```


### variable target_dsets

```
dictionary target_dsets =  {};
```


### variable all_sync_dsets

```
all_sync_dsets =  set([]).union(*sync_dsets);
```


### variable all_RA_dsets

```
all_RA_dsets =  set([]).union(*RA_dsets);
```


### variable chunks

```
chunks;
```


### variable dtype

```
dtype;
```


### variable dt

```
dt;
```


### variable maxshape

```
maxshape;
```


### variable nextempty

```
nextempty = init_output_length;
```


### variable fin

```
dictionary fin =  files[fname];
```


### variable dset_length

```
dset_length = None;
```


### variable item

```
dictionary item =  fin[group][itemname];
```


### variable nchunks

```
nchunks =  np.ceil(dset_length / (1.*max_ppidpairs));
```


### variable imin

```
int imin =  i*max_ppidpairs;
```


### variable imax

```
imax =  np.min([(i+1)*max_ppidpairs, dset_length]);
```


### variable pointIDs_in

```
dictionary pointIDs_in =  fin[RA_group]["RA_pointID"][imin:imax];
```


### variable mpiranks_in

```
dictionary mpiranks_in =  fin[RA_group]["RA_MPIrank"][imin:imax];
```


### variable pointIDs_isvalid_in

```
pointIDs_isvalid_in =  np.array(fin[RA_group]["RA_pointID_isvalid"][imin:imax],dtype=np.bool);
```


### variable mpiranks_isvalid_in

```
mpiranks_isvalid_in =  np.array(fin[RA_group]["RA_MPIrank_isvalid"][imin:imax],dtype=np.bool);
```


### variable mask_in

```
tuple mask_in =  (pointIDs_isvalid_in & mpiranks_isvalid_in);
```


### variable IDs_in

```
IDs_in =  cantor_pairing(pointIDs_in[mask_in],mpiranks_in[mask_in]);
```


### variable pointIDs_out

```
pointIDs_out =  fout[group]["pointID"];
```


### variable mpiranks_out

```
mpiranks_out =  fout[group]["MPIrank"];
```


### variable pointIDs_isvalid_out

```
pointIDs_isvalid_out =  np.array(fout[group]["pointID_isvalid"][:],dtype=np.bool);
```


### variable mpiranks_isvalid_out

```
mpiranks_isvalid_out =  np.array(fout[group]["MPIrank_isvalid"][:],dtype=np.bool);
```


### variable mask_out

```
tuple mask_out =  (pointIDs_isvalid_out & mpiranks_isvalid_out);
```


### variable IDs_out

```
IDs_out =  cantor_pairing(
                     np.array(pointIDs_out[mask_out],dtype=np.longlong),
                     np.array(mpiranks_out[mask_out],dtype=np.longlong)
                     );
```


### variable ids

```
ids =  IDs_out;
```


### variable pid

```
pid =  pointIDs_out[mask_out];
```


### variable rank

```
rank =  mpiranks_out[mask_out];
```


### variable Nmatches

```
Nmatches =  np.sum(ID==ids);
```


### variable Match

```
Match =  np.sum((p==pid) & (r==rank));
```


### variable target_mask_small

```
target_mask_small =  np.in1d(IDs_out,IDs_in);
```


### variable target_length

```
target_length =  fout[group]["pointID"].shape[0];
```


### variable alltargetindices

```
alltargetindices =  np.arange(target_length);
```


### variable maskindices

```
maskindices =  alltargetindices[mask_out][target_mask_small];
```


### variable target_mask

```
target_mask =  np.zeros(target_length, dtype=bool);
```


### variable indexid

```
indexid =  np.where( (np.array(IDs_out)==ID) );
```


### variable index

```
index =  np.where( (np.array(pointIDs_out[mask_out])==pid) &
                                      (np.array(mpiranks_out[mask_out])==rank) );
```


### variable ntargets

```
ntargets =  np.sum(target_mask);
```


### variable nsources

```
nsources =  np.sum(mask_in);
```


### variable xsort

```
xsort =  np.argsort(IDs_in);
```

Just some test code which I decided to keep around since it is helpful for understand how the rearrangment of the input data to match the output selection works. 



```cpp
# Compute sorting index array for rearranging the source entries to match the target locations
# The way this works is a bit trippy, but it is fast.
#y = target (IDs_out)
#x = sources (IDs_in)
#result = array of length(y), containing positions of
#e.g.
#x = np.array([3,5,7,1 ,9  ,8,6,6])
#y = np.array([2,1,5,10,100,6])
# out = [ - 3 1 - - 6 ]
# i.e. "1" in y, is in position index 3 of x.
x1 = np.array([0,1,2,3,4,5,6,7,8])
y1 = np.array([4,3,5,0,1,2,6,8,7])
# where in x is each element of y?
# should give back y, since e.g. 4 is at index 4 in x
# then using ypos as indices on x[sort1], should again return y.
xsort1 = np.argsort(x1)
ypos1 = np.searchsorted(x1[xsort1], y1)
print "verifying..."
print y1
print ypos1
print xsort1[ypos1]
# less trivial test:
x2 = np.array([0,1,7,2,7,8,6,4])
y2 = np.array([4,0,1,2,6,8,7])
# indices array should be:
#            [8,1,2,3,7,5,2]
# (but in our case we don't want duplicates in either the target or input arrays!)
xsort2 = np.argsort(x2)
ypos2 = np.searchsorted(x2[xsort2], y2)
indices = xsort2[ypos2]
print "verifying..."
print x2
print xsort2
print x2[xsort2]
print "y2"
print y2
print ypos2
print indices
print x2[indices]
```


### variable yindex

```
yindex =  np.searchsorted(IDs_in[xsort], IDs_out[target_mask_small]);
```


### variable fancyindices

```
fancyindices =  xsort[yindex];
```


### variable indset

```
dictionary indset =  item[imin:imax];
```


### variable outdset

```
outdset =  fout[group][itemname];
```





-------------------------------

Updated on 2022-09-07 at 23:22:07 +0000