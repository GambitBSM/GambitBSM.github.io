---
title: "class Gambit::Options"

description: "[No description available]"

---

# class Gambit::Options



[No description available] [More...](#detailed-description)


`#include <yaml_options.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <typename... args\> <br>bool | **[hasKey](/documentation/code/classes/classgambit_1_1options/#function-haskey)**(const args &... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValue](/documentation/code/classes/classgambit_1_1options/#function-getvalue)**(const args &... keys) const |
| template <typename TYPE ,typename... args\> <br>TYPE | **[getValueOrDef](/documentation/code/classes/classgambit_1_1options/#function-getvalueordef)**(TYPE def, const args &... keys) const |
| template <typename KEYTYPE ,typename VALTYPE \> <br>void | **[setValue](/documentation/code/classes/classgambit_1_1options/#function-setvalue)**(const KEYTYPE & key, const VALTYPE & val) |
| | **[Options](/documentation/code/classes/classgambit_1_1options/#function-options)**()<br>Default constructor.  |
| | **[Options](/documentation/code/classes/classgambit_1_1options/#function-options)**(const YAML::Node & options)<br>Copy constructor.  |
| | **[Options](/documentation/code/classes/classgambit_1_1options/#function-options)**(YAML::Node && options)<br>Move constructor.  |
| template <typename TYPE \> <br>std::vector< TYPE > | **[getVector](/documentation/code/classes/classgambit_1_1options/#function-getvector)**(std::string key) const<br>Get a `std::vector` of a particular type.  |
| template <typename... args\> <br>const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[getNames](/documentation/code/classes/classgambit_1_1options/#function-getnames)**(const args &... keys) const |
| const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[getNames](/documentation/code/classes/classgambit_1_1options/#function-getnames)**() const |
| template <typename... args\> <br>const [Options](/documentation/code/classes/classgambit_1_1options/) | **[getOptions](/documentation/code/classes/classgambit_1_1options/#function-getoptions)**(const args &... keys) const<br>Recursive options retrieval.  |
| template <typename... args\> <br>YAML::Node | **[getNode](/documentation/code/classes/classgambit_1_1options/#function-getnode)**(const args &... keys) const<br>Retrieve raw [YAML](/documentation/code/namespaces/namespaceyaml/) node.  |
| template <typename... args\> <br>YAML::Node | **[loadFromFile](/documentation/code/classes/classgambit_1_1options/#function-loadfromfile)**(const args &... keys) const<br>Get [YAML](/documentation/code/namespaces/namespaceyaml/) node from file.  |
| YAML::const_iterator | **[begin](/documentation/code/classes/classgambit_1_1options/#function-begin)**() const<br>Return begin and end of options.  |
| YAML::const_iterator | **[end](/documentation/code/classes/classgambit_1_1options/#function-end)**() const |
| std::string | **[toString](/documentation/code/classes/classgambit_1_1options/#function-tostring)**(size_t level) const<br>Convert to string with some indentation.  |
| void | **[toMap](/documentation/code/classes/classgambit_1_1options/#function-tomap)**([map_str_str](/documentation/code/namespaces/namespacegambit/#typedef-map-str-str) & map, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) header ="") const<br>Convert the options node a map.  |

## Detailed Description

```
class Gambit::Options;
```


A small wrapper object for 'options' nodes. These can be extracted from the prior, observable/likelihood and rules sections of the inifile, or set by hand in module standalone mode. 

## Public Functions Documentation

### function hasKey

```
template <typename... args>
inline bool hasKey(
    const args &... keys
) const
```


Getters for key/value pairs (which is all the options node should contain) 


### function getValue

```
template <typename TYPE ,
typename... args>
inline TYPE getValue(
    const args &... keys
) const
```


### function getValueOrDef

```
template <typename TYPE ,
typename... args>
inline TYPE getValueOrDef(
    TYPE def,
    const args &... keys
) const
```


### function setValue

```
template <typename KEYTYPE ,
typename VALTYPE >
inline void setValue(
    const KEYTYPE & key,
    const VALTYPE & val
)
```


Basic setter, for adding extra options 


### function Options

```
inline Options()
```

Default constructor. 

### function Options

```
inline Options(
    const YAML::Node & options
)
```

Copy constructor. 

### function Options

```
inline Options(
    YAML::Node && options
)
```

Move constructor. 

### function getVector

```
template <typename TYPE >
inline std::vector< TYPE > getVector(
    std::string key
) const
```

Get a `std::vector` of a particular type. 

If the entry is a scalar rather than a vector, try to convert it to a size one `std::vector`


### function getNames

```
template <typename... args>
inline const std::vector< str > getNames(
    const args &... keys
) const
```


Retrieve values from key-value pairs in options node. Works for an arbitrary set of input keys (of any type), and returns all values as strings. 


### function getNames

```
inline const std::vector< str > getNames() const
```


Retrieve values from all key-value pairs in options node. Returns all keys as strings. 


### function getOptions

```
template <typename... args>
inline const Options getOptions(
    const args &... keys
) const
```

Recursive options retrieval. 

### function getNode

```
template <typename... args>
inline YAML::Node getNode(
    const args &... keys
) const
```

Retrieve raw [YAML](/documentation/code/namespaces/namespaceyaml/) node. 

### function loadFromFile

```
template <typename... args>
inline YAML::Node loadFromFile(
    const args &... keys
) const
```

Get [YAML](/documentation/code/namespaces/namespaceyaml/) node from file. 

### function begin

```
inline YAML::const_iterator begin() const
```

Return begin and end of options. 

### function end

```
inline YAML::const_iterator end() const
```


### function toString

```
inline std::string toString(
    size_t level
) const
```

Convert to string with some indentation. 

### function toMap

```
inline void toMap(
    map_str_str & map,
    str header =""
) const
```

Convert the options node a map. 

-------------------------------

Updated on 2025-02-12 at 16:10:31 +0000