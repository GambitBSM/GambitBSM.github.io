---
title: "file printers/asciireader.hpp"

description: "[No description available]"

---

# file printers/asciireader.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::Printers](/documentation/code/namespaces/namespacegambit_1_1printers/)** <br>Forward declaration.  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::Printers::asciiReader](/documentation/code/classes/classgambit_1_1printers_1_1asciireader/)** <br>Derived EntryGetterInterface class for accessing [asciiPrinter](/documentation/code/classes/classgambit_1_1printers_1_1asciiprinter/) output points.  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[DECLARE_RETRIEVE](/documentation/code/files/asciireader_8hpp/#define-declare-retrieve)**(r, data, i, elem)  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@monash.edu.au](mailto:benjamin.farmer@monash.edu.au)) 

**Date**: 2016 Jan

Ascii printer retriever class declaration This is a class accompanying the asciiPrinter which takes care of _reading_ from output created by the asciiPrinter.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define DECLARE_RETRIEVE

```
#define DECLARE_RETRIEVE(
    r,
    data,
    i,
    elem
)
bool _retrieve(elem&, const std::string&, const uint, const ulong);
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Ascii printer retriever class declaration
///  This is a class accompanying the asciiPrinter
///  which takes care of *reading* from output
///  created by the asciiPrinter.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Ben Farmer
///          (benjamin.farmer@monash.edu.au)
///  \date 2016 Jan
///
///  *********************************************

#include "gambit/Printers/baseprinter.hpp"
#include "gambit/Printers/printers/asciitypes.hpp"
#include <boost/preprocessor/seq/for_each_i.hpp>

#ifndef __ascii_reader_hpp__
#define __ascii_reader_hpp__

namespace Gambit
{
  namespace Printers
  {

     /// Derived EntryGetterInterface class for accessing asciiPrinter output points
     class asciiReader : public BaseReader
     {
       public:
         asciiReader(const Options& options);

         /// @{ Base class virtual interface functions
         virtual void reset(); // Reset 'read head' position to first entry
         virtual ulong get_dataset_length(); // Get length of input dataset
         virtual PPIDpair get_next_point(); // Get next rank/ptID pair in data file
         virtual PPIDpair get_current_point(); // Get current rank/ptID pair in data file
         virtual ulong    get_current_index(); // Get a linear index which corresponds to the current rank/ptID pair in the iterative sense
         virtual bool eoi(); // Check if 'current point' is past the end of the data file (and thus invalid!)
         /// Get type information for a data entry, i.e. defines the C++ type which this should be
         /// retrieved as, not what it is necessarily literally stored as in the output.
         /// For ASCIIPrinter, everything is currently a double.
         virtual std::size_t get_type(const std::string&) { return getTypeID<double>(); }
         virtual std::set<std::string> get_all_labels(); // Get all output column labels
         /// @}

         ///@{ Retrieval functions
         using BaseReader::_retrieve; // Tell compiler we are using some of the base class overloads of this on purpose.
         #define DECLARE_RETRIEVE(r,data,i,elem) bool _retrieve(elem&, const std::string&, const uint, const ulong);
         BOOST_PP_SEQ_FOR_EACH_I(DECLARE_RETRIEVE, , ASCII_TYPES)
         #ifndef SCANNER_STANDALONE
           BOOST_PP_SEQ_FOR_EACH_I(DECLARE_RETRIEVE, , ASCII_BACKEND_TYPES)
         #endif
         #undef DECLARE_RETRIEVE
         ///@}

       private:
         const std::string infoFile_name;
         const std::string dataFile_name;
         const std::map<std::string,uint> column_map; // Map from column names to indices
         const uint col_rank;
         const uint col_ptID;
         std::ifstream dataFile;
         ulong       dataset_length;
         ulong       current_row;
         PPIDpair    current_point;
         std::string current_line;

         /// Get column descriptions from an info file
         std::map<std::string,uint> get_column_info(const std::string& info_filename);

         /// Move 'read head' forward to next row
         void next_row();

         /// Advance the 'read head' position for output retrieval until the requested rank/pointID entry is found
         void advance_to_point(const PPIDpair& target_point);

     };

    // Register reader so it can be constructed via inifile instructions
    // First argument is string label for inifile access, second is class from which to construct printer
    LOAD_READER(ascii, asciiReader)
  }
}

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
