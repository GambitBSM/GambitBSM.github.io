---
title: "file SpectrumContents/Models/src/SpectrumContents/VectorSingletDM.cpp"

description: "[No description available]"

---

# file SpectrumContents/Models/src/SpectrumContents/VectorSingletDM.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: 

  * Ankit Beniwal ([ankit.beniwal@adelaide.edu.au](mailto:ankit.beniwal@adelaide.edu.au)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2016 Sep, 2017 Jun
  * 2018 Sep


Class defining the parameters that SubSpectrum objects providing VectorSingletDM spectra data must provide



------------------

Authors:



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Class defining the parameters that SubSpectrum
///  objects providing VectorSingletDM spectra
///  data must provide
///
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Ankit Beniwal
///          (ankit.beniwal@adelaide.edu.au)
///  \date 2016 Sep, 2017 Jun
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2018 Sep
///
///  *********************************************

#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit
{

  SpectrumContents::VectorSingletDM_Z2::VectorSingletDM_Z2()
  {
     setName("VectorSingletDM_Z2");

     // shape prototypes
     std::vector<int> m3x3 = initVector(3,3);

     addParameter(Par::mass1, "vev");
     addParameter(Par::dimensionless, "lambda_hV");
     addParameter(Par::dimensionless, "lambda_h");

     addParameter(Par::Pole_Mass, "h0_1");
     addParameter(Par::Pole_Mass, "V" );

     addParameter(Par::dimensionless, "g1");
     addParameter(Par::dimensionless, "g2");
     addParameter(Par::dimensionless, "g3");

     addParameter(Par::dimensionless, "sinW2");

     addParameter(Par::dimensionless, "Yd", m3x3);
     addParameter(Par::dimensionless, "Yu", m3x3);
     addParameter(Par::dimensionless, "Ye", m3x3);
  }

}
```


-------------------------------

Updated on 2025-02-12 at 15:36:41 +0000
