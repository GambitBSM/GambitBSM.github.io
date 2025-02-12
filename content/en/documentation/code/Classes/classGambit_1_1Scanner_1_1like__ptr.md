---
title: "class Gambit::Scanner::like_ptr"
description: "likelihood pointer holder for scanner plugins. "

---

# class Gambit::Scanner::like_ptr



likelihood pointer holder for scanner plugins. 


`#include <factory_defs.hpp>`

Inherits from [Gambit::Scanner::scan_ptr< double(std::unordered_map< std::string, double > &)>](/documentation/code/classes/classgambit_1_1scanner_1_1scan__ptr/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[like_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/#function-like-ptr)**() |
| | **[like_ptr](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/#function-like-ptr)**(void * in) |
| double | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/#function-operator)**(const std::vector< double > & vec) |
| double | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/#function-operator)**([hyper_cube_ref](/documentation/code/namespaces/namespacegambit_1_1scanner/#using-hyper-cube-ref)< double > vec) |
| double | **[operator()](/documentation/code/classes/classgambit_1_1scanner_1_1like__ptr/#function-operator)**(std::unordered_map< std::string, double > & map, bool use_prior =false) |

## Public Functions Documentation

### function like_ptr

```
inline like_ptr()
```


### function like_ptr

```
inline like_ptr(
    void * in
)
```


### function operator()

```
inline double operator()(
    const std::vector< double > & vec
)
```


### function operator()

```
inline double operator()(
    hyper_cube_ref< double > vec
)
```


### function operator()

```
inline double operator()(
    std::unordered_map< std::string, double > & map,
    bool use_prior =false
)
```


-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000