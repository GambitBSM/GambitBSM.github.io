---
title: "class Gambit::FptrFinder"
description: "Forward declaration of [FptrFinder](). "

---

# class Gambit::FptrFinder



Forward declaration of [FptrFinder]().  [More...](#detailed-description)


`#include <spec_fptrfinder.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| int | **[get_error_code](/documentation/code/classes/classgambit_1_1fptrfinder/#function-get-error-code)**()<br>Error reporting.  |
| std::string | **[get_error_message](/documentation/code/classes/classgambit_1_1fptrfinder/#function-get-error-message)**() |
| void | **[raise_error](/documentation/code/classes/classgambit_1_1fptrfinder/#function-raise-error)**(const std::string & origin) |
| void | **[check_index_initd](/documentation/code/classes/classgambit_1_1fptrfinder/#function-check-index-initd)**(const std::string & origin, const int index, const std::string & label) |
| bool | **[find_override_0index](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find-override-0index)**(const std::string & name)<br>Search 0-index override map.  |
| bool | **[find_override_1index](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find-override-1index)**(const std::string & name, const int i)<br>Search 1-index override map.  |
| bool | **[find_override_2index](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find-override-2index)**(const std::string & name, const int i, const int j)<br>Search 2-index override map.  |
| bool | **[find_0index](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find-0index)**(const std::string & name)<br>Search 0-index wrapper maps.  |
| bool | **[find_1index](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find-1index)**(const std::string & name, const int i)<br>Search 1-index wrapper maps.  |
| bool | **[find_2index](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find-2index)**(const std::string & name, const int i, const int j)<br>Search 2-index wrapper maps.  |
| | **[FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/#function-fptrfinder)**(const [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/)< HostSpec, MTag > & params) |
| template <class Map \> <br>bool | **[search_map](/documentation/code/classes/classgambit_1_1fptrfinder/#function-search-map)**(const std::string & name, const Map *const map, typename Map::const_iterator & it)<br>helper functions for searching individual maps  |
| void | **[check](/documentation/code/classes/classgambit_1_1fptrfinder/#function-check)**(bool safe) |
| template <class ITER \> <br>bool | **[check_indices_1](/documentation/code/classes/classgambit_1_1fptrfinder/#function-check-indices-1)**(const std::string & name, const ITER & it, const int i, const int whichit, const bool debug) |
| template <class ITER \> <br>bool | **[check_indices_2](/documentation/code/classes/classgambit_1_1fptrfinder/#function-check-indices-2)**(const std::string & , const ITER & it, const int i, const int j, const int whichit) |
| bool | **[find](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find)**(const std::string & name, bool  =true, [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true))<br>Search function for 0-index maps.  |
| bool | **[find](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find)**(const std::string & name, int i, bool  =true, [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true))<br>Search function for 1-index maps.  |
| bool | **[find](/documentation/code/classes/classgambit_1_1fptrfinder/#function-find)**(const std::string & name, int i, int j)<br>Search function for 2-index maps.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [CallFcn](/documentation/code/classes/classgambit_1_1callfcn/)< HostSpec, MTag > | **[callfcn](/documentation/code/classes/classgambit_1_1fptrfinder/#variable-callfcn)**  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[CallFcn< HostSpec, MTag >](/documentation/code/classes/classgambit_1_1fptrfinder/#friend-callfcn-hostspec-mtag)**  |

## Detailed Description

```
template <class HostSpec ,
class MTag >
class Gambit::FptrFinder;
```

Forward declaration of [FptrFinder](). 

Helper class for locating the function pointer corresponding to a requested string, from amongst the various different maps in which it could be located. 

## Public Functions Documentation

### function get_error_code

```
inline int get_error_code()
```

Error reporting. 

### function get_error_message

```
inline std::string get_error_message()
```


### function raise_error

```
inline void raise_error(
    const std::string & origin
)
```


### function check_index_initd

```
inline void check_index_initd(
    const std::string & origin,
    const int index,
    const std::string & label
)
```


### function find_override_0index

```
inline bool find_override_0index(
    const std::string & name
)
```

Search 0-index override map. 

Functions to search for specific entries with no translation (to factorise the various pieces of the complicated search functions) 


### function find_override_1index

```
inline bool find_override_1index(
    const std::string & name,
    const int i
)
```

Search 1-index override map. 

### function find_override_2index

```
inline bool find_override_2index(
    const std::string & name,
    const int i,
    const int j
)
```

Search 2-index override map. 

### function find_0index

```
inline bool find_0index(
    const std::string & name
)
```

Search 0-index wrapper maps. 

### function find_1index

```
inline bool find_1index(
    const std::string & name,
    const int i
)
```

Search 1-index wrapper maps. 

### function find_2index

```
inline bool find_2index(
    const std::string & name,
    const int i,
    const int j
)
```

Search 2-index wrapper maps. 

### function FptrFinder

```
inline FptrFinder(
    const SetMaps< HostSpec, MTag > & params
)
```


### function search_map

```
template <class Map >
inline bool search_map(
    const std::string & name,
    const Map *const map,
    typename Map::const_iterator & it
)
```

helper functions for searching individual maps 

### function check

```
inline void check(
    bool safe
)
```


Check if it is (supposed to be) safe to dereference a map iterator Throw an error if it isn't 


### function check_indices_1

```
template <class ITER >
inline bool check_indices_1(
    const std::string & name,
    const ITER & it,
    const int i,
    const int whichit,
    const bool debug
)
```


Methods for setting parameters (named parameter idiom) E.g. call constructor like this to use named "parameters" FptrFinder().map(x).map2(z).mapM(y) Could protect parameters from being reset by putting these setters in a friend class, which can only set the [FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/) parameters via the [FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/) constructor, but this is good enough for the use here I think. NOTE: I think this comment refers to moved/removed functionality... 


### function check_indices_2

```
template <class ITER >
inline bool check_indices_2(
    const std::string & ,
    const ITER & it,
    const int i,
    const int j,
    const int whichit
)
```


### function find

```
inline bool find(
    const std::string & name,
    bool  =true,
    SafeBool check_antiparticle =SafeBool(true)
)
```

Search function for 0-index maps. 

Get antiparticle name if it exists Slightly wasteful to do this all the time if not needed, but makes the code simpler and realistically won't make any difference.


### function find

```
inline bool find(
    const std::string & name,
    int i,
    bool  =true,
    SafeBool check_antiparticle =SafeBool(true)
)
```

Search function for 1-index maps. 

Get antiparticle name if it exists


### function find

```
inline bool find(
    const std::string & name,
    int i,
    int j
)
```

Search function for 2-index maps. 

## Public Attributes Documentation

### variable callfcn

```
CallFcn< HostSpec, MTag > callfcn;
```


Caller for whatever function was found HostSpec has to work slightly differently depending on whether [FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/) is specialised for [MapTag::Get](/documentation/code/classes/structgambit_1_1maptag_1_1get/) or [MapTag::Set](/documentation/code/classes/structgambit_1_1maptag_1_1set/), so we just declare it here and do the specialisation after the class declaration. HostSpec has to be a struct, since we partial specialisation of functions is not allowed in C++, but it is treated like a member function. 


## Friends

### friend CallFcn< HostSpec, MTag >

```
friend class CallFcn< HostSpec, MTag >(
    CallFcn< HostSpec, MTag > 
);
```


-------------------------------

Updated on 2024-05-31 at 15:12:03 +0000