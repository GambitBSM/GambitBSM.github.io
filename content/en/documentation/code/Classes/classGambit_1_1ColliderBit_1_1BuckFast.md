---
title: "class Gambit::ColliderBit::BuckFast"
description: "A base class for [BuckFast]() simple smearing simulations within ColliderBit. "

---

# class Gambit::ColliderBit::BuckFast



A base class for [BuckFast]() simple smearing simulations within ColliderBit. 


`#include <BuckFast.hpp>`

Inherits from [Gambit::ColliderBit::BaseDetector](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual void | **[init](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#function-init)**(const std::vector< std::string > & )<br>[Settings](/documentation/code/classes/structsettings/) parsing and initialization for any sub-class.  |
| virtual void | **[init](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#function-init)**()<br>General init for any collider of this type.  |
| virtual void | **[processEvent](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#function-processevent)**(HEPUtils::Event & event) const<br>Process an event with [BuckFast](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/).  |
| | **[BuckFast](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#function-buckfast)**()<br>Constructor.  |
| virtual | **[~BuckFast](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#function-buckfast)**()<br>Destructor.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| void(*)(std::vector< HEPUtils::Particle * > &) | **[smearElectronEnergy](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#variable-smearelectronenergy)**  |
| void(*)(std::vector< HEPUtils::Particle * > &) | **[smearMuonMomentum](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#variable-smearmuonmomentum)**  |
| void(*)(std::vector< HEPUtils::Particle * > &) | **[smearTaus](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#variable-smeartaus)**  |
| void(*)(std::vector< HEPUtils::Jet * > &) | **[smearJets](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/#variable-smearjets)**  |

## Additional inherited members

**Public Functions inherited from [Gambit::ColliderBit::BaseDetector](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseDetector](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/#function-basedetector)**()<br>Constructor.  |
| virtual | **[~BaseDetector](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/#function-basedetector)**()<br>Destructor.  |
| virtual void | **[clear](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/#function-clear)**()<br>Reset this instance for reuse, avoiding the need for "new" or "delete".  |


## Public Functions Documentation

### function init

```
inline virtual void init(
    const std::vector< std::string > & 
)
```

[Settings](/documentation/code/classes/structsettings/) parsing and initialization for any sub-class. 

**Reimplements**: [Gambit::ColliderBit::BaseDetector::init](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/#function-init)


### function init

```
inline virtual void init()
```

General init for any collider of this type. 

**Reimplements**: [Gambit::ColliderBit::BaseDetector::init](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/#function-init)


### function processEvent

```
virtual void processEvent(
    HEPUtils::Event & event
) const
```

Process an event with [BuckFast](/documentation/code/classes/classgambit_1_1colliderbit_1_1buckfast/). 

**Reimplements**: [Gambit::ColliderBit::BaseDetector::processEvent](/documentation/code/classes/classgambit_1_1colliderbit_1_1basedetector/#function-processevent)


TodoRun-dependence? 

TodoRun-dependence? 


### function BuckFast

```
inline BuckFast()
```

Constructor. 

### function ~BuckFast

```
inline virtual ~BuckFast()
```

Destructor. 

## Public Attributes Documentation

### variable smearElectronEnergy

```
void(*)(std::vector< HEPUtils::Particle * > &) smearElectronEnergy;
```


Pointers to actual detector response functions 


### variable smearMuonMomentum

```
void(*)(std::vector< HEPUtils::Particle * > &) smearMuonMomentum;
```


### variable smearTaus

```
void(*)(std::vector< HEPUtils::Particle * > &) smearTaus;
```


### variable smearJets

```
void(*)(std::vector< HEPUtils::Jet * > &) smearJets;
```


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000