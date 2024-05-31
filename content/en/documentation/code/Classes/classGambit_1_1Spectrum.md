---
title: "class Gambit::Spectrum"
description: "Standard Model (low-energy) plus high-energy model container class "

---

# class Gambit::Spectrum



"Standard Model" (low-energy) plus high-energy model container class 


`#include <spectrum.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< YAML::sdd > | **[mc_info](/documentation/code/classes/classgambit_1_1spectrum/#typedef-mc-info)**  |
| typedef std::vector< YAML::ssdd > | **[mr_info](/documentation/code/classes/classgambit_1_1spectrum/#typedef-mr-info)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Spectrum](/documentation/code/classes/classgambit_1_1spectrum/#function-spectrum)**()<br>Default constructor.  |
| | **[Spectrum](/documentation/code/classes/classgambit_1_1spectrum/#function-spectrum)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & le, const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & he, const [SMInputs](/documentation/code/classes/structgambit_1_1sminputs/) & smi, const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< const double > > * input_Param, const [mc_info](/documentation/code/classes/classgambit_1_1spectrum/#typedef-mc-info) & mci, const mr_info & mri)<br>Construct new object, cloning the [SubSpectrum]() objects supplied and taking possession of them.  |
| | **[Spectrum](/documentation/code/classes/classgambit_1_1spectrum/#function-spectrum)**([SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) *const le, [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) *const he, const [SMInputs](/documentation/code/classes/structgambit_1_1sminputs/) & smi, const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< const double > > * input_Param, const [mc_info](/documentation/code/classes/classgambit_1_1spectrum/#typedef-mc-info) & mci, const mr_info & mri) |
| | **[Spectrum](/documentation/code/classes/classgambit_1_1spectrum/#function-spectrum)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & he, const [SMInputs](/documentation/code/classes/structgambit_1_1sminputs/) & smi, const std::map< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< const double > > * input_Param, const [mc_info](/documentation/code/classes/classgambit_1_1spectrum/#typedef-mc-info) & mci, const mr_info & mri)<br>Construct new object, automatically creating an [SMSimpleSpec](/documentation/code/classes/classgambit_1_1smsimplespec/) as the LE subspectrum, and cloning the HE [SubSpectrum]() object supplied and taking possession of it.  |
| | **[Spectrum](/documentation/code/classes/classgambit_1_1spectrum/#function-spectrum)**(const [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) & other) |
| [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) & | **[operator=](/documentation/code/classes/classgambit_1_1spectrum/#function-operator)**(const [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) & other) |
| | **[Spectrum](/documentation/code/classes/classgambit_1_1spectrum/#function-spectrum)**([Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) && other)<br>Move constructor.  |
| [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & | **[get_LE](/documentation/code/classes/classgambit_1_1spectrum/#function-get-le)**() |
| [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & | **[get_HE](/documentation/code/classes/classgambit_1_1spectrum/#function-get-he)**() |
| [SMInputs](/documentation/code/classes/structgambit_1_1sminputs/) & | **[get_SMInputs](/documentation/code/classes/classgambit_1_1spectrum/#function-get-sminputs)**() |
| const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & | **[get_LE](/documentation/code/classes/classgambit_1_1spectrum/#function-get-le)**() const |
| const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & | **[get_HE](/documentation/code/classes/classgambit_1_1spectrum/#function-get-he)**() const |
| const [SMInputs](/documentation/code/classes/structgambit_1_1sminputs/) & | **[get_SMInputs](/documentation/code/classes/classgambit_1_1spectrum/#function-get-sminputs)**() const |
| std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone_LE](/documentation/code/classes/classgambit_1_1spectrum/#function-clone-le)**() const |
| std::unique_ptr< [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) > | **[clone_HE](/documentation/code/classes/classgambit_1_1spectrum/#function-clone-he)**() const |
| bool | **[has](/documentation/code/classes/classgambit_1_1spectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass) const |
| double | **[get](/documentation/code/classes/classgambit_1_1spectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1spectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass, const int index) const |
| double | **[get](/documentation/code/classes/classgambit_1_1spectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass, const int index) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1spectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass, const int index1, const int index2) const |
| double | **[get](/documentation/code/classes/classgambit_1_1spectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass, const int index1, const int index2) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1spectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const int pdg_code, const int context) const<br>PDB getter/checker overloads.  |
| double | **[get](/documentation/code/classes/classgambit_1_1spectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const int pdg_code, const int context) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1spectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< int, int > pdgpr) const |
| double | **[get](/documentation/code/classes/classgambit_1_1spectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< int, int > pdgpr) const |
| bool | **[has](/documentation/code/classes/classgambit_1_1spectrum/#function-has)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr) const |
| double | **[get](/documentation/code/classes/classgambit_1_1spectrum/#function-get)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1spectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass) const<br>Getters which first check the sanity of the thing they are returning.  |
| double | **[safeget](/documentation/code/classes/classgambit_1_1spectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::string & mass, const int index) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1spectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const int pdg_code, const int context) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1spectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< int, int > pdgpr) const |
| double | **[safeget](/documentation/code/classes/classgambit_1_1spectrum/#function-safeget)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) partype, const std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), int > shortpr) const |
| double | **[Wolf2V_ud](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-ud)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_ud standard parameterisation convertor.  |
| double | **[Wolf2V_us](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-us)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_us standard parameterisation convertor.  |
| std::complex< double > | **[Wolf2V_ub](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-ub)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_ub standard parameterisation convertor.  |
| std::complex< double > | **[Wolf2V_cd](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-cd)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_cd standard parameterisation convertor.  |
| std::complex< double > | **[Wolf2V_cs](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-cs)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_cs standard parameterisation convertor.  |
| double | **[Wolf2V_cb](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-cb)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_cb standard parameterisation convertor.  |
| std::complex< double > | **[Wolf2V_td](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-td)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_td standard parameterisation convertor.  |
| std::complex< double > | **[Wolf2V_ts](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-ts)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_ts standard parameterisation convertor.  |
| double | **[Wolf2V_tb](/documentation/code/classes/classgambit_1_1spectrum/#function-wolf2v-tb)**(double l, double A, double rhobar, double etabar)<br>CKM Wolfenstein --> V_tb standard parameterisation convertor.  |
| void | **[RunBothToScale](/documentation/code/classes/classgambit_1_1spectrum/#function-runbothtoscale)**(double scale) |
| void | **[check_mass_cuts](/documentation/code/classes/classgambit_1_1spectrum/#function-check-mass-cuts)**()<br>Check the that the spectrum satisifies any mass cuts requested from the yaml file.  |
| [SLHAstruct](/documentation/code/namespaces/namespacegambit/#typedef-slhastruct) | **[getSLHAea](/documentation/code/classes/classgambit_1_1spectrum/#function-getslhaea)**(int slha_version) const |
| void | **[writeSLHAfile](/documentation/code/classes/classgambit_1_1spectrum/#function-writeslhafile)**(int slha_version, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & filename) const<br>Output spectrum contents as an SLHA file, using getSLHAea.  |
| void | **[drop_SLHAs_if_requested](/documentation/code/classes/classgambit_1_1spectrum/#function-drop-slhas-if-requested)**(const [safe_ptr](/documentation/code/classes/classgambit_1_1safe__ptr/)< [Options](/documentation/code/classes/classgambit_1_1options/) > & runOptions, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & default_name)<br>Helper function to drop SLHA files.  |
| const std::map< int, int > & | **[PDG_translator](/documentation/code/classes/classgambit_1_1spectrum/#function-pdg-translator)**() const<br>PDG code translation map, for special cases where an SLHA file has been read in and the PDG codes changed.  |

## Friends

|                | Name           |
| -------------- | -------------- |
| void | **[swap](/documentation/code/classes/classgambit_1_1spectrum/#friend-swap)**([Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) & first, [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) & second) <br>Friend function: swap resources of two [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) objects.  |

## Public Types Documentation

### typedef mc_info

```
typedef std::vector<YAML::sdd> Gambit::Spectrum::mc_info;
```


Typedefs for making it easier to manipulate mass cut and mass ratio cut info. 


### typedef mr_info

```
typedef std::vector<YAML::ssdd> Gambit::Spectrum::mr_info;
```


## Public Functions Documentation

### function Spectrum

```
Spectrum()
```

Default constructor. 

Constructors/destructors.

Constructors/Destructors Need custom copy and move constructors plus copy-assignment operator in order to manage the unique_ptrs properly.

Default constructor 


### function Spectrum

```
Spectrum(
    const SubSpectrum & le,
    const SubSpectrum & he,
    const SMInputs & smi,
    const std::map< str, safe_ptr< const double > > * input_Param,
    const mc_info & mci,
    const mr_info & mri
)
```

Construct new object, cloning the [SubSpectrum]() objects supplied and taking possession of them. 

### function Spectrum

```
Spectrum(
    SubSpectrum *const le,
    SubSpectrum *const he,
    const SMInputs & smi,
    const std::map< str, safe_ptr< const double > > * input_Param,
    const mc_info & mci,
    const mr_info & mri
)
```


Construct new object, wrapping existing [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) objects Make sure the original objects don't get deleted before this wrapper does! 


### function Spectrum

```
Spectrum(
    const SubSpectrum & he,
    const SMInputs & smi,
    const std::map< str, safe_ptr< const double > > * input_Param,
    const mc_info & mci,
    const mr_info & mri
)
```

Construct new object, automatically creating an [SMSimpleSpec](/documentation/code/classes/classgambit_1_1smsimplespec/) as the LE subspectrum, and cloning the HE [SubSpectrum]() object supplied and taking possession of it. 

Construct new object, automatically creating an [SMSimpleSpec](/documentation/code/classes/classgambit_1_1smsimplespec/) as the LE subspectrum, and cloning the HE [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object supplied and taking possession of it. (won't make a version of this taking a pointer, since this is an "advanced" task, let people use the full contructor to do it.) 


### function Spectrum

```
Spectrum(
    const Spectrum & other
)
```


Copy constructor, clones [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) objects. Make a non-const copy in order to use e.g. RunBothToScale function. 


### function operator=

```
Spectrum & operator=(
    const Spectrum & other
)
```


Copy-assignment Using "copy-and-swap" idiom 


### function Spectrum

```
Spectrum(
    Spectrum && other
)
```

Move constructor. 

### function get_LE

```
SubSpectrum & get_LE()
```


Standard [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) getters Return references to internal data members. Make sure original [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) object doesn't get destroyed before you finish using these or you will cause a segfault.

Standard getters Return references to internal data members. Make sure original [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) object doesn't get destroyed before you finish using these or you will cause a segfault. 


### function get_HE

```
SubSpectrum & get_HE()
```


### function get_SMInputs

```
SMInputs & get_SMInputs()
```


### function get_LE

```
const SubSpectrum & get_LE() const
```


### function get_HE

```
const SubSpectrum & get_HE() const
```


### function get_SMInputs

```
const SMInputs & get_SMInputs() const
```


### function clone_LE

```
std::unique_ptr< SubSpectrum > clone_LE() const
```


Clone [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) getters To clone whole object, just use copy constructor.

Clone getters Note: If you want to clone the whole [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) object, just use copy constructor, not these. 


### function clone_HE

```
std::unique_ptr< SubSpectrum > clone_HE() const
```


### function has

```
bool has(
    const Par::Tags partype,
    const std::string & mass
) const
```


Pole mass getters "Shortcut" getters to access pole masses in hosted [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) objects. HE object given higher priority; if no match found, LE object will be checked. If still no match, error is thrown.

Pole mass getters/checkers "Shortcut" getters/checkers to access pole masses in hosted [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) objects. HE object given higher priority; if no match found, LE object will be checked. If still no match, error is thrown. TODO: These currently work for anything! Need to restrict them to only allow access to pole masses and their estimated uncertainties Also need to change error messages etc, plus the PDG overloads 


### function get

```
double get(
    const Par::Tags partype,
    const std::string & mass
) const
```


### function has

```
bool has(
    const Par::Tags partype,
    const std::string & mass,
    const int index
) const
```


### function get

```
double get(
    const Par::Tags partype,
    const std::string & mass,
    const int index
) const
```


### function has

```
bool has(
    const Par::Tags partype,
    const std::string & mass,
    const int index1,
    const int index2
) const
```


### function get

```
double get(
    const Par::Tags partype,
    const std::string & mass,
    const int index1,
    const int index2
) const
```


### function has

```
bool has(
    const Par::Tags partype,
    const int pdg_code,
    const int context
) const
```

PDB getter/checker overloads. 

### function get

```
double get(
    const Par::Tags partype,
    const int pdg_code,
    const int context
) const
```


### function has

```
bool has(
    const Par::Tags partype,
    const std::pair< int, int > pdgpr
) const
```


### function get

```
double get(
    const Par::Tags partype,
    const std::pair< int, int > pdgpr
) const
```


### function has

```
bool has(
    const Par::Tags partype,
    const std::pair< str, int > shortpr
) const
```


### function get

```
double get(
    const Par::Tags partype,
    const std::pair< str, int > shortpr
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const std::string & mass
) const
```

Getters which first check the sanity of the thing they are returning. 

### function safeget

```
double safeget(
    const Par::Tags partype,
    const std::string & mass,
    const int index
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const int pdg_code,
    const int context
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const std::pair< int, int > pdgpr
) const
```


### function safeget

```
double safeget(
    const Par::Tags partype,
    const std::pair< str, int > shortpr
) const
```


### function Wolf2V_ud

```
static double Wolf2V_ud(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_ud standard parameterisation convertor. 

CKM Wolfenstein (lambda, A, rhobar, etabar) --> V_qq standard parameterisation convertors 


### function Wolf2V_us

```
static double Wolf2V_us(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_us standard parameterisation convertor. 

### function Wolf2V_ub

```
static std::complex< double > Wolf2V_ub(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_ub standard parameterisation convertor. 

### function Wolf2V_cd

```
static std::complex< double > Wolf2V_cd(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_cd standard parameterisation convertor. 

### function Wolf2V_cs

```
static std::complex< double > Wolf2V_cs(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_cs standard parameterisation convertor. 

### function Wolf2V_cb

```
static double Wolf2V_cb(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_cb standard parameterisation convertor. 

### function Wolf2V_td

```
static std::complex< double > Wolf2V_td(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_td standard parameterisation convertor. 

### function Wolf2V_ts

```
static std::complex< double > Wolf2V_ts(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_ts standard parameterisation convertor. 

### function Wolf2V_tb

```
static double Wolf2V_tb(
    double l,
    double A,
    double rhobar,
    double etabar
)
```

CKM Wolfenstein --> V_tb standard parameterisation convertor. 

### function RunBothToScale

```
void RunBothToScale(
    double scale
)
```


Linked running Only possible with non-const object

Overloads for PDG types These just convert the types and then call the properly defined functions Linked running Only possible with non-const object 


### function check_mass_cuts

```
void check_mass_cuts()
```

Check the that the spectrum satisifies any mass cuts requested from the yaml file. 

### function getSLHAea

```
SLHAstruct getSLHAea(
    int slha_version
) const
```


SLHAea object getter First constructs an SLHAea object from the SMINPUTS object, then adds the info from the LE subspectrum (if possible), followed by the HE subspectrum (if possible). Any duplicate entries are overwritten at each step, so HE takes precendence over LE, and LE takes precedence over SMINPUTS. 


### function writeSLHAfile

```
void writeSLHAfile(
    int slha_version,
    const str & filename
) const
```

Output spectrum contents as an SLHA file, using getSLHAea. 

### function drop_SLHAs_if_requested

```
void drop_SLHAs_if_requested(
    const safe_ptr< Options > & runOptions,
    const str & default_name
)
```

Helper function to drop SLHA files. 

### function PDG_translator

```
const std::map< int, int > & PDG_translator() const
```

PDG code translation map, for special cases where an SLHA file has been read in and the PDG codes changed. 

## Friends

### friend swap

```
friend void swap(
    Spectrum & first,

    Spectrum & second
);
```

Friend function: swap resources of two [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) objects. 

Swap resources of two [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) objects Note: Not a member function! This is an external function which is a friend of the [Spectrum](/documentation/code/classes/classgambit_1_1spectrum/) class. 


-------------------------------

Updated on 2024-05-31 at 15:12:03 +0000