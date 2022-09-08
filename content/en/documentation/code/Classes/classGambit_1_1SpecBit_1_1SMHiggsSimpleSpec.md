---
title: "class Gambit::SpecBit::SMHiggsSimpleSpec"
description: "[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) wrapper class for the SM Higgs sector. "

---

# class Gambit::SpecBit::SMHiggsSimpleSpec



[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) wrapper class for the SM Higgs sector. 


`#include <SMHiggsSimpleSpec.hpp>`

Inherits from [Gambit::Spec< SMHiggsSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SMHiggsSimpleSpec](/documentation/code/classes/classgambit_1_1specbit_1_1smhiggssimplespec/)**(const Model & m)<br>Constructor.  |
| Model & | **[get_Model](/documentation/code/classes/classgambit_1_1specbit_1_1smhiggssimplespec/)**() |
| Input & | **[get_Input](/documentation/code/classes/classgambit_1_1specbit_1_1smhiggssimplespec/)**() |
| const Model & | **[get_Model](/documentation/code/classes/classgambit_1_1specbit_1_1smhiggssimplespec/)**() const |
| const Input & | **[get_Input](/documentation/code/classes/classgambit_1_1specbit_1_1smhiggssimplespec/)**() const |
| [GetterMaps](/documentation/code/classes/classgambit_1_1spec/) | **[fill_getter_maps](/documentation/code/classes/classgambit_1_1specbit_1_1smhiggssimplespec/)**()<br>Definitions of map fillers.  |

## Additional inherited members

