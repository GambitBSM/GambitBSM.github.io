---
title: "file limits/OPALDegenerateCharginoLimits.hpp"

description: "[No description available]"

---

# file limits/OPALDegenerateCharginoLimits.hpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::ColliderBit::OPALDegenerateCharginoLimitAt208GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1opaldegeneratecharginolimitat208gev/)** <br>A class to contain the limit data from OPAL, hep-ex/0210043, figure 5a (in colour)  |




## Source code

```
#pragma once
#include "gambit/ColliderBit/limits/BaseLimitContainer.hpp"

namespace Gambit
{
  namespace ColliderBit 
  {
    /// @brief A class to contain the limit data from OPAL, hep-ex/0210043, figure 5a (in colour)
    class OPALDegenerateCharginoLimitAt208GeV : public BaseLimitContainer {

      //@{
      public:

        P2 convertPt(double, double) const;

        /// @read off the csv file containting the data
        std::vector<P2> dataFromLimit(double);

        /// @brief Check to see if the point is within the exclusion region
        bool isWithinExclusionRegion(double x, double y, double) const;
      //@}

      //@{
      public:
        /// @name Construction, initializing with all necessary data from the plot
        OPALDegenerateCharginoLimitAt208GeV();
      //@}
    };

  }
}
```


-------------------------------

Updated on 2025-02-12 at 16:10:35 +0000
