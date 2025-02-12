---
title: "struct Gambit::ColliderBit::SignalRegionData"
description: "A simple container for the result of one signal region from one analysis. "

---

# struct Gambit::ColliderBit::SignalRegionData



A simple container for the result of one signal region from one analysis. 


`#include <SignalRegionData.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-signalregiondata)**(const [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) & scounter, double nobs, const std::pair< double, double > & nbkg, double nsigscaled =0)<br>Constructor with [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) arg for the signal count and SR name.  |
| | **[SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-signalregiondata)**(const std::string & sr, double nobs, const [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) & scounter, const std::pair< double, double > & nbkg, double nsigscaled =0)<br>Constructor with [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) arg for the signal count, but separate name.  |
| | **[SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-signalregiondata)**(const std::string & sr, double nobs, const std::pair< double, double > & nsigMC, const std::pair< double, double > & nbkg, double nsigscaled =0)<br>Constructor with {n,nsys} pair args.  |
| | **[SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-signalregiondata)**(const std::string & sr, double nobs, double nsigMC, double nbkg, double nsigMCsys, double nbkgerr, double nsigscaled =0)<br>Constructor with separate n & nsys args.  |
| | **[SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-signalregiondata)**()<br>Default constructor.  |
| bool | **[check](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-check)**() const<br>Consistency check.  |
| double | **[scalefactor](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-scalefactor)**() const<br>Uncertainty calculators.  |
| double | **[calc_n_sig_MC_err](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-calc-n-sig-mc-err)**() const |
| double | **[calc_n_sig_scaled_err](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-calc-n-sig-scaled-err)**() const |
| double | **[calc_n_sigbkg_err](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-calc-n-sigbkg-err)**() const |
| void | **[combine_SR_MC_signal](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#function-combine-sr-mc-signal)**(const [SignalRegionData](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/) & other) |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| std::string | **[sr_label](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-sr-label)** <br>A label for the particular signal region of the analysis.  |
| double | **[n_obs](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-n-obs)** <br>The number of events passing selection for this signal region as reported by the experiment.  |
| double | **[n_sig_MC](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-n-sig-mc)** <br>The number of simulated model events passing selection for this signal region.  |
| double | **[n_sig_MC_sys](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-n-sig-mc-sys)** <br>The absolute systematic error of n_sig_MC.  |
| double | **[n_sig_MC_stat](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-n-sig-mc-stat)** <br>The absolute statistical (MC) error of n_sig_MC.  |
| double | **[n_sig_scaled](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-n-sig-scaled)** <br>n_sig_MC, scaled to luminosity * cross-section  |
| double | **[n_bkg](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-n-bkg)** <br>The number of standard model events expected to pass the selection for this signal region, as reported by the experiment.  |
| double | **[n_bkg_err](/documentation/code/classes/structgambit_1_1colliderbit_1_1signalregiondata/#variable-n-bkg-err)** <br>The absolute error of n_bkg.  |

## Public Functions Documentation

### function SignalRegionData

```
inline SignalRegionData(
    const EventCounter & scounter,
    double nobs,
    const std::pair< double, double > & nbkg,
    double nsigscaled =0
)
```

Constructor with [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) arg for the signal count and SR name. 

### function SignalRegionData

```
inline SignalRegionData(
    const std::string & sr,
    double nobs,
    const EventCounter & scounter,
    const std::pair< double, double > & nbkg,
    double nsigscaled =0
)
```

Constructor with [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) arg for the signal count, but separate name. 

### function SignalRegionData

```
inline SignalRegionData(
    const std::string & sr,
    double nobs,
    const std::pair< double, double > & nsigMC,
    const std::pair< double, double > & nbkg,
    double nsigscaled =0
)
```

Constructor with {n,nsys} pair args. 

### function SignalRegionData

```
inline SignalRegionData(
    const std::string & sr,
    double nobs,
    double nsigMC,
    double nbkg,
    double nsigMCsys,
    double nbkgerr,
    double nsigscaled =0
)
```

Constructor with separate n & nsys args. 

### function SignalRegionData

```
inline SignalRegionData()
```

Default constructor. 

### function check

```
inline bool check() const
```

Consistency check. 

TodoAdd SR consistency checks 


### function scalefactor

```
inline double scalefactor() const
```

Uncertainty calculators. 

### function calc_n_sig_MC_err

```
inline double calc_n_sig_MC_err() const
```


### function calc_n_sig_scaled_err

```
inline double calc_n_sig_scaled_err() const
```


### function calc_n_sigbkg_err

```
inline double calc_n_sigbkg_err() const
```


### function combine_SR_MC_signal

```
inline void combine_SR_MC_signal(
    const SignalRegionData & other
)
```


## Public Attributes Documentation

### variable sr_label

```
std::string sr_label;
```

A label for the particular signal region of the analysis. 

### variable n_obs

```
double n_obs;
```

The number of events passing selection for this signal region as reported by the experiment. 

### variable n_sig_MC

```
double n_sig_MC;
```

The number of simulated model events passing selection for this signal region. 

### variable n_sig_MC_sys

```
double n_sig_MC_sys;
```

The absolute systematic error of n_sig_MC. 

### variable n_sig_MC_stat

```
double n_sig_MC_stat;
```

The absolute statistical (MC) error of n_sig_MC. 

### variable n_sig_scaled

```
double n_sig_scaled;
```

n_sig_MC, scaled to luminosity * cross-section 

### variable n_bkg

```
double n_bkg;
```

The number of standard model events expected to pass the selection for this signal region, as reported by the experiment. 

### variable n_bkg_err

```
double n_bkg_err;
```

The absolute error of n_bkg. 

-------------------------------

Updated on 2025-02-12 at 15:36:39 +0000