**Public Types inherited from [Gambit::Spec< SMHiggsSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| typedef DerivedSpec | **[D](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef [Spec](/documentation/code/classes/classgambit_1_1spec/)< D > | **[Self](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Contents | **[Contents](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Model | **[Model](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Input | **[Input](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< D, [MapTag::Get](/documentation/code/classes/structgambit_1_1maptag_1_1get/) > | **[MTget](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< D, [MapTag::Set](/documentation/code/classes/structgambit_1_1maptag_1_1set/) > | **[MTset](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTget](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[GetterMaps](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTset](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[SetterMaps](/documentation/code/classes/classgambit_1_1spec/)**  |

**Public Functions inherited from [Gambit::Spec< SMHiggsSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>[Spec](/documentation/code/classes/classgambit_1_1spec/) member function definitions.  |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const int j) |
| const std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTset](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[fill_setter_maps](/documentation/code/classes/classgambit_1_1spec/)**() |
| int | **[index_offset](/documentation/code/classes/classgambit_1_1spec/)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1spec/)**() const<br>Main public interface functions.  |
| | **[Spec](/documentation/code/classes/classgambit_1_1spec/)**() |
| virtual | **[~Spec](/documentation/code/classes/classgambit_1_1spec/)**()<br>Virtual destructor.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1spec/)**() const |

**Public Attributes inherited from [Gambit::Spec< SMHiggsSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| [DummyModel](/documentation/code/classes/classgambit_1_1dummymodel/) | **[dummymodel](/documentation/code/classes/classgambit_1_1spec/)**  |
| [DummyInput](/documentation/code/classes/classgambit_1_1dummyinput/) | **[dummyinput](/documentation/code/classes/classgambit_1_1spec/)**  |
| const [GetterMaps](/documentation/code/classes/classgambit_1_1spec/) | **[getter_maps](/documentation/code/classes/classgambit_1_1spec/)** <br>Initialise maps (uses filler overrides from DerivedSpec if defined)  |
| const SetterMaps | **[setter_maps](/documentation/code/classes/classgambit_1_1spec/)**  |

**Friends inherited from [Gambit::Spec< SMHiggsSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| class | **[FptrFinder](/documentation/code/classes/classgambit_1_1spec/)**  |

**Public Functions inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| | **[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**()<br>Constructors/destructors.  |
| virtual | **[~SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1subspectrum/)**() const =0<br>Main public interface functions.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1subspectrum/)**() const =0<br>Clone the [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object.  |
| virtual void | **[writeSLHAfile](/documentation/code/classes/classgambit_1_1subspectrum/)**(int slha_version, const [str](/documentation/code/namespaces/namespacegambit/) & filename) const<br>Dump out spectrum information to an SLHA file (if possible)  |
| virtual [SLHAstruct](/documentation/code/namespaces/namespacegambit/) | **[getSLHAea](/documentation/code/classes/classgambit_1_1subspectrum/)**(int slha_version) const<br>Get spectrum information in SLHAea format (if possible)  |
| virtual void | **[add_to_SLHAea](/documentation/code/classes/classgambit_1_1subspectrum/)**(int , [SLHAstruct](/documentation/code/namespaces/namespacegambit/) & ) const<br>Add spectrum information to an SLHAea object (if possible)  |
| virtual int | **[get_numbers_stable_particles](/documentation/code/classes/classgambit_1_1subspectrum/)**() const |
| virtual double | **[hard_upper](/documentation/code/classes/classgambit_1_1subspectrum/)**() const |
| virtual double | **[soft_upper](/documentation/code/classes/classgambit_1_1subspectrum/)**() const |
| virtual double | **[soft_lower](/documentation/code/classes/classgambit_1_1subspectrum/)**() const |
| virtual double | **[hard_lower](/documentation/code/classes/classgambit_1_1subspectrum/)**() const |
| virtual void | **[RunToScaleOverride](/documentation/code/classes/classgambit_1_1subspectrum/)**(double )<br>Run spectrum to new scale.  |
| virtual double | **[GetScale](/documentation/code/classes/classgambit_1_1subspectrum/)**() const<br>Returns the renormalisation scale of parameters.  |
| virtual void | **[SetScale](/documentation/code/classes/classgambit_1_1subspectrum/)**(double ) |
| void | **[RunToScale](/documentation/code/classes/classgambit_1_1subspectrum/)**(double scale, const int behave =0) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const bool allow_new =false, const bool decouple =false)<br>Parameter override functions.  |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const int j, const bool allow_new =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & params, const bool allow_new =false, const bool decouple =false)<br>Vector override functions.  |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & params, const std::vector< int > indices, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/) > & params, const int i, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) tag, const double value, const [str](/documentation/code/namespaces/namespacegambit/) & par, const std::vector< int > indices, const bool allow_new =false, const bool decouple =false) |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>PDB getter/checker overloads.  |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & mass, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>safeget functions, by Abram  |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & mass, const int i, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & mass, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double value, const int PDGcode, const int context, const bool allow_new =false, const bool decouple =false)<br>PDB overloads for setters.  |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double value, const std::pair< int, int > pdgpr, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double value, const std::pair< [str](/documentation/code/namespaces/namespacegambit/), int > shortpr, const bool allow_new =false, const bool decouple =false)<br>PDB overloads of set_override functions.  |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const [str](/documentation/code/namespaces/namespacegambit/) & , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0<br>Getters/Setters etc.  |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const [str](/documentation/code/namespaces/namespacegambit/) & , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const [str](/documentation/code/namespaces/namespacegambit/) & , const int , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const [str](/documentation/code/namespaces/namespacegambit/) & , const int , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const [str](/documentation/code/namespaces/namespacegambit/) & , const int , const int , const SpecOverrideOptions =use_overrides) const =0 |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const [str](/documentation/code/namespaces/namespacegambit/) & , const int , const int , const SpecOverrideOptions =use_overrides) const =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const double , const [str](/documentation/code/namespaces/namespacegambit/) & , const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const double , const [str](/documentation/code/namespaces/namespacegambit/) & , const int , const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) , const double , const [str](/documentation/code/namespaces/namespacegambit/) & , const int , const int ) =0 |
| virtual const std::map< int, int > & | **[PDG_translator](/documentation/code/classes/classgambit_1_1subspectrum/)**() const<br>TODO: extra PDB overloads to handle all the one and two index cases (well all the ones that are feasible...)  |

**Protected Attributes inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/), [OverrideMaps](/documentation/code/classes/structgambit_1_1overridemaps/) > | **[override_maps](/documentation/code/classes/classgambit_1_1subspectrum/)** <br>Map of override maps.  |


## Public Functions Documentation

### function SMHiggsSimpleSpec

```
inline SMHiggsSimpleSpec(
    const Model & m
)
```

Constructor. 

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


### function fill_getter_maps

```
static inline GetterMaps fill_getter_maps()
```

Definitions of map fillers. 

Map fillers Used to initialise maps in the RunparDer and PhysDer classes (specialisations created and stored automatically by [Spec<QedQcdWrapper>](/documentation/code/classes/classgambit_1_1spec/)) 


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000