---
title: "class Gambit::Printers::asciiReader"
description: "Derived EntryGetterInterface class for accessing [asciiPrinter](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/) output points. "

---

# class Gambit::Printers::asciiReader



Derived EntryGetterInterface class for accessing [asciiPrinter](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/) output points. 


`#include <asciireader.hpp>`

Inherits from [Gambit::Printers::BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/), [Gambit::Printers::BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[asciiReader](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-asciireader)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & options)<br>General members of '[asciiReader](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/)'.  |
| virtual void | **[reset](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-reset)**()<br>Base class virtual interface functions.  |
| virtual ulong | **[get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-dataset-length)**()<br>Get total length of dataset.  |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-next-point)**()<br>Get next rank/ptID pair.  |
| virtual [PPIDpair](/documentation/code/classes/structgambit_1_1printers_1_1ppidpair/) | **[get_current_point](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-current-point)**() |
| virtual ulong | **[get_current_index](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-current-index)**() |
| virtual bool | **[eoi](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-eoi)**() |
| virtual std::size_t | **[get_type](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-type)**(const std::string & ) |
| virtual std::set< std::string > | **[get_all_labels](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-get-all-labels)**()<br>Get all output column labels.  |
| template <typename T \> <br>bool | **[_retrieve](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/#function-retrieve)**(T & , const std::string & label, const uint, const ulong)<br>Retrieval functions.  |

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

### function asciiReader

```
asciiReader(
    const Options & options
)
```

General members of '[asciiReader](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/)'. 

Constructor 


Open output data file

Scan through file and figure out how many points are in the dataset


### function reset

```
virtual void reset()
```

Base class virtual interface functions. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::reset](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-reset)


Reset read head position to zero. 


Reset row count


### function get_dataset_length

```
virtual ulong get_dataset_length()
```

Get total length of dataset. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::get_dataset_length](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-dataset-length)


### function get_next_point

```
virtual PPIDpair get_next_point()
```

Get next rank/ptID pair. 

**Reimplements**: [Gambit::Printers::BaseBaseReader::get_next_point](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-next-point)


### function get_current_point

```
virtual PPIDpair get_current_point()
```


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


**Reimplements**: [Gambit::Printers::BaseBaseReader::eoi](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-eoi)


### function get_type

```
inline virtual std::size_t get_type(
    const std::string & 
)
```


**Reimplements**: [Gambit::Printers::BaseBaseReader::get_type](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/#function-get-type)


Get type information for a data entry, i.e. defines the C++ type which this should be retrieved as, not what it is necessarily literally stored as in the output. For ASCIIPrinter, everything is currently a double. 


### function get_all_labels

```
virtual std::set< std::string > get_all_labels()
```

Get all output column labels. 

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

Retrieval functions. 

-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000