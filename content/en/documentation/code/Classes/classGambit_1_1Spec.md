---
title: "class Gambit::Spec"
description: "Need to forward declare [Spec]() class. "

---

# class Gambit::Spec



Need to forward declare [Spec]() class.  [More...](#detailed-description)

Inherits from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef DerivedSpec | **[D](/documentation/code/classes/classgambit_1_1spec/#typedef-d)**  |
| typedef [Spec](/documentation/code/classes/classgambit_1_1spec/)< D > | **[Self](/documentation/code/classes/classgambit_1_1spec/#typedef-self)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Contents | **[Contents](/documentation/code/classes/classgambit_1_1spec/#typedef-contents)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Model | **[Model](/documentation/code/classes/classgambit_1_1spec/#typedef-model)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Input | **[Input](/documentation/code/classes/classgambit_1_1spec/#typedef-input)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< D, [MapTag::Get](/documentation/code/classes/structgambit_1_1maptag_1_1get/) > | **[MTget](/documentation/code/classes/classgambit_1_1spec/#typedef-mtget)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< D, [MapTag::Set](/documentation/code/classes/structgambit_1_1maptag_1_1set/) > | **[MTset](/documentation/code/classes/classgambit_1_1spec/#typedef-mtset)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTget](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gettermaps)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTset](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[SetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-settermaps)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| Model & | **[get_Model](/documentation/code/classes/classgambit_1_1spec/#function-get-model)**() |
| Input & | **[get_Input](/documentation/code/classes/classgambit_1_1spec/#function-get-input)**() |
| const Model & | **[get_Model](/documentation/code/classes/classgambit_1_1spec/#function-get-model)**() const |
| const Input & | **[get_Input](/documentation/code/classes/classgambit_1_1spec/#function-get-input)**() const |
| Model & | **[model](/documentation/code/classes/classgambit_1_1spec/#function-model)**()<br>Get model object on which to call function pointers.  |
| const Model & | **[model](/documentation/code/classes/classgambit_1_1spec/#function-model)**() const<br>Return it as const if we are a const object.  |
| Input & | **[input](/documentation/code/classes/classgambit_1_1spec/#function-input)**()<br>Get struct containing any extra data input on [SubSpectrum]() object creation.  |
| const Input & | **[input](/documentation/code/classes/classgambit_1_1spec/#function-input)**() const<br>Return it as const if we are a const object.  |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>[Spec](/documentation/code/classes/classgambit_1_1spec/) member function definitions.  |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/#function-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/#function-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/#function-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const int j) |
| const std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTget](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[fill_getter_maps](/documentation/code/classes/classgambit_1_1spec/#function-fill-getter-maps)**() |
| const std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTset](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[fill_setter_maps](/documentation/code/classes/classgambit_1_1spec/#function-fill-setter-maps)**() |
| int | **[index_offset](/documentation/code/classes/classgambit_1_1spec/#function-index-offset)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1spec/#function-getname)**() const<br>Main public interface functions.  |
| | **[Spec](/documentation/code/classes/classgambit_1_1spec/#function-spec)**() |
| virtual | **[~Spec](/documentation/code/classes/classgambit_1_1spec/#function-spec)**()<br>Virtual destructor.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1spec/#function-clone)**() const |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| [DummyModel](/documentation/code/classes/classgambit_1_1dummymodel/) | **[dummymodel](/documentation/code/classes/classgambit_1_1spec/#variable-dummymodel)**  |
| [DummyInput](/documentation/code/classes/classgambit_1_1dummyinput/) | **[dummyinput](/documentation/code/classes/classgambit_1_1spec/#variable-dummyinput)**  |
| const [GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gettermaps) | **[getter_maps](/documentation/code/classes/classgambit_1_1spec/#variable-getter-maps)** <br>Initialise maps (uses filler overrides from DerivedSpec if defined)  |
| const SetterMaps | **[setter_maps](/documentation/code/classes/classgambit_1_1spec/#variable-setter-maps)**  |

## Friends

|                | Name           |
| -------------- | -------------- |
| class | **[FptrFinder](/documentation/code/classes/classgambit_1_1spec/#friend-fptrfinder)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| | **[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-subspectrum)**()<br>Constructors/destructors.  |
| virtual | **[~SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-subspectrum)**() |
| virtual void | **[writeSLHAfile](/documentation/code/classes/classgambit_1_1subspectrum/#function-writeslhafile)**(int slha_version, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & filename) const<br>Dump out spectrum information to an SLHA file (if possible)  |
| virtual [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) | **[getSLHAea](/documentation/code/classes/classgambit_1_1subspectrum/#function-getslhaea)**(int slha_version) const<br>Get spectrum information in SLHAea format (if possible)  |
| virtual void | **[add_to_SLHAea](/documentation/code/classes/classgambit_1_1subspectrum/#function-add-to-slhaea)**(int , [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & ) const<br>Add spectrum information to an SLHAea object (if possible)  |
| virtual int | **[get_numbers_stable_particles](/documentation/code/classes/classgambit_1_1subspectrum/#function-get-numbers-stable-particles)**() const |
| virtual double | **[hard_upper](/documentation/code/classes/classgambit_1_1subspectrum/#function-hard-upper)**() const |
| virtual double | **[soft_upper](/documentation/code/classes/classgambit_1_1subspectrum/#function-soft-upper)**() const |
| virtual double | **[soft_lower](/documentation/code/classes/classgambit_1_1subspectrum/#function-soft-lower)**() const |
| virtual double | **[hard_lower](/documentation/code/classes/classgambit_1_1subspectrum/#function-hard-lower)**() const |
| virtual void | **[RunToScaleOverride](/documentation/code/classes/classgambit_1_1subspectrum/#function-runtoscaleoverride)**(double )<br>Run spectrum to new scale.  |
| virtual double | **[GetScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-getscale)**() const<br>Returns the renormalisation scale of parameters.  |
| virtual void | **[SetScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-setscale)**(double ) |
| void | **[RunToScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-runtoscale)**(double scale, const int behave =0) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const bool allow_new =false, const bool decouple =false)<br>Parameter override functions.  |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & name, const int i, const int j, const bool allow_new =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & params, const bool allow_new =false, const bool decouple =false)<br>Vector override functions.  |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & params, const std::vector< int > indices, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > & params, const int i, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & par, const std::vector< int > indices, const bool allow_new =false, const bool decouple =false) |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>safeget functions, by Abram  |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass, const int i, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const int PDGcode, const int context, const bool allow_new =false, const bool decouple =false)<br>PDB overloads for setters.  |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const std::pair< int, int > pdgpr, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr, const bool allow_new =false, const bool decouple =false)<br>PDB overloads of set_override functions.  |
| virtual const std::map< int, int > & | **[PDG_translator](/documentation/code/classes/classgambit_1_1subspectrum/#function-pdg-translator)**() const<br>TODO: extra PDB overloads to handle all the one and two index cases (well all the ones that are feasible...)  |

**Protected Attributes inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [OverrideMaps](/documentation/code/classes/structgambit_1_1overridemaps/) > | **[override_maps](/documentation/code/classes/classgambit_1_1subspectrum/#variable-override-maps)** <br>Map of override maps.  |


## Detailed Description

```
template <class DerivedSpec >
class Gambit::Spec;
```

Need to forward declare [Spec]() class. 
## Public Types Documentation

### typedef D

```
typedef DerivedSpec Gambit::Spec< DerivedSpec >::D;
```


### typedef Self

```
typedef Spec<D> Gambit::Spec< DerivedSpec >::Self;
```


### typedef Contents

```
typedef SpecTraits<D>::Contents Gambit::Spec< DerivedSpec >::Contents;
```


Note: Wrapper need to define a specialisation of [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/), which typedefs Model and Input. "Grab" these typedefs here to simplify notation 


### typedef Model

```
typedef SpecTraits<D>::Model Gambit::Spec< DerivedSpec >::Model;
```


### typedef Input

```
typedef SpecTraits<D>::Input Gambit::Spec< DerivedSpec >::Input;
```


### typedef MTget

```
typedef MapTypes<D,MapTag::Get> Gambit::Spec< DerivedSpec >::MTget;
```


### typedef MTset

```
typedef MapTypes<D,MapTag::Set> Gambit::Spec< DerivedSpec >::MTset;
```


### typedef GetterMaps

```
typedef std::map<Par::Tags,MapCollection<MTget> > Gambit::Spec< DerivedSpec >::GetterMaps;
```


Will need a map of map collections for both the getters and setters, containing the map collections for the permitted parameter types 


### typedef SetterMaps

```
typedef std::map<Par::Tags,MapCollection<MTset> > Gambit::Spec< DerivedSpec >::SetterMaps;
```


## Public Functions Documentation

### function get_Model

```
inline Model & get_Model()
```


### function get_Input

```
inline Input & get_Input()
```


### function get_Model

```
inline const Model & get_Model() const
```


### function get_Input

```
inline const Input & get_Input() const
```


### function model

```
inline Model & model()
```

Get model object on which to call function pointers. 

### function model

```
inline const Model & model() const
```

Return it as const if we are a const object. 

### function input

```
inline Input & input()
```

Get struct containing any extra data input on [SubSpectrum]() object creation. 

### function input

```
inline const Input & input() const
```

Return it as const if we are a const object. 

### function has

```
virtual bool has(
    const Par::Tags partype,
    const str & name,
    const SpecOverrideOptions =use_overrides,
    const SafeBool =SafeBool(true)
) const
```

[Spec](/documentation/code/classes/classgambit_1_1spec/) member function definitions. 

**Reimplements**: [Gambit::SubSpectrum::has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)


No indices 


TODO: Could avoid dismantling the [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/) struct by just letting the [SetMaps](/documentation/code/classes/classgambit_1_1setmaps/) class do it, but one step at a time... Could also reduce duplication between getter and checker functions by making the 'has' function take an optional argument to return an [FptrFinder](/documentation/code/classes/classgambit_1_1fptrfinder/), which can then just be used to call the found function.


### function get

```
virtual double get(
    const Par::Tags partype,
    const str & name,
    const SpecOverrideOptions =use_overrides,
    const SafeBool =SafeBool(true)
) const
```


**Reimplements**: [Gambit::SubSpectrum::get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)


### function set

```
virtual void set(
    const Par::Tags partype,
    const double set_value,
    const str & name,
    const SafeBool =SafeBool(true)
)
```


**Reimplements**: [Gambit::SubSpectrum::set](/documentation/code/classes/classgambit_1_1subspectrum/#function-set)


### function has

```
virtual bool has(
    const Par::Tags partype,
    const str & name,
    const int i,
    const SpecOverrideOptions =use_overrides,
    const SafeBool =SafeBool(true)
) const
```


**Reimplements**: [Gambit::SubSpectrum::has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)


One index 


### function get

```
virtual double get(
    const Par::Tags partype,
    const str & name,
    const int i,
    const SpecOverrideOptions =use_overrides,
    const SafeBool =SafeBool(true)
) const
```


**Reimplements**: [Gambit::SubSpectrum::get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)


### function set

```
virtual void set(
    const Par::Tags partype,
    const double set_value,
    const str & name,
    const int i,
    const SafeBool =SafeBool(true)
)
```


**Reimplements**: [Gambit::SubSpectrum::set](/documentation/code/classes/classgambit_1_1subspectrum/#function-set)


### function has

```
virtual bool has(
    const Par::Tags partype,
    const str & name,
    const int i,
    const int j,
    const SpecOverrideOptions =use_overrides
) const
```


**Reimplements**: [Gambit::SubSpectrum::has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)


Two indices 


### function get

```
virtual double get(
    const Par::Tags partype,
    const str & name,
    const int i,
    const int j,
    const SpecOverrideOptions =use_overrides
) const
```


**Reimplements**: [Gambit::SubSpectrum::get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)


### function set

```
virtual void set(
    const Par::Tags partype,
    const double set_value,
    const str & name,
    const int i,
    const int j
)
```


**Reimplements**: [Gambit::SubSpectrum::set](/documentation/code/classes/classgambit_1_1subspectrum/#function-set)


### function fill_getter_maps

```
static inline const std::map< Par::Tags, MapCollection< MTget > > fill_getter_maps()
```


Default (empty) map filler functions Override as needed in derived classes 


### function fill_setter_maps

```
static inline const std::map< Par::Tags, MapCollection< MTset > > fill_setter_maps()
```


### function index_offset

```
static inline int index_offset()
```


Get integer offset convention used by internal model class (needed by getters which take indices) By default assume no offset. Overrride as needed in derived class. 


### function getName

```
inline virtual std::string getName() const
```

Main public interface functions. 

**Reimplements**: [Gambit::SubSpectrum::getName](/documentation/code/classes/classgambit_1_1subspectrum/#function-getname)


Get name 


### function Spec

```
inline Spec()
```


Constructor This uses the "Contents" class to verify (once, not every construction) that this wrapper provides all the basic functionality that it is supposed to. 


### function ~Spec

```
inline virtual ~Spec()
```

Virtual destructor. 

### function clone

```
inline virtual std::unique_ptr< SubSpectrum > clone() const
```


**Reimplements**: [Gambit::SubSpectrum::clone](/documentation/code/classes/classgambit_1_1subspectrum/#function-clone)


CRTP-style polymorphic clone function Now derived classes will not need to re-implement the clone function. 


## Public Attributes Documentation

### variable dummymodel

```
DummyModel dummymodel;
```


Getters for wrapped data; be sure to define the 'get_Model' and 'get_Input' functions in the wrappers (with public access) Might as well use static polymorphism rather than virtual functions, since we are using the CRTP already anyway. Default "null" versions of get_Model and get_Input, to be used if wrapper does not override them. 


### variable dummyinput

```
DummyInput dummyinput;
```


### variable getter_maps

```
static const GetterMaps getter_maps;
```

Initialise maps (uses filler overrides from DerivedSpec if defined) 

### variable setter_maps

```
static const SetterMaps setter_maps;
```


## Friends

### friend FptrFinder

```
friend class FptrFinder(
    FptrFinder 
);
```


-------------------------------

Updated on 2024-07-18 at 13:53:30 +0000