---
title: "file src/Utils.cpp"

description: "[No description available]"

---

# file src/Utils.cpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Detailed Description


**Author**: 

  * Andy Buckley ([andy.buckley@glasgow.ac.uk](mailto:andy.buckley@glasgow.ac.uk)) 
  * Abram Krislock ([a.m.b.krislock@fys.uio.no](mailto:a.m.b.krislock@fys.uio.no)) 
  * Anders Kvellestad ([anders.kvellestad@fys.uio.no](mailto:anders.kvellestad@fys.uio.no)) 
  * Pat Scott ([pat.scott@uq.edu.au](mailto:pat.scott@uq.edu.au)) 
  * Tomas Gonzalo ([gonzalo@physk.rwth-aachen.de](mailto:gonzalo@physk.rwth-aachen.de)) 


**Date**: 

  * 2017 Aug
  * 2016 Mar
  * 2019 Jan
  * 2020 Jan
  * 2021 Jul


Util function definitions for ColliderBit



------------------

Authors (add name and date if you modify):



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//  *********************************************
///  \file
///
///  Util function definitions for ColliderBit
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Andy Buckley
///          (andy.buckley@glasgow.ac.uk)
///  \date 2017 Aug
///
///  \author Abram Krislock
///          (a.m.b.krislock@fys.uio.no)
///  \date 2016 Mar
///
///  \author Anders Kvellestad
///          (anders.kvellestad@fys.uio.no)
///  \date 2019 Jan
///
///  \author Pat Scott
///          (pat.scott@uq.edu.au)
///  \date 2020 Jan
///
///  \author Tomas Gonzalo
///          (gonzalo@physk.rwth-aachen.de)
///  \date 2021 Jul
///
///  *********************************************

#include "gambit/ColliderBit/Utils.hpp"
#include "gambit/ColliderBit/ColliderBit_eventloop.hpp"
#include "gambit/Utils/threadsafe_rng.hpp"
#include <iostream>
using namespace std;

namespace Gambit
{
  namespace ColliderBit
  {


    /// Storage of different FastJet methods
    FJNS::JetAlgorithm FJalgorithm_map(str algorithm)
    {
      FJNS::JetAlgorithm result;
      if (algorithm == "antikt") {result = FJNS::antikt_algorithm;}
      else if (algorithm == "cambridge") {result = FJNS::cambridge_algorithm;}
      else if (algorithm == "kt") {result = FJNS::kt_algorithm;}
      else if (algorithm == "genkt") {result = FJNS::genkt_algorithm;}
      else if (algorithm == "cambridge_for_passive") {result = FJNS::cambridge_for_passive_algorithm;}
      else
      {
        ColliderBit_error().raise(LOCAL_INFO, "Could not find jet algorithm in list available. Please add the missing option to the FJalgorithm_map function in ColliderBit/src/Utils.cpp.");
      }
      return result;
    }

    FJNS::Strategy FJstrategy_map(str strategy)
    {
      FJNS::Strategy result;
      if (strategy == "Best") {result = FJNS::Best;}
      else if (strategy == "NlnN") {result = FJNS::NlnN;}
      else
      {
        ColliderBit_error().raise(LOCAL_INFO, "Could not find jet strategy in list available. Please add the missing option to the FJstrategy_map function in ColliderBit/src/Utils.cpp.");
      }
      return result;
    }

    FJNS::RecombinationScheme FJRecomScheme_map(str reco_scheme)
    {
      FJNS::RecombinationScheme result;
      if (reco_scheme == "E_scheme") {result = FJNS::E_scheme;}
      else if (reco_scheme == "pt_scheme") {result = FJNS::pt_scheme;}
      else if (reco_scheme == "pt2_scheme") {result = FJNS::pt2_scheme;}
      else
      {
        ColliderBit_error().raise(LOCAL_INFO, "Could not find jet recombination scheme in list available. Please add the missing option to the FJRecomScheme_map function in ColliderBit/src/Utils.cpp.");
      }
      return result;
    }

    bool random_bool(double eff)
    {
      /// @todo Handle out-of-range eff values
      return Random::draw() < eff;
    }


    void filtereff(std::vector<const HEPUtils::Particle*>& particles, double eff, bool do_delete)
    {
      if (particles.empty()) return;
      auto keptParticlesEnd = std::remove_if(particles.begin(), particles.end(),
                                             [&](const HEPUtils::Particle* p) {
                                               const bool rm = !random_bool(eff);
                                               if (do_delete && rm) delete p;
                                               return rm;
                                             } );
      particles.erase(keptParticlesEnd, particles.end());
    }


    /// Utility function for filtering a supplied particle vector by sampling wrt a binned 1D efficiency map in pT
    void filtereff(std::vector<const HEPUtils::Particle*>& particles, std::function<double(const HEPUtils::Particle*)> eff_fn, bool do_delete)
    {
      if (particles.empty()) return;
      auto keptParticlesEnd = std::remove_if(particles.begin(), particles.end(),
                                             [&](const HEPUtils::Particle* p)
                                             {
                                               const double eff = eff_fn(p);
                                               const bool rm = !random_bool(eff);
                                               if (do_delete && rm) delete p;
                                               return rm;
                                             } );
      particles.erase(keptParticlesEnd, particles.end());
    }


