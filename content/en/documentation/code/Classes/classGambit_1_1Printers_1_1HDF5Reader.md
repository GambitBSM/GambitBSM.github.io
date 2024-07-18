---
title: "class Gambit::Printers::HDF5Reader"

description: "[No description available]"

---

# class Gambit::Printers::HDF5Reader



[No description available]

Inherits from [Gambit::Printers::BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/), [Gambit::Printers::BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-reset)**()<br>Base class virtual interface functions.  |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-dataset-length)**()<br>Get length of input dataset.  |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-next-point)**()<br>Get next rank/ptID pair in data file.  |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-current-point)**()<br>Get current rank/ptID pair in data file.  |
| virtual ulong | **[get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-current-index)**() |
| virtual bool | **[eoi](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-eoi)**()<br>Check if 'current point' is past the end of the datasets (and thus invalid!)  |
| virtual std::size_t | **[get_type](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-type)**(const std::string & label) |
| virtual std::set< std::string > | **[get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-all-labels)**()<br>Get labels of all datasets in the linked group.  |
| template <typename T \> <br>bool | **[_retrieve](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-retrieve)**(T & , const std::string & label, const uint, const ulong)<br>Retrieve functions.  |
| | **[HDF5Reader](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-hdf5reader)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| | **[~HDF5Reader](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-hdf5reader)**() |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/#function-basereader)**() |
| virtual | **[~BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/#function-basereader)**()<br>Destructor.  |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basereader/#function-retrieve)**(T & out, const std::string & label)<br>Reimplement overload for 'retrieve' that uses the current point as the input for rank/pointID.  |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basereader/#function-retrieve)**(T & out, const std::string & label, const uint rank, const ulong pointID) |
| virtual bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basereader/#function-retrieve-and-print)**(const std::string & in_label, const std::string & out_label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer, const uint rank, const ulong pointID)<br>Retrieve and directly print data to new output.  |

**Public Functions inherited from [Gambit::Printers::BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-basebasereader)**() |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve)**(T & out, const std::string & label, const uint rank, const ulong pointID) |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve)**(T & out, const std::string & label)<br>Overload for 'retrieve' that uses the current point as the input for rank/pointID.  |
| bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer, const uint rank, const ulong pointID)<br>Retrieve and directly print data to new output.  |
| virtual bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & in_label, const std::string & out_label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer, const uint rank, const ulong pointID) =0 |
| bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer)<br>Overload for 'retrieve_and_print' that uses the current point as the input for rank/pointID.  |
| bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & in_label, const std::string & out_label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer)<br>As above, but allows for different input/output labels.  |


## Public Functions Documentation

### function reset

```
virtual void reset()
```

Base class virtual interface functions. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::reset](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-reset)


Reset 'read head' position to first entry 


### function get_dataset_length

```
virtual ulong get_dataset_length()
```

Get length of input dataset. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-dataset-length)


### function get_next_point

```
virtual PPIDpair get_next_point()
```

Get next rank/ptID pair in data file. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-next-point)


### function get_current_point

```
virtual PPIDpair get_current_point()
```

Get current rank/ptID pair in data file. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-current-point)


### function get_current_index

```
virtual ulong get_current_index()
```


**Reimplements**: [Gambit::Printers::BaseBaseReader::get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-current-index)


### function eoi

```
virtual bool eoi()
```

Check if 'current point' is past the end of the datasets (and thus invalid!) 

**Reimplements**: [Gambit::Printers::BaseBaseReader::eoi](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-eoi)


### function get_type

```
virtual std::size_t get_type(
    const std::string & label
)
```


**Reimplements**: [Gambit::Printers::BaseBaseReader::get_type](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-type)


Get type information for a data entry, i.e. defines the C++ type which this should be retrieved as, not what it is necessarily literally stored as in the output. 


Release HDF5 type ID number


### function get_all_labels

```
virtual std::set< std::string > get_all_labels()
```

Get labels of all datasets in the linked group. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-all-labels)


### function _retrieve

```
template <typename T >
inline bool _retrieve(
    T & ,
    const std::string & label,
    const uint,
    const ulong
)
```

Retrieve functions. 

### function HDF5Reader

```
HDF5Reader(
    const Options & options
)
```


### function ~HDF5Reader

```
~HDF5Reader()
```


-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000