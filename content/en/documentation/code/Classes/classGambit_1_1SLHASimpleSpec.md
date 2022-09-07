---
title: "class Gambit::SLHASimpleSpec"

description: "[No description available]"

---

# class Gambit::SLHASimpleSpec



[No description available] [More...](#detailed-description)

Inherits from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< Derived >::Model | **[Model](/documentation/code/classes/classgambit_1_1slhasimplespec/#typedef-model)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< Derived >::Input | **[Input](/documentation/code/classes/classgambit_1_1slhasimplespec/#typedef-input)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< Derived, [MapTag::Get](/documentation/code/classes/structgambit_1_1maptag_1_1get/) > | **[MTget](/documentation/code/classes/classgambit_1_1slhasimplespec/#typedef-mtget)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[add_to_SLHAea](/documentation/code/classes/classgambit_1_1slhasimplespec/#function-add-to-slhaea)**(int , SLHAea::Coll & slha) const<br>Add spectrum information to an SLHAea object.  |
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

## Protected Attributes

|                | Name           |
| -------------- | -------------- |
| Model | **[slhawrap](/documentation/code/classes/classgambit_1_1slhasimplespec/#variable-slhawrap)**  |
| Input | **[dummyinput](/documentation/code/classes/classgambit_1_1slhasimplespec/#variable-dummyinput)**  |

## Additional inherited members

**Public Types inherited from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| typedef DerivedSpec | **[D](/documentation/code/classes/classgambit_1_1spec/#typedef-d)**  |
| typedef [Spec](/documentation/code/classes/classgambit_1_1spec/)< D > | **[Self](/documentation/code/classes/classgambit_1_1spec/#typedef-self)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Contents | **[Contents](/documentation/code/classes/classgambit_1_1spec/#typedef-contents)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< D, [MapTag::Set](/documentation/code/classes/structgambit_1_1maptag_1_1set/) > | **[MTset](/documentation/code/classes/classgambit_1_1spec/#typedef-mtset)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTget](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gettermaps)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTset](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[SetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-settermaps)**  |

**Public Functions inherited from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
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

**Public Attributes inherited from [Gambit::Spec< Derived >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| [DummyModel](/documentation/code/classes/classgambit_1_1dummymodel/) | **[dummymodel](/documentation/code/classes/classgambit_1_1spec/#variable-dummymodel)**  |
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

**Protected Attributes inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags), [OverrideMaps](/documentation/code/classes/structgambit_1_1overridemaps/) > | **[override_maps](/documentation/code/classes/classgambit_1_1subspectrum/#variable-override-maps)** <br>Map of override maps.  |


## Detailed Description

```
template <class Derived >
class Gambit::SLHASimpleSpec;
```

## Public Types Documentation

### typedef Model

```
typedef SpecTraits<Derived>::Model Gambit::SLHASimpleSpec< Derived >::Model;
```


### typedef Input

```
typedef SpecTraits<Derived>::Input Gambit::SLHASimpleSpec< Derived >::Input;
```


### typedef MTget

```
typedef MapTypes<Derived,MapTag::Get> Gambit::SLHASimpleSpec< Derived >::MTget;
```


## Public Functions Documentation

### function add_to_SLHAea

```
virtual void add_to_SLHAea(
    int ,
    SLHAea::Coll & slha
) const
```

Add spectrum information to an SLHAea object. 

**Reimplements**: [Gambit::SubSpectrum::add_to_SLHAea](/documentation/code/classes/classgambit_1_1subspectrum/#function-add-to-slhaea)


Member functions for [SLHASimpleSpec](/documentation/code/classes/classgambit_1_1slhasimplespec/) class.

Add spectrum information to an SLHAea object 


### function GetScale

```
inline virtual double GetScale() const
```

(using bass class version of getSLHAea) 

**Reimplements**: [Gambit::SubSpectrum::GetScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-getscale)


**Reimplemented by**: [Gambit::SMSimpleSpec::GetScale](/documentation/code/classes/classgambit_1_1smsimplespec/#function-getscale)


RunningPars interface overrides 


TODO: Currently assumes all blocks at same scale. Should at least check if this is true in constructor.


### function SetScale

```
inline virtual void SetScale(
    double 
)
```


**Reimplements**: [Gambit::SubSpectrum::SetScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-setscale)


Manually set the renormalisation scale of parameters somewhat dangerous to allow this but may be needed 


### function RunToScaleOverride

```
inline virtual void RunToScaleOverride(
    double 
)
```

Run spectrum to new scale. 

**Reimplements**: [Gambit::SubSpectrum::RunToScaleOverride](/documentation/code/classes/classgambit_1_1subspectrum/#function-runtoscaleoverride)


Functions to be overridden in classes derived from [Spec<Derived>](/documentation/code/classes/classgambit_1_1spec/) (i.e. the final wrappers) 


### function SLHASimpleSpec

```
inline SLHASimpleSpec()
```


### function SLHASimpleSpec

```
inline SLHASimpleSpec(
    const SLHAea::Coll & input_slha
)
```


### function ~SLHASimpleSpec

```
inline virtual ~SLHASimpleSpec()
```


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


## Protected Attributes Documentation

### variable slhawrap

```
Model slhawrap;
```


### variable dummyinput

```
Input dummyinput;
```


-------------------------------

Updated on 2022-09-07 at 23:22:06 +0000