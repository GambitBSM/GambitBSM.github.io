---
title: "class Gambit::ColliderBit::EventCounter"
description: "A simple class for counting events of type HEPUtils::Event. "

---

# class Gambit::ColliderBit::EventCounter



A simple class for counting events of type HEPUtils::Event. 


`#include <EventCounter.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-eventcounter)**() |
| | **[EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-eventcounter)**(const std::string name) |
| void | **[init](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-init)**(const std::string name) |
| void | **[reset](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-reset)**() |
| void | **[set_name](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-set-name)**(const std::string name) |
| std::string | **[name](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-name)**() const |
| void | **[set_sum](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-set-sum)**(int sum) |
| int | **[sum](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-sum)**() const |
| void | **[set_weight_sum](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-set-weight-sum)**(double weight_sum) |
| double | **[weight_sum](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-weight-sum)**() const |
| void | **[set_weight_sum_err](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-set-weight-sum-err)**(double weight_sum_err) |
| double | **[weight_sum_err](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-weight-sum-err)**() const |
| void | **[add_event](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-add-event)**(const HEPUtils::Event & event, double w, double werr =0.0) |
| void | **[add_event](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-add-event)**(const HEPUtils::Event * event_ptr, double w, double werr =0.0) |
| void | **[add_event](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-add-event)**(const HEPUtils::Event & event) |
| void | **[add_event](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-add-event)**(const HEPUtils::Event * event_ptr) |
| [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) & | **[operator+=](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-operator)**(const HEPUtils::Event & event) |
| [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) & | **[operator+=](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-operator)**(const [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) & rhs) |
| [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) & | **[combine](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-combine)**(const [EventCounter](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/) & other) |
| void | **[set_store_accepted_event_IDs](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-set-store-accepted-event-ids)**(bool setting) |
| bool | **[store_accepted_event_IDs](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-store-accepted-event-ids)**() |
| std::vector< unsigned int > | **[get_event_acceptance_record](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-get-event-acceptance-record)**() const |
| void | **[clear_event_acceptance_record](/documentation/code/classes/classgambit_1_1colliderbit_1_1eventcounter/#function-clear-event-acceptance-record)**() |

## Public Functions Documentation

### function EventCounter

```
inline EventCounter()
```


### function EventCounter

```
inline EventCounter(
    const std::string name
)
```


### function init

```
inline void init(
    const std::string name
)
```


### function reset

```
inline void reset()
```


### function set_name

```
inline void set_name(
    const std::string name
)
```


### function name

```
inline std::string name() const
```


### function set_sum

```
inline void set_sum(
    int sum
)
```


### function sum

```
inline int sum() const
```


### function set_weight_sum

```
inline void set_weight_sum(
    double weight_sum
)
```


### function weight_sum

```
inline double weight_sum() const
```


### function set_weight_sum_err

```
inline void set_weight_sum_err(
    double weight_sum_err
)
```


### function weight_sum_err

```
inline double weight_sum_err() const
```


### function add_event

```
inline void add_event(
    const HEPUtils::Event & event,
    double w,
    double werr =0.0
)
```


### function add_event

```
inline void add_event(
    const HEPUtils::Event * event_ptr,
    double w,
    double werr =0.0
)
```


### function add_event

```
inline void add_event(
    const HEPUtils::Event & event
)
```


### function add_event

```
inline void add_event(
    const HEPUtils::Event * event_ptr
)
```


### function operator+=

```
inline EventCounter & operator+=(
    const HEPUtils::Event & event
)
```


### function operator+=

```
inline EventCounter & operator+=(
    const EventCounter & rhs
)
```


### function combine

```
inline EventCounter & combine(
    const EventCounter & other
)
```


### function set_store_accepted_event_IDs

```
inline void set_store_accepted_event_IDs(
    bool setting
)
```


### function store_accepted_event_IDs

```
inline bool store_accepted_event_IDs()
```


### function get_event_acceptance_record

```
inline std::vector< unsigned int > get_event_acceptance_record() const
```


### function clear_event_acceptance_record

```
inline void clear_event_acceptance_record()
```


-------------------------------

Updated on 2026-11-03 at 14:50:43 +0000