---
title: "class Gambit::SpectrumParameter"
description: "Simple class to contain information defining how some parameter in a [SubSpectrum]() object can be accessed. "

---

# class Gambit::SpectrumParameter



Simple class to contain information defining how some parameter in a [SubSpectrum]() object can be accessed. 


`#include <subspectrum_contents.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SpectrumParameter](/documentation/code/classes/classgambit_1_1spectrumparameter/#function-gambitspectrumparameter-spectrumparameter)**(const [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) tag, const std::string label, const std::vector< int > shape, const std::string blockname, const int blockindex) |
| [Par::Tags](/documentation/code/namespaces/namespacegambit_1_1par/#enum-gambitpar-tags) | **[tag](/documentation/code/classes/classgambit_1_1spectrumparameter/#function-gambitspectrumparameter-tag)**() const |
| std::string | **[name](/documentation/code/classes/classgambit_1_1spectrumparameter/#function-gambitspectrumparameter-name)**() const |
| std::vector< int > | **[shape](/documentation/code/classes/classgambit_1_1spectrumparameter/#function-gambitspectrumparameter-shape)**() const |
| std::string | **[blockname](/documentation/code/classes/classgambit_1_1spectrumparameter/#function-gambitspectrumparameter-blockname)**() const |
| int | **[blockindex](/documentation/code/classes/classgambit_1_1spectrumparameter/#function-gambitspectrumparameter-blockindex)**() const |

## Public Functions Documentation

### function SpectrumParameter

```
inline SpectrumParameter(
    const Par::Tags tag,
    const std::string label,
    const std::vector< int > shape,
    const std::string blockname,
    const int blockindex
)
```


### function tag

```
inline Par::Tags tag() const
```


### function name

```
inline std::string name() const
```


### function shape

```
inline std::vector< int > shape() const
```


### function blockname

```
inline std::string blockname() const
```


### function blockindex

```
inline int blockindex() const
```


-------------------------------

Updated on 2022-09-08 at 01:48:54 +0000