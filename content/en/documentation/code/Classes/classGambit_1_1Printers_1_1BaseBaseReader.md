---
title: "class Gambit::Printers::BaseBaseReader"

description: "[No description available]"

---

# class Gambit::Printers::BaseBaseReader



[No description available] [More...](#detailed-description)


`#include <basebaseprinter.hpp>`

Inherited by [Gambit::Printers::BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-basebasereader)**() |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-reset)**() =0 |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-dataset-length)**() =0 |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-current-point)**() =0 |
| virtual ulong | **[get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-current-index)**() =0 |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-next-point)**() =0 |
| virtual bool | **[eoi](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-eoi)**() =0 |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve)**(T & out, const std::string & label, const uint rank, const ulong pointID) |
| template <typename T \> <br>bool | **[retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve)**(T & out, const std::string & label)<br>Overload for 'retrieve' that uses the current point as the input for rank/pointID.  |
| bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer, const uint rank, const ulong pointID)<br>Retrieve and directly print data to new output.  |
| virtual bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & in_label, const std::string & out_label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer, const uint rank, const ulong pointID) =0 |
| bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer)<br>Overload for 'retrieve_and_print' that uses the current point as the input for rank/pointID.  |
| bool | **[retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve-and-print)**(const std::string & in_label, const std::string & out_label, [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer)<br>As above, but allows for different input/output labels.  |
| virtual std::size_t | **[get_type](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-type)**(const std::string & label) =0 |
| virtual std::set< std::string > | **[get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-all-labels)**() =0 |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| template <typename T \> <br>bool | **[_retrieve](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-retrieve)**(T & , const std::string & label, const uint, const ulong) |

## Detailed Description

```
class Gambit::Printers::BaseBaseReader;
```


Printer READ interface For reading data back _into_[Gambit](/documentation/code/namespaces/namespacegambit/) from a printer output file. This is mainly designed for performing "reweighting" of scans, e.g. loading up previously scanned points in order to recompute some new observables or likelihoods.

It is pretty hard to permit generic read-in of ALL data, so for now I will focus on just getting the parameter data. If we read in other data we will have to do some gnarly stuff like automatically wrap it into functors, and to appropriate capabilities etc, in order for it to be usable in other in other calculations. So for now, the idea will simply be to take the parameter values and recompute everything anew that is needed for calculating the new likelihoods or whatever. Otherwise it is kind of a nightmare to e.g. reconstruct a [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) object from printer data, would need special module functions and so on that know how to put all the data back together. I guess it is possible if we give module writers access to the printer read interface so that they can do this task themselves... but will leave this aside for now. So, need:

1. some way to iterate through printer output
2. a generic function that can read in a particular entry, knowing e.g. the following: 

```cpp
Column 6: #NormalDist_parameters @NormalDist::primary_parameters::mu
```

 and can put it back into some [Gambit](/documentation/code/namespaces/namespacegambit/) object, e.g. Parameters: NormalDist: mu: sigma:
I guess this latter part is scannerbits responsibility, i.e. it will have the parameter object and need to fill it with numbers that it gets from the printer. 

```
     functor (model) name    parameter name
```

 str key = act_it->first + "::" + *par_it; 

## Public Functions Documentation

### function ~BaseBaseReader

```
inline virtual ~BaseBaseReader()
```


### function reset

```
virtual void reset() =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::reset](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-reset), [Gambit::Printers::HDF5Reader::reset](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-reset), [Gambit::Printers::SQLiteReader::reset](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-reset)


### function get_dataset_length

```
virtual ulong get_dataset_length() =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-dataset-length), [Gambit::Printers::HDF5Reader::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-dataset-length), [Gambit::Printers::SQLiteReader::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-get-dataset-length)


### function get_current_point

```
virtual PPIDpair get_current_point() =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-current-point), [Gambit::Printers::HDF5Reader::get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-current-point), [Gambit::Printers::SQLiteReader::get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-get-current-point)


### function get_current_index

```
virtual ulong get_current_index() =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-current-index), [Gambit::Printers::HDF5Reader::get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-current-index), [Gambit::Printers::SQLiteReader::get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-get-current-index)


