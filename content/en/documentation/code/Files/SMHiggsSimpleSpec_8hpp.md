---
title: "file SimpleSpectra/SMHiggsSimpleSpec.hpp"

description: "[No description available]"

---

# file SimpleSpectra/SMHiggsSimpleSpec.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::SpecBit](/documentation/code/namespaces/namespacegambit_1_1specbit/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::SpecBit::SMHiggsModel](/documentation/code/classes/structgambit_1_1specbit_1_1smhiggsmodel/)**  |
| struct | **[Gambit::SpecTraits< SpecBit::SMHiggsSimpleSpec >](/documentation/code/classes/structgambit_1_1spectraits_3_01specbit_1_1smhiggssimplespec_01_4/)** <br>Specialisation of traits class needed to inform base spectrum class of the Model and Input types.  |
| class | **[Gambit::SpecBit::SMHiggsSimpleSpec](/documentation/code/classes/classgambit_1_1specbit_1_1smhiggssimplespec/)** <br>[SubSpectrum](/documentation/code/classes/classgambit_1_1subspectrum/) wrapper class for the SM Higgs sector.  |

## Detailed Description


**Author**: Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 

**Date**: 2015 May

A simple SubSpectrum wrapper for Standard Model Higgs information. No RGEs included.



------------------

Authors:



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  A simple SubSpectrum wrapper for Standard
///  Model Higgs information. No RGEs included.
///
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2015 May
///
///  *********************************************

#ifndef __SMHiggsSimpleSpec_hpp__
#define __SMHiggsSimpleSpec_hpp__

#include "gambit/Elements/spec.hpp"
#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit
{
   namespace SpecBit
   {
      /// Simple container "model object" for the SM Higgs sector variables.
      /// We will derived from this for simple extensions, like for scalar singlet DM
      struct SMHiggsModel
      {
         double HiggsPoleMass;
         double HiggsVEV;

         double get_HiggsPoleMass()  const { return HiggsPoleMass; }
         double get_HiggsVEV()       const { return HiggsVEV;      }
         double get_HiggsPoleMass_1srd_high()  const { return 0; }
         double get_HiggsPoleMass_1srd_low()  const { return 0; }
      };

      class SMHiggsSimpleSpec;
   }

   /// Specialisation of traits class needed to inform base spectrum class of the Model and Input types
   template <>
   struct SpecTraits<SpecBit::SMHiggsSimpleSpec>
   {
        static std::string name() { return "SMHiggsSimpleSpec"; }
        typedef SpectrumContents::SMHiggs Contents;
        typedef SpecBit::SMHiggsModel Model;
        typedef DummyInput            Input; // DummyInput is just an empty struct
   };

   namespace SpecBit
   {
      /// SubSpectrum wrapper class for the SM Higgs sector
      class SMHiggsSimpleSpec : public Spec<SMHiggsSimpleSpec>
      {
         private:
            /// Store the struct containing the parameters plus get/set functions
            Model model;

            /// Just a placeholder required by the base class; this wrapper doesn't use it
            Input input;

         public:
            /// Constructor
            SMHiggsSimpleSpec(const Model& m)
              : model(m)
              , input()
            {}

            // Functions to interface Model and Input objects with the base 'Spec' class
            Model& get_Model() { return model; }
            Input& get_Input() { return input; }
            const Model& get_Model() const { return model; }
            const Input& get_Input() const { return input; }

            /// Map fillers
            /// Used to initialise maps in the RunparDer and PhysDer classes
            /// (specialisations created and stored automatically by Spec<QedQcdWrapper>)

            /// Definitions of map fillers
            static GetterMaps fill_getter_maps()
            {
               GetterMaps map_collection;

               map_collection[Par::mass1].map0["vev"] = &Model::get_HiggsVEV;
               map_collection[Par::Pole_Mass].map0["h0_1"] = &Model::get_HiggsPoleMass;
               map_collection[Par::Pole_Mass_1srd_high].map0["h0_1"]    = &Model::get_HiggsPoleMass_1srd_high;
               map_collection[Par::Pole_Mass_1srd_low].map0["h0_1"]    = &Model::get_HiggsPoleMass_1srd_low;


               return map_collection;
            }

     };


   } // end SpecBit namespace
} // end Gambit namespace

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
