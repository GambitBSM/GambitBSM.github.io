---
title: "file Pythia_8_312/wrapper_PartonLevel_def.h"

description: "[No description available]"

---

# file Pythia_8_312/wrapper_PartonLevel_def.h

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| namespace | **[CAT_3](/documentation/code/files/wrapper__partonlevel__def_8h/#function-cat-3)**(BACKENDNAME , _ , SAFE_VERSION ) |


## Functions Documentation

### function CAT_3

```
namespace CAT_3(
    BACKENDNAME ,
    _ ,
    SAFE_VERSION 
)
```




## Source code

```
#ifndef __wrapper_PartonLevel_def_Pythia_8_312_h__
#define __wrapper_PartonLevel_def_Pythia_8_312_h__

#include <vector>
#include "wrapper_Event_decl.h"
#include "wrapper_BeamParticle_decl.h"
#include "wrapper_ResonanceDecays_decl.h"

#include "identification.hpp"

namespace CAT_3(BACKENDNAME,_,SAFE_VERSION)
{
    
    namespace Pythia8
    {
        
        // Member functions: 
        inline void PartonLevel::initSwitchID(const std::vector<int>& idAList)
        {
            get_BEptr()->initSwitchID(idAList);
        }
        
        inline void PartonLevel::setBeamID(int iPDFA)
        {
            get_BEptr()->setBeamID(iPDFA);
        }
        
        inline void PartonLevel::setBeamID()
        {
            get_BEptr()->setBeamID__BOSS();
        }
        
        inline bool PartonLevel::next(Pythia8::Event& process, Pythia8::Event& event)
        {
            return get_BEptr()->next__BOSS(*process.get_BEptr(), *event.get_BEptr());
        }
        
        inline void PartonLevel::setupShowerSys(Pythia8::Event& process, Pythia8::Event& event)
        {
            get_BEptr()->setupShowerSys__BOSS(*process.get_BEptr(), *event.get_BEptr());
        }
        
        inline bool PartonLevel::resonanceShowers(Pythia8::Event& process, Pythia8::Event& event, bool skipForR)
        {
            return get_BEptr()->resonanceShowers__BOSS(*process.get_BEptr(), *event.get_BEptr(), skipForR);
        }
        
        inline bool PartonLevel::wzDecayShowers(Pythia8::Event& event)
        {
            return get_BEptr()->wzDecayShowers__BOSS(*event.get_BEptr());
        }
        
        inline bool PartonLevel::hasVetoed() const
        {
            return get_BEptr()->hasVetoed();
        }
        
        inline bool PartonLevel::hasVetoedDiff() const
        {
            return get_BEptr()->hasVetoedDiff();
        }
        
        inline bool PartonLevel::hasVetoedMerging() const
        {
            return get_BEptr()->hasVetoedMerging();
        }
        
        inline void PartonLevel::accumulate()
        {
            get_BEptr()->accumulate();
        }
        
        inline void PartonLevel::statistics(bool reset)
        {
            get_BEptr()->statistics(reset);
        }
        
        inline void PartonLevel::statistics()
        {
            get_BEptr()->statistics__BOSS();
        }
        
        inline void PartonLevel::resetStatistics()
        {
            get_BEptr()->resetStatistics();
        }
        
        inline void PartonLevel::resetTrial()
        {
            get_BEptr()->resetTrial();
        }
        
        inline double PartonLevel::pTLastInShower()
        {
            return get_BEptr()->pTLastInShower();
        }
        
        inline int PartonLevel::typeLastInShower()
        {
            return get_BEptr()->typeLastInShower();
        }
        
        inline bool PartonLevel::canEnhanceTrial()
        {
            return get_BEptr()->canEnhanceTrial();
        }
        
        inline double PartonLevel::getEnhancedTrialPT()
        {
            return get_BEptr()->getEnhancedTrialPT();
        }
        
        inline double PartonLevel::getEnhancedTrialWeight()
        {
            return get_BEptr()->getEnhancedTrialWeight();
        }
        
        
        // Wrappers for original constructors: 
        inline PartonLevel::PartonLevel() :
            WrapperBase(__factory0())
        {
            get_BEptr()->set_wptr(this);
            get_BEptr()->set_delete_wrapper(false);
        }
        
        // Special pointer-based constructor: 
        inline PartonLevel::PartonLevel(Abstract_PartonLevel* in) :
            WrapperBase(in)
        {
            get_BEptr()->set_wptr(this);
            get_BEptr()->set_delete_wrapper(false);
        }
        
        // Copy constructor: 
        inline PartonLevel::PartonLevel(const PartonLevel& in) :
            WrapperBase(in.get_BEptr()->pointer_copy__BOSS())
        {
            get_BEptr()->set_wptr(this);
            get_BEptr()->set_delete_wrapper(false);
        }
        
        // Assignment operator: 
        inline PartonLevel& PartonLevel::operator=(const PartonLevel& in)
        {
            if (this != &in)
            {
                get_BEptr()->pointer_assign__BOSS(in.get_BEptr());
            }
            return *this;
        }
        
        
        // Destructor: 
        inline PartonLevel::~PartonLevel()
        {
            if (get_BEptr() != 0)
            {
                get_BEptr()->set_delete_wrapper(false);
                if (can_delete_BEptr())
                {
                    delete BEptr;
                    BEptr = 0;
                }
            }
            set_delete_BEptr(false);
        }
        
        // Returns correctly casted pointer to Abstract class: 
        inline Abstract_PartonLevel* Pythia8::PartonLevel::get_BEptr() const
        {
            return dynamic_cast<Abstract_PartonLevel*>(BEptr);
        }
    }
    
}


#include "gambit/Backends/backend_undefs.hpp"

#endif /* __wrapper_PartonLevel_def_Pythia_8_312_h__ */
```


-------------------------------

Updated on 2025-02-12 at 15:36:43 +0000