    // Utility function for filtering a supplied particle vector by sampling wrt a binned 1D efficiency map in pT
    void filtereff_pt(std::vector<const HEPUtils::Particle*>& particles, const HEPUtils::BinnedFn1D<double>& eff_pt, bool do_delete)
    {
      if (particles.empty()) return;
      auto keptParticlesEnd = std::remove_if(particles.begin(), particles.end(),
                                             [&](const HEPUtils::Particle* p)
                                             {
                                               const bool rm = !random_bool(eff_pt, p->pT());
                                               if (do_delete && rm) delete p;
                                               return rm;
                                             } );
      particles.erase(keptParticlesEnd, particles.end());
    }


    // Utility function for filtering a supplied particle vector by sampling wrt a binned 2D efficiency map in |eta| and pT
    void filtereff_etapt(std::vector<const HEPUtils::Particle*>& particles, const HEPUtils::BinnedFn2D<double>& eff_etapt, bool do_delete)
    {
      if (particles.empty()) return;
      auto keptParticlesEnd = std::remove_if(particles.begin(), particles.end(),
                                             [&](const HEPUtils::Particle* p)
                                             {
                                               const bool rm = !random_bool(eff_etapt, p->abseta(), p->pT());
                                               if (do_delete && rm) delete p;
                                               return rm;
                                             } );
      particles.erase(keptParticlesEnd, particles.end());
    }


    // Utility function for returning a collection of same-flavour, oppsosite-sign particle pairs
    std::vector<std::vector<const HEPUtils::Particle*>> getSFOSpairs(std::vector<const HEPUtils::Particle*> particles)
    {
      std::vector<std::vector<const HEPUtils::Particle*>> SFOSpair_container;
      for (size_t ip1=0; ip1<particles.size(); ip1++)
      {
        for (size_t ip2=ip1+1; ip2<particles.size(); ip2++)
        {
          if (particles[ip1]->abspid()==particles[ip2]->abspid() && particles[ip1]->pid()!=particles[ip2]->pid())
          {
            std::vector<const HEPUtils::Particle*> SFOSpair;
            SFOSpair.push_back(particles[ip1]);
            SFOSpair.push_back(particles[ip2]);
            SFOSpair_container.push_back(SFOSpair);
          }
        }
      }
      return SFOSpair_container;
    }


    // Utility function for returning a collection of oppsosite-sign particle pairs
    std::vector<std::vector<const HEPUtils::Particle*>> getOSpairs(std::vector<const HEPUtils::Particle*> particles)
    {
      std::vector<std::vector<const HEPUtils::Particle*>> OSpair_container;
      for (size_t ip1=0;ip1<particles.size();ip1++)
      {
        for (size_t ip2=ip1+1; ip2<particles.size(); ip2++)
        {
          if (particles[ip1]->pid()*particles[ip2]->pid()<0.)
          {
            std::vector<const HEPUtils::Particle*> OSpair;
            OSpair.push_back(particles[ip1]);
            OSpair.push_back(particles[ip2]);
            OSpair_container.push_back(OSpair);
          }
        }
      }
      return OSpair_container;
    }


    // Utility function for returning a collection of same-sign particle pairs
    std::vector<std::vector<const HEPUtils::Particle*>> getSSpairs(std::vector<const HEPUtils::Particle*> particles)
    {
      std::vector<std::vector<const HEPUtils::Particle*>> SSpair_container;
      for (size_t ip1=0;ip1<particles.size();ip1++)
      {
        for (size_t ip2=ip1+1; ip2<particles.size(); ip2++)
        {
          if (particles[ip1]->pid()*particles[ip2]->pid()>0.)
          {
            std::vector<const HEPUtils::Particle*> SSpair;
            SSpair.push_back(particles[ip1]);
            SSpair.push_back(particles[ip2]);
            SSpair_container.push_back(SSpair);
          }
        }
      }
      return SSpair_container;
    }

    // Utility function for returning a collection of b-tagged jet pairs
    std::vector<std::vector<const HEPUtils::Jet*>> getBJetPairs(std::vector<const HEPUtils::Jet*> bjets)
    {
      std::vector<std::vector<const HEPUtils::Jet*>> BJetpair_container;
      for (size_t ibj1=0; ibj1<bjets.size(); ++ibj1)
      {
        for (size_t ibj2=ibj1+1; ibj2<bjets.size(); ++ibj2)
        {
          std::vector<const HEPUtils::Jet*> BJetpair;
          BJetpair.push_back(bjets[ibj1]);
          BJetpair.push_back(bjets[ibj2]);
          BJetpair_container.push_back(BJetpair);
        }
      }
      return BJetpair_container;
    }

  }
}
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
