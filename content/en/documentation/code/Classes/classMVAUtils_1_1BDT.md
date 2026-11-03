---
title: "class MVAUtils::BDT"

description: "[No description available]"

---

# class MVAUtils::BDT



[No description available] [More...](#detailed-description)


`#include <BDT.h>`

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[BDT](/documentation/code/classes/classmvautils_1_1bdt/#function-bdt)**(TTree * tree) |
| | **[BDT](/documentation/code/classes/classmvautils_1_1bdt/#function-bdt)**(TMVA::MethodBDT * bdt, bool isRegression =true, bool useYesNoLeaf =false) |
| | **[~BDT](/documentation/code/classes/classmvautils_1_1bdt/#function-bdt)**() |
| unsigned int | **[GetNTrees](/documentation/code/classes/classmvautils_1_1bdt/#function-getntrees)**() const |
| int | **[GetNVars](/documentation/code/classes/classmvautils_1_1bdt/#function-getnvars)**() const |
| float | **[GetOffset](/documentation/code/classes/classmvautils_1_1bdt/#function-getoffset)**() const |
| float | **[GetResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-getresponse)**(const std::vector< float > & values) const |
| float | **[GetResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-getresponse)**(const std::vector< float * > & pointers) const |
| float | **[GetResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-getresponse)**() const |
| float | **[GetClassification](/documentation/code/classes/classmvautils_1_1bdt/#function-getclassification)**(const std::vector< float > & values) const |
| float | **[GetClassification](/documentation/code/classes/classmvautils_1_1bdt/#function-getclassification)**(const std::vector< float * > & pointers) const |
| float | **[GetClassification](/documentation/code/classes/classmvautils_1_1bdt/#function-getclassification)**() const |
| float | **[GetGradBoostMVA](/documentation/code/classes/classmvautils_1_1bdt/#function-getgradboostmva)**(const std::vector< float > & values) const |
| float | **[GetGradBoostMVA](/documentation/code/classes/classmvautils_1_1bdt/#function-getgradboostmva)**(const std::vector< float * > & pointers) const |
| std::vector< float > | **[GetMultiResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-getmultiresponse)**(const std::vector< float > & values, unsigned int numClasses) const |
| std::vector< float > | **[GetMultiResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-getmultiresponse)**(const std::vector< float * > & pointers, unsigned int numClasses) const |
| std::vector< float > | **[GetMultiResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-getmultiresponse)**(unsigned int numClasses) const |
| std::vector< float > | **[GetValues](/documentation/code/classes/classmvautils_1_1bdt/#function-getvalues)**() const |
| const std::vector< float * > & | **[GetPointers](/documentation/code/classes/classmvautils_1_1bdt/#function-getpointers)**() const |
| void | **[SetPointers](/documentation/code/classes/classmvautils_1_1bdt/#function-setpointers)**(const std::vector< float * > & pointers) |
| TTree * | **[WriteTree](/documentation/code/classes/classmvautils_1_1bdt/#function-writetree)**(TString name ="BDT") const |
| void | **[PrintForest](/documentation/code/classes/classmvautils_1_1bdt/#function-printforest)**() const |
| void | **[PrintTree](/documentation/code/classes/classmvautils_1_1bdt/#function-printtree)**(unsigned int itree) const |
| float | **[GetTreeResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-gettreeresponse)**(const std::vector< float > & values, MVAUtils::index_t index) const |
| float | **[GetTreeResponse](/documentation/code/classes/classmvautils_1_1bdt/#function-gettreeresponse)**(const std::vector< float * > & pointers, MVAUtils::index_t index) const |

## Detailed Description

```
class MVAUtils::BDT;
```


Simplified Boosted Regression Tree, support TMVA, lgbm, and xgboost. Holds a forest (vector of top nodes of each decision tree) and a constant offset or set of weights (not always used).

Can be constructed from TMVA::MethodBDT or a TTree. Each entry of the TTree represents a binary tree and each element of the vectors stored in the TTree represent a node.

The response can be evaluated from a vector of floats or a vector of pointers (to avoid creating vectors at each call) which can be stored internally (m_pointers) 

## Public Functions Documentation

### function BDT

```
explicit BDT(
    TTree * tree
)
```


Constructor. The input tree must be created with convertLGBMToRootTree.py (for lgbm training) or with convertXGBoostToRootTree.py (for xgboost training) or with convertXmlToRootTree (for tmva training) 


### function BDT

```
explicit BDT(
    TMVA::MethodBDT * bdt,
    bool isRegression =true,
    bool useYesNoLeaf =false
)
```


c-tor from TMVA::MethodBDT 


### function ~BDT

```
~BDT()
```


### function GetNTrees

```
unsigned int GetNTrees() const
```


Number of trees in the whole forest 


### function GetNVars

```
int GetNVars() const
```


Number of variables expected in the inputs 


### function GetOffset

```
float GetOffset() const
```


Get the offset to the whole forest 


### function GetResponse

```
float GetResponse(
    const std::vector< float > & values
) const
```


Get response of the forest, for regression

Return offset + the sum of the response of each tree 


### function GetResponse

```
float GetResponse(
    const std::vector< float * > & pointers
) const
```


Return offset + the sum of the response of each tree 


### function GetResponse

```
inline float GetResponse() const
```


### function GetClassification

```
float GetClassification(
    const std::vector< float > & values
) const
```


Get response of the forest, for classification 


### function GetClassification

```
float GetClassification(
    const std::vector< float * > & pointers
) const
```


### function GetClassification

```
inline float GetClassification() const
```


### function GetGradBoostMVA

```
float GetGradBoostMVA(
    const std::vector< float > & values
) const
```


### function GetGradBoostMVA

```
float GetGradBoostMVA(
    const std::vector< float * > & pointers
) const
```


### function GetMultiResponse

```
std::vector< float > GetMultiResponse(
    const std::vector< float > & values,
    unsigned int numClasses
) const
```


Get response of the forest, for multiclassification (e.g. b-tagging) 


### function GetMultiResponse

```
std::vector< float > GetMultiResponse(
    const std::vector< float * > & pointers,
    unsigned int numClasses
) const
```


### function GetMultiResponse

```
inline std::vector< float > GetMultiResponse(
    unsigned int numClasses
) const
```


### function GetValues

```
inline std::vector< float > GetValues() const
```


Return the values corresponding to m_pointers (or an empty vector) 


### function GetPointers

```
inline const std::vector< float * > & GetPointers() const
```


Return stored pointers (which are used by methods with no args) 


### function SetPointers

```
inline void SetPointers(
    const std::vector< float * > & pointers
)
```


Set the stored pointers so that one can use methods with no args 


### function WriteTree

```
TTree * WriteTree(
    TString name ="BDT"
) const
```


Return a TTree representing the [BDT](/documentation/code/classes/classmvautils_1_1bdt/): each entry is a binary tree, each element of the vectors is a node 


### function PrintForest

```
void PrintForest() const
```


for debugging, print out tree or forest to stdout 


### function PrintTree

```
void PrintTree(
    unsigned int itree
) const
```


### function GetTreeResponse

```
float GetTreeResponse(
    const std::vector< float > & values,
    MVAUtils::index_t index
) const
```


for debugging, return the response of a sigle tree given the index of its top node 


### function GetTreeResponse

```
float GetTreeResponse(
    const std::vector< float * > & pointers,
    MVAUtils::index_t index
) const
```


-------------------------------

Updated on 2026-11-03 at 14:50:42 +0000