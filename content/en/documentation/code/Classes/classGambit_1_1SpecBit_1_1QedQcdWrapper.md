---
title: "class Gambit::SpecBit::QedQcdWrapper"

description: "[No description available]"

---

# class Gambit::SpecBit::QedQcdWrapper



[No description available]

Inherits from [Gambit::Spec< QedQcdWrapper >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual double | **[hard_upper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-hard-upper)**() const |
| virtual double | **[soft_upper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-soft-upper)**() const |
| virtual double | **[soft_lower](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-soft-lower)**() const |
| virtual double | **[hard_lower](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-hard-lower)**() const |
| | **[QedQcdWrapper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-qedqcdwrapper)**()<br>[QedQcdWrapper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/) member functions.  |
| | **[QedQcdWrapper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-qedqcdwrapper)**(const softsusy::QedQcd & model, const [SMInputs](/documentation/code/classes/structgambit_1_1sminputs/) & input) |
| virtual int | **[get_numbers_stable_particles](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-get-numbers-stable-particles)**() const |
| [GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-gettermaps) | **[fill_getter_maps](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-fill-getter-maps)**()<br>Map fillers.  |
| SetterMaps | **[fill_setter_maps](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-fill-setter-maps)**() |
| virtual | **[~QedQcdWrapper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-qedqcdwrapper)**()<br>Destructor.  |
| Model & | **[get_Model](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-get-model)**() |
| Input & | **[get_Input](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-get-input)**() |
| const Model & | **[get_Model](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-get-model)**() const |
| const Input & | **[get_Input](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-get-input)**() const |
| virtual void | **[add_to_SLHAea](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-add-to-slhaea)**(int , [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-gambit-slhastruct) & slha) const<br>Add QEDQCD information to an SLHAea object.  |
| virtual double | **[GetScale](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-getscale)**() const<br>RunningPars interface overrides.  |
| virtual void | **[SetScale](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-setscale)**(double scale)<br>Manually define the current renormalisation scale (do this at own risk!)  |
| virtual void | **[RunToScaleOverride](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#function-gambitspecbitqedqcdwrapper-runtoscaleoverride)**(double end_scale)<br>Run masses and couplings to end_scale.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| double | **[hardup](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#variable-gambitspecbitqedqcdwrapper-hardup)**  |
| double | **[softup](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#variable-gambitspecbitqedqcdwrapper-softup)**  |
| double | **[softlow](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#variable-gambitspecbitqedqcdwrapper-softlow)**  |
| double | **[hardlow](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/#variable-gambitspecbitqedqcdwrapper-hardlow)**  |

## Additional inherited members

**Public Types inherited from [Gambit::Spec< QedQcdWrapper >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| typedef DerivedSpec | **[D](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-d)**  |
| typedef [Spec](/documentation/code/classes/classgambit_1_1spec/)< D > | **[Self](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-self)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Contents | **[Contents](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-contents)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Model | **[Model](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-model)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Input | **[Input](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-input)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< D, [MapTag::Get](/documentation/code/classes/structgambit_1_1maptag_1_1get/) > | **[MTget](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-mtget)**  |
| typedef [MapTypes](/documentation/code/classes/structgambit_1_1maptypes/)< D, [MapTag::Set](/documentation/code/classes/structgambit_1_1maptag_1_1set/) > | **[MTset](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-mtset)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTget](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-gettermaps)**  |
| typedef std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags), [MapCollection](/documentation/code/classes/structgambit_1_1mapcollection/)< [MTset](/documentation/code/classes/structgambit_1_1maptypes/) > > | **[SetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-settermaps)**  |

**Public Functions inherited from [Gambit::Spec< QedQcdWrapper >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| Model & | **[model](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-model)**()<br>Get model object on which to call function pointers.  |
| const Model & | **[model](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-model)**() const<br>Return it as const if we are a const object.  |
| Input & | **[input](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-input)**()<br>Get struct containing any extra data input on [SubSpectrum]() object creation.  |
| const Input & | **[input](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-input)**() const<br>Return it as const if we are a const object.  |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>[Spec](/documentation/code/classes/classgambit_1_1spec/) member function definitions.  |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const int j) |
| int | **[index_offset](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-index-offset)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-getname)**() const<br>Main public interface functions.  |
| | **[Spec](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-spec)**() |
| virtual | **[~Spec](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-spec)**()<br>Virtual destructor.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1spec/#function-gambitspec-clone)**() const |

**Public Attributes inherited from [Gambit::Spec< QedQcdWrapper >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| [DummyModel](/documentation/code/classes/classgambit_1_1dummymodel/) | **[dummymodel](/documentation/code/classes/classgambit_1_1spec/#variable-gambitspec-dummymodel)**  |
| [DummyInput](/documentation/code/classes/classgambit_1_1dummyinput/) | **[dummyinput](/documentation/code/classes/classgambit_1_1spec/#variable-gambitspec-dummyinput)**  |
| const [GetterMaps](/documentation/code/classes/classgambit_1_1spec/#typedef-gambitspec-gettermaps) | **[getter_maps](/documentation/code/classes/classgambit_1_1spec/#variable-gambitspec-getter-maps)** <br>Initialise maps (uses filler overrides from DerivedSpec if defined)  |
| const SetterMaps | **[setter_maps](/documentation/code/classes/classgambit_1_1spec/#variable-gambitspec-setter-maps)**  |

**Friends inherited from [Gambit::Spec< QedQcdWrapper >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| class | **[FptrFinder](/documentation/code/classes/classgambit_1_1spec/#friend-gambitspec-fptrfinder)**  |

**Public Functions inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| | **[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-subspectrum)**()<br>Constructors/destructors.  |
| virtual | **[~SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-subspectrum)**() |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-getname)**() const =0<br>Main public interface functions.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-clone)**() const =0<br>Clone the [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object.  |
| virtual void | **[writeSLHAfile](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-writeslhafile)**(int slha_version, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & filename) const<br>Dump out spectrum information to an SLHA file (if possible)  |
| virtual [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-gambit-slhastruct) | **[getSLHAea](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-getslhaea)**(int slha_version) const<br>Get spectrum information in SLHAea format (if possible)  |
| void | **[RunToScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-runtoscale)**(double scale, const int behave =0) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const bool allow_new =false, const bool decouple =false)<br>Parameter override functions.  |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & name, const int i, const int j, const bool allow_new =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > & params, const bool allow_new =false, const bool decouple =false)<br>Vector override functions.  |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > & params, const std::vector< int > indices, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) tag, const double value, const std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) > & params, const int i, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override_vector](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override-vector)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) tag, const double value, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & par, const std::vector< int > indices, const bool allow_new =false, const bool decouple =false) |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>PDB getter/checker overloads.  |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & mass, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>safeget functions, by Abram  |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & mass, const int i, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & mass, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const int pdg_code, const int context, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const std::pair< int, int > pdgpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), int > shortpr, const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double value, const int PDGcode, const int context, const bool allow_new =false, const bool decouple =false)<br>PDB overloads for setters.  |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double value, const std::pair< int, int > pdgpr, const bool allow_new =false, const bool decouple =false) |
| void | **[set_override](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set-override)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) partype, const double value, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str), int > shortpr, const bool allow_new =false, const bool decouple =false)<br>PDB overloads of set_override functions.  |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0<br>Getters/Setters etc.  |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const int , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const int , const SpecOverrideOptions =use_overrides, const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const =0 |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const int , const int , const SpecOverrideOptions =use_overrides) const =0 |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const int , const int , const SpecOverrideOptions =use_overrides) const =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const double , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const double , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const int , const [SafeBool](/documentation/code/classes/classgambit_1_1safebool/) check_antiparticle =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) =0 |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-set)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) , const double , const [str](/documentation/code/namespaces/namespacegambit/#typedef-gambit-str) & , const int , const int ) =0 |
| virtual const std::map< int, int > & | **[PDG_translator](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-pdg-translator)**() const<br>TODO: extra PDB overloads to handle all the one and two index cases (well all the ones that are feasible...)  |

**Protected Attributes inherited from [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)**

|                | Name           |
| -------------- | -------------- |
| std::map< [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags), [OverrideMaps](/documentation/code/classes/structgambit_1_1overridemaps/) > | **[override_maps](/documentation/code/classes/classgambit_1_1subspectrum/#variable-gambitsubspectrum-override-maps)** <br>Map of override maps.  |


## Public Functions Documentation

### function hard_upper

```
inline virtual double hard_upper() const
```


**Reimplements**: [Gambit::SubSpectrum::hard_upper](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-hard-upper)


Limits to RGE running; warning/error raised if running beyond these is attempted. If these aren't overridden in the derived class then effectively no limit on running will exist. These are public so that module writers can use them to check what the limits are. 


### function soft_upper

```
inline virtual double soft_upper() const
```


**Reimplements**: [Gambit::SubSpectrum::soft_upper](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-soft-upper)


### function soft_lower

```
inline virtual double soft_lower() const
```


**Reimplements**: [Gambit::SubSpectrum::soft_lower](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-soft-lower)


### function hard_lower

```
inline virtual double hard_lower() const
```


**Reimplements**: [Gambit::SubSpectrum::hard_lower](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-hard-lower)


### function QedQcdWrapper

```
QedQcdWrapper()
```

[QedQcdWrapper](/documentation/code/classes/classgambit_1_1specbit_1_1qedqcdwrapper/) member functions. 

Constructors 


### function QedQcdWrapper

```
QedQcdWrapper(
    const softsusy::QedQcd & model,
    const SMInputs & input
)
```


### function get_numbers_stable_particles

```
virtual int get_numbers_stable_particles() const
```


**Reimplements**: [Gambit::SubSpectrum::get_numbers_stable_particles](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-get-numbers-stable-particles)


Currently unused virtual functions 


### function fill_getter_maps

```
static GetterMaps fill_getter_maps()
```

Map fillers. 

mass1 - mass dimension 1 parameters


### function fill_setter_maps

```
static SetterMaps fill_setter_maps()
```


Pole_Mass - Pole mass parameters

Functions utilising the "extraI" signature (Zero-index, "Inputs" object used as argument)


### function ~QedQcdWrapper

```
virtual ~QedQcdWrapper()
```

Destructor. 

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


### function add_to_SLHAea

```
virtual void add_to_SLHAea(
    int ,
    SLHAstruct & slha
) const
```

Add QEDQCD information to an SLHAea object. 

**Reimplements**: [Gambit::SubSpectrum::add_to_SLHAea](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-add-to-slhaea)


Add QED x QCD information to an SLHAea object. 


### function GetScale

```
virtual double GetScale() const
```

RunningPars interface overrides. 

**Reimplements**: [Gambit::SubSpectrum::GetScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-getscale)


Retrieve the current renormalisation scale at which running parameters are defined. 


### function SetScale

```
virtual void SetScale(
    double scale
)
```

Manually define the current renormalisation scale (do this at own risk!) 

**Reimplements**: [Gambit::SubSpectrum::SetScale](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-setscale)


### function RunToScaleOverride

```
virtual void RunToScaleOverride(
    double end_scale
)
```

Run masses and couplings to end_scale. 

**Reimplements**: [Gambit::SubSpectrum::RunToScaleOverride](/documentation/code/classes/classgambit_1_1subspectrum/#function-gambitsubspectrum-runtoscaleoverride)


## Public Attributes Documentation

### variable hardup

```
double hardup;
```


Limits for running 


### variable softup

```
double softup;
```


### variable softlow

```
double softlow;
```


### variable hardlow

```
double hardlow;
```


-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000