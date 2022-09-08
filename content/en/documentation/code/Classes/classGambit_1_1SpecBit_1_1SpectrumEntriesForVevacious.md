---
title: "class Gambit::SpecBit::SpectrumEntriesForVevacious"

description: "[No description available]"

---

# class Gambit::SpecBit::SpectrumEntriesForVevacious



[No description available] [More...](#detailed-description)


`#include <SpecBit_types.hpp>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SpectrumEntriesForVevacious](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-spectrumentriesforvevacious)**() |
| void | **[set_scale](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-set-scale)**(double inScale) |
| void | **[set_inputPath](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-set-inputpath)**(std::string inPath) |
| void | **[set_inputFilename](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-set-inputfilename)**(std::string inFile) |
| double | **[get_scale](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-get-scale)**() |
| std::string | **[get_inputFilename](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-get-inputfilename)**() |
| std::string | **[get_inputPath](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-get-inputpath)**() |
| void | **[add_entry](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-add-entry)**(std::string name, vec_pair_int_dbl vec, int dimension) |
| [map_str_SpectrumEntry](/documentation/code/namespaces/namespacegambit_1_1specbit/#typedef-gambitspecbit-map-str-spectrumentry) | **[get_spec_entry_map](/documentation/code/classes/classgambit_1_1specbit_1_1spectrumentriesforvevacious/#function-gambitspecbitspectrumentriesforvevacious-get-spec-entry-map)**() |

## Detailed Description

```
class Gambit::SpecBit::SpectrumEntriesForVevacious;
```


class for setting & storing all spectrum entries of type [SpectrumEntry](/documentation/code/classes/structgambit_1_1specbit_1_1spectrumentry/) that need to be passed to vevacious (scale, input filenames & paths as well as spectrum entries) passed to vevacious before calling it 

## Public Functions Documentation

### function SpectrumEntriesForVevacious

```
inline SpectrumEntriesForVevacious()
```


### function set_scale

```
inline void set_scale(
    double inScale
)
```


### function set_inputPath

```
inline void set_inputPath(
    std::string inPath
)
```


### function set_inputFilename

```
inline void set_inputFilename(
    std::string inFile
)
```


### function get_scale

```
inline double get_scale()
```


### function get_inputFilename

```
inline std::string get_inputFilename()
```


### function get_inputPath

```
inline std::string get_inputPath()
```


### function add_entry

```
void add_entry(
    std::string name,
    vec_pair_int_dbl vec,
    int dimension
)
```


add a [SpectrumEntry](/documentation/code/classes/structgambit_1_1specbit_1_1spectrumentry/) type to the 'spec_entry_map' map. GAMBIT will iterate through it and pass all contents to vevacious before it is called. 


### function get_spec_entry_map

```
inline map_str_SpectrumEntry get_spec_entry_map()
```


-------------------------------

Updated on 2022-09-08 at 01:48:56 +0000