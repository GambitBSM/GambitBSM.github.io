---
title: "class Gambit::PID_pair"

description: "[No description available]"

---

# class Gambit::PID_pair



[No description available] [More...](#detailed-description)


`#include <PID_pair.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef std::pair< int, int > | **[iipair](/documentation/code/classes/classgambit_1_1pid__pair/#typedef-iipair)**  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/#function-pid-pair)**()<br>Constructors.  |
| | **[PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/#function-pid-pair)**(int pid1_in, int pid2_in) |
| | **[PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/#function-pid-pair)**(const iipair & PIDs_in) |
| virtual | **[~PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/#function-pid-pair)**()<br>Detstructor.  |
| void | **[set_pids](/documentation/code/classes/classgambit_1_1pid__pair/#function-set-pids)**(int pid1_in, int pid2_in)<br>Set PIDs, with sorting.  |
| void | **[set_pids](/documentation/code/classes/classgambit_1_1pid__pair/#function-set-pids)**(const iipair & PIDs_in) |
| const iipair & | **[PIDs](/documentation/code/classes/classgambit_1_1pid__pair/#function-pids)**() const<br>Get PIDs.  |
| int | **[pid1](/documentation/code/classes/classgambit_1_1pid__pair/#function-pid1)**() const |
| int | **[pid2](/documentation/code/classes/classgambit_1_1pid__pair/#function-pid2)**() const |
| [PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/) | **[cc_pid_pair](/documentation/code/classes/classgambit_1_1pid__pair/#function-cc-pid-pair)**() const<br>Get the charge-conjugated PID pair.  |
| bool | **[is_antiparticle_pair](/documentation/code/classes/classgambit_1_1pid__pair/#function-is-antiparticle-pair)**() const<br>Check if |pid1| == |pid2|.  |
| bool | **[operator==](/documentation/code/classes/classgambit_1_1pid__pair/#function-operator)**(const [PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/) & rhs) const |
| bool | **[operator!=](/documentation/code/classes/classgambit_1_1pid__pair/#function-operator)**(const [PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/) & rhs) const |
| bool | **[operator<](/documentation/code/classes/classgambit_1_1pid__pair/#function-operator)**(const [PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/) & rhs) const |
| bool | **[operator<=](/documentation/code/classes/classgambit_1_1pid__pair/#function-operator)**(const [PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/) & rhs) const |
| bool | **[operator>](/documentation/code/classes/classgambit_1_1pid__pair/#function-operator)**(const [PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/) & rhs) const |
| bool | **[operator>=](/documentation/code/classes/classgambit_1_1pid__pair/#function-operator)**(const [PID_pair](/documentation/code/classes/classgambit_1_1pid__pair/) & rhs) const |
| void | **[reset](/documentation/code/classes/classgambit_1_1pid__pair/#function-reset)**()<br>Reset the PIDs.  |
| std::string | **[str](/documentation/code/classes/classgambit_1_1pid__pair/#function-str)**() const<br>Get the PID pair as a string: "<pid1>_<pid2>".  |

## Detailed Description

```
class Gambit::PID_pair;
```


Simple class for holding a sorted pair of particle ID (PID) codes. This is essentially just a wrapper around a std::pair<int,int>, with forced ordering (first element <= second element) and some extra bells and whistles. 

## Public Types Documentation

### typedef iipair

```
typedef std::pair<int,int> Gambit::PID_pair::iipair;
```


## Public Functions Documentation

### function PID_pair

```
inline PID_pair()
```

Constructors. 

### function PID_pair

```
inline PID_pair(
    int pid1_in,
    int pid2_in
)
```


### function PID_pair

```
inline PID_pair(
    const iipair & PIDs_in
)
```


### function ~PID_pair

```
inline virtual ~PID_pair()
```

Detstructor. 

### function set_pids

```
inline void set_pids(
    int pid1_in,
    int pid2_in
)
```

Set PIDs, with sorting. 

### function set_pids

```
inline void set_pids(
    const iipair & PIDs_in
)
```


### function PIDs

```
inline const iipair & PIDs() const
```

Get PIDs. 

### function pid1

```
inline int pid1() const
```


### function pid2

```
inline int pid2() const
```


### function cc_pid_pair

```
inline PID_pair cc_pid_pair() const
```

Get the charge-conjugated PID pair. 

### function is_antiparticle_pair

```
inline bool is_antiparticle_pair() const
```

Check if |pid1| == |pid2|. 

### function operator==

```
inline bool operator==(
    const PID_pair & rhs
) const
```


Relational operators, simply using the relational operators for the underlying pair<int,int> 


### function operator!=

```
inline bool operator!=(
    const PID_pair & rhs
) const
```


### function operator<

```
inline bool operator<(
    const PID_pair & rhs
) const
```


### function operator<=

```
inline bool operator<=(
    const PID_pair & rhs
) const
```


### function operator>

```
inline bool operator>(
    const PID_pair & rhs
) const
```


### function operator>=

```
inline bool operator>=(
    const PID_pair & rhs
) const
```


### function reset

```
inline void reset()
```

Reset the PIDs. 

### function str

```
inline std::string str() const
```

Get the PID pair as a string: "<pid1>_<pid2>". 

-------------------------------

Updated on 2022-09-08 at 03:46:43 +0000