---
title: "class TMVAReader"

description: "[No description available]"

---

# class TMVAReader



[No description available]

Inherits from [MVA](/documentation/code/classes/classmva/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[TMVAReader](/documentation/code/classes/classtmvareader/#function-tmvareader)**(const std::string & name, const std::vector< std::string > & variableDefs, const std::string fname1, const std::string fname2 ="") |
| virtual double | **[evaluate](/documentation/code/classes/classtmvareader/#function-evaluate)**(const std::vector< double > & values, const std::string nodeName ="") |
| | **[~TMVAReader](/documentation/code/classes/classtmvareader/#function-tmvareader)**() |

## Additional inherited members

**Public Functions inherited from [MVA](/documentation/code/classes/classmva/)**

|                | Name           |
| -------------- | -------------- |
| | **[MVA](/documentation/code/classes/classmva/#function-mva)**(const std::string & name, const std::vector< std::string > variableDefs ={}) |
| void | **[setEventNumber](/documentation/code/classes/classmva/#function-seteventnumber)**(int eventNumber) |
| virtual std::vector< double > | **[evaluateMulti](/documentation/code/classes/classmva/#function-evaluatemulti)**(const std::vector< double > & , int ) |
| virtual std::vector< float > | **[evaluateMulti](/documentation/code/classes/classmva/#function-evaluatemulti)**(const std::vector< float > & , int ) |

**Protected Attributes inherited from [MVA](/documentation/code/classes/classmva/)**

|                | Name           |
| -------------- | -------------- |
| std::string | **[m_name](/documentation/code/classes/classmva/#variable-m-name)**  |
| std::vector< std::string > | **[m_variableDefs](/documentation/code/classes/classmva/#variable-m-variabledefs)**  |
| int | **[m_eventNumber](/documentation/code/classes/classmva/#variable-m-eventnumber)**  |


## Public Functions Documentation

### function TMVAReader

```
TMVAReader(
    const std::string & name,
    const std::vector< std::string > & variableDefs,
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


### function ~TMVAReader

```
inline ~TMVAReader()
```


-------------------------------

Updated on 2026-11-03 at 14:50:41 +0000