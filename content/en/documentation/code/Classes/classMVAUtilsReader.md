---
title: "class MVAUtilsReader"

description: "[No description available]"

---

# class MVAUtilsReader



[No description available]

Inherits from [MVA](/documentation/code/classes/classmva/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MVAUtilsReader](/documentation/code/classes/classmvautilsreader/#function-mvautilsreader)**(const std::string & name, const std::string fname1, const std::string fname2 ="") |
| virtual double | **[evaluate](/documentation/code/classes/classmvautilsreader/#function-evaluate)**(const std::vector< double > & values, const std::string nodeName ="") |
| virtual std::vector< double > | **[evaluateMulti](/documentation/code/classes/classmvautilsreader/#function-evaluatemulti)**(const std::vector< double > & values, int numClasses) |
| virtual std::vector< float > | **[evaluateMulti](/documentation/code/classes/classmvautilsreader/#function-evaluatemulti)**(const std::vector< float > & , int ) |
| | **[~MVAUtilsReader](/documentation/code/classes/classmvautilsreader/#function-mvautilsreader)**() |

## Additional inherited members

**Public Functions inherited from [MVA](/documentation/code/classes/classmva/)**

|                | Name           |
| -------------- | -------------- |
| | **[MVA](/documentation/code/classes/classmva/#function-mva)**(const std::string & name, const std::vector< std::string > variableDefs ={}) |
| void | **[setEventNumber](/documentation/code/classes/classmva/#function-seteventnumber)**(int eventNumber) |

**Protected Attributes inherited from [MVA](/documentation/code/classes/classmva/)**

|                | Name           |
| -------------- | -------------- |
| std::string | **[m_name](/documentation/code/classes/classmva/#variable-m-name)**  |
| std::vector< std::string > | **[m_variableDefs](/documentation/code/classes/classmva/#variable-m-variabledefs)**  |
| int | **[m_eventNumber](/documentation/code/classes/classmva/#variable-m-eventnumber)**  |


## Public Functions Documentation

### function MVAUtilsReader

```
MVAUtilsReader(
    const std::string & name,
    const std::string fname1,
    const std::string fname2 =""
)
```


### function evaluate

```
virtual double evaluate(
    const std::vector< double > & values,
    const std::string nodeName =""
)
```


**Reimplements**: [MVA::evaluate](/documentation/code/classes/classmva/#function-evaluate)


### function evaluateMulti

```
virtual std::vector< double > evaluateMulti(
    const std::vector< double > & values,
    int numClasses
)
```


**Reimplements**: [MVA::evaluateMulti](/documentation/code/classes/classmva/#function-evaluatemulti)


### function evaluateMulti

```
inline virtual std::vector< float > evaluateMulti(
    const std::vector< float > & ,
    int 
)
```


**Reimplements**: [MVA::evaluateMulti](/documentation/code/classes/classmva/#function-evaluatemulti)


### function ~MVAUtilsReader

```
inline ~MVAUtilsReader()
```


-------------------------------

Updated on 2026-11-03 at 14:50:41 +0000