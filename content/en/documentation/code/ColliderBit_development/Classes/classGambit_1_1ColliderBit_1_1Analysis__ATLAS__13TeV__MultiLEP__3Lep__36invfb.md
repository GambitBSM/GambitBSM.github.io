---
title: 'class Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_3Lep_36invfb'

description: "[No description available]"

---








[No description available]

Inherits from [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/), Analysis

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_ATLAS_13TeV_MultiLEP_3Lep_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__3lep__36invfb/#function-analysis-atlas-13tev-multilep-3lep-36invfb)**() |
| virtual void | **[collect_results](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__3lep__36invfb/#function-collect-results)**() |

## Additional inherited members

**Public Classes inherited from [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| struct | **[ptComparison](/documentation/code/colliderbit_development/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb_1_1ptcomparison/)**  |
| struct | **[ptJetComparison](/documentation/code/colliderbit_development/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb_1_1ptjetcomparison/)**  |

**Public Functions inherited from [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| | **[Analysis_ATLAS_13TeV_MultiLEP_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#function-analysis-atlas-13tev-multilep-36invfb)**() |
| void | **[run](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#function-run)**(const HEPUtils::Event * event) |
| void | **[combine](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#function-combine)**(const Analysis * other)<br>Combine the variables of another copy of this analysis (typically on another thread) into this one.  |
| vector< HEPUtils::P4 > | **[get_W_ISR](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#function-get-w-isr)**(vector< const HEPUtils::Jet * > jets, HEPUtils::P4 Z, HEPUtils::P4 met) |

**Protected Functions inherited from [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| void | **[analysis_specific_reset](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#function-analysis-specific-reset)**() |

**Public Attributes inherited from [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| constexpr const char * | **[detector](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#variable-detector)**  |
| struct [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb::ptComparison](/documentation/code/colliderbit_development/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb_1_1ptcomparison/) | **[comparePt](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#variable-comparept)**  |
| struct [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb::ptJetComparison](/documentation/code/colliderbit_development/classes/structgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb_1_1ptjetcomparison/) | **[compareJetPt](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#variable-comparejetpt)**  |

**Protected Attributes inherited from [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/)**

|                | Name           |
| -------------- | -------------- |
| std::map< string, EventCounter > | **[_counters](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#variable--counters)**  |


## Public Functions Documentation

### function Analysis_ATLAS_13TeV_MultiLEP_3Lep_36invfb

```
inline Analysis_ATLAS_13TeV_MultiLEP_3Lep_36invfb()
```


### function collect_results

```
inline virtual void collect_results()
```


**Reimplements**: [Gambit::ColliderBit::Analysis_ATLAS_13TeV_MultiLEP_36invfb::collect_results](/documentation/code/colliderbit_development/classes/classgambit_1_1colliderbit_1_1analysis__atlas__13tev__multilep__36invfb/#function-collect-results)


-------------------------------

Updated on 2022-08-03 at 03:17:01 +0000