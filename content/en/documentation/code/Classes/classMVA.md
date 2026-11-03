---
title: "class MVA"

description: "[No description available]"

---

# class MVA



[No description available]

Inherited by [MVAUtilsReader](/documentation/code/classes/classmvautilsreader/), [TMVAReader](/documentation/code/classes/classtmvareader/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MVA](/documentation/code/classes/classmva/#function-mva)**(const std::string & name, const std::vector< std::string > variableDefs ={}) |
| void | **[setEventNumber](/documentation/code/classes/classmva/#function-seteventnumber)**(int eventNumber) |
| virtual double | **[evaluate](/documentation/code/classes/classmva/#function-evaluate)**(const std::vector< double > & values, const std::string nodeName ="") =0 |
| virtual std::vector< double > | **[evaluateMulti](/documentation/code/classes/classmva/#function-evaluatemulti)**(const std::vector< double > & , int ) |
| virtual std::vector< float > | **[evaluateMulti](/documentation/code/classes/classmva/#function-evaluatemulti)**(const std::vector< float > & , int ) |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[m_name](/documentation/code/classes/classmva/#variable-m-name)**  |
| std::vector< std::string > | **[m_variableDefs](/documentation/code/classes/classmva/#variable-m-variabledefs)**  |
| int | **[m_eventNumber](/documentation/code/classes/classmva/#variable-m-eventnumber)**  |

## Public Functions Documentation

### function MVA

```
inline MVA(
    const std::string & name,
    const std::vector< std::string > variableDefs ={}
)
```


### function setEventNumber

```
inline void setEventNumber(
    int eventNumber
)
```


### function evaluate

```
virtual double evaluate(
    const std::vector< double > & values,
    const std::string nodeName =""
) =0
```


**Reimplemented by**: [TMVAReader::evaluate](/documentation/code/classes/classtmvareader/#function-evaluate), [MVAUtilsReader::evaluate](/documentation/code/classes/classmvautilsreader/#function-evaluate)


### function evaluateMulti

```
inline virtual std::vector< double > evaluateMulti(
    const std::vector< double > & ,
    int 
)
```


**Reimplemented by**: [MVAUtilsReader::evaluateMulti](/documentation/code/classes/classmvautilsreader/#function-evaluatemulti)


### function evaluateMulti

```
inline virtual std::vector< float > evaluateMulti(
    const std::vector< float > & ,
    int 
)
```


**Reimplemented by**: [MVAUtilsReader::evaluateMulti](/documentation/code/classes/classmvautilsreader/#function-evaluatemulti)


## Protected Attributes Documentation

### variable m_name

```
std::string m_name;
```


### variable m_variableDefs

```
std::vector< std::string > m_variableDefs;
```


### variable m_eventNumber

```
int m_eventNumber;
```


-------------------------------

Updated on 2026-11-03 at 14:50:41 +0000