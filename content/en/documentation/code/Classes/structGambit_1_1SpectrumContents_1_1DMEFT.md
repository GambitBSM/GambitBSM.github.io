---
title: "struct Gambit::SpectrumContents::DMEFT"

description: "[No description available]"

---

# struct Gambit::SpectrumContents::DMEFT



[No description available]

Inherits from [Gambit::SubSpectrumContents](/documentation/code/classes/classgambit_1_1subspectrumcontents/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[DMEFT](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1dmeft/#function-dmeft)**() |

## Additional inherited members

**Public Functions inherited from [Gambit::SubSpectrumContents](/documentation/code/classes/classgambit_1_1subspectrumcontents/)**

|                | Name           |
| -------------- | -------------- |
| std::string | **[getName](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-getname)**() const |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_parameters](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-parameters)**() const<br>Function to retreive all parameters.  |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_parameters_with_tag](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-parameters-with-tag)**([Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag) const<br>Function to retreive all parameters matching a certain tag.  |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_parameters_with_tag_and_shape](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-parameters-with-tag-and-shape)**([Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, std::vector< int > & shape) const<br>Function to retrieve all parameters matching a certain tag and shape.  |
| std::vector< [SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/) > | **[all_BSM_parameters](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-all-bsm-parameters)**() const<br>Function to retrieve all parameters whose blockName is not SMINPUTS, YUKAWA, CKMBLOCK, or empty.  |
| void | **[verify_contents](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-verify-contents)**(const [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) & spec) const<br>Function to verify that a [SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) wrapper contains everything that this class says it should.  |

**Protected Functions inherited from [Gambit::SubSpectrumContents](/documentation/code/classes/classgambit_1_1subspectrumcontents/)**

|                | Name           |
| -------------- | -------------- |
| void | **[addParameter](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-addparameter)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-tags) tag, const std::string & name, const std::vector< int > & shape =initVector(1), const std::string & blockname ="", const int index =0)<br>Add a parameter to the Contents object.  |
| void | **[setName](/documentation/code/classes/classgambit_1_1subspectrumcontents/#function-setname)**(const std::string & name)<br>Set the name of this Contents object (i.e. the name of the model to which this spectrum data applies)  |


## Public Functions Documentation

### function DMEFT

```
DMEFT()
```


-------------------------------

Updated on 2022-09-08 at 03:17:34 +0000