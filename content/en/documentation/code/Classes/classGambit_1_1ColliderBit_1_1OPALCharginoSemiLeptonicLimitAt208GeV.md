---
title: "class Gambit::ColliderBit::OPALCharginoSemiLeptonicLimitAt208GeV"
description: "A class to contain the limit data from OPAL_EPJC35_2004_1, figure 6b. "

---

# class Gambit::ColliderBit::OPALCharginoSemiLeptonicLimitAt208GeV



A class to contain the limit data from OPAL_EPJC35_2004_1, figure 6b. 


`#include <OPALGauginoLimits.hpp>`

Inherits from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| virtual [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginosemileptoniclimitat208gev/#function-convertpt)**(double x, double y) const<br>Convert a point from pixel units to axis units.  |
| virtual bool | **[isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginosemileptoniclimitat208gev/#function-iswithinexclusionregion)**(double x, double y, double ) const<br>Check to see if the point is within the exclusion region.  |
| | **[OPALCharginoSemiLeptonicLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opalcharginosemileptoniclimitat208gev/#function-opalcharginosemileptoniclimitat208gev)**() |

## Additional inherited members

**Protected Types inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| typedef std::vector< [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) > | **[Corners](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-corners)**  |
| typedef std::vector< [LineSegment](/documentation/code/classes/classgambit_1_1colliderbit_1_1linesegment/) > | **[Contours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-contours)**  |
| typedef Contours * | **[ContoursPointer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-contourspointer)**  |
| typedef std::map< unsigned, Contours * > | **[LimitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-limitcontours)**  |
| typedef std::pair< unsigned, Contours * > | **[LimitContourEntry](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#typedef-limitcontourentry)**  |

**Public Functions inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| | **[BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-baselimitcontainer)**() |
| virtual | **[~BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-baselimitcontainer)**() |
| virtual double | **[specialLimit](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-speciallimit)**(double , double ) const<br>Return the limit value outside of the exclusion region.  |
| double | **[limitAverage](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-limitaverage)**(double x, double y, double mZ) const<br>Two-pi averaging interpolator to find limits between limit curves.  |
| void | **[dumpPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-dumpplotdata)**(double xlow, double xhigh, double ylow, double yhigh, double mZ, std::string filename, int ngrid =100) const<br>Dump limit average data into a file for average debugging.  |
| void | **[dumpLightPlotData](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-dumplightplotdata)**(std::string filename, int nperLine =20) const<br>Dump input limit contour data into a file for limit debugging.  |

**Protected Attributes inherited from [Gambit::ColliderBit::BaseLimitContainer](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< double > | **[_limitValuesSorted](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#variable-limitvaluessorted)**  |
| LimitContours | **[_limitContours](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#variable-limitcontours)**  |
| [P2](/documentation/code/classes/classgambit_1_1colliderbit_1_1p2/) | **[_externalPoint](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#variable-externalpoint)**  |


## Public Functions Documentation

### function convertPt

```
virtual P2 convertPt(
    double x,
    double y
) const
```

Convert a point from pixel units to axis units. 

**Reimplements**: [Gambit::ColliderBit::BaseLimitContainer::convertPt](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-convertpt)


### function isWithinExclusionRegion

```
virtual bool isWithinExclusionRegion(
    double x,
    double y,
    double 
) const
```

Check to see if the point is within the exclusion region. 

**Reimplements**: [Gambit::ColliderBit::BaseLimitContainer::isWithinExclusionRegion](/documentation/code/classes/classgambit_1_1colliderbit_1_1baselimitcontainer/#function-iswithinexclusionregion)


Plots only go down to 75 GeV


### function OPALCharginoSemiLeptonicLimitAt208GeV

```
OPALCharginoSemiLeptonicLimitAt208GeV()
```


0.05pb ///// : This limit has multiple regions, so care must be taken below


-------------------------------

Updated on 2025-02-12 at 16:10:32 +0000