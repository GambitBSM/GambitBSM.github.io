---
title: "file Elements/translator.hpp"

description: "[No description available]"

---

# file Elements/translator.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Utils](/documentation/code/namespaces/namespacegambit_1_1utils/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Utils::translator](/documentation/code/classes/classgambit_1_1utils_1_1translator/)**  |

## Detailed Description


**Author**: Pat Scott ([pat.scott@uq.edu.au](mailto:pat.scott@uq.edu.au)) 

**Date**: 2020 Feb

A simple container for storing and looking up equivalent terms in an arbitrary number of languages, using [YAML](/documentation/code/namespaces/namespaceyaml/).



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  A simple container for storing and looking up
///  equivalent terms in an arbitrary number of
///  languages, using YAML.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (pat.scott@uq.edu.au)
///  \date 2020 Feb
///
///  *********************************************

#include <map>
#include <vector>

#include "gambit/Utils/util_types.hpp"

namespace Gambit
{
  namespace Utils
  {

    class translator
    {

      private:

        /// Set of supported languages
        std::vector<str> languages;

        /// Actual database of terms
        std::map<str, std::vector<str>> rosetta;

      public:

        /// Constructor for translator
        translator(const str& filename_);

        /// Translate terms from one language to another.
        /// @{
        str operator()(const str& from, const str& to, const str& obs);
        str operator()(const str& from, const str& to, const str& obs, const str& suffix);
        std::vector<str> operator()(const str& from, const str& to, const std::vector<str>& obs);
        std::vector<str> operator()(const str& from, const str& to, const std::vector<str>& obs, const str& suffix);
        /// @}

    };


  }
}
```


-------------------------------

Updated on 2025-02-12 at 15:36:41 +0000
