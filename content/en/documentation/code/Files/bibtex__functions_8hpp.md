---
title: "file Utils/bibtex_functions.hpp"

description: "[No description available]"

---

# file Utils/bibtex_functions.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::BibTeX](/documentation/code/classes/classgambit_1_1bibtex/)**  |

## Detailed Description


**Author**: Tomas Gonzalo ([gonzalo@physik.rwth-aachen.de](mailto:gonzalo@physik.rwth-aachen.de)) 

**Date**: 2021 Sep

Utility functions and classes for bibtex files



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Utility functions and classes for bibtex files
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Tomas Gonzalo
///          (gonzalo@physik.rwth-aachen.de)
///  \date 2021 Sep
///
///  *********************************************


#ifndef __bibtex_functions_hpp__
#define __bibtex_functions_hpp__

#include <vector>
#include <fstream>

#include "gambit/Utils/util_types.hpp"

namespace Gambit
{

  class BibTeX
  {
     private:

       str _filename;
       std::vector<str> _bibtex_entries;
       std::map<str,std::map<str,str> > _bibtex_data;

     public:

       // Constructor
       BibTeX(str);

       // Return filename
       const str filename() const;

       // Get the list of bibtex entries on a bibtex file
       const std::vector<str> getBibTeXEntries() const;

       // Get the bibtex data
       const std::map<str,std::map<str,str>> getBibTeXData() const;

       // Drop a bibtex file with all stored data
       void dropBibTeXFile(str) const;

       // Drop a bibtex file only with given set of keys
       void dropBibTeXFile(std::vector<str>&, str) const;

       // Drop a sample tex file citing a given set of keys
       void dropTeXFile(std::vector<str>&, str, str) const;

       // Static function to add a citation key to a list of keys
       static void addCitationKey(std::vector<str>&, str);
  };
}

#endif //defined __bibtex_functions_hpp__
```


-------------------------------

Updated on 2023-06-26 at 21:36:53 +0000
