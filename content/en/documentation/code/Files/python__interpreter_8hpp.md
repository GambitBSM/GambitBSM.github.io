---
title: "file Utils/python_interpreter.hpp"

description: "[No description available]"

---

# file Utils/python_interpreter.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Utils](/documentation/code/namespaces/namespacegambit_1_1utils/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Utils::python_interpreter_guard](/documentation/code/classes/classgambit_1_1utils_1_1python__interpreter__guard/)** <br>Dummy guard class for python interpreters when python support is turned off.  |

## Detailed Description


**Author**: Pat Scott ([patrickcolinscott@gmail.com](mailto:patrickcolinscott@gmail.com)) 

**Date**: 2023 Jun

Singleton class for holding the python interpreter instance.



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Singleton class for holding the python 
///  interpreter instance.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patrickcolinscott@gmail.com)
///  \date 2023 Jun
///
///  *********************************************

#pragma once

#include "gambit/cmake/cmake_variables.hpp"
#include "gambit/Utils/util_macros.hpp"

#ifndef HAVE_PYBIND11

  namespace Gambit
  { 
    namespace Utils
    {
      /// Dummy guard class for python interpreters when python support is turned off. 
      class EXPORT_SYMBOLS python_interpreter_guard {};
    }
  }  

#else

  #include "gambit/Utils/begin_ignore_warnings_pybind11.hpp"
  #include <pybind11/pybind11.h>
  #include "gambit/Utils/end_ignore_warnings.hpp"

  namespace pybind11
  {
    class scoped_interpreter;
  }
  
  namespace Gambit
  {
  
    namespace Utils
    {
  
      /// A singleton class that holds a pointer to the python interpreter. 
      class EXPORT_SYMBOLS python_interpreter
      {
      
        public:
      
          /// Singleton accessor function 
          static python_interpreter& get();
    
          /// sys module loaded at construction time
          pybind11::module* sys;
      
          /// os module loaded at construction time
          pybind11::module* os;
    
        private:
      
          /// Regular constructor. No access as it is private.
          python_interpreter();
          
          /// Regular destructor. No access as it is private.
          ~python_interpreter();
    
          /// Shut off access to copy constructor by making it private
          python_interpreter (const python_interpreter&);
    
          /// Shut off access to assignment operator by making it private 
          const python_interpreter& operator= (const python_interpreter&);
      
          /// Pointer to the Python interpreter
          pybind11::scoped_interpreter* iptr;
      
      };
    
      /// Guard class for python interpreters 
      class EXPORT_SYMBOLS python_interpreter_guard
      {
        public:
          /// Constructor just gets interpreter object
          python_interpreter_guard();
      };
      
    }
  
  }

#endif
```


-------------------------------

Updated on 2024-07-18 at 13:53:32 +0000
