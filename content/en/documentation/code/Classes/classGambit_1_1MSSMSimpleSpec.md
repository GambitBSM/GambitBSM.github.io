---
title: "class Gambit::MSSMSimpleSpec"
description: "MSSM specialisation of SLHAea object wrapper version of [SubSpectrum]() class. "

---

# class Gambit::MSSMSimpleSpec



MSSM specialisation of SLHAea object wrapper version of [SubSpectrum]() class. 


`#include <MSSMSimpleSpec.hpp>`

Inherits from [Gambit::SLHASimpleSpec< MSSMSimpleSpec >](/documentation/code/classes/classgambit_1_1slhasimplespec/), [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MSSMSimpleSpec](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-mssmsimplespec)**(double uncert =0.03)<br>Member functions for [MSSMSimpleSpec](/documentation/code/classes/classgambit_1_1mssmsimplespec/) class.  |
| | **[MSSMSimpleSpec](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-mssmsimplespec)**(const [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) & input, double uncert =0.03)<br>Constructor via SLHAea object.  |
| | **[MSSMSimpleSpec](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-mssmsimplespec)**(const [MSSMSimpleSpec](/documentation/code/classes/classgambit_1_1mssmsimplespec/) & other, double uncert =0.03)<br>Copy constructor: needed by clone function.  |
| virtual | **[~MSSMSimpleSpec](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-mssmsimplespec)**()<br>Destructor.  |
| virtual int | **[get_index_offset](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-get-index-offset)**() const<br>Ofset from user-input indices (user assumes 1,2,3 indexed, e.g. use offset=-1 for zero-indexing)  |
| virtual void | **[add_to_SLHAea](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-add-to-slhaea)**(int slha_version, SLHAea::Coll & slha) const<br>Retrieve SLHAea object.  |
| virtual const std::map< int, int > & | **[PDG_translator](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-pdg-translator)**() const<br>Retrieve the PDG translation map.  |
| [GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gettermaps) | **[fill_getter_maps](/documentation/code/classes/classgambit_1_1mssmsimplespec/#function-fill-getter-maps)**() |

## Additional inherited members

**Public Types inherited from [Gambit::SLHASimpleSpec< MSSMSimpleSpec >](/documentation/code/classes/classgambit_1_1slhasimplespec/)**

|                | Name           |
| -------------- | -------------- |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< Derived >::Model | **[Model](/documentation/code/classes/classgambit_1_1slhasimplespec/#typedef-model)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< Derived >::Input | **[Input](/documentation/code/classes/classgambit_1_1slhasimplespec/#typedef-input)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< Derived, [MapTag::Get](/documentation/code/classes/structgambit_1_1maptag_1_1get/) > | **[MTget](/documentation/code/classes/classgambit_1_1slhasimplespec/#typedef-mtget)**  |

**Public Functions inherited from [Gambit::SLHASimpleSpec< MSSMSimpleSpec >](/documentation/code/classes/classgambit_1_1slhasimplespec/)**

|                | Name           |
| -------------- | -------------- |
| virtual double | **[GetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-getscale)**() const<br>(using bass class version of getSLHAea)  |
| virtual void | **[SetScale](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-setscale)**(double ) |
| virtual void | **[RunToScaleOverride](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-runtoscaleoverride)**(double )<br>Run spectrum to new scale.  |
| | **[SLHASimpleSpec](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-slhasimplespec)**() |
| | **[SLHASimpleSpec](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-slhasimplespec)**(const SLHAea::Coll & input_slha) |
| virtual | **[~SLHASimpleSpec](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-slhasimplespec)**() |
| Model & | **[get_Model](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-get-model)**() |
| Input & | **[get_Input](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-get-input)**() |
| const Model & | **[get_Model](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-get-model)**() const |
| const Input & | **[get_Input](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-get-input)**() const |

**Protected Attributes inherited from [Gambit::SLHASimpleSpec< MSSMSimpleSpec >](/documentation/code/classes/classgambit_1_1slhasimplespec/)**

|                | Name           |
| -------------- | -------------- |
| Model | **[slhawrap](/documentation/code/classes/classgambit_1_1slhasimplespec/#variable-slhawrap)**  |
| Input | **[dummyinput](/documentation/code/classes/classgambit_1_1slhasimplespec/#variable-dummyinput)**  |

**Public Types inherited from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/)**

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

**Public Functions inherited from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/)**

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
| const std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTset](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[fill_setter_maps](/documentation/code/classes/classgambit_1_1spec/#function-fill-setter-maps)**() |
| int | **[index_offset](/documentation/code/classes/classgambit_1_1spec/#function-index-offset)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1spec/#function-getname)**() const<br>Main public interface functions.  |
| | **[Spec](/documentation/code/classes/classgambit_1_1spec/#function-spec)**() |
| virtual | **[~Spec](/documentation/code/classes/classgambit_1_1spec/#function-spec)**()<br>Virtual destructor.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1spec/#function-clone)**() const |

**Public Attributes inherited from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| [DummyModel](/documentation/code/classes/classgambit_1_1dummymodel/) | **[dummymodel](/documentation/code/classes/classgambit_1_1spec/#variable-dummymodel)**  |
| [DummyInput](/documentation/code/classes/classgambit_1_1dummyinput/) | **[dummyinput](/documentation/code/classes/classgambit_1_1spec/#variable-dummyinput)**  |
| const [GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gettermaps) | **[getter_maps](/documentation/code/classes/classgambit_1_1spec/#variable-getter-maps)** <br>Initialise maps (uses filler overrides from DerivedSpec if defined)  |
| const SetterMaps | **[setter_maps](/documentation/code/classes/classgambit_1_1spec/#variable-setter-maps)**  |

**Friends inherited from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| class | **[FptrFinder](/documentation/code/classes/classgambit_1_1spec/#friend-fptrfinder)**  |

**Public Functions inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| | **[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-subspectrum)**()<br>Constructors/destructors.  |
| virtual | **[~SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-subspectrum)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1subspectrum/#function-getname)**() const =0<br>Main public interface functions.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1subspectrum/#function-clone)**() const =0<br>Clone the [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object.  |
| virtual void | **[writeSLHAfile](/documentation/code/classes/classgambit_1_1subspectrum/#function-writeslhafile)**(int slha_version, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & filename) const<br>Dump out spectrum information to an SLHA file (if possible)  |
| virtual [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) | **[getSLHAea](/documentation/code/classes/classgambit_1_1subspectrum/#function-getslhaea)**(int slha_version) const<br>Get spectrum information in SLHAea format (if possible)  |
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

**Protected Attributes inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [OverrideMaps](/documentation/code/classes/structgambit_1_1overridemaps/) > | **[override_maps](/documentation/code/classes/classgambit_1_1subspectrum/#variable-override-maps)** <br>Map of override maps.  |


## Public Functions Documentation

### function MSSMSimpleSpec

```
MSSMSimpleSpec(
    double uncert =0.03
)
```

Member functions for [MSSMSimpleSpec](/documentation/code/classes/classgambit_1_1mssmsimplespec/) class. 

Constructors. The optional double uncert is the uncertainty to assign to pole masses (default is 3%).

Constructors Default Constructor 


### function MSSMSimpleSpec

```
MSSMSimpleSpec(
    const SLHAstruct & input,
    double uncert =0.03
)
```

Constructor via SLHAea object. 

### function MSSMSimpleSpec

```
MSSMSimpleSpec(
    const MSSMSimpleSpec & other,
    double uncert =0.03
)
```

Copy constructor: needed by clone function. 

### function ~MSSMSimpleSpec

```
inline virtual ~MSSMSimpleSpec()
```

Destructor. 

### function get_index_offset

```
virtual int get_index_offset() const
```

Ofset from user-input indices (user assumes 1,2,3 indexed, e.g. use offset=-1 for zero-indexing) 

### function add_to_SLHAea

```
virtual void add_to_SLHAea(
    int slha_version,
    SLHAea::Coll & slha
) const
```

Retrieve SLHAea object. 

**Reimplements**: [Gambit::SubSpectrum::add_to_SLHAea](/documentation/code/classes/classgambit_1_1subspectrum/#function-add-to-slhaea)


Add SLHAea object to another 


### function PDG_translator

```
virtual const std::map< int, int > & PDG_translator() const
```

Retrieve the PDG translation map. 

**Reimplements**: [Gambit::SubSpectrum::PDG_translator](/documentation/code/classes/classgambit_1_1subspectrum/#function-pdg-translator)


### function fill_getter_maps

```
static GetterMaps fill_getter_maps()
```


Map fillers Used to initialise maps in [Spec](/documentation/code/classes/classgambit_1_1spec/) class, accessed via [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) interface class (specialisations created and stored automatically by [Spec<QedQcdWrapper>](/documentation/code/classes/classgambit_1_1spec/)) 


-------------------------------

Updated on 2022-09-08 at 03:17:32 +0000