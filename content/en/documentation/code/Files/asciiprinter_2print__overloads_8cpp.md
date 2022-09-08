---
title: "file asciiprinter/asciiprinter/print_overloads.cpp"

description: "[No description available]"

---

# file asciiprinter/asciiprinter/print_overloads.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[ASIMPLEPRINT](/documentation/code/files/asciiprinter_2print__overloads_8cpp/#define-asimpleprint)**(r, data, elem) <br>Macros to add all the simple print functions that just use the above templates.  |
|  | **[ASIMPLEPRINT_VEC](/documentation/code/files/asciiprinter_2print__overloads_8cpp/#define-asimpleprint-vec)**(r, data, elem)  |
|  | **[ADD_ASCII_SIMPLE_PRINTS](/documentation/code/files/asciiprinter_2print__overloads_8cpp/#define-add-ascii-simple-prints)**(TYPES)  |
|  | **[ADD_ASCII_VECTOR_PRINTS](/documentation/code/files/asciiprinter_2print__overloads_8cpp/#define-add-ascii-vector-prints)**(TYPES)  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@monash.edu.au](mailto:benjamin.farmer@monash.edu.au)) 
  * Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 


**Date**: 

  * 2013 Jul, Sep, 2014 Jan
  * 2014 Jan 
  * 2017 Mar


ASCII printer print function overloads. Add a new overload of the _print function in this file if you want to be able to print a new type.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define ASIMPLEPRINT

```
#define ASIMPLEPRINT(
    r,
    data,
    elem
)
      void asciiPrinter::_print(elem const& value, const std::string& label, \
                           const int IDcode, const uint rank, \
                           const ulong pointID) \
      { \
        template_print(value,label,IDcode,rank,pointID); \
      }
```

Macros to add all the simple print functions that just use the above templates. 

### define ASIMPLEPRINT_VEC

```
#define ASIMPLEPRINT_VEC(
    r,
    data,
    elem
)
      void asciiPrinter::_print(elem const& value, const std::string& label, \
                           const int IDcode, const uint rank, \
                           const ulong pointID) \
      { \
        template_print_vec(value,label,IDcode,rank,pointID); \
      }
```


### define ADD_ASCII_SIMPLE_PRINTS

```
#define ADD_ASCII_SIMPLE_PRINTS(
    TYPES
)
BOOST_PP_SEQ_FOR_EACH(ASIMPLEPRINT, _, TYPES)
```


### define ADD_ASCII_VECTOR_PRINTS

```
#define ADD_ASCII_VECTOR_PRINTS(
    TYPES
)
BOOST_PP_SEQ_FOR_EACH(ASIMPLEPRINT_VEC, _, TYPES)
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  ASCII printer print function overloads.
///  Add a new overload of the _print function
///  in this file if you want to be able to print
///  a new type.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@monash.edu.au)
///  \date 2013 Jul, Sep, 2014 Jan
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2014 Jan
///  \date 2017 Mar
///
///  *********************************************

#include "gambit/Printers/printers/asciiprinter.hpp"
#include "gambit/Printers/printers/common_print_overloads.hpp"

namespace Gambit
{

  namespace Printers
  {

    /// @{ PRINT FUNCTIONS
    /// Need to define one of these for every type we want to print!
    /// Could use macros again to generate identical print functions
    /// for all types that have a << operator already defined.

    /// Template for print functions of "simple" types
    template<class T>
    void asciiPrinter::template_print(T const& value, const std::string& label, const int IDcode, const uint thread, const ulong pointID)
    {
      std::vector<double> vdvalue(1,value); // For now everything has to end up as a vector of doubles
      std::vector<std::string> labels(1,label);
      addtobuffer(vdvalue,labels,IDcode,thread,pointID);
    }

    /// Template for print functions of vectors of "simple" types
    template<class T>
    void asciiPrinter::template_print_vec(std::vector<T> const& value, const std::string& label, const int IDcode, const uint thread, const ulong pointID)
    {
      std::vector<std::string> labels;
      std::vector<double> d_values; // Values need to be converted to doubles for printing with asciiPrinter.
      labels.reserve(value.size());
      d_values.reserve(value.size());
      for(unsigned int i=0;i<value.size();i++)
      {
        // Might want to find some way to avoid doing this every single loop, seems kind of wasteful.
        std::stringstream ss;
        ss<<label<<"["<<i<<"]";
        labels.push_back(ss.str());
        d_values.push_back(value.at(i)); // Convert to double
      }
      addtobuffer(d_values,labels,IDcode,thread,pointID);
    }

    /// Macros to add all the simple print functions that just use the above templates
    #define ASIMPLEPRINT(r,data,elem) \
      void asciiPrinter::_print(elem const& value, const std::string& label, \
                           const int IDcode, const uint rank, \
                           const ulong pointID) \
      { \
        template_print(value,label,IDcode,rank,pointID); \
      }
    #define ASIMPLEPRINT_VEC(r,data,elem) \
      void asciiPrinter::_print(elem const& value, const std::string& label, \
                           const int IDcode, const uint rank, \
                           const ulong pointID) \
      { \
        template_print_vec(value,label,IDcode,rank,pointID); \
      }

    #define ADD_ASCII_SIMPLE_PRINTS(TYPES) BOOST_PP_SEQ_FOR_EACH(ASIMPLEPRINT, _, TYPES)
    #define ADD_ASCII_VECTOR_PRINTS(TYPES) BOOST_PP_SEQ_FOR_EACH(ASIMPLEPRINT_VEC, _, TYPES)
    ADD_ASCII_SIMPLE_PRINTS(SCANNER_SIMPLE_TYPES)
    ADD_ASCII_VECTOR_PRINTS(SCANNER_VECTOR_TYPES)

    void asciiPrinter::_print(map_str_dbl const& value, const std::string& label, const int IDcode, const uint thread, const ulong pointID)
    {
      std::vector<std::string> names;
      std::vector<double> vdvalue;
      names.reserve(value.size());
      vdvalue.reserve(value.size());
      for (map_str_dbl::const_iterator it = value.begin(); it != value.end(); it++)
      {
        std::stringstream ss;
        ss<<label<<"::"<<it->first;
        names.push_back( ss.str() );
        vdvalue.push_back( it->second );
      }
      addtobuffer(vdvalue,names,IDcode,thread,pointID);
    }

    void asciiPrinter::_print(map_intpair_dbl const& value, const std::string& label, const int IDcode, const uint thread, const ulong pointID)
    {
      std::vector<std::string> channels;
      std::vector<double> vdvalue;
      channels.reserve(value.size());
      vdvalue.reserve(value.size());
      for (map_intpair_dbl::const_iterator it = value.begin(); it != value.end(); it++)
      {
        std::stringstream ss;
        ss<<label<<"::"<<it->first.first<<it->first.second;
        channels.push_back( ss.str() );
        vdvalue.push_back( it->second );
      }
      addtobuffer(vdvalue,channels,IDcode,thread,pointID);
    }

    // Piggyback off existing print functions to build standard overloads
    USE_COMMON_PRINT_OVERLOAD(asciiPrinter, ModelParameters)
    USE_COMMON_PRINT_OVERLOAD(asciiPrinter, triplet<double>)
    #ifndef SCANNER_STANDALONE
      USE_COMMON_PRINT_OVERLOAD(asciiPrinter, DM_nucleon_couplings)
      USE_COMMON_PRINT_OVERLOAD(asciiPrinter, BBN_container)
    #endif

    /// @}

  }
}
```


-------------------------------

Updated on 2022-09-08 at 02:23:03 +0000
