---
title: "class Gambit::SpecBit::ScalarSingletDM_Z3Spec"

description: "[No description available]"

---

# class Gambit::SpecBit::ScalarSingletDM_Z3Spec



[No description available] [More...](#detailed-description)

Inherits from [Gambit::Spec< ScalarSingletDM_Z3Spec< MI > >](/documentation/code/classes/classgambit_1_1spec/), [Gambit::SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/)

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef [ScalarSingletDM_Z3Spec](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)< MI > | **[Self](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |
| typedef Self::MTget | **[MTget](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |
| typedef Self::MTset | **[MTset](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |
| typedef Self::GetterMaps | **[GetterMaps](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |
| typedef Self::SetterMaps | **[SetterMaps](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< [Self](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/) >::Model | **[Model](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< [Self](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/) >::Input | **[Input](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| SetterMaps | **[fill_setter_maps](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() |
| int | **[index_offset](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**()<br>Interface function overrides.  |
| GetterMaps | **[fill_getter_maps](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**()<br>Map filler overrides.  |
| virtual double | **[GetScale](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() const<br>Returns the renormalisation scale of parameters.  |
| virtual void | **[SetScale](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**(double ) |
| virtual void | **[RunToScaleOverride](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**(double )<br>Run spectrum to new scale.  |
| | **[ScalarSingletDM_Z3Spec](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() |
| | **[ScalarSingletDM_Z3Spec](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**(MI mi, [str](/documentation/code/namespaces/namespacegambit/) backend_name, [str](/documentation/code/namespaces/namespacegambit/) backend_version) |
| virtual | **[~ScalarSingletDM_Z3Spec](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() |
| Model & | **[get_Model](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() |
| Input & | **[get_Input](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() |
| const Model & | **[get_Model](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() const |
| const Input & | **[get_Input](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**() const |
| virtual std::string | **[AccessError](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**(std::string state) const |
| template <class ScalarSingletDM_Z3like \> <br>void | **[get_lowe_data_from](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**(ScalarSingletDM_Z3like & othermodel) |
| void | **[get_external_spectrum](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**(typename MI::Model & othermodel) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| MI | **[model_interface](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |
| [DummyInput](/documentation/code/classes/classgambit_1_1dummyinput/) | **[dummyinput](/documentation/code/classes/classgambit_1_1specbit_1_1scalarsingletdm__z3spec/)**  |

## Additional inherited members

**Public Types inherited from [Gambit::Spec< ScalarSingletDM_Z3Spec< MI > >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| typedef DerivedSpec | **[D](/documentation/code/classes/classgambit_1_1spec/)**  |
| typedef [SpecTraits](/documentation/code/classes/structgambit_1_1spectraits/)< D >::Contents | **[Contents](/documentation/code/classes/classgambit_1_1spec/)**  |

**Public Functions inherited from [Gambit::Spec< ScalarSingletDM_Z3Spec< MI > >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| Model & | **[model](/documentation/code/classes/classgambit_1_1spec/)**()<br>Get model object on which to call function pointers.  |
| const Model & | **[model](/documentation/code/classes/classgambit_1_1spec/)**() const<br>Return it as const if we are a const object.  |
| Input & | **[input](/documentation/code/classes/classgambit_1_1spec/)**()<br>Get struct containing any extra data input on [SubSpectrum]() object creation.  |
| const Input & | **[input](/documentation/code/classes/classgambit_1_1spec/)**() const<br>Return it as const if we are a const object.  |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const<br>[Spec](/documentation/code/classes/classgambit_1_1spec/) member function definitions.  |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const SpecOverrideOptions =use_overrides, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const SafeBool =[SafeBool](/documentation/code/classes/classgambit_1_1safebool/)(true)) |
| virtual bool | **[has](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual double | **[get](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const int j, const SpecOverrideOptions =use_overrides) const |
| virtual void | **[set](/documentation/code/classes/classgambit_1_1spec/)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/) partype, const double set_value, const [str](/documentation/code/namespaces/namespacegambit/) & name, const int i, const int j) |
| virtual std::string | **[getName](/documentation/code/classes/classgambit_1_1spec/)**() const<br>Main public interface functions.  |
| | **[Spec](/documentation/code/classes/classgambit_1_1spec/)**() |
| virtual | **[~Spec](/documentation/code/classes/classgambit_1_1spec/)**()<br>Virtual destructor.  |
| virtual std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone](/documentation/code/classes/classgambit_1_1spec/)**() const |

**Public Attributes inherited from [Gambit::Spec< ScalarSingletDM_Z3Spec< MI > >](/documentation/code/classes/classgambit_1_1spec/)**

|                | Name           |
| -------------- | -------------- |
| [DummyModel](/documentation/code/classes/classgambit_1_1dummymodel/) | **[dummymodel](/documentation/code/classes/classgambit_1_1spec/)**  |
| const [GetterMaps](/documentation/code/classes/classgambit_1_1spec/) | **[getter_maps](/documentation/code/classes/classgambit_1_1spec/)** <br>Initialise maps (uses filler overrides from DerivedSpec if defined)  |
| const SetterMaps | **[setter_maps](/documentation/code/classes/classgambit_1_1spec/)**  |

**Friends inherited from [Gambit::Spec< ScalarSingletDM_Z3Spec< MI > >](/documentation/code/classes/classgambit_1_1spec/)**

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


## Detailed Description

```
template <class MI >
class Gambit::SpecBit::ScalarSingletDM_Z3Spec;
```

## Public Types Documentation

### typedef Self

```
typedef ScalarSingletDM_Z3Spec<MI> Gambit::SpecBit::ScalarSingletDM_Z3Spec< MI >::Self;
```


These typedefs are inherited, but the name lookup doesn't work so smoothly in templated wrapper classes, so need to help them along: 


### typedef MTget

```
typedef Self::MTget Gambit::SpecBit::ScalarSingletDM_Z3Spec< MI >::MTget;
```


### typedef MTset

```
typedef Self::MTset Gambit::SpecBit::ScalarSingletDM_Z3Spec< MI >::MTset;
```


### typedef GetterMaps

```
typedef Self::GetterMaps Gambit::SpecBit::ScalarSingletDM_Z3Spec< MI >::GetterMaps;
```


### typedef SetterMaps

```
typedef Self::SetterMaps Gambit::SpecBit::ScalarSingletDM_Z3Spec< MI >::SetterMaps;
```


### typedef Model

```
typedef SpecTraits<Self>::Model Gambit::SpecBit::ScalarSingletDM_Z3Spec< MI >::Model;
```


### typedef Input

```
typedef SpecTraits<Self>::Input Gambit::SpecBit::ScalarSingletDM_Z3Spec< MI >::Input;
```


## Public Functions Documentation

### function fill_setter_maps

```
static SetterMaps fill_setter_maps()
```


mass2 - mass dimension 2 parameters


### function index_offset

```
static inline int index_offset()
```

Interface function overrides. 

### function fill_getter_maps

```
static GetterMaps fill_getter_maps()
```

Map filler overrides. 

### function GetScale

```
virtual double GetScale() const
```

Returns the renormalisation scale of parameters. 

**Reimplements**: [Gambit::SubSpectrum::GetScale](/documentation/code/classes/classgambit_1_1subspectrum/)


### function SetScale

```
virtual void SetScale(
    double 
)
```


**Reimplements**: [Gambit::SubSpectrum::SetScale](/documentation/code/classes/classgambit_1_1subspectrum/)


Manually set the renormalisation scale of parameters somewhat dangerous to allow this but may be needed 


### function RunToScaleOverride

```
virtual void RunToScaleOverride(
    double 
)
```

Run spectrum to new scale. 

**Reimplements**: [Gambit::SubSpectrum::RunToScaleOverride](/documentation/code/classes/classgambit_1_1subspectrum/)


Functions to be overridden in classes derived from [Spec<Derived>](/documentation/code/classes/classgambit_1_1spec/) (i.e. the final wrappers) 


### function ScalarSingletDM_Z3Spec

```
ScalarSingletDM_Z3Spec()
```


### function ScalarSingletDM_Z3Spec

```
ScalarSingletDM_Z3Spec(
    MI mi,
    str backend_name,
    str backend_version
)
```


### function ~ScalarSingletDM_Z3Spec

```
virtual ~ScalarSingletDM_Z3Spec()
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


### function AccessError

```
virtual std::string AccessError(
    std::string state
) const
```


### function get_lowe_data_from

```
template <class ScalarSingletDM_Z3like >
inline void get_lowe_data_from(
    ScalarSingletDM_Z3like & othermodel
)
```


### function get_external_spectrum

```
inline void get_external_spectrum(
    typename MI::Model & othermodel
)
```


## Public Attributes Documentation

### variable model_interface

```
MI model_interface;
```


### variable dummyinput

```
DummyInput dummyinput;
```


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000