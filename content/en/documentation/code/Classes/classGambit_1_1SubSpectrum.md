---
title: "class Gambit::SubSpectrum"
description: "Virtual base class for interacting with spectrum generator output. "

---

# class Gambit::SubSpectrum



Virtual base class for interacting with spectrum generator output. 


`#include <subspectrum.hpp>`

Inherited by [Gambit::Spec< MSSMSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< DMEFTSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< DiracSingletDM_Z2SimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< MajoranaSingletDM_Z2SimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< ScalarSingletDM_Z2SimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< ScalarSingletDM_Z3SimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< VectorSingletDM_Z2SimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< SMSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< MDMSpec< MI > >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< MSSMSpec< MI > >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< QedQcdWrapper >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< SMHiggsSimpleSpec >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< ScalarSingletDM_Z2Spec< MI > >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< ScalarSingletDM_Z3Spec< MI > >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::Spec< DerivedSpec >](/documentation/code/classes/classgambit_1_1spec/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-subspectrum)**()<br>Constructors/destructors.  |
| virtual | **[~SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-subspectrum)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1subspectrum/#function-getname)**() const =0<br>Main public interface functions.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1subspectrum/#function-clone)**() const =0<br>Clone the [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object.  |
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
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>PDB getter/checker overloads.  |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>safeget functions, by Abram  |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass, const int i, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & mass, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const int PDGcode, const int context, const bool allow_new =false, const bool decouple =false)<br>PDB overloads for setters.  |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const std::pair< int, int > pdgpr, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const double value, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr, const bool allow_new =false, const bool decouple =false)<br>PDB overloads of set_override functions.  |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0<br>Getters/Setters etc.  |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const int , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const int , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const int , const int , const SpecOverrideOptions =use_overrides) const =0 |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const int , const int , const SpecOverrideOptions =use_overrides) const =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/#function-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const double , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/#function-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const double , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const int , const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/#function-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) , const double , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const int , const int ) =0 |
| virtual const std::map< int, int > & | **[PDG_translator](/documentation/code/classes/classgambit_1_1subspectrum/#function-pdg-translator)**() const<br>TODO: extra PDB overloads to handle all the one and two index cases (well all the ones that are feasible...)  |

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [OverrideMaps](/documentation/code/classes/structgambit_1_1overridemaps/) > | **[override_maps](/documentation/code/classes/classgambit_1_1subspectrum/#variable-override-maps)** <br>Map of override maps.  |

## Public Functions Documentation

### function SubSpectrum

```
inline SubSpectrum()
```

Constructors/destructors. 

### function ~SubSpectrum

```
inline virtual ~SubSpectrum()
```


### function getName

```
virtual std::string getName() const =0
```

Main public interface functions. 

**Reimplemented by**: [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname), [Gambit::Spec::getName](/documentation/code/classes/classgambit_1_1spec/#function-getname)


Get name 


### function clone

```
virtual std::unique_ptr< SubSpectrum > clone() const =0
```

Clone the [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object. 

**Reimplemented by**: [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone), [Gambit::Spec::clone](/documentation/code/classes/classgambit_1_1spec/#function-clone)


### function writeSLHAfile

```
virtual void writeSLHAfile(
    int slha_version,
    const str & filename
) const
```

Dump out spectrum information to an SLHA file (if possible) 

[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) member function definitions.

Dump out spectrum information to an SLHA file (if possible) 


### function getSLHAea

```
virtual SLHAstruct getSLHAea(
    int slha_version
) const
```

Get spectrum information in SLHAea format (if possible) 

### function add_to_SLHAea

```
inline virtual void add_to_SLHAea(
    int ,
    SLHAstruct & 
) const
```

Add spectrum information to an SLHAea object (if possible) 

**Reimplemented by**: [Gambit::SpecBit::MSSMSpec::add_to_SLHAea](/documentation/code/classes/classgambit_1_1specbit_1_1mssmspec/#function-add-to-slhaea), [Gambit::MSSMSimpleSpec::add_to_SLHAea](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-add-to-slhaea), [Gambit::SLHASimpleSpec::add_to_SLHAea](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-add-to-slhaea), [Gambit::SLHASimpleSpec::add_to_SLHAea](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-add-to-slhaea), [Gambit::SLHASimpleSpec::add_to_SLHAea](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-add-to-slhaea), [Gambit::Models::DMEFTSimpleSpec::add_to_SLHAea](/documentation/code/classes/classgambit_1_1models_1_1dmeftsimplespec/#function-add-to-slhaea), [Gambit::SpecBit::QedQcdWrapper::add_to_SLHAea](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-add-to-slhaea)


### function get_numbers_stable_particles

```
inline virtual int get_numbers_stable_particles() const
```


**Reimplemented by**: [Gambit::SpecBit::MSSMSpec::get_numbers_stable_particles](/documentation/code/classes/classgambit_1_1specbit_1_1mssmspec/#function-get-numbers-stable-particles), [Gambit::SpecBit::QedQcdWrapper::get_numbers_stable_particles](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-get-numbers-stable-particles)


There may be more than one _new_ stable particle this method will tell you how many. If more than zero you probbaly _need_ to know what model you are working on, so we don't give all stable particles 


### function hard_upper

```
inline virtual double hard_upper() const
```


**Reimplemented by**: [Gambit::SpecBit::QedQcdWrapper::hard_upper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-hard-upper)


Limits to RGE running; warning/error raised if running beyond these is attempted. If these aren't overridden in the derived class then effectively no limit on running will exist. These are public so that module writers can use them to check what the limits are. 


### function soft_upper

```
inline virtual double soft_upper() const
```


**Reimplemented by**: [Gambit::SpecBit::QedQcdWrapper::soft_upper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-soft-upper)


### function soft_lower

```
inline virtual double soft_lower() const
```


**Reimplemented by**: [Gambit::SpecBit::QedQcdWrapper::soft_lower](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-soft-lower)


### function hard_lower

```
inline virtual double hard_lower() const
```


**Reimplemented by**: [Gambit::SpecBit::QedQcdWrapper::hard_lower](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-hard-lower)


### function RunToScaleOverride

```
inline virtual void RunToScaleOverride(
    double 
)
```

Run spectrum to new scale. 

**Reimplemented by**: [Gambit::SpecBit::MDMSpec::RunToScaleOverride](/documentation/code/classes/classgambit_1_1specbit_1_1mdmspec/#function-runtoscaleoverride), [Gambit::SpecBit::MSSMSpec::RunToScaleOverride](/documentation/code/classes/classgambit_1_1specbit_1_1mssmspec/#function-runtoscaleoverride), [Gambit::SpecBit::ScalarSingletDM_Z2Spec::RunToScaleOverride](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z2spec/#function-runtoscaleoverride), [Gambit::SpecBit::ScalarSingletDM_Z3Spec::RunToScaleOverride](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/#function-runtoscaleoverride), [Gambit::SLHASimpleSpec::RunToScaleOverride](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-runtoscaleoverride), [Gambit::SLHASimpleSpec::RunToScaleOverride](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-runtoscaleoverride), [Gambit::SLHASimpleSpec::RunToScaleOverride](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-runtoscaleoverride), [Gambit::SpecBit::QedQcdWrapper::RunToScaleOverride](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-runtoscaleoverride)


Functions to be overridden in classes derived from [Spec<Derived>](/documentation/code/classes/classgambit_1_1spec/) (i.e. the final wrappers) 


### function GetScale

```
inline virtual double GetScale() const
```

Returns the renormalisation scale of parameters. 

**Reimplemented by**: [Gambit::SLHASimpleSpec::GetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-getscale), [Gambit::SLHASimpleSpec::GetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-getscale), [Gambit::SLHASimpleSpec::GetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-getscale), [Gambit::SMSimpleSpec::GetScale](/documentation/code/classes/classgambit_1_1smsimplespec/#function-getscale), [Gambit::SpecBit::MDMSpec::GetScale](/documentation/code/classes/classgambit_1_1specbit_1_1mdmspec/#function-getscale), [Gambit::SpecBit::MSSMSpec::GetScale](/documentation/code/classes/classgambit_1_1specbit_1_1mssmspec/#function-getscale), [Gambit::SpecBit::QedQcdWrapper::GetScale](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-getscale), [Gambit::SpecBit::ScalarSingletDM_Z2Spec::GetScale](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z2spec/#function-getscale), [Gambit::SpecBit::ScalarSingletDM_Z3Spec::GetScale](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/#function-getscale)


### function SetScale

```
inline virtual void SetScale(
    double 
)
```


**Reimplemented by**: [Gambit::SpecBit::MDMSpec::SetScale](/documentation/code/classes/classgambit_1_1specbit_1_1mdmspec/#function-setscale), [Gambit::SpecBit::MSSMSpec::SetScale](/documentation/code/classes/classgambit_1_1specbit_1_1mssmspec/#function-setscale), [Gambit::SpecBit::QedQcdWrapper::SetScale](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-setscale), [Gambit::SpecBit::ScalarSingletDM_Z2Spec::SetScale](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z2spec/#function-setscale), [Gambit::SpecBit::ScalarSingletDM_Z3Spec::SetScale](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/#function-setscale), [Gambit::SLHASimpleSpec::SetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-setscale), [Gambit::SLHASimpleSpec::SetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-setscale), [Gambit::SLHASimpleSpec::SetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-setscale)


Manually set the renormalisation scale of parameters somewhat dangerous to allow this but may be needed 


### function RunToScale

```
void RunToScale(
    double scale,
    const int behave =0
)
```


Run spectrum to a new scale This function is a wrapper for RunToScaleOverride which automatically checks limits and raises warnings. 


### function set_override

```
void set_override(
    const Par::Tags partype,
    const double value,
    const str & name,
    const bool allow_new =false,
    const bool decouple =false
)
```

Parameter override functions. 

### function set_override

```
void set_override(
    const Par::Tags partype,
    const double value,
    const str & name,
    const int i,
    const bool allow_new =false,
    const bool decouple =false
)
```


### function set_override

```
void set_override(
    const Par::Tags partype,
    const double value,
    const str & name,
    const int i,
    const int j,
    const bool allow_new =false
)
```


### function set_override_vector

```
void set_override_vector(
    const Par::Tags tag,
    const double value,
    const std::vector< str > & params,
    const bool allow_new =false,
    const bool decouple =false
)
```

Vector override functions. 

### function set_override_vector

```
void set_override_vector(
    const Par::Tags tag,
    const double value,
    const std::vector< str > & params,
    const std::vector< int > indices,
    const bool allow_new =false,
    const bool decouple =false
)
```


### function set_override_vector

```
void set_override_vector(
    const Par::Tags tag,
    const double value,
    const std::vector< str > & params,
    const int i,
    const bool allow_new =false,
    const bool decouple =false
)
```


### function set_override_vector

```
void set_override_vector(
    const Par::Tags tag,
    const double value,
    const str & par,
    const std::vector< int > indices,
    const bool allow_new =false,
    const bool decouple =false
)
```


### function has

```
bool has(
    const Par::Tags partype,
    const int pdg_code,
    const int context,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```

PDB getter/checker overloads. 

### function get

```
double get(
    const Par::Tags partype,
    const int pdg_code,
    const int context,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function has

```
bool has(
    const Par::Tags partype,
    const std::pair< int, int > pdgpr,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function get

```
double get(
    const Par::Tags partype,
    const std::pair< int, int > pdgpr,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function has

```
bool has(
    const Par::Tags partype,
    const std::pair< str, int > shortpr,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function get

```
double get(
    const Par::Tags partype,
    const std::pair< str, int > shortpr,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const str & mass,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```

safeget functions, by Abram 

### function safeget

```
double safeget(
    const Par::Tags partype,
    const str & mass,
    const int i,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const str & mass,
    const int i,
    const int j,
    const SpecOverrideOptions =use_overrides
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const int pdg_code,
    const int context,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const std::pair< int, int > pdgpr,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const std::pair< str, int > shortpr,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const
```


### function set_override

```
void set_override(
    const Par::Tags partype,
    const double value,
    const int PDGcode,
    const int context,
    const bool allow_new =false,
    const bool decouple =false
)
```

PDB overloads for setters. 

### function set_override

```
void set_override(
    const Par::Tags partype,
    const double value,
    const std::pair< int, int > pdgpr,
    const bool allow_new =false,
    const bool decouple =false
)
```


### function set_override

```
void set_override(
    const Par::Tags partype,
    const double value,
    const std::pair< str, int > shortpr,
    const bool allow_new =false,
    const bool decouple =false
)
```

PDB overloads of set_override functions. 

### function has

```
virtual bool has(
    const Par::Tags ,
    const str & ,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const =0
```

Getters/Setters etc. 

**Reimplemented by**: [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has)


### function get

```
virtual double get(
    const Par::Tags ,
    const str & ,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const =0
```


**Reimplemented by**: [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get)


### function has

```
virtual bool has(
    const Par::Tags ,
    const str & ,
    const int ,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const =0
```


**Reimplemented by**: [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has)


### function get

```
virtual double get(
    const Par::Tags ,
    const str & ,
    const int ,
    const SpecOverrideOptions =use_overrides,
    const SafeBool check_antiparticle =SafeBool(true)
) const =0
```


**Reimplemented by**: [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get)


### function has

```
virtual bool has(
    const Par::Tags ,
    const str & ,
    const int ,
    const int ,
    const SpecOverrideOptions =use_overrides
) const =0
```


**Reimplemented by**: [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has), [Gambit::Spec::has](/documentation/code/classes/classgambit_1_1spec/#function-has)


### function get

```
virtual double get(
    const Par::Tags ,
    const str & ,
    const int ,
    const int ,
    const SpecOverrideOptions =use_overrides
) const =0
```


**Reimplemented by**: [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get), [Gambit::Spec::get](/documentation/code/classes/classgambit_1_1spec/#function-get)


### function set

```
virtual void set(
    const Par::Tags ,
    const double ,
    const str & ,
    const SafeBool check_antiparticle =SafeBool(true)
) =0
```


**Reimplemented by**: [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set)


### function set

```
virtual void set(
    const Par::Tags ,
    const double ,
    const str & ,
    const int ,
    const SafeBool check_antiparticle =SafeBool(true)
) =0
```


**Reimplemented by**: [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set)


### function set

```
virtual void set(
    const Par::Tags ,
    const double ,
    const str & ,
    const int ,
    const int 
) =0
```


**Reimplemented by**: [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set), [Gambit::Spec::set](/documentation/code/classes/classgambit_1_1spec/#function-set)


### function PDG_translator

```
inline virtual const std::map< int, int > & PDG_translator() const
```

TODO: extra PDB overloads to handle all the one and two index cases (well all the ones that are feasible...) 

**Reimplemented by**: [Gambit::MSSMSimpleSpec::PDG_translator](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-pdg-translator)


PDG code translation map, for special cases where an SLHA file has been read in and the PDG codes changed. 


## Protected Attributes Documentation

### variable override_maps

```
std::map< Par::Tags, OverrideMaps > override_maps;
```

Map of override maps. 

-------------------------------

Updated on 2022-09-08 at 00:43:00 +0000