### function get_next_point

```
virtual PPIDpair get_next_point() =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-next-point), [Gambit::Printers::HDF5Reader::get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-next-point), [Gambit::Printers::SQLiteReader::get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-get-next-point)


### function eoi

```
virtual bool eoi() =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::eoi](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-eoi), [Gambit::Printers::HDF5Reader::eoi](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-eoi), [Gambit::Printers::SQLiteReader::eoi](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-eoi)


### function retrieve

```
template <typename T >
inline bool retrieve(
    T & out,
    const std::string & label,
    const uint rank,
    const ulong pointID
)
```


Printer-retrieve dispatch function. If a virtual function override exists for the retrieve type, info is passed on, otherwise the function call is resolved to a default function which raises an informative runtime error explaining that the type is not retrievable.

Note; this is not quite enough because the entries in the printer output need not be one-to-one with the printed object, e.g. vectors currently go into a series of indexed output slots. Hard for e.g. scanner plugins to know the label that they need to ask for...

Perhaps return a map of results matching the label? Or vector? Perhaps both in different cases...

Note, cannot overload based on return type, so need to use an "out" parameter In addition, there may not be a valid result printed for a given entry, so an extra output flag "out_valid" must be set to indicate whether the entry was marked invalid in the old output. Use the return value for this. 


### function retrieve

```
template <typename T >
inline bool retrieve(
    T & out,
    const std::string & label
)
```

Overload for 'retrieve' that uses the current point as the input for rank/pointID. 

### function retrieve_and_print

```
inline bool retrieve_and_print(
    const std::string & label,
    BaseBasePrinter & printer,
    const uint rank,
    const ulong pointID
)
```

Retrieve and directly print data to new output. 

Just use the same label for input and output


### function retrieve_and_print

```
virtual bool retrieve_and_print(
    const std::string & in_label,
    const std::string & out_label,
    BaseBasePrinter & printer,
    const uint rank,
    const ulong pointID
) =0
```


**Reimplemented by**: [Gambit::Printers::BaseReader::retrieve_and_print](/documentation/code/classes/classgambit_1_1printers_1_1basereader/#function-retrieve-and-print)


Retrieve and directly print data to new output, renaming the output to something new Implemented in [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) where complete type info is available. 


### function retrieve_and_print

```
inline bool retrieve_and_print(
    const std::string & label,
    BaseBasePrinter & printer
)
```

Overload for 'retrieve_and_print' that uses the current point as the input for rank/pointID. 

Uses same label for input and output


### function retrieve_and_print

```
inline bool retrieve_and_print(
    const std::string & in_label,
    const std::string & out_label,
    BaseBasePrinter & printer
)
```

As above, but allows for different input/output labels. 

### function get_type

```
virtual std::size_t get_type(
    const std::string & label
) =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::get_type](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-type), [Gambit::Printers::HDF5Reader::get_type](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-type), [Gambit::Printers::SQLiteReader::get_type](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-get-type)


Get type information for a data entry, i.e. defines the C++ type which this should be retrieved as, not what it is necessarily literally stored as in the output. It isn't human readable, it is just for matching retrieved data to a print type, mainly for the 'retrieve_and_print' function. Needs to be implemented in each complete derived Reader class 


### function get_all_labels

```
virtual std::set< std::string > get_all_labels() =0
```


**Reimplemented by**: [Gambit::Printers::asciiReader::get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-all-labels), [Gambit::Printers::HDF5Reader::get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1hdf5reader/#function-get-all-labels), [Gambit::Printers::SQLiteReader::get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1sqlitereader/#function-get-all-labels)


Get list of output labels that can be retrieved by this printer. Needs to be implemented in each complete derived Reader class 


## Protected Functions Documentation

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


Default _retrieve function. Throws an error if no virtual function matching the type of the attempted retrieval is found. 


-------------------------------

Updated on 2023-06-26 at 21:36:52 +0000