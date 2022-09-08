---
title: "struct Gambit::MapTypes< DerivedSpec, MapTag::Set >"

description: "[No description available]"

---

# struct Gambit::MapTypes< DerivedSpec, MapTag::Set >



[No description available] [More...](#detailed-description)


`#include <spectrum_helpers.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< DerivedSpec >::Model | **[Model](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-model)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< DerivedSpec >::Input | **[Input](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-input)**  |
| typedef void(Model::*)(double) | **[FSptr](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fsptr)**  |
| typedef void(Model::*)(int, const double &) | **[FSptr1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fsptr1)**  |
| typedef void(Model::*)(int, int, const double &) | **[FSptr2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fsptr2)**  |
| typedef void(DerivedSpec::*)(double) | **[FSptrW](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fsptrw)**  |
| typedef void(DerivedSpec::*)(double, int) | **[FSptr1W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fsptr1w)**  |
| typedef void(DerivedSpec::*)(double, int, int) | **[FSptr2W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fsptr2w)**  |
| typedef void(*)(Model &, double) | **[plainfptrM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-plainfptrm)**  |
| typedef void(*)(Model &, double, int) | **[plainfptrM1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-plainfptrm1)**  |
| typedef void(*)(Model &, double, int, int) | **[plainfptrM2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-plainfptrm2)**  |
| typedef void(*)(Input &, double) | **[plainfptrI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-plainfptri)**  |
| typedef void(*)(Input &, double, int) | **[plainfptrI1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-plainfptri1)**  |
| typedef void(*)(Input &, double, int, int) | **[plainfptrI2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-plainfptri2)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< FSptr1 > | **[FInfo1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo1)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< FSptr2 > | **[FInfo2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo2)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< FSptr1W > | **[FInfo1W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo1w)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< FSptr2W > | **[FInfo2W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo2w)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< plainfptrM1 > | **[FInfo1M](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo1m)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< plainfptrM2 > | **[FInfo2M](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo2m)**  |
| typedef [FcnInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/)< plainfptrI1 > | **[FInfo1I](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo1i)**  |
| typedef [FcnInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/)< plainfptrI2 > | **[FInfo2I](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-finfo2i)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), FSptr > | **[fmap0](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap0)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo1](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap1)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo2](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap2)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), FSptrW > | **[fmap0W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap0w)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo1W](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap1w)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo2W](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2W](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap2w)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), plainfptrM > | **[fmap0_extraM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap0-extram)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo1M](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1_extraM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap1-extram)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo2M](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2_extraM](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap2-extram)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), plainfptrI > | **[fmap0_extraI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap0-extrai)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo1I](/documentation/code/classes/structgambit_1_1fcninfo1/) > | **[fmap1_extraI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap1-extrai)**  |
| typedef std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), [FInfo2I](/documentation/code/classes/structgambit_1_1fcninfo2/) > | **[fmap2_extraI](/documentation/code/classes/structgambit_1_1maptypes_3_01derivedspec_00_01maptag_1_1set_01_4/#typedef-gambitmaptypes-derivedspec-maptagset-fmap2-extrai)**  |

## Detailed Description

```
template <class DerivedSpec >
struct Gambit::MapTypes< DerivedSpec, MapTag::Set >;
```


Types needed for function pointer maps Partial specialisation for "setter" maps 

## Public Types Documentation

### typedef Model

```
typedef SpecTraits<DerivedSpec>::Model Gambit::MapTypes< DerivedSpec, MapTag::Set >::Model;
```


### typedef Input

```
typedef SpecTraits<DerivedSpec>::Input Gambit::MapTypes< DerivedSpec, MapTag::Set >::Input;
```


### typedef FSptr

```
typedef void(Model::* Gambit::MapTypes< DerivedSpec, MapTag::Set >::FSptr) (double);
```


### typedef FSptr1

```
typedef void(Model::* Gambit::MapTypes< DerivedSpec, MapTag::Set >::FSptr1) (int, const double &);
```


### typedef FSptr2

```
typedef void(Model::* Gambit::MapTypes< DerivedSpec, MapTag::Set >::FSptr2) (int, int, const double &);
```


### typedef FSptrW

```
typedef void(DerivedSpec::* Gambit::MapTypes< DerivedSpec, MapTag::Set >::FSptrW) (double);
```


### typedef FSptr1W

```
typedef void(DerivedSpec::* Gambit::MapTypes< DerivedSpec, MapTag::Set >::FSptr1W) (double, int);
```


### typedef FSptr2W

```
typedef void(DerivedSpec::* Gambit::MapTypes< DerivedSpec, MapTag::Set >::FSptr2W) (double, int, int);
```


### typedef plainfptrM

```
typedef void(* Gambit::MapTypes< DerivedSpec, MapTag::Set >::plainfptrM) (Model &, double);
```


### typedef plainfptrM1

```
typedef void(* Gambit::MapTypes< DerivedSpec, MapTag::Set >::plainfptrM1) (Model &, double, int);
```


### typedef plainfptrM2

```
typedef void(* Gambit::MapTypes< DerivedSpec, MapTag::Set >::plainfptrM2) (Model &, double, int, int);
```


### typedef plainfptrI

```
typedef void(* Gambit::MapTypes< DerivedSpec, MapTag::Set >::plainfptrI) (Input &, double);
```


### typedef plainfptrI1

```
typedef void(* Gambit::MapTypes< DerivedSpec, MapTag::Set >::plainfptrI1) (Input &, double, int);
```


### typedef plainfptrI2

```
typedef void(* Gambit::MapTypes< DerivedSpec, MapTag::Set >::plainfptrI2) (Input &, double, int, int);
```


### typedef FInfo1

```
typedef FcnInfo1<FSptr1> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo1;
```


### typedef FInfo2

```
typedef FcnInfo2<FSptr2> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo2;
```


### typedef FInfo1W

```
typedef FcnInfo1<FSptr1W> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo1W;
```


### typedef FInfo2W

```
typedef FcnInfo2<FSptr2W> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo2W;
```


### typedef FInfo1M

```
typedef FcnInfo1<plainfptrM1> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo1M;
```


### typedef FInfo2M

```
typedef FcnInfo2<plainfptrM2> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo2M;
```


### typedef FInfo1I

```
typedef FcnInfo1<plainfptrI1> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo1I;
```


### typedef FInfo2I

```
typedef FcnInfo2<plainfptrI2> Gambit::MapTypes< DerivedSpec, MapTag::Set >::FInfo2I;
```


### typedef fmap0

```
typedef std::map<str, FSptr> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap0;
```


### typedef fmap1

```
typedef std::map<str, FInfo1> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap1;
```


### typedef fmap2

```
typedef std::map<str, FInfo2> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap2;
```


### typedef fmap0W

```
typedef std::map<str, FSptrW> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap0W;
```


### typedef fmap1W

```
typedef std::map<str, FInfo1W> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap1W;
```


### typedef fmap2W

```
typedef std::map<str, FInfo2W> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap2W;
```


### typedef fmap0_extraM

```
typedef std::map<str, plainfptrM> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap0_extraM;
```


### typedef fmap1_extraM

```
typedef std::map<str, FInfo1M> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap1_extraM;
```


### typedef fmap2_extraM

```
typedef std::map<str, FInfo2M> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap2_extraM;
```


### typedef fmap0_extraI

```
typedef std::map<str, plainfptrI> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap0_extraI;
```


### typedef fmap1_extraI

```
typedef std::map<str, FInfo1I> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap1_extraI;
```


### typedef fmap2_extraI

```
typedef std::map<str, FInfo2I> Gambit::MapTypes< DerivedSpec, MapTag::Set >::fmap2_extraI;
```


-------------------------------

Updated on 2022-09-08 at 01:48:54 +0000