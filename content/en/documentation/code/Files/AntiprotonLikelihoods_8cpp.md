---
title: "file src/AntiprotonLikelihoods.cpp"

description: "[No description available]"

---

# file src/AntiprotonLikelihoods.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::DarkBit](/documentation/code/namespaces/namespacegambit_1_1darkbit/)**  |

## Detailed Description


**Author**: 

  * Sowmiya Balan ([sowmiya.balan@kit.edu](mailto:sowmiya.balan@kit.edu)) 
  * Torsten Bringmann ([torsten.bringmann@fys.uio.no](mailto:torsten.bringmann@fys.uio.no)) 


**Date**: 

  * 2022 June
  * Oct 2023


Likelihood for 7-year antiproton data from AMS-02



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Likelihood for 7-year antiproton data from AMS-02
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Sowmiya Balan
///          (sowmiya.balan@kit.edu)
///  \date 2022 June
///
///  \author Torsten Bringmann
///         (torsten.bringmann@fys.uio.no)
///  \date Oct 2023
///
///  *********************************************

#include <iostream>
#include <fstream>
#include "gambit/Elements/gambit_module_headers.hpp"
#include "gambit/DarkBit/DarkBit_rollcall.hpp"
#include "gambit/Utils/util_functions.hpp"

#include <boost/multi_array.hpp>

namespace Gambit
{
  namespace DarkBit
  {
    void lnL_pbarAMS02 (map_str_dbl& result)
    {
      using namespace Pipes::lnL_pbarAMS02;
      LocalMaxwellianHalo LocalHaloParameters = *Dep::LocalHalo;
      double rho0_resc = LocalHaloParameters.rho0/0.43;
      double suppression = *Dep::ID_suppression;
      std::string DM_ID = Dep::WIMP_properties->name;
      std::string DMbar_ID = Dep::WIMP_properties->conjugate;
      double DM_mass = Dep::WIMP_properties->mass;
      TH_Process process = Dep::TH_ProcessCatalog->getProcess(DM_ID, DMbar_ID);
      map_str_dbl input;
      double sv=0;
      std::vector<std::string> fs;
      std::string finalStates;
      double rate=0;
      for (std::vector<TH_Channel>::iterator it = process.channelList.begin(); it!=process.channelList.end();it++)
      {
        fs = it->finalStateIDs;
        finalStates = fs[0] + " " + fs[1];
        rate = it->genRate->bind("v")->eval(0.);
        rate = rate * suppression * rho0_resc * rho0_resc;
        input.insert({finalStates, rate});
        sv += rate;
      }
      result = BEreq::drn_pbar_logLikes(DM_mass, input, sv);
    }

    void lnL_pbarAMS02_uncorr (double& result)
    {
      using namespace Pipes::lnL_pbarAMS02_uncorr;
      map_str_dbl del_chi2 = *Dep::pbar_logLikes;
      result = -1./2*del_chi2["uncorrelated"];
    }

    void lnL_pbarAMS02_corr (double& result)
    {
      using namespace Pipes::lnL_pbarAMS02_corr;
      map_str_dbl del_chi2 = *Dep::pbar_logLikes;
      result = -1./2*del_chi2["correlated"];
    }
  }
}
```


-------------------------------

Updated on 2024-07-18 at 13:53:34 +0000
