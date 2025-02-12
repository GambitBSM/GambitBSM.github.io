---
title: "file SpectrumContents/RegisteredSpectra.hpp"

description: "[No description available]"

---

# file SpectrumContents/RegisteredSpectra.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::SpectrumContents](/documentation/code/namespaces/namespacegambit_1_1spectrumcontents/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::SpectrumContents::SM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1sm/)**  |
| struct | **[Gambit::SpectrumContents::SM_slha](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1sm__slha/)**  |
| struct | **[Gambit::SpectrumContents::SMHiggs](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1smhiggs/)**  |
| struct | **[Gambit::SpectrumContents::MSSM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1mssm/)**  |
| struct | **[Gambit::SpectrumContents::MDM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1mdm/)**  |
| struct | **[Gambit::SpectrumContents::ScalarSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1scalarsingletdm__z2/)**  |
| struct | **[Gambit::SpectrumContents::ScalarSingletDM_Z3](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1scalarsingletdm__z3/)**  |
| struct | **[Gambit::SpectrumContents::VectorSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1vectorsingletdm__z2/)**  |
| struct | **[Gambit::SpectrumContents::MajoranaSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1majoranasingletdm__z2/)**  |
| struct | **[Gambit::SpectrumContents::DiracSingletDM_Z2](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1diracsingletdm__z2/)**  |
| struct | **[Gambit::SpectrumContents::DMEFT](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1dmeft/)**  |
| struct | **[Gambit::SpectrumContents::DMsimpVectorMedDiracDM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1dmsimpvectormeddiracdm/)**  |
| struct | **[Gambit::SpectrumContents::DMsimpVectorMedMajoranaDM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1dmsimpvectormedmajoranadm/)**  |
| struct | **[Gambit::SpectrumContents::DMsimpVectorMedScalarDM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1dmsimpvectormedscalardm/)**  |
| struct | **[Gambit::SpectrumContents::DMsimpVectorMedVectorDM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1dmsimpvectormedvectordm/)**  |
| struct | **[Gambit::SpectrumContents::SubGeVDM](/documentation/code/classes/structgambit_1_1spectrumcontents_1_1subgevdm/)**  |

## Detailed Description


**Author**: 

  * Ben Farmer ([benjamin.farmer@fysik.su.se](mailto:benjamin.farmer@fysik.su.se)) 
  * Ankit Beniwal ([ankit.beniwal@adelaide.edu.au](mailto:ankit.beniwal@adelaide.edu.au)) 
  * Inigo Saez Casares ([inigo.saez_casares@ens-paris-saclay.fr](mailto:inigo.saez_casares@ens-paris-saclay.fr)))


**Date**: 

  * 2016 Feb
  * 2016 Aug


Register the definitions of SubSpectrum contents here.



------------------

Authors:



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Register the definitions of SubSpectrum
///  contents here.
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
///  \author Ankit Beniwal
///          (ankit.beniwal@adelaide.edu.au)
///  \date 2016 Aug
///
///  \author Inigo Saez Casares
///          (inigo.saez_casares@ens-paris-saclay.fr))
///
///  *********************************************

#ifndef __registeredspectra_hpp__
#define __registeredspectra_hpp__

#include "gambit/Models/SpectrumContents/subspectrum_contents.hpp"

/// Just declare the classes here; should be defined in source files

namespace Gambit
{
  namespace SpectrumContents
  {

    struct SM                       : SubSpectrumContents { SM(); };
    struct SM_slha                  : SubSpectrumContents { SM_slha(); }; // Missing some running masses that aren't part of SMINPUTS in slha
    struct SMHiggs                  : SubSpectrumContents { SMHiggs(); };
    struct MSSM                     : SubSpectrumContents { MSSM(); };
    struct MDM                      : SubSpectrumContents { MDM(); };
    struct ScalarSingletDM_Z2       : SubSpectrumContents { ScalarSingletDM_Z2(); };
    struct ScalarSingletDM_Z3       : SubSpectrumContents { ScalarSingletDM_Z3(); };
    struct VectorSingletDM_Z2       : SubSpectrumContents { VectorSingletDM_Z2(); };
    struct MajoranaSingletDM_Z2     : SubSpectrumContents { MajoranaSingletDM_Z2(); };
    struct DiracSingletDM_Z2        : SubSpectrumContents { DiracSingletDM_Z2(); };
    struct DMEFT                    : SubSpectrumContents { DMEFT(); };
    struct DMsimpVectorMedDiracDM   : SubSpectrumContents { DMsimpVectorMedDiracDM(); };
    struct DMsimpVectorMedMajoranaDM: SubSpectrumContents { DMsimpVectorMedMajoranaDM(); };
    struct DMsimpVectorMedScalarDM  : SubSpectrumContents { DMsimpVectorMedScalarDM(); };
    struct DMsimpVectorMedVectorDM  : SubSpectrumContents { DMsimpVectorMedVectorDM(); };
    struct SubGeVDM                 : SubSpectrumContents { SubGeVDM(); };

    // TODO: Temporarily disabled until project is ready
    // struct SuperRenormHP        : SubSpectrumContents { SuperRenormHP(); };

  }
}
#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:34 +0000
