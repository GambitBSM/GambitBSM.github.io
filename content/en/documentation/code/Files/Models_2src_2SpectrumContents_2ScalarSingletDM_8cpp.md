---
title: "file SpectrumContents/Models/src/SpectrumContents/ScalarSingletDM.cpp"

description: "[No description available]"

---

# file SpectrumContents/Models/src/SpectrumContents/ScalarSingletDM.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * James McKay ([j.mckay14@imperial.ac.uk](mailto:j.mckay14@imperial.ac.uk)) 
  * Pat Scott ([p.scott@imperial.ac.uk](mailto:p.scott@imperial.ac.uk)) 


**Date**: 

  * 2016 Feb
  * 2016 Mar
  * 2018 Sep


Class defining the parameters that SubSpectrum objects providing Scalar Singlet Dark Matter spectrum data must provide



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
///  objects providing Scalar Singlet Dark Matter
///  spectrum data must provide
///
///  *********************************************
///
///  Authors:
///  <!-- add name and date if you modify -->
///
///  \author Ben Farmer
///          (benjamin.farmer@fysik.su.se)
///  \date 2016 Feb
///
///  \author James McKay
///          (j.mckay14@imperial.ac.uk)
///  \date 2016 Mar
///
///  \author Pat Scott
///          (p.scott@imperial.ac.uk)
///  \date 2018 Sep
///
///  *********************************************

#include "gambit/Models/SpectrumContents/RegisteredSpectra.hpp"

namespace Gambit
{

  /////// Z2 model ///////
  SpectrumContents::ScalarSingletDM_Z2::ScalarSingletDM_Z2()
  {
     setName("ScalarSingletDM_Z2");

     // shape prototypes
     std::vector<int> m3x3 = initVector(3,3);

     addParameter(Par::mass1, "vev");
     addParameter(Par::dimensionless, "lambda_hS");
     addParameter(Par::dimensionless, "lambda_S");
     addParameter(Par::dimensionless, "lambda_h");

     addParameter(Par::Pole_Mass, "h0_1");
     addParameter(Par::Pole_Mass, "S" );

     addParameter(Par::dimensionless, "g1");
     addParameter(Par::dimensionless, "g2");
     addParameter(Par::dimensionless, "g3");

     addParameter(Par::dimensionless, "sinW2");

     addParameter(Par::dimensionless, "Yd", m3x3);
     addParameter(Par::dimensionless, "Yu", m3x3);
     addParameter(Par::dimensionless, "Ye", m3x3);
  }

  /////// Z3 model ///////
  SpectrumContents::ScalarSingletDM_Z3::ScalarSingletDM_Z3()
  {
     setName("ScalarSingletDM_Z3");

     // shape prototypes
     std::vector<int> m3x3 = initVector(3,3);

     addParameter(Par::mass1, "vev");
     addParameter(Par::dimensionless, "lambda_hS");
     addParameter(Par::dimensionless, "lambda_S");
     addParameter(Par::dimensionless, "lambda_h");
     addParameter(Par::mass1, "mu3");

     addParameter(Par::Pole_Mass, "h0_1");
     addParameter(Par::Pole_Mass, "S" );

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

Updated on 2022-09-07 at 23:22:09 +0000
