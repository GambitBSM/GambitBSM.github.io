---
title: "file src/lhef2heputils.cpp"

description: "[No description available]"

---

# file src/lhef2heputils.cpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |
| **[FJNS](/documentation/code/namespaces/namespacefjns/)**  |




## Source code

```
// -*- C++ -*-
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///
///  lhef2heputils: a Les Houches Event Format (LHEF)
///  -> HEPUtils::Event MC generator event file
///  converter, based on lhef2hepmc.
///
///  Hat tip: Leif Lönnblad for writing the LHEF
///  parser that actually makes this possible!
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Andy Buckley
///  (andy.buckley@cern.ch)
///  \date May 2019
///
///  \author Pat Scott
///  (p.scott@imperial.ac.uk)
///  \date May 2019
///
///  *********************************************

#include "gambit/cmake/cmake_variables.hpp"

#ifndef EXCLUDE_HEPMC

#include <iostream>

using namespace std;

#include "gambit/ColliderBit/lhef2heputils.hpp"

#include "gambit/Utils/begin_ignore_warnings_hepmc.hpp"
#include "HepMC3/LHEF.h"
#include "gambit/Utils/end_ignore_warnings.hpp"

#include "HEPUtils/FastJet.h"

//#define COLLIDERBIT_DEBUG

using namespace HEPUtils;
using namespace FJNS;

namespace Gambit
{

  namespace ColliderBit
  {

    /// Extract an LHE event as a HEPUtils::Event
    void get_HEPUtils_event(const LHEF::Reader& lhe, Event& evt, double jet_pt_min, std::vector<jet_collection_settings> all_jet_collection_settings)
    {

      P4 vmet;
      vector<PseudoJet> jetparticles;

      evt.set_weight(lhe.hepeup.weight());

      // Loop over all particles in the event
      for (int i = 0; i < lhe.hepeup.NUP; ++i)
      {
        // Get status and PID code
        const int st = lhe.hepeup.ISTUP[i];
        const int pid = lhe.hepeup.IDUP[i];
        const int apid = fabs(pid);

        // Use LHE-stable particles only
        if (st != 1) continue;

        // Get 4-momentum
        const P4 p4 = P4::mkXYZM(lhe.hepeup.PUP[i][0], lhe.hepeup.PUP[i][1], lhe.hepeup.PUP[i][2], lhe.hepeup.PUP[i][4]);

        // Store interacting prompt particles
        /// @todo Dress leptons?
        if (apid == 22 || apid == 11 || apid == 13 || apid == 15)
        {
          Particle* p = new Particle(p4, pid); // the event will take ownership of this pointer
          p->set_prompt(true);
          evt.add_particle(p);
        }

        // Aggregate missing ET
        else if (apid == 12 || apid == 14 || apid == 16 || apid == 1000022 || apid == 1000039)
        {
          Particle* p = new Particle(p4, pid); // the event will take ownership of this pointer
          p->set_prompt(true);
          evt.add_particle(p);
          vmet += p4;
        }

        // Store non-prompt momenta for Jet building
        else
        {
          PseudoJet pj = mk_pj(p4);
          pj.set_user_index(apid);
          jetparticles.push_back(pj);
        }
      }

      // MET
      vmet.setPz(0);
      vmet.setM(0);
      evt.set_missingmom(vmet);

      // Jet Finding
      for (jet_collection_settings jetcollection : all_jet_collection_settings)
      {

        // @todo get_jets function could accept a more general jet definition
        vector<PseudoJet> jets = HEPUtils::get_jets(jetparticles, 0.4, jet_pt_min, FJalgorithm_map(jetcollection.algorithm));

        for (const PseudoJet& pj : jets)
        {
          bool hasC = false, hasB = false;
          /// @todo Bug in HEPUtils::get_jets means that constituent info is lost for now...
          // for (const PseudoJet& c : pj.constituents()) {
          //   if (c.user_index() == 4) hasC = true;
          //   if (c.user_index() == 5) hasB = true;
          // }
          evt.add_jet(new Jet(mk_p4(pj), hasB, hasC), jetcollection.key);
        }

        #ifdef COLLIDERBIT_DEBUG
          // Print event summary
          cout << "  MET  = " << evt.met() << " GeV" << endl;
          cout << "  #e   = " << evt.electrons().size() << endl;
          cout << "  #mu  = " << evt.muons().size() << endl;
          cout << "  #tau = " << evt.taus().size() << endl;
          cout << "  #jet = " << evt.jets().size() << endl;
          cout << "  #pho  = " << evt.photons().size() << endl;
          cout << endl;
        #endif
      }

    }

  }

}

#endif
```


-------------------------------

Updated on 2025-02-12 at 16:10:36 +0000
