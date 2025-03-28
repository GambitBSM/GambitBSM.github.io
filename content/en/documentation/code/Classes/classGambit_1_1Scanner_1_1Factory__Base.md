---
title: "class Gambit::Scanner::Factory_Base"
description: "Pure Base class of a plugin Factory function. "

---

# class Gambit::Scanner::Factory_Base



Pure Base class of a plugin Factory function. 


`#include <factory_defs.hpp>`

Inherited by [Gambit::Likelihood_Container_Factory](/documentation/code/classes/classgambit_1_1likelihood__container__factory/), [Gambit::Scanner::Plugin_Function_Factory](/documentation/code/classes/classgambit_1_1scanner_1_1plugin__function__factory/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void * | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/#function-operator)**(const std::string & purpose) const =0 |
| virtual | **[~Factory_Base](/documentation/code/classes/classgambit_1_1scanner_1_1factory__base/#function-factory-base)**() |

## Public Functions Documentation

### function operator()

```
virtual void * operator()(
    const std::string & purpose
) const =0
```


**Reimplemented by**: [Gambit::Scanner::Plugin_Function_Factory::operator()](/documentation/code/classes/classgambit_1_1scanner_1_1plugin__function__factory/#function-operator), [Gambit::Likelihood_Container_Factory::operator()](/documentation/code/classes/classgambit_1_1likelihood__container__factory/#function-operator)


### function ~Factory_Base

```
inline virtual ~Factory_Base()
```


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000