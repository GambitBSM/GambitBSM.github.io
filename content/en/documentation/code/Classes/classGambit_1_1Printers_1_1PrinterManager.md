---
title: "class Gambit::Printers::PrinterManager"
description: "Manager class for creating printer objects "

---

# class Gambit::Printers::PrinterManager



Manager class for creating printer objects 


`#include <printermanager.hpp>`

Inherits from [Gambit::Printers::BasePrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const [Options](/documentation/code/classes/classgambit_1_1options/) & printerNode, bool resume_mode)<br>Constructor.  |
| | **[~PrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**()<br>Destructor.  |
| virtual void | **[new_stream](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & streamname, const [Options](/documentation/code/classes/classgambit_1_1options/) & new_options)<br>Create auxiliary printer object.  |
| virtual void | **[new_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & readstreamname, const [Options](/documentation/code/classes/classgambit_1_1options/) & options)<br>Create reader object.  |
| virtual void | **[create_resume_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**()<br>Create for reader object for previous print output ("resume reader")  |
| virtual [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) * | **[get_stream](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & streamname ="")<br>Getter for auxiliary printer objects.  |
| virtual [BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/) * | **[get_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & readername)<br>Getter for reader objects.  |
| [BaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basereader/) * | **[get_full_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & readername)<br>Retrieve non-basebase version of reader object (for use in module functions rather than ScannerBit)  |
| virtual bool | **[reader_exists](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & readername)<br>Checker for existence of reader object.  |
| virtual void | **[delete_stream](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & name ="")<br>Destruct printer/reader objects.  |
| virtual void | **[delete_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(const std::string & name) |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)**(bool abnormal =false)<br>Instruct printers that scan has finished and to perform cleanup.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [BasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1baseprinter/) * | **[printerptr](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)** <br>Pointer to main printer object.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Printers::BasePrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)**

|                | Name           |
| -------------- | -------------- |
| | **[BasePrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)**() |
| | **[BasePrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)**(bool r) |
| bool | **[resume_mode](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)**()<br>Getter for "resume" mode flag.  |
| void | **[set_resume_mode](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)**(bool rflag) |


## Public Functions Documentation

### function PrinterManager

```
PrinterManager(
    const Options & printerNode,
    bool resume_mode
)
```

Constructor. 

Manager class for creating printer objects. 


### function ~PrinterManager

```
~PrinterManager()
```

Destructor. 

### function new_stream

```
virtual void new_stream(
    const std::string & streamname,
    const Options & new_options
)
```

Create auxiliary printer object. 

**Reimplements**: [Gambit::Printers::BasePrinterManager::new_stream](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


### function new_reader

```
virtual void new_reader(
    const std::string & readstreamname,
    const Options & options
)
```

Create reader object. 

**Reimplements**: [Gambit::Printers::BasePrinterManager::new_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


### function create_resume_reader

```
virtual void create_resume_reader()
```

Create for reader object for previous print output ("resume reader") 

**Reimplements**: [Gambit::Printers::BasePrinterManager::create_resume_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


### function get_stream

```
virtual BaseBasePrinter * get_stream(
    const std::string & streamname =""
)
```

Getter for auxiliary printer objects. 

**Reimplements**: [Gambit::Printers::BasePrinterManager::get_stream](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


### function get_reader

```
virtual BaseBaseReader * get_reader(
    const std::string & readername
)
```

Getter for reader objects. 

**Reimplements**: [Gambit::Printers::BasePrinterManager::get_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


Retrieve pointer to named reader object. 


### function get_full_reader

```
BaseReader * get_full_reader(
    const std::string & readername
)
```

Retrieve non-basebase version of reader object (for use in module functions rather than ScannerBit) 

Retrieve non-base version of reader object (for use in module functions rather than ScannerBit) 


### function reader_exists

```
virtual bool reader_exists(
    const std::string & readername
)
```

Checker for existence of reader object. 

**Reimplements**: [Gambit::Printers::BasePrinterManager::reader_exists](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


### function delete_stream

```
virtual void delete_stream(
    const std::string & name =""
)
```

Destruct printer/reader objects. 

**Reimplements**: [Gambit::Printers::BasePrinterManager::delete_stream](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


### function delete_reader

```
virtual void delete_reader(
    const std::string & name
)
```


**Reimplements**: [Gambit::Printers::BasePrinterManager::delete_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


### function finalise

```
virtual void finalise(
    bool abnormal =false
)
```

Instruct printers that scan has finished and to perform cleanup. 

**Reimplements**: [Gambit::Printers::BasePrinterManager::finalise](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/)


Instruct all printers that scan has finished and to perform cleanup. 


## Public Attributes Documentation

### variable printerptr

```
BasePrinter * printerptr;
```

Pointer to main printer object. 

-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000