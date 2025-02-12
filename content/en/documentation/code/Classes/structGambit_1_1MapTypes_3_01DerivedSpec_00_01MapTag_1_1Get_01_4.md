---
title: "struct Gambit::MapTypes< DerivedSpec, MapTag::Get >"

description: "[No description available]"

---

# struct Gambit::MapTypes< DerivedSpec, MapTag::Get >



[No description available] [More...](#detailed-description)


`#include <spectrum_helpers.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< DerivedSpec >::Model | **[Model](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-model)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< DerivedSpec >::Input | **[Input](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-input)**  |
| typedef double(Model::*)(void) const | **[FSptr](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fsptr)**  |
| typedef double(Model::*)(int) const | **[FSptr1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fsptr1)**  |
| typedef double(Model::*)(int, int) const | **[FSptr2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fsptr2)**  |
| typedef double(DerivedSpec::*)(void) const | **[FSptrW](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fsptrw)**  |
| typedef double(DerivedSpec::*)(int) const | **[FSptr1W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fsptr1w)**  |
| typedef double(DerivedSpec::*)(int, int) const | **[FSptr2W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fsptr2w)**  |
| typedef double(*)(const Model &) | **[plainfptrM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-plainfptrm)**  |
| typedef double(*)(const Model &, int) | **[plainfptrM1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-plainfptrm1)**  |
| typedef double(*)(const Model &, int, int) | **[plainfptrM2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-plainfptrm2)**  |
| typedef double(*)(const Input &) | **[plainfptrI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-plainfptri)**  |
| typedef double(*)(const Input &, int) | **[plainfptrI1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-plainfptri1)**  |
| typedef double(*)(const Input &, int, int) | **[plainfptrI2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-plainfptri2)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< FSptr1 > | **[FInfo1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo1)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< FSptr2 > | **[FInfo2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo2)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< FSptr1W > | **[FInfo1W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo1w)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< FSptr2W > | **[FInfo2W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo2w)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< plainfptrM1 > | **[FInfo1M](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo1m)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< plainfptrM2 > | **[FInfo2M](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo2m)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< plainfptrI1 > | **[FInfo1I](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo1i)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< plainfptrI2 > | **[FInfo2I](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-finfo2i)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), FSptr > | **[fmap0](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap0)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap1)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap2)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), FSptrW > | **[fmap0W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap0w)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo1W](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap1w)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo2W](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap2w)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), plainfptrM > | **[fmap0_extraM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap0-extram)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo1M](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1_extraM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap1-extram)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo2M](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2_extraM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap2-extram)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), plainfptrI > | **[fmap0_extraI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap0-extrai)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo1I](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1_extraI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap1-extrai)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [FInfo2I](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2_extraI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1get_01_4/#typedef-fmap2-extrai)**  |

## Detailed Description

```
template <class DerivedSpec >
struct Gambit::MapTypes< DerivedSpec, MapTag::Get >;
```


Types needed for function pointer maps Partial specialisation for "getter" maps 

## Public Types Documentation

### typedef Model

```
typedef SpecTraits<DerivedSpec>::Model Gambit::MapTypes< DerivedSpec, MapTag::Get >::Model;
```


### typedef Input

```
typedef SpecTraits<DerivedSpec>::Input Gambit::MapTypes< DerivedSpec, MapTag::Get >::Input;
```


### typedef FSptr

```
typedef double(Model::* Gambit::MapTypes< DerivedSpec, MapTag::Get >::FSptr) (void) const;
```


### typedef FSptr1

```
typedef double(Model::* Gambit::MapTypes< DerivedSpec, MapTag::Get >::FSptr1) (int) const;
```


### typedef FSptr2

```
typedef double(Model::* Gambit::MapTypes< DerivedSpec, MapTag::Get >::FSptr2) (int, int) const;
```


### typedef FSptrW

```
typedef double(DerivedSpec::* Gambit::MapTypes< DerivedSpec, MapTag::Get >::FSptrW) (void) const;
```


### typedef FSptr1W

```
typedef double(DerivedSpec::* Gambit::MapTypes< DerivedSpec, MapTag::Get >::FSptr1W) (int) const;
```


### typedef FSptr2W

```
typedef double(DerivedSpec::* Gambit::MapTypes< DerivedSpec, MapTag::Get >::FSptr2W) (int, int) const;
```


### typedef plainfptrM

```
typedef double(* Gambit::MapTypes< DerivedSpec, MapTag::Get >::plainfptrM) (const Model &);
```


### typedef plainfptrM1

```
typedef double(* Gambit::MapTypes< DerivedSpec, MapTag::Get >::plainfptrM1) (const Model &, int);
```


### typedef plainfptrM2

```
typedef double(* Gambit::MapTypes< DerivedSpec, MapTag::Get >::plainfptrM2) (const Model &, int, int);
```


### typedef plainfptrI

```
typedef double(* Gambit::MapTypes< DerivedSpec, MapTag::Get >::plainfptrI) (const Input &);
```


### typedef plainfptrI1

```
typedef double(* Gambit::MapTypes< DerivedSpec, MapTag::Get >::plainfptrI1) (const Input &, int);
```


### typedef plainfptrI2

```
typedef double(* Gambit::MapTypes< DerivedSpec, MapTag::Get >::plainfptrI2) (const Input &, int, int);
```


### typedef FInfo1

```
typedef FcnInfo1<FSptr1> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo1;
```


### typedef FInfo2

```
typedef FcnInfo2<FSptr2> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo2;
```


### typedef FInfo1W

```
typedef FcnInfo1<FSptr1W> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo1W;
```


### typedef FInfo2W

```
typedef FcnInfo2<FSptr2W> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo2W;
```


### typedef FInfo1M

```
typedef FcnInfo1<plainfptrM1> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo1M;
```


### typedef FInfo2M

```
typedef FcnInfo2<plainfptrM2> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo2M;
```


### typedef FInfo1I

```
typedef FcnInfo1<plainfptrI1> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo1I;
```


### typedef FInfo2I

```
typedef FcnInfo2<plainfptrI2> Gambit::MapTypes< DerivedSpec, MapTag::Get >::FInfo2I;
```


### typedef fmap0

```
typedef std::map<str, FSptr> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap0;
```


### typedef fmap1

```
typedef std::map<str, FInfo1> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap1;
```


### typedef fmap2

```
typedef std::map<str, FInfo2> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap2;
```


### typedef fmap0W

```
typedef std::map<str, FSptrW> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap0W;
```


### typedef fmap1W

```
typedef std::map<str, FInfo1W> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap1W;
```


### typedef fmap2W

```
typedef std::map<str, FInfo2W> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap2W;
```


### typedef fmap0_extraM

```
typedef std::map<str, plainfptrM> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap0_extraM;
```


### typedef fmap1_extraM

```
typedef std::map<str, FInfo1M> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap1_extraM;
```


### typedef fmap2_extraM

```
typedef std::map<str, FInfo2M> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap2_extraM;
```


### typedef fmap0_extraI

```
typedef std::map<str, plainfptrI> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap0_extraI;
```


### typedef fmap1_extraI

```
typedef std::map<str, FInfo1I> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap1_extraI;
```


### typedef fmap2_extraI

```
typedef std::map<str, FInfo2I> Gambit::MapTypes< DerivedSpec, MapTag::Get >::fmap2_extraI;
```


-------------------------------

Updated on 2025-02-12 at 15:36:38 +0000