---
title: "class Gambit::Printers::BasePrinterManager"
description: "Manager class for creating printer objects "

---

# class Gambit::Printers::BasePrinterManager



Manager class for creating printer objects 


`#include <baseprintermanager.hpp>`

Inherited by [Gambit::Printers::PrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BasePrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-baseprintermanager)**() |
| | **[BasePrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-baseprintermanager)**(bool r) |
| bool | **[resume_mode](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-resume-mode)**()<br>Getter for "resume" mode flag.  |
| void | **[set_resume_mode](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-set-resume-mode)**(bool rflag) |
| virtual void | **[new_stream](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-new-stream)**(const std::string & , const [Options](/documentation/code/classes/classgambit_1_1options/) & ) =0<br>Create auxiliary printer object.  |
| virtual void | **[new_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-new-reader)**(const std::string & , const [Options](/documentation/code/classes/classgambit_1_1options/) & ) =0<br>Create reader object.  |
| virtual void | **[create_resume_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-create-resume-reader)**() =0<br>Create for reader object for previous print output ("resume reader")  |
| virtual [BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) * | **[get_stream](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-get-stream)**(const std::string &  ="") =0<br>Getter for auxiliary printer objects.  |
| virtual [BaseBaseReader](/documentation/code/classes/classgambit_1_1printers_1_1basebasereader/) * | **[get_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-get-reader)**(const std::string & ) =0<br>Getter for readers.  |
| virtual bool | **[reader_exists](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-reader-exists)**(const std::string & ) =0<br>Checker for reader existence.  |
| virtual void | **[delete_stream](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-delete-stream)**(const std::string &  ="") =0<br>Delete reader and printer objects (does not harm output, just deletes the objects)  |
| virtual void | **[delete_reader](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-delete-reader)**(const std::string & ) =0 |
| virtual void | **[finalise](/documentation/code/classes/classgambit_1_1printers_1_1baseprintermanager/#function-finalise)**(bool abnormal =false) =0<br>Instruct printers that scan has finished and to perform cleanup.  |

## Public Functions Documentation

### function BasePrinterManager

```
inline BasePrinterManager()
```


### function BasePrinterManager

```
inline BasePrinterManager(
    bool r
)
```


### function resume_mode

```
inline bool resume_mode()
```

Getter for "resume" mode flag. 

### function set_resume_mode

```
inline void set_resume_mode(
    bool rflag
)
```


Setter for "resume" mode flag (printer may override user choice if no previous output exists) 


### function new_stream

```
virtual void new_stream(
    const std::string & ,
    const Options & 
) =0
```

Create auxiliary printer object. 

**Reimplemented by**: [Gambit::Printers::PrinterManager::new_stream](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-new-stream)


### function new_reader

```
virtual void new_reader(
    const std::string & ,
    const Options & 
) =0
```

Create reader object. 

**Reimplemented by**: [Gambit::Printers::PrinterManager::new_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-new-reader)


### function create_resume_reader

```
virtual void create_resume_reader() =0
```

Create for reader object for previous print output ("resume reader") 

**Reimplemented by**: [Gambit::Printers::PrinterManager::create_resume_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-create-resume-reader)


### function get_stream

```
virtual BaseBasePrinter * get_stream(
    const std::string &  =""
) =0
```

Getter for auxiliary printer objects. 

**Reimplemented by**: [Gambit::Printers::PrinterManager::get_stream](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-get-stream)


### function get_reader

```
virtual BaseBaseReader * get_reader(
    const std::string & 
) =0
```

Getter for readers. 

**Reimplemented by**: [Gambit::Printers::PrinterManager::get_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-get-reader)


### function reader_exists

```
virtual bool reader_exists(
    const std::string & 
) =0
```

Checker for reader existence. 

**Reimplemented by**: [Gambit::Printers::PrinterManager::reader_exists](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-reader-exists)


### function delete_stream

```
virtual void delete_stream(
    const std::string &  =""
) =0
```

Delete reader and printer objects (does not harm output, just deletes the objects) 

**Reimplemented by**: [Gambit::Printers::PrinterManager::delete_stream](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-delete-stream)


### function delete_reader

```
virtual void delete_reader(
    const std::string & 
) =0
```


**Reimplemented by**: [Gambit::Printers::PrinterManager::delete_reader](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-delete-reader)


### function finalise

```
virtual void finalise(
    bool abnormal =false
) =0
```

Instruct printers that scan has finished and to perform cleanup. 

**Reimplemented by**: [Gambit::Printers::PrinterManager::finalise](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/#function-finalise)


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000