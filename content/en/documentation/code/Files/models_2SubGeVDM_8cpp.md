---
title: "file models/models/SubGeVDM.cpp"

description: "[No description available]"

---

# file models/models/SubGeVDM.cpp

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| | **[USE_MODEL_PIPE](/documentation/code/files/models_2subgevdm_8cpp/#function-use-model-pipe)**(PARENT ) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("mDM" , mDM ) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("mAp" , mAp ) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("gDM" , gDM ) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("kappa" , kappa ) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("etaDM" , myP ["etaDM"]) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("mDM" , myP ["mDM"]) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("mAp" , myP ["mAp"]) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("gDM" , myP ["gDM"]) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("kappa" , myP ["kappa"]) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("etaDM" , myP/ myP["etaDM_mDM"]["mDM"]) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("mAp" , 2 *myP * sqrt(myP["epsR"]+1)["mDM"]) |
| targetP | **[setValue](/documentation/code/files/models_2subgevdm_8cpp/#function-setvalue)**("epsR" , myP ["epsR"]) |

## Attributes

|                | Name           |
| -------------- | -------------- |
| void ModelParameters & | **[targetP](/documentation/code/files/models_2subgevdm_8cpp/#variable-targetp)**  |
| double | **[mDM](/documentation/code/files/models_2subgevdm_8cpp/#variable-mdm)**  |
| double | **[kappa](/documentation/code/files/models_2subgevdm_8cpp/#variable-kappa)**  |
| double | **[sigmae](/documentation/code/files/models_2subgevdm_8cpp/#variable-sigmae)**  |
| double | **[reduced_mass](/documentation/code/files/models_2subgevdm_8cpp/#variable-reduced-mass)**  |
| double | **[effective_coupling](/documentation/code/files/models_2subgevdm_8cpp/#variable-effective-coupling)**  |
| double | **[gDM](/documentation/code/files/models_2subgevdm_8cpp/#variable-gdm)**  |
| double | **[sigmaN](/documentation/code/files/models_2subgevdm_8cpp/#variable-sigman)**  |
| double | **[gN](/documentation/code/files/models_2subgevdm_8cpp/#variable-gn)**  |

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |
|  | **[MODEL](/documentation/code/files/models_2subgevdm_8cpp/#define-model)**  |
|  | **[PARENT](/documentation/code/files/models_2subgevdm_8cpp/#define-parent)**  |


## Functions Documentation

### function USE_MODEL_PIPE

```
USE_MODEL_PIPE(
    PARENT 
)
```


### function setValue

```
targetP setValue(
    "mDM" ,
    mDM 
)
```


### function setValue

```
targetP setValue(
    "mAp" ,
    mAp 
)
```


### function setValue

```
targetP setValue(
    "gDM" ,
    gDM 
)
```


### function setValue

```
targetP setValue(
    "kappa" ,
    kappa 
)
```


### function setValue

```
targetP setValue(
    "etaDM" ,
    myP ["etaDM"]
)
```


### function setValue

```
targetP setValue(
    "mDM" ,
    myP ["mDM"]
)
```


### function setValue

```
targetP setValue(
    "mAp" ,
    myP ["mAp"]
)
```


### function setValue

```
targetP setValue(
    "gDM" ,
    myP ["gDM"]
)
```


### function setValue

```
targetP setValue(
    "kappa" ,
    myP ["kappa"]
)
```


### function setValue

```
targetP setValue(
    "etaDM" ,
    myP/ myP["etaDM_mDM"]["mDM"]
)
```


### function setValue

```
targetP setValue(
    "mAp" ,
    2 *myP * sqrt(myP["epsR"]+1)["mDM"]
)
```


### function setValue

```
targetP setValue(
    "epsR" ,
    myP ["epsR"]
)
```



## Attributes Documentation

### variable targetP

```
void ModelParameters & targetP {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;
```


### variable mDM

```
double mDM = myP["mDM"];
```


### variable kappa

```
double kappa = myP["kappa"];
```


### variable sigmae

```
double sigmae = myP["sigmae"];
```


### variable reduced_mass

```
double reduced_mass = mDM * m_electron / (mDM + m_electron);
```


### variable effective_coupling

```
double effective_coupling = sqrt(sigmae/gev2cm2*pi*pow(pow(mAp,2)+pow(alpha_EM*m_electron,2),2))/reduced_mass;
```


### variable gDM

```
double gDM = effective_coupling/sqrt(4*pi*alpha_EM)/kappa;
```


### variable sigmaN

```
double sigmaN = myP["sigmaN"];
```


### variable gN

```
double gN = sqrt(sigmaN*pi/gev2cm2)/reduced_mass;
```



## Macros Documentation

### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


### define MODEL

```
#define MODEL SubGeVDM_fermion
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for the SubGeVDM models

Contains the interpret-as-parent translation functions for:

SubGeVDM_fermion_sigmae --> SubGeVDM_fermion SubGeVDM_fermion_sigmaN --> SubGeVDM_fermion SubGeVDM_fermion_RDprior --> SubGeVDM_fermion Resonant_SubGeVDM_fermion --> SubGeVDM_fermion Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion

As well as the interpret-as-friend translation

SubGeVDM_fermion --> AnnihilatingDM_general



------------------


# Authors

(add name and date if you modify)

Felix Kahlhoefer ([kahlhoefer@kit.edu](mailto:kahlhoefer@kit.edu)) 

2022 May

Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

2023 Oct



------------------


### define PARENT

```
#define PARENT SubGeVDM_fermion
```


## Source code

```
///  GAMBIT: Global and Modular BSM Inference Tool
///  *********************************************
///
///  Model translation functions for the SubGeVDM models
///
///  Contains the interpret-as-parent translation
///  functions for:
///
///  SubGeVDM_fermion_sigmae           --> SubGeVDM_fermion
///  SubGeVDM_fermion_sigmaN           --> SubGeVDM_fermion
///  SubGeVDM_fermion_RDprior          --> SubGeVDM_fermion
///  Resonant_SubGeVDM_fermion         --> SubGeVDM_fermion
///  Resonant_SubGeVDM_fermion_RDprior --> Resonant_SubGeVDM_fermion
///
///  As well as the interpret-as-friend translation
///
///  SubGeVDM_fermion          --> AnnihilatingDM_general
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Felix Kahlhoefer
///          (kahlhoefer@kit.edu)
///  \date 2022 May
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@kit.edu)
///  \date 2023 Oct
///
///  *********************************************


#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"
#include "gambit/Utils/numerical_constants.hpp"

#include "gambit/Models/models/SubGeVDM.hpp"

#define MODEL SubGeVDM_fermion
  void MODEL_NAMESPACE::SubGeVDM_fermion_to_AnnihilatingDM_general (const ModelParameters &, ModelParameters &targetP)
  {
    USE_MODEL_PIPE(AnnihilatingDM_general) // get pipe for "interpret as friend" function
    logger()<<"Running interpret_as_friend calculations for SubGeVDM_fermion -> AnnihilatingDM_general ..."<<EOM;

    const double k = (*Dep::wimp_sc) ? 1. : 0.5;
    const double suppression = *Dep::ID_suppression;

    targetP.setValue("mass", *Dep::mwimp);
    // In AnnihilatingDM_general the parameter "sigmav" is assumed to already include
    // supression and the factor k
    targetP.setValue("sigmav", k*suppression*(*Dep::sigmav));
  }
#undef MODEL

#define MODEL SubGeVDM_fermion_sigmae
#define PARENT SubGeVDM_fermion
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

    USE_MODEL_PIPE(PARENT) // get pipe for "interpret as PARENT" function

    double mAp = myP["mAp"];
    double mDM = myP["mDM"];
    double kappa = myP["kappa"];
    double sigmae = myP["sigmae"];

    double reduced_mass = mDM * m_electron / (mDM + m_electron);
    double effective_coupling = sqrt(sigmae/gev2cm2*pi*pow(pow(mAp,2)+pow(alpha_EM*m_electron,2),2))/reduced_mass;
    double gDM = effective_coupling/sqrt(4*pi*alpha_EM)/kappa;

    targetP.setValue("mDM", mDM);
    targetP.setValue("mAp", mAp);
    targetP.setValue("gDM", gDM);
    targetP.setValue("kappa", kappa);
    targetP.setValue("etaDM", myP["etaDM"]);
  }
#undef PARENT
#undef MODEL

#define MODEL SubGeVDM_fermion_sigmaN
#define PARENT SubGeVDM_fermion
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

    USE_MODEL_PIPE(PARENT) // get pipe for "interprete as PARENT" function

    double mAp = myP["mAp"];
    double mDM = myP["mDM"];
    double kappa = myP["kappa"];
    double sigmaN = myP["sigmaN"];

    double reduced_mass = mDM * m_proton / (mDM + m_proton);
    double gN = sqrt(sigmaN*pi/gev2cm2)/reduced_mass;
    double gDM = gN*pow(mAp,2)/sqrt(4*pi*alpha_EM)/kappa;

    targetP.setValue("mDM", mDM);
    targetP.setValue("mAp", mAp);
    targetP.setValue("gDM", gDM);
    targetP.setValue("kappa", kappa);
    targetP.setValue("etaDM", myP["etaDM"]);
  }
#undef PARENT
#undef MODEL

#define MODEL SubGeVDM_fermion_RDprior
#define PARENT SubGeVDM_fermion
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

    targetP.setValue("mDM", myP["mDM"]);
    targetP.setValue("mAp", myP["mAp"]);
    targetP.setValue("gDM", myP["gDM"]);
    targetP.setValue("kappa", myP["kappa"]);
    targetP.setValue("etaDM", myP["etaDM_mDM"]/myP["mDM"]);
  }
#undef PARENT
#undef MODEL

#define MODEL Resonant_SubGeVDM_fermion
#define PARENT SubGeVDM_fermion
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for Resonant_SubGeVDM_fermion -> SubGeVDM_fermion ..."<<EOM;

    targetP.setValue("mDM", myP["mDM"]);
    targetP.setValue("gDM", myP["gDM"]);
    targetP.setValue("kappa", myP["kappa"]);
    targetP.setValue("etaDM", myP["etaDM"]);
    targetP.setValue("mAp", 2 * myP["mDM"] * sqrt(myP["epsR"] + 1));
  }
#undef PARENT
#undef MODEL

#define MODEL Resonant_SubGeVDM_fermion_RDprior
#define PARENT Resonant_SubGeVDM_fermion
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

    targetP.setValue("mDM", myP["mDM"]);
    targetP.setValue("gDM", myP["gDM"]);
    targetP.setValue("kappa", myP["kappa"]);
    targetP.setValue("epsR", myP["epsR"]);
    targetP.setValue("etaDM", myP["etaDM_mDM"]/myP["mDM"]);
  }
#undef PARENT
#undef MODEL

#define MODEL SubGeVDM_scalar
  void MODEL_NAMESPACE::SubGeVDM_scalar_to_AnnihilatingDM_general (const ModelParameters &, ModelParameters &targetP)
  {
    USE_MODEL_PIPE(AnnihilatingDM_general) // get pipe for "interpret as friend" function
    logger()<<"Running interpret_as_friend calculations for SubGeVDM_scalar -> AnnihilatingDM_general ..."<<EOM;

    const double k = (*Dep::wimp_sc) ? 1. : 0.5;
    const double suppression = *Dep::ID_suppression;

    targetP.setValue("mass", *Dep::mwimp);
    // In AnnihilatingDM_general the parameter "sigmav" is assumed to already include
    // supression and the factor k
    targetP.setValue("sigmav", k*suppression*(*Dep::sigmav));
  }
#undef MODEL

#define MODEL SubGeVDM_scalar_RDprior
#define PARENT SubGeVDM_scalar
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

    targetP.setValue("mDM", myP["mDM"]);
    targetP.setValue("mAp", myP["mAp"]);
    targetP.setValue("gDM", myP["gDM"]);
    targetP.setValue("kappa", myP["kappa"]);
    targetP.setValue("etaDM", myP["etaDM_mDM"]/myP["mDM"]);
  }
#undef PARENT
#undef MODEL

#define MODEL Resonant_SubGeVDM_scalar
#define PARENT SubGeVDM_scalar
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

    targetP.setValue("mDM", myP["mDM"]);
    targetP.setValue("gDM", myP["gDM"]);
    targetP.setValue("kappa", myP["kappa"]);
    targetP.setValue("etaDM", myP["etaDM"]);
    targetP.setValue("mAp", 2 * myP["mDM"] * sqrt(myP["epsR"] + 1));
  }
#undef PARENT
#undef MODEL

#define MODEL Resonant_SubGeVDM_scalar_RDprior
#define PARENT Resonant_SubGeVDM_scalar
  void MODEL_NAMESPACE::CAT_3(MODEL,_to_,PARENT) (const ModelParameters &myP, ModelParameters &targetP)
  {
    logger()<<"Running interpret_as_parent calculations for " STRINGIFY(MODEL) " --> " STRINGIFY(PARENT) "."<<LogTags::info<<EOM;

    targetP.setValue("mDM", myP["mDM"]);
    targetP.setValue("gDM", myP["gDM"]);
    targetP.setValue("kappa", myP["kappa"]);
    targetP.setValue("epsR", myP["epsR"]);
    targetP.setValue("etaDM", myP["etaDM_mDM"]/myP["mDM"]);
  }
#undef PARENT
#undef MODEL
```


-------------------------------

Updated on 2024-07-18 at 13:53:33 +0000
