---
title: "file SimpleSpectra/SLHASimpleSpec.cpp"

description: "[No description available]"

---

# file SimpleSpectra/SLHASimpleSpec.cpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[addtomap_EL](/documentation/code/files/slhasimplespec_8cpp/#define-addtomap-el)**(r, PRODUCT) <br>Macro to help assign the same function pointers to multiple string keys.  |
|  | **[addtomap](/documentation/code/files/slhasimplespec_8cpp/#define-addtomap)**(__KEYS, FPTR)  |




## Macros Documentation

### define addtomap_EL

```
#define addtomap_EL(
    r,
    PRODUCT
)
{                                                                       \
   str key      = BOOST_PP_SEQ_ELEM(0,PRODUCT); /* string map key */    \
   tmp_map[key] = BOOST_PP_SEQ_ELEM(1,PRODUCT); /* function pointer */  \
}
```

Macro to help assign the same function pointers to multiple string keys. 

**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 
  * Tomas Gonzalo ([tomas.gonzalo@monash.edu](mailto:tomas.gonzalo@monash.edu)) 


**Date**: 

  * 2015 Apr
  * 2016 Oct
  * 2020 Mar




------------------

Authors:



------------------


### define addtomap

```
#define addtomap(
    __KEYS,
    FPTR
)
BOOST_PP_SEQ_FOR_EACH_PRODUCT(addtomap_EL, (BOOST_PP_TUPLE_TO_SEQ(__KEYS))((FPTR)) )
```


## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
//
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 Apr
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2016 Oct
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@monash.edu)
///  \date 2020 Mar
///
///  *********************************************

#include "gambit/Models/SimpleSpectra/SLHASimpleSpec.hpp"

#include <boost/preprocessor/tuple/to_seq.hpp>
#include <boost/preprocessor/seq/elem.hpp>
#include <boost/preprocessor/seq/for_each_product.hpp>

/// Macro to help assign the same function pointers to multiple string keys
// Relies on "tmp_map" being used as the variable name for the temporary maps
// inside the fill_map functions.
#define addtomap_EL(r, PRODUCT)                                         \
{                                                                       \
   str key      = BOOST_PP_SEQ_ELEM(0,PRODUCT); /* string map key */    \
   tmp_map[key] = BOOST_PP_SEQ_ELEM(1,PRODUCT); /* function pointer */  \
}

#define addtomap(__KEYS,FPTR) BOOST_PP_SEQ_FOR_EACH_PRODUCT(addtomap_EL, (BOOST_PP_TUPLE_TO_SEQ(__KEYS))((FPTR)) )

using namespace SLHAea;

namespace Gambit
{

      /// @{ Member functions for SLHAeaModel class

      /// Default Constructor
      SLHAeaModel::SLHAeaModel()
        : data()
      {}

      /// Constructor via SLHAea object
      SLHAeaModel::SLHAeaModel(const SLHAea::Coll& input)
        : data(input)
      {
         // No idea what kind of model this is, so cannot set valid slha_version. Use "0" for "unknown" or "n/a"
         // If you write a model-specific derived class from this, be sure to add a sensible check for this and
         // overwrite what we set here in the base class.
         wrapped_slha_version = 0;
      }

      /// Get the SLHA version of the internal SLHAea object
      int SLHAeaModel::slha_version() const { return wrapped_slha_version; }

      /// Get reference to internal SLHAea object
      const SLHAea::Coll& SLHAeaModel::get_slhaea() const { return data; }

      /// PDG code translation map, for special cases where an SLHA file has been read in and the PDG codes changed.
      const std::map<int, int>& SLHAeaModel::PDG_translator() const
      {
        return PDG_translation_map;
      }

      /// @{ Helper functions to do error checking for SLHAea object contents

      /// One index
      double SLHAeaModel::getdata(const std::string& block, int index) const
      {
         double output = 0.0;
         try
         {
           output = to<double>(data.at(block).at(index).at(1));
         }
         catch (const std::out_of_range& e)
         {
           std::ostringstream errmsg;
           errmsg << "Error accessing data at index "<<index<<" of block "<<block<<". Please check that the SLHAea object was properly filled." << std::endl;
           errmsg  << "(Received out_of_range error from SLHAea class with message: " << e.what() << ")";
           utils_error().raise(LOCAL_INFO,errmsg.str());
         }
         return output;
      }

      /// Two indices
      double SLHAeaModel::getdata(const std::string& block, int i, int j) const
      {
         double output = 0.0;
         try
         {
           output = to<double>(data.at(block).at(i,j).at(2));
         }
         catch (const std::out_of_range& e)
         {
           std::ostringstream errmsg;
           errmsg << "Error accessing data at index "<<i<<","<<j<<" of block "<<block<<". Please check that the SLHAea object was properly filled." << std::endl;
           errmsg  << "(Received out_of_range error from SLHAea class with message: " << e.what() << ")";
           utils_error().raise(LOCAL_INFO,errmsg.str());
         }
         return output;
      }

      // Check if block and entry exist, 1 index
      bool SLHAeaModel::checkdata(const std::string& block, int i) const
      {
        if (data.find(block) == data.end()) return false;

        SLHAea::Block::key_type key(1);
        key[0] = std::to_string(i);
        if (data.at(block).find(key) != data.at(block).end())
          return true;

        return false;
      }

      /// @}

      /// @}


} // end Gambit namespace
```


-------------------------------

Updated on 2024-05-31 at 15:12:06 +0000
