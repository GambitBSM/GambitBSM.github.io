---
title: "class Gambit::Likelihood_Container_Factory"

description: "[No description available]"

---

# class Gambit::Likelihood_Container_Factory



[No description available]

Inherits from [Gambit::Scanner::Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Likelihood_Container_Factory](/documentation/code/classes/classgambit_1_1likelihood__container__factory/#function-gambitlikelihood-container-factory-likelihood-container-factory)**(const [gambit_core](/documentation/code/classes/classgambit_1_1gambit__core/) & core, [DRes::DependencyResolver](/documentation/code/classes/classgambit_1_1dres_1_1dependencyresolver/) & dependencyResolver, [IniParser::IniFile](/documentation/code/classes/classgambit_1_1iniparser_1_1inifile/) & iniFile, [Printers::BaseBasePrinter](/documentation/code/classes/classgambit_1_1printers_1_1basebaseprinter/) & printer) |
| | **[~Likelihood_Container_Factory](/documentation/code/classes/classgambit_1_1likelihood__container__factory/#function-gambitlikelihood-container-factory-likelihood-container-factory)**() |
| virtual void * | **[operator()](/documentation/code/classes/classgambit_1_1likelihood__container__factory/#function-gambitlikelihood-container-factory-operator)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & purpose) const |

## Additional inherited members

**Public Functions inherited from [Gambit::Scanner::Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/#function-gambitscannerfactory-base-factory-base)**() |


## Public Functions Documentation

### function Likelihood_Container_Factory

```
Likelihood_Container_Factory(
    const gambit_core & core,
    DRes::DependencyResolver & dependencyResolver,
    IniParser::IniFile & iniFile,
    Printers::BaseBasePrinter & printer
)
```


### function ~Likelihood_Container_Factory

```
inline ~Likelihood_Container_Factory()
```


### function operator()

```
virtual void * operator()(
    const str & purpose
) const
```


**Reimplements**: [Gambit::Scanner::Factory_Base::operator()](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/#function-gambitscannerfactory-base-operator)


-------------------------------

Updated on 2022-09-08 at 01:48:54 +0000