---
title: "class Gambit::ColliderBit::MC_xsec_container"
description: "A class for holding a total cross-section calculated via MC across multiple threads. "

---

# class Gambit::ColliderBit::MC_xsec_container



A class for holding a total cross-section calculated via MC across multiple threads. 


`#include <xsec.hpp>`

Inherits from [Gambit::ColliderBit::xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[MC_xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-mc-xsec-container)**()<br>Constructor.  |
| virtual | **[~MC_xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-mc-xsec-container)**() |
| void | **[reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-reset)**()<br>Reset this instance for reuse.  |
| void | **[log_event](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-log-event)**()<br>Tell the xsec object that there has been a new event.  |
| long long | **[num_events](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-num-events)**() const<br>Return the total number of events seen so far.  |
| double | **[xsec_per_event](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-xsec-per-event)**() const<br>Return the cross-section per event seen (in fb).  |
| void | **[set_num_events](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-set-num-events)**(long long n)<br>Set the total number of events seen so far.  |
| void | **[average_xsec](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-average-xsec)**(double other_xsec, double other_xsecerr, long long other_ntot)<br>Average cross-sections and combine errors.  |
| void | **[average_xsec](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-average-xsec)**(const [MC_xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/) & other) |
| void | **[sum_xsecs](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-sum-xsecs)**(double other_xsec, double other_xsecerr, long long other_ntot)<br>Sum cross-sections and add errors in quadrature.  |
| void | **[sum_xsecs](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-sum-xsecs)**(const [MC_xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/) & other) |
| void | **[gather_xsecs](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-gather-xsecs)**()<br>Collect xsec predictions from other threads and do a weighted combination.  |
| void | **[gather_num_events](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-gather-num-events)**()<br>Collect total events seen on all threads.  |
| std::map< std::string, double > | **[get_content_as_map](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/#function-gambitcolliderbitmc-xsec-container-get-content-as-map)**() const<br>Get content as map <string,double> map (for easy printing).  |

## Additional inherited members

**Public Functions inherited from [Gambit::ColliderBit::xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/)**

|                | Name           |
| -------------- | -------------- |
| | **[xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-xsec-container)**()<br>Constructor.  |
| virtual | **[~xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-xsec-container)**() |
| double | **[operator()](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-operator)**() const<br>Return the full cross-section (in fb).  |
| double | **[xsec](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-xsec)**() const |
| double | **[xsec_err](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-xsec-err)**() const<br>Return the cross-section error (in fb).  |
| double | **[xsec_relerr](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-xsec-relerr)**() const<br>Return the cross-section relative error.  |
| void | **[set_xsec](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-set-xsec)**(double xs, double xserr)<br>Set the cross-section and its error (in fb).  |
| void | **[set_info_string](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-set-info-string)**(std::string info_string_in)<br>Set the info string.  |
| std::string | **[info_string](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-info-string)**() const<br>Get the info string.  |
| void | **[set_trust_level](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-set-trust-level)**(int trust_level_in)<br>Set the trust level.  |
| int | **[trust_level](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#function-gambitcolliderbitxsec-container-trust-level)**() const<br>Get the trust level.  |

**Public Attributes inherited from [Gambit::ColliderBit::xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/)**

|                | Name           |
| -------------- | -------------- |
| const std::string | **[unit](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#variable-gambitcolliderbitxsec-container-unit)** <br>String Let's make it clear that we work with fb as unit.  |

**Protected Attributes inherited from [Gambit::ColliderBit::xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/)**

|                | Name           |
| -------------- | -------------- |
| double | **[_xsec](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#variable-gambitcolliderbitxsec-container-xsec)**  |
| double | **[_xsecerr](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#variable-gambitcolliderbitxsec-container-xsecerr)**  |
| std::string | **[_info_string](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#variable-gambitcolliderbitxsec-container-info-string)**  |
| int | **[_trust_level](/documentation/code/classes/classgambit_1_1colliderbit_1_1xsec__container/#variable-gambitcolliderbitxsec-container-trust-level)**  |


## Public Functions Documentation

### function MC_xsec_container

```
MC_xsec_container()
```

Constructor. 

Definitions of [MC_xsec_container](/documentation/code/classes/classgambit_1_1colliderbit_1_1mc__xsec__container/) members 


### function ~MC_xsec_container

```
inline virtual ~MC_xsec_container()
```


### function reset

```
void reset()
```

Reset this instance for reuse. 

Public method to reset this instance for reuse, avoiding the need for "new" or "delete". 


### function log_event

```
void log_event()
```

Tell the xsec object that there has been a new event. 

Increment the number of events seen so far. 


### function num_events

```
long long num_events() const
```

Return the total number of events seen so far. 

### function xsec_per_event

```
double xsec_per_event() const
```

Return the cross-section per event seen (in fb). 

### function set_num_events

```
void set_num_events(
    long long n
)
```

Set the total number of events seen so far. 

### function average_xsec

```
void average_xsec(
    double other_xsec,
    double other_xsecerr,
    long long other_ntot
)
```

Average cross-sections and combine errors. 

### function average_xsec

```
void average_xsec(
    const MC_xsec_container & other
)
```


### function sum_xsecs

```
void sum_xsecs(
    double other_xsec,
    double other_xsecerr,
    long long other_ntot
)
```

Sum cross-sections and add errors in quadrature. 

### function sum_xsecs

```
void sum_xsecs(
    const MC_xsec_container & other
)
```


### function gather_xsecs

```
void gather_xsecs()
```

Collect xsec predictions from other threads and do a weighted combination. 

### function gather_num_events

```
void gather_num_events()
```

Collect total events seen on all threads. 

### function get_content_as_map

```
std::map< std::string, double > get_content_as_map() const
```

Get content as map <string,double> map (for easy printing). 

Get content as a <string,double> map (for easy printing). 


-------------------------------

Updated on 2022-09-08 at 02:00:48 +0000