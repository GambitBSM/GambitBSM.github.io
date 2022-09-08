---
title: "class Gambit::SubSpectrumContents"
description: "Base class for defining the required contents of a [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object. "

---

# class Gambit::SubSpectrumContents



Base class for defining the required contents of a [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object. 


`#include <subspectrum_contents.hpp>`

Inherited by [Gambit::SpectrumContents::DMEFT](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1dmeft/), [Gambit::SpectrumContents::DiracSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1diracsingletdm__z2/), [Gambit::SpectrumContents::MDM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1mdm/), [Gambit::SpectrumContents::MSSM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1mssm/), [Gambit::SpectrumContents::MajoranaSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1majoranasingletdm__z2/), [Gambit::SpectrumContents::SM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1sm/), [Gambit::SpectrumContents::SMHiggs](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1smhiggs/), [Gambit::SpectrumContents::SM_slha](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1sm__slha/), [Gambit::SpectrumContents::ScalarSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1scalarsingletdm__z2/), [Gambit::SpectrumContents::ScalarSingletDM_Z3](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1scalarsingletdm__z3/), [Gambit::SpectrumContents::VectorSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1vectorsingletdm__z2/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| std::string | **[getName](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-getname)**() const |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_parameters](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-parameters)**() const<br>Function to retreive all parameters.  |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_parameters_with_tag](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-parameters-with-tag)**([Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag) const<br>Function to retreive all parameters matching a certain tag.  |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_parameters_with_tag_and_shape](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-parameters-with-tag-and-shape)**([Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, std::vector< int > & shape) const<br>Function to retrieve all parameters matching a certain tag and shape.  |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_BSM_parameters](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-bsm-parameters)**() const<br>Function to retrieve all parameters whose blockName is not SMINPUTS, YUKAWA, CKMBLOCK, or empty.  |
| void | **[verify_contents](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-verify-contents)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & spec) const<br>Function to verify that a [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) wrapper contains everything that this class says it should.  |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[addParameter](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-addparameter)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, const std::string & name, const std::vector< int > & shape =initVector(1), const std::string & blockname ="", const int index =0)<br>Add a parameter to the Contents object.  |
| void | **[setName](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-setname)**(const std::string & name)<br>Set the name of this Contents object (i.e. the name of the model to which this spectrum data applies)  |

## Public Functions Documentation

### function getName

```
inline std::string getName() const
```


### function all_parameters

```
std::vector< SpectrumParameter > all_parameters() const
```

Function to retreive all parameters. 

### function all_parameters_with_tag

```
std::vector< SpectrumParameter > all_parameters_with_tag(
    Par::Tags tag
) const
```

Function to retreive all parameters matching a certain tag. 

### function all_parameters_with_tag_and_shape

```
std::vector< SpectrumParameter > all_parameters_with_tag_and_shape(
    Par::Tags tag,
    std::vector< int > & shape
) const
```

Function to retrieve all parameters matching a certain tag and shape. 

### function all_BSM_parameters

```
std::vector< SpectrumParameter > all_BSM_parameters() const
```

Function to retrieve all parameters whose blockName is not SMINPUTS, YUKAWA, CKMBLOCK, or empty. 

Function to retrieve all parameters whose blockname is not SMINPUTS, YUKAWA, CKMBLOCK, or empty. 


### function verify_contents

```
void verify_contents(
    const SubSpectrum & spec
) const
```

Function to verify that a [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) wrapper contains everything that this class says it should. 

Verify that the supplied [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) object conforms to the requirements specified by the Contents class. 


## Protected Functions Documentation

### function addParameter

```
void addParameter(
    const Par::Tags tag,
    const std::string & name,
    const std::vector< int > & shape =initVector(1),
    const std::string & blockname ="",
    const int index =0
)
```

Add a parameter to the Contents object. 

### function setName

```
void setName(
    const std::string & name
)
```

Set the name of this Contents object (i.e. the name of the model to which this spectrum data applies) 

-------------------------------

Updated on 2022-09-08 at 03:46:43 +0000