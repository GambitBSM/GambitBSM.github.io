---
title: "class Gambit::SetMaps"
description: "[FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/) friend class for implementing named parameter idiom. "

---

# class Gambit::SetMaps



[FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/) friend class for implementing named parameter idiom.  [More...](#detailed-description)


`#include <spec_fptrfinder.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef HostSpec::D | **[D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d)** <br>Type of derived spectrum wrapper is known to HostSpec as D.  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SetMaps](/documentation/code/classes/classgambit_1_1setmaps/#function-setmaps)**(const std::string & label, HostSpec *const fakethis) |
| | **[SetMaps](/documentation/code/classes/classgambit_1_1setmaps/#function-setmaps)**(const std::string & label, const HostSpec *const fakethis)<br>Version to deal with const host object.  |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map0](/documentation/code/classes/classgambit_1_1setmaps/#function-map0)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap0 & map0)<br>derived class maps  |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map1](/documentation/code/classes/classgambit_1_1setmaps/#function-map1)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap1 & map1) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map2](/documentation/code/classes/classgambit_1_1setmaps/#function-map2)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap2 & map2) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map0W](/documentation/code/classes/classgambit_1_1setmaps/#function-map0w)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap0W & map0W) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map1W](/documentation/code/classes/classgambit_1_1setmaps/#function-map1w)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap1W & map1W) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map2W](/documentation/code/classes/classgambit_1_1setmaps/#function-map2w)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap2W & map2W) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map0M](/documentation/code/classes/classgambit_1_1setmaps/#function-map0m)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap0_extraM & map0M) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map1M](/documentation/code/classes/classgambit_1_1setmaps/#function-map1m)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap1_extraM & map1M) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map2M](/documentation/code/classes/classgambit_1_1setmaps/#function-map2m)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap2_extraM & map2M) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map0I](/documentation/code/classes/classgambit_1_1setmaps/#function-map0i)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap0_extraI & map0I) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map1I](/documentation/code/classes/classgambit_1_1setmaps/#function-map1i)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap1_extraI & map1I) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[map2I](/documentation/code/classes/classgambit_1_1setmaps/#function-map2i)**(const typename [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< [D](/documentation/code/classes/classgambit_1_1setmaps/#typedef-d), MTag >::fmap2_extraI & map2I) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[omap0](/documentation/code/classes/classgambit_1_1setmaps/#function-omap0)**(const std::map< std::string, double > & om0)<br>base class override maps  |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[omap1](/documentation/code/classes/classgambit_1_1setmaps/#function-omap1)**(const std::map< std::string, std::map< int, double > > & om1) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[omap2](/documentation/code/classes/classgambit_1_1setmaps/#function-omap2)**(const std::map< std::string, std::map< int, std::map< int, double > > > & om2) |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[no_overrides](/documentation/code/classes/classgambit_1_1setmaps/#function-no-overrides)**(const bool flag)<br>Flag to disable searching of override maps (for retrieving original, unoverriden values)  |
| [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) & | **[override_only](/documentation/code/classes/classgambit_1_1setmaps/#function-override-only)**(const bool flag)<br>Flag to permit searching only override maps.  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[FptrFinder< HostSpec, MTag >](/documentation/code/classes/classgambit_1_1setmaps/#friend-fptrfinder-hostspec-mtag)**  |

## Detailed Description

```
template <class HostSpec ,
class MTag >
class Gambit::SetMaps;
```

[FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/) friend class for implementing named parameter idiom. 

Forward declarations related to [FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/) class. 

## Public Types Documentation

### typedef D

```
typedef HostSpec::D Gambit::SetMaps< HostSpec, MTag >::D;
```

Type of derived spectrum wrapper is known to HostSpec as D. 

## Public Functions Documentation

### function SetMaps

```
inline SetMaps(
    const std::string & label,
    HostSpec *const fakethis
)
```


### function SetMaps

```
inline SetMaps(
    const std::string & label,
    const HostSpec *const fakethis
)
```

Version to deal with const host object. 

### function map0

```
inline SetMaps & map0(
    const typename MapTypes< D, MTag >::fmap0 & map0
)
```

derived class maps 

### function map1

```
inline SetMaps & map1(
    const typename MapTypes< D, MTag >::fmap1 & map1
)
```


### function map2

```
inline SetMaps & map2(
    const typename MapTypes< D, MTag >::fmap2 & map2
)
```


### function map0W

```
inline SetMaps & map0W(
    const typename MapTypes< D, MTag >::fmap0W & map0W
)
```


### function map1W

```
inline SetMaps & map1W(
    const typename MapTypes< D, MTag >::fmap1W & map1W
)
```


### function map2W

```
inline SetMaps & map2W(
    const typename MapTypes< D, MTag >::fmap2W & map2W
)
```


### function map0M

```
inline SetMaps & map0M(
    const typename MapTypes< D, MTag >::fmap0_extraM & map0M
)
```


### function map1M

```
inline SetMaps & map1M(
    const typename MapTypes< D, MTag >::fmap1_extraM & map1M
)
```


### function map2M

```
inline SetMaps & map2M(
    const typename MapTypes< D, MTag >::fmap2_extraM & map2M
)
```


### function map0I

```
inline SetMaps & map0I(
    const typename MapTypes< D, MTag >::fmap0_extraI & map0I
)
```


### function map1I

```
inline SetMaps & map1I(
    const typename MapTypes< D, MTag >::fmap1_extraI & map1I
)
```


### function map2I

```
inline SetMaps & map2I(
    const typename MapTypes< D, MTag >::fmap2_extraI & map2I
)
```


### function omap0

```
inline SetMaps & omap0(
    const std::map< std::string, double > & om0
)
```

base class override maps 

### function omap1

```
inline SetMaps & omap1(
    const std::map< std::string, std::map< int, double > > & om1
)
```


### function omap2

```
inline SetMaps & omap2(
    const std::map< std::string, std::map< int, std::map< int, double > > > & om2
)
```


### function no_overrides

```
inline SetMaps & no_overrides(
    const bool flag
)
```

Flag to disable searching of override maps (for retrieving original, unoverriden values) 

### function override_only

```
inline SetMaps & override_only(
    const bool flag
)
```

Flag to permit searching only override maps. 

## Friends

### friend FptrFinder< HostSpec, MTag >

```
friend class FptrFinder< HostSpec, MTag >(
    FptrFinder< HostSpec, MTag > 
);
```


-------------------------------

Updated on 2022-09-08 at 03:46:43 +0000