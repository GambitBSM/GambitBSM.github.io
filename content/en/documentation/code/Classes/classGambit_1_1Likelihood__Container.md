---
title: "class Gambit::Likelihood_Container"
description: "Class for collecting pointers to all the likelihood components, then running and combining them. "

---

# class Gambit::Likelihood_Container



Class for collecting pointers to all the likelihood components, then running and combining them. 


`#include <likelihood_container.hpp>`

Inherits from [Gambit::Scanner::Function_Base< double(std::unordered_map< std::string, double > &)>](/documentation/code/classes/classgambit_1_1scanner_1_1function__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Likelihood_Container](/documentation/code/classes/classgambit_1_1likelihood__container/#function-likelihood-container)**(const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [primary_model_functor](/documentation/code/classes/classgambit_1_1primary__model__functor/) * > & functorMap, [DRes::DependencyResolver](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/) & dependencyResolver, [IniParser::IniFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/) & iniFile, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & purpose, [Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer)<br>Constructor.  |
| void | **[setParameters](/documentation/code/classes/classgambit_1_1likelihood__container/#function-setparameters)**(const std::unordered_map< std::string, double > & parameterMap)<br>Do the prior transformation and populate the parameter map.  |
| double | **[main](/documentation/code/classes/classgambit_1_1likelihood__container/#function-main)**(std::unordered_map< std::string, double > & in)<br>Evaluate total likelihood function.  |
| double | **[purposeModifier](/documentation/code/classes/classgambit_1_1likelihood__container/#function-purposemodifier)**(double lnlike)<br>Use this to modify the total likelihood function before passing it to the scanner.  |
| void | **[set_scanID](/documentation/code/classes/classgambit_1_1likelihood__container/#function-set-scanid)**()<br>Set the scanID.  |

## Public Functions Documentation

### function Likelihood_Container

```
Likelihood_Container(
    const std::map< str, primary_model_functor * > & functorMap,
    DRes::DependencyResolver & dependencyResolver,
    IniParser::IniFile & iniFile,
    const str & purpose,
    Printers::BaseBasePrinter & printer
)
```

Constructor. 

### function setParameters

```
void setParameters(
    const std::unordered_map< std::string, double > & parameterMap
)
```

Do the prior transformation and populate the parameter map. 

### function main

```
double main(
    std::unordered_map< std::string, double > & in
)
```

Evaluate total likelihood function. 

### function purposeModifier

```
double purposeModifier(
    double lnlike
)
```

Use this to modify the total likelihood function before passing it to the scanner. 

### function set_scanID

```
void set_scanID()
```

Set the scanID. 

Work out what the scanID should be and set it. 


-------------------------------

Updated on 2025-02-12 at 16:10:31 +0000