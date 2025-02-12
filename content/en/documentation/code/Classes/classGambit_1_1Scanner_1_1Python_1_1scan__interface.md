---
title: "class Gambit::Scanner::Python::scan_interface"

description: "[No description available]"

---

# class Gambit::Scanner::Python::scan_interface



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[scan_interface](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/#function-scan-interface)**(bool ) |
| [Printers::PrinterManager](/documentation/code/classes/classgambit_1_1printers_1_1printermanager/) & | **[get_printer_manager](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/#function-get-printer-manager)**() const |
| std::shared_ptr< [printer_wrapper](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1printer__wrapper/) > | **[get_printer](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/#function-get-printer)**() |
| int | **[run_scan](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/#function-run-scan)**([Gambit::IniParser::Parser](/documentation/code/classes/classgambit_1_1iniparser_1_1parser/) & iniFile, const [Gambit::Scanner::Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/) * factory, [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) * user_prior, bool resume)<br>Main scan execution program.  |
| int | **[run_scan_node](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/#function-run-scan-node)**(YAML::Node * node, const [Gambit::Scanner::Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/) * factory, [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) * user_prior, bool resume) |
| int | **[run_scan_str](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/#function-run-scan-str)**(std::string * filename, const [Gambit::Scanner::Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/) * factory, [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/) * user_prior, bool resume) |
| | **[~scan_interface](/documentation/code/classes/classgambit_1_1scanner_1_1python_1_1scan__interface/#function-scan-interface)**() |

## Public Functions Documentation

### function scan_interface

```
scan_interface(
    bool 
)
```


### function get_printer_manager

```
inline Printers::PrinterManager & get_printer_manager() const
```


### function get_printer

```
std::shared_ptr< printer_wrapper > get_printer()
```


### function run_scan

```
int run_scan(
    Gambit::IniParser::Parser & iniFile,
    const Gambit::Scanner::Factory_Base * factory,
    Gambit::Priors::BasePrior * user_prior,
    bool resume
)
```

Main scan execution program. 

Idea by Tom Fogal, for optionally preventing execution of code until debugger allows it Source: [http://www.sci.utah.edu/~tfogal/academic/Fogal-ParallelDebugging.pdf](http://www.sci.utah.edu/~tfogal/academic/Fogal-ParallelDebugging.pdf)

Special catch block for silent shutdown This exception is designed to be thrown during diagnostic mode

Special catch block for controlled shutdown This exception should only be thrown if it is safe to call MPI_Finalise, as this will occur once we leave the catch block.

Special catch block for hard shutdown No MPI_Finalise called, nor MPI_Abort. Should only be triggered when all processes are supposed to be trying to shut themselves down quickly, for example if synchronising for soft shutdown fails.

Shut down due receipt of MPI emergency shutdown message


### function run_scan_node

```
int run_scan_node(
    YAML::Node * node,
    const Gambit::Scanner::Factory_Base * factory,
    Gambit::Priors::BasePrior * user_prior,
    bool resume
)
```


### function run_scan_str

```
int run_scan_str(
    std::string * filename,
    const Gambit::Scanner::Factory_Base * factory,
    Gambit::Priors::BasePrior * user_prior,
    bool resume
)
```


### function ~scan_interface

```
inline ~scan_interface()
```


-------------------------------

Updated on 2025-02-12 at 15:36:40 +0000