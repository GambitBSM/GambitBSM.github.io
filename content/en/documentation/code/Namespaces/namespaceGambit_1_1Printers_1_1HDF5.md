---
title: "namespace Gambit::Printers::HDF5"

description: "[No description available]"

---

# namespace Gambit::Printers::HDF5

[No description available]

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Printers::HDF5::copy_hdf5](/documentation/code/classes/structgambit_1_1printers_1_1hdf5_1_1copy__hdf5/)**  |
| class | **[Gambit::Printers::HDF5::hdf5_stuff](/documentation/code/classes/classgambit_1_1printers_1_1hdf5_1_1hdf5__stuff/)**  |
| struct | **[Gambit::Printers::HDF5::ra_copy_hdf5](/documentation/code/classes/structgambit_1_1printers_1_1hdf5_1_1ra__copy__hdf5/)**  |
| struct | **[Gambit::Printers::HDF5::read_hdf5](/documentation/code/classes/structgambit_1_1printers_1_1hdf5_1_1read__hdf5/)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| hid_t | **[openFile](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-openfile)**(const std::string & fname, bool overwrite, bool & oldfile, const char access_type ='r')<br>File and group manipulation.  |
| hid_t | **[openFile](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-openfile)**(const std::string & fname, bool overwrite =false, const char access_type ='r')<br>Create or open hdf5 file (ignoring feedback regarding whether file already existed)  |
| hid_t | **[closeFile](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-closefile)**(hid_t file)<br>Close hdf5 file.  |
| bool | **[checkFileReadable](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-checkfilereadable)**(const std::string & fname, std::string & msg)<br>Check if hdf5 file exists and can be opened in read/write mode.  |
| bool | **[checkFileReadable](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-checkfilereadable)**(const std::string & fname)<br>Thin wrapper for the above to discard failure message.  |
| bool | **[checkGroupReadable](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-checkgroupreadable)**(hid_t location, const std::string & groupname, std::string & msg)<br>Check if a group exists and can be accessed.  |
| bool | **[checkGroupReadable](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-checkgroupreadable)**(hid_t location, const std::string & groupname)<br>Thin wrapper for the above to discard failure message.  |
| std::pair< bool, std::size_t > | **[checkDatasetReadable](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-checkdatasetreadable)**(hid_t location, const std::string & dsetname) |
| hid_t | **[createFile](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-createfile)**(const std::string & fname)<br>Create hdf5 file (always overwrite existing files)  |
| hid_t | **[createGroup](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-creategroup)**(hid_t location, const std::string & name)<br>Create a group inside the specified location.  |
| void | **[errorsOff](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-errorsoff)**()<br>Silence error report (e.g. while probing for file existence)  |
| void | **[errorsOn](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-errorson)**()<br>Restore error report.  |
| hid_t | **[openGroup](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-opengroup)**(hid_t file_id, const std::string & name, bool nocreate =false, bool fatal =true) |
| hid_t | **[closeGroup](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-closegroup)**(hid_t group)<br>Close group.  |
| std::vector< std::string > | **[lsGroup](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-lsgroup)**(hid_t group_id)<br>List object names in a group.  |
| hid_t | **[getH5DatasetType](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-geth5datasettype)**(hid_t group_id, const std::string & dset_name)<br>Get type of an object in a group.  |
| hid_t | **[closeType](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-closetype)**(hid_t type_id)<br>Release datatype identifier.  |
| hid_t | **[openDataset](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-opendataset)**(hid_t dset_id, const std::string & name, bool error_off =false)<br>Dataset and dataspace manipulation.  |
| hid_t | **[closeDataset](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-closedataset)**(hid_t dset_id)<br>Close dataset.  |
| hid_t | **[getSpace](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getspace)**(hid_t dset_id)<br>Get dataspace.  |
| hid_t | **[closeSpace](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-closespace)**(hid_t space_id)<br>Close dataspace.  |
| hssize_t | **[getSimpleExtentNpoints](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getsimpleextentnpoints)**(hid_t dset_id)<br>Get simple dataspace extent.  |
| std::string | **[getName](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getname)**(hid_t dset_id)<br>Get name of dataset.  |
| std::pair< hid_t, hid_t > | **[selectChunk](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-selectchunk)**(const hid_t dset_id, std::size_t offset, std::size_t length)<br>Select a simple hyperslab in a 1D dataset.  |
| bool | **[isDataSet](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-isdataset)**(hid_t group_id, const std::string & name)<br>Check if an object in a group is a dataset.  |
| template <class T \> <br>std::vector< T > | **[getChunk](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getchunk)**(const hid_t dset_id, std::size_t offset, std::size_t length) |
| std::vector< bool > | **[getChunk](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getchunk)**(const hid_t dset_id, std::size_t offset, std::size_t length) |
| int | **[inttype_from_h5type](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-inttype-from-h5type)**(hid_t h5type) |
| bool | **[is_float_type](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-is-float-type)**(int inttype) |
| template <typename T \> <br>T | **[type_ret](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-type-ret)**() |
| template <class U ,typename... T\> <br>void | **[Enter_HDF5](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-enter-hdf5)**(hid_t dataset, T &... params) |
| void | **[combine_hdf5_files](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-combine-hdf5-files)**(const std::string output_file, const std::string & base_file_name, const std::string & group, const std::string & metadata_group, const size_t num, const bool resume, const bool cleanup, const bool skip, const std::vector< std::string > input_files =std::vector< std::string >()) |
| std::unordered_map< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), unsigned long long, [PPIDHash](/documentation/code/classes/structgambit_1_1printers_1_1ppidhash/), [PPIDEqual](/documentation/code/classes/structgambit_1_1printers_1_1ppidequal/) > | **[get_RA_write_hash](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-get-ra-write-hash)**(hid_t group_id, std::unordered_set< [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/), [PPIDHash](/documentation/code/classes/structgambit_1_1printers_1_1ppidhash/), [PPIDEqual](/documentation/code/classes/structgambit_1_1printers_1_1ppidequal/) > & left_to_match) |
| std::pair< std::vector< std::string >, std::vector< size_t > > | **[find_temporary_files](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-find-temporary-files)**(const std::string & finalfile)<br>Search for temporary files to be combined.  |
| std::pair< std::vector< std::string >, std::vector< size_t > > | **[find_temporary_files](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-find-temporary-files)**(const std::string & finalfile, size_t & max_i)<br>Search for temporary files to be combined.  |
| hsize_t | **[getGroupNum](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getgroupnum)**(hid_t group_id) |
| hid_t | **[getType](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-gettype)**(hid_t dataset) |
| std::vector< std::string > | **[get_dset_names](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-get-dset-names)**(hid_t group_id) |
| herr_t | **[op_func](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-op-func)**(hid_t loc_id, const char * name_in, const H5L_info_t * , void * operator_data) |
| herr_t | **[op_func_aux](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-op-func-aux)**(hid_t loc_id, const char * name_in, const H5L_info_t * , void * operator_data) |
| void | **[setup_hdf5_points](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-setup-hdf5-points)**(hid_t new_group, hid_t type, unsigned long long size_tot, const std::string & name) |
| void | **[setup_hdf5_points](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-setup-hdf5-points)**(hid_t new_group, hid_t type, hid_t type2, unsigned long long size_tot, const std::string & name) |
| std::vector< std::string > | **[getGroups](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getgroups)**(std::string groups) |
| hid_t | **[create_GAMBIT_fapl](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-create-gambit-fapl)**()<br>GAMBIT default file access property list.  |
| const hid_t | **[H5P_GAMBIT](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-h5p-gambit)**(create_GAMBIT_fapl() )<br>Const global for the GAMBIT fapl.  |
| std::vector< bool > | **[getChunk](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-getchunk)**(const hid_t dset_id, std::size_t offset, std::size_t length) |
| template <class T \> <br>std::pair< bool, std::size_t > | **[_checkDatasetReadable_helper](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-checkdatasetreadable-helper)**(hid_t dset_id, const std::string dset_name) |
| herr_t | **[group_ls](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#function-group-ls)**(hid_t g_id, const char * name, const H5L_info_t * , void * op_data) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| H5E_auto2_t | **[old_func](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#variable-old-func)** <br>Close hdf5 type ID.  |
| void * | **[old_client_data](/documentation/code/namespaces/namespacegambit_1_1printers_1_1hdf5/#variable-old-client-data)**  |


## Functions Documentation

### function openFile

```
hid_t openFile(
    const std::string & fname,
    bool overwrite,
    bool & oldfile,
    const char access_type ='r'
)
```

File and group manipulation. 

Create or open hdf5 file

Create or open hdf5 file third argument "oldfile" is used to report whether an existing file was opened (true if yes) 


### function openFile

```
hid_t openFile(
    const std::string & fname,
    bool overwrite =false,
    const char access_type ='r'
)
```

Create or open hdf5 file (ignoring feedback regarding whether file already existed) 

### function closeFile

```
hid_t closeFile(
    hid_t file
)
```

Close hdf5 file. 

### function checkFileReadable

```
bool checkFileReadable(
    const std::string & fname,
    std::string & msg
)
```

Check if hdf5 file exists and can be opened in read/write mode. 

Check if hdf5 file exists and can be opened in read mode. 


### function checkFileReadable

```
inline bool checkFileReadable(
    const std::string & fname
)
```

Thin wrapper for the above to discard failure message. 

### function checkGroupReadable

```
bool checkGroupReadable(
    hid_t location,
    const std::string & groupname,
    std::string & msg
)
```

Check if a group exists and can be accessed. 

### function checkGroupReadable

```
inline bool checkGroupReadable(
    hid_t location,
    const std::string & groupname
)
```

Thin wrapper for the above to discard failure message. 

### function checkDatasetReadable

```
std::pair< bool, std::size_t > checkDatasetReadable(
    hid_t location,
    const std::string & dsetname
)
```


Check if a dataset exists and can be read from fully (Reads through entire dataset to make sure! May take some time) 


### function createFile

```
hid_t createFile(
    const std::string & fname
)
```

Create hdf5 file (always overwrite existing files) 

### function createGroup

```
hid_t createGroup(
    hid_t location,
    const std::string & name
)
```

Create a group inside the specified location. 

### function errorsOff

```
void errorsOff()
```

Silence error report (e.g. while probing for file existence) 

Silence error report (e.g. while probing for file existence) Just silences default error stack, since we aren't using anything else TESTING! I changed from using H5Eget_auto to H5Eget_auto2 If that still causes errors, try switching to H5Eget_auto1 and let me know if it works :) 


### function errorsOn

```
void errorsOn()
```

Restore error report. 

### function openGroup

```
hid_t openGroup(
    hid_t file_id,
    const std::string & name,
    bool nocreate =false,
    bool fatal =true
)
```


### function closeGroup

```
hid_t closeGroup(
    hid_t group
)
```

Close group. 

### function lsGroup

```
std::vector< std::string > lsGroup(
    hid_t group_id
)
```

List object names in a group. 

### function getH5DatasetType

```
hid_t getH5DatasetType(
    hid_t group_id,
    const std::string & dset_name
)
```

Get type of an object in a group. 

Get type of a dataset in a group NOTE: Make sure to call closeType when the ID is no longer needed! 


### function closeType

```
hid_t closeType(
    hid_t type_id
)
```

Release datatype identifier. 

### function openDataset

```
hid_t openDataset(
    hid_t dset_id,
    const std::string & name,
    bool error_off =false
)
```

Dataset and dataspace manipulation. 

Dataset manipulations.

Open dataset 


### function closeDataset

```
hid_t closeDataset(
    hid_t dset_id
)
```

Close dataset. 

### function getSpace

```
hid_t getSpace(
    hid_t dset_id
)
```

Get dataspace. 

### function closeSpace

```
hid_t closeSpace(
    hid_t space_id
)
```

Close dataspace. 

### function getSimpleExtentNpoints

```
hssize_t getSimpleExtentNpoints(
    hid_t dset_id
)
```

Get simple dataspace extent. 

### function getName

```
std::string getName(
    hid_t dset_id
)
```

Get name of dataset. 

Close dataset.

Open/close dataspace; input dataset, output dataspace Get simple dataspace extent (number of points); input dataspace, output data extent (size) Get dataset name 


### function selectChunk

```
std::pair< hid_t, hid_t > selectChunk(
    const hid_t dset_id,
    std::size_t offset,
    std::size_t length
)
```

Select a simple hyperslab in a 1D dataset. 

### function isDataSet

```
bool isDataSet(
    hid_t group_id,
    const std::string & name
)
```

Check if an object in a group is a dataset. 

Check if an object in a file or group is a dataset. 


### function getChunk

```
template <class T >
std::vector< T > getChunk(
    const hid_t dset_id,
    std::size_t offset,
    std::size_t length
)
```


Retrieve a chunk of data from a simple dataset NOTE! Doesn't work for T=bool! Have a custom specialisation in the source file for that. 


### function getChunk

```
std::vector< bool > getChunk(
    const hid_t dset_id,
    std::size_t offset,
    std::size_t length
)
```


### function inttype_from_h5type

```
int inttype_from_h5type(
    hid_t h5type
)
```


### function is_float_type

```
bool is_float_type(
    int inttype
)
```


### function type_ret

```
template <typename T >
inline T type_ret()
```


### function Enter_HDF5

```
template <class U ,
typename... T>
inline void Enter_HDF5(
    hid_t dataset,
    T &... params
)
```


### function combine_hdf5_files

```
inline void combine_hdf5_files(
    const std::string output_file,
    const std::string & base_file_name,
    const std::string & group,
    const std::string & metadata_group,
    const size_t num,
    const bool resume,
    const bool cleanup,
    const bool skip,
    const std::vector< std::string > input_files =std::vector< std::string >()
)
```


### function get_RA_write_hash

```
std::unordered_map< PPIDpair, unsigned long long, PPIDHash, PPIDEqual > get_RA_write_hash(
    hid_t group_id,
    std::unordered_set< PPIDpair, PPIDHash, PPIDEqual > & left_to_match
)
```


Helper function to create output hash map for RA points note: left_to_match points will be erased as we go, and are passed by reference, so will be erased in calling context also. 


### function find_temporary_files

```
std::pair< std::vector< std::string >, std::vector< size_t > > find_temporary_files(
    const std::string & finalfile
)
```

Search for temporary files to be combined. 

### function find_temporary_files

```
std::pair< std::vector< std::string >, std::vector< size_t > > find_temporary_files(
    const std::string & finalfile,
    size_t & max_i
)
```

Search for temporary files to be combined. 

### function getGroupNum

```
inline hsize_t getGroupNum(
    hid_t group_id
)
```


### function getType

```
inline hid_t getType(
    hid_t dataset
)
```


### function get_dset_names

```
std::vector< std::string > get_dset_names(
    hid_t group_id
)
```


### function op_func

```
inline herr_t op_func(
    hid_t loc_id,
    const char * name_in,
    const H5L_info_t * ,
    void * operator_data
)
```


### function op_func_aux

```
inline herr_t op_func_aux(
    hid_t loc_id,
    const char * name_in,
    const H5L_info_t * ,
    void * operator_data
)
```


### function setup_hdf5_points

```
inline void setup_hdf5_points(
    hid_t new_group,
    hid_t type,
    unsigned long long size_tot,
    const std::string & name
)
```


### function setup_hdf5_points

```
inline void setup_hdf5_points(
    hid_t new_group,
    hid_t type,
    hid_t type2,
    unsigned long long size_tot,
    const std::string & name
)
```


### function getGroups

```
inline std::vector< std::string > getGroups(
    std::string groups
)
```


### function create_GAMBIT_fapl

```
hid_t create_GAMBIT_fapl()
```

GAMBIT default file access property list. 

### function H5P_GAMBIT

```
const hid_t H5P_GAMBIT(
    create_GAMBIT_fapl() 
)
```

Const global for the GAMBIT fapl. 

### function getChunk

```
std::vector< bool > getChunk(
    const hid_t dset_id,
    std::size_t offset,
    std::size_t length
)
```


### function _checkDatasetReadable_helper

```
template <class T >
std::pair< bool, std::size_t > _checkDatasetReadable_helper(
    hid_t dset_id,
    const std::string dset_name
)
```


### function group_ls

```
herr_t group_ls(
    hid_t g_id,
    const char * name,
    const H5L_info_t * ,
    void * op_data
)
```



## Attributes Documentation

### variable old_func

```
H5E_auto2_t old_func;
```

Close hdf5 type ID. 

Close hdf5 group global error variables (handler) 


### variable old_client_data

```
void * old_client_data;
```





-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000