---
title: "file limits/L3GauginoLimits.hpp"

description: "[No description available]"

---

# file limits/L3GauginoLimits.hpp

[No description available]

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |
| **[Gambit::ColliderBit](/documentation/code/namespaces/namespacegambit_1_1colliderbit/)**  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::ColliderBit::L3CharginoAllChannelsLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoallchannelslimitat188pt6gev/)** <br>A class to contain the limit data from L3PLB_472_2000_420, figure 2a.  |
| class | **[Gambit::ColliderBit::L3CharginoLeptonicLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3charginoleptoniclimitat188pt6gev/)** <br>A class to contain the limit data from L3PLB_472_2000_420, figure 2b.  |
| class | **[Gambit::ColliderBit::L3NeutralinoAllChannelsLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoallchannelslimitat188pt6gev/)** <br>A class to contain the limit data from L3PLB_472_2000_420, figure 3a.  |
| class | **[Gambit::ColliderBit::L3NeutralinoLeptonicLimitAt188pt6GeV](/documentation/code/classes/classgambit_1_1colliderbit_1_1l3neutralinoleptoniclimitat188pt6gev/)** <br>A class to contain the limit data from L3PLB_472_2000_420, figure 3b.  |




## Source code

```
#include "gambit/ColliderBit/limits/BaseLimitContainer.hpp"

namespace Gambit {
  namespace ColliderBit {


    /// @brief A class to contain the limit data from L3PLB_472_2000_420, figure 2a.
    class L3CharginoAllChannelsLimitAt188pt6GeV : public BaseLimitContainer {
      /// @name Point interpolation, conversion, and region checks
      //@{
      public:
        /// @brief Convert a point from pixel units to axis units
        P2 convertPt(double x, double y) const;
        /// @brief Check to see if the point is within the exclusion region
        bool isWithinExclusionRegion(double x, double y, double mZ) const;
      //@}

      /// @name Construction, initializing with all necessary data from the plot
      //@{
      public:
        L3CharginoAllChannelsLimitAt188pt6GeV();
      //@}
    };


    /// @brief A class to contain the limit data from L3PLB_472_2000_420, figure 2b.
    class L3CharginoLeptonicLimitAt188pt6GeV : public BaseLimitContainer {
      /// @name Point interpolation, conversion, and region checks
      //@{
      public:
        /// @brief Convert a point from pixel units to axis units
        P2 convertPt(double x, double y) const;
        /// @brief Check to see if the point is within the exclusion region
        bool isWithinExclusionRegion(double x, double y, double mZ) const;
      //@}

      /// @name Construction, initializing with all necessary data from the plot
      //@{
      public:
        L3CharginoLeptonicLimitAt188pt6GeV();
      //@}
    };


    /// @brief A class to contain the limit data from L3PLB_472_2000_420, figure 3a.
    class L3NeutralinoAllChannelsLimitAt188pt6GeV : public BaseLimitContainer {
      /// @name Point interpolation, conversion, and region checks
      //@{
      public:
        /// @brief Convert a point from pixel units to axis units
        P2 convertPt(double x, double y) const;
        /// @brief Check to see if the point is within the exclusion region
        bool isWithinExclusionRegion(double x, double y, double mZ) const;
      //@}

      /// @name Construction, initializing with all necessary data from the plot
      //@{
      public:
        L3NeutralinoAllChannelsLimitAt188pt6GeV();
      //@}
    };


    /// @brief A class to contain the limit data from L3PLB_472_2000_420, figure 3b.
    class L3NeutralinoLeptonicLimitAt188pt6GeV : public BaseLimitContainer {
      /// @name Point interpolation, conversion, and region checks
      //@{
      public:
        /// @brief Convert a point from pixel units to axis units
        P2 convertPt(double x, double y) const;
        /// @brief Check to see if the point is within the exclusion region
        bool isWithinExclusionRegion(double x, double y, double mZ) const;
      //@}

      /// @name Construction, initializing with all necessary data from the plot
      //@{
      public:
        L3NeutralinoLeptonicLimitAt188pt6GeV();
      //@}
    };


  }
}
```


-------------------------------

Updated on 2022-09-08 at 01:48:59 +0000
