---
title: 'file models/CosmoEnergyInjection.cpp'

description: "[No description available]"

---

# models/CosmoEnergyInjection.cpp

[No description available]

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[MODEL](/documentation/code/files/cosmoenergyinjection_8cpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/cosmoenergyinjection_8cpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/cosmoenergyinjection_8cpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/cosmoenergyinjection_8cpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/cosmoenergyinjection_8cpp/#define-model)**  |
|  | **[MODEL](/documentation/code/files/cosmoenergyinjection_8cpp/#define-model)**  |




## Macros Documentation

### define MODEL

```
#define MODEL AnnihilatingDM_mixture
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for Cosmological Energy injection



------------------


# Authors

(add name and date if you modify)

Patrick Stöcker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2019 Sep 

2020 Jan



------------------


### define MODEL

```
#define MODEL AnnihilatingDM_mixture
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for Cosmological Energy injection



------------------


# Authors

(add name and date if you modify)

Patrick Stöcker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2019 Sep 

2020 Jan



------------------


### define MODEL

```
#define MODEL AnnihilatingDM_mixture
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for Cosmological Energy injection



------------------


# Authors

(add name and date if you modify)

Patrick Stöcker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2019 Sep 

2020 Jan



------------------


### define MODEL

```
#define MODEL AnnihilatingDM_mixture
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for Cosmological Energy injection



------------------


# Authors

(add name and date if you modify)

Patrick Stöcker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2019 Sep 

2020 Jan



------------------


### define MODEL

```
#define MODEL AnnihilatingDM_mixture
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for Cosmological Energy injection



------------------


# Authors

(add name and date if you modify)

Patrick Stöcker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2019 Sep 

2020 Jan



------------------


### define MODEL

```
#define MODEL AnnihilatingDM_mixture
```


GAMBIT: Global and Modular BSM Inference Tool 

------------------

Model translation functions for Cosmological Energy injection



------------------


# Authors

(add name and date if you modify)

Patrick Stöcker ([stoecker@physik.rwth-aachen.de](mailto:stoecker@physik.rwth-aachen.de)) 

2019 Sep 

2020 Jan



------------------


## Source code

```
///  GAMBIT: Global and Modular BSM Inference Tool
///  *********************************************
///
///  Model translation functions for Cosmological Energy injection
///
///  *********************************************
///
///  Authors
///  =======
///
///  (add name and date if you modify)
///
///  \author Patrick Stöcker
///          (stoecker@physik.rwth-aachen.de)
///  \date 2019 Sep
///  \date 2020 Jan
///
///  *********************************************

#include <string>
#include <vector>

#include "gambit/Models/model_macros.hpp"
#include "gambit/Models/model_helpers.hpp"
#include "gambit/Logs/logger.hpp"
#include "gambit/Utils/util_functions.hpp"
#include "gambit/Utils/numerical_constants.hpp"

#include "gambit/Models/models/CosmoEnergyInjection.hpp"

#define MODEL AnnihilatingDM_mixture
void MODEL_NAMESPACE::AnnihilatingDM_mixture_to_AnnihilatingDM_general (const ModelParameters &myP, ModelParameters &targetP)
{
  logger()<<"Running interpret_as_parent calculations for AnnihilatingDM_mixture --> AnnihilatingDM_general ..."<<LogTags::info<<EOM;

  targetP.setValue("mass", myP.getValue("mass"));
  targetP.setValue("sigmav", myP.getValue("sigmav"));
}
#undef MODEL

#define MODEL AnnihilatingDM_photon
void MODEL_NAMESPACE::AnnihilatingDM_photon_to_AnnihilatingDM_mixture (const ModelParameters &myP, ModelParameters &targetP)
{
  logger()<<"Running interpret_as_parent calculations for AnnihilatingDM_photon --> AnnihilatingDM_mixture ..."<<LogTags::info<<EOM;

  targetP.setValue("mass", myP.getValue("mass"));
  targetP.setValue("sigmav", myP.getValue("sigmav"));

  // All decays into photons (BR into electrons is 0.0)
  targetP.setValue("BR_el", 0.0);
  targetP.setValue("BR_ph", 1.0);
}
#undef MODEL

#define MODEL AnnihilatingDM_electron
void MODEL_NAMESPACE::AnnihilatingDM_electron_to_AnnihilatingDM_mixture (const ModelParameters &myP, ModelParameters &targetP)
{
  USE_MODEL_PIPE(AnnihilatingDM_mixture)
  logger()<<"Running interpret_as_parent calculations for AnnihilatingDM_electron --> AnnihilatingDM_mixture ..."<<LogTags::info<<EOM;

  targetP.setValue("mass", myP.getValue("mass"));
  targetP.setValue("sigmav", myP.getValue("sigmav"));

  // All decays into electrons (BR into photons is 0.0)
  targetP.setValue("BR_el", 1.0);
  targetP.setValue("BR_ph", 0.0);
}
#undef MODEL

#define MODEL DecayingDM_mixture
void MODEL_NAMESPACE::DecayingDM_mixture_to_DecayingDM_general (const ModelParameters &myP, ModelParameters &targetP)
{
  logger()<<"Running interpret_as_parent calculations for DecayingDM_mixture --> DecayingDM_general ..."<<LogTags::info<<EOM;

  targetP.setValue("mass", myP.getValue("mass"));
  targetP.setValue("lifetime", myP.getValue("lifetime"));
  targetP.setValue("fraction", myP.getValue("fraction"));
}
#undef MODEL

#define MODEL DecayingDM_photon
void MODEL_NAMESPACE::DecayingDM_photon_to_DecayingDM_mixture (const ModelParameters &myP, ModelParameters &targetP)
{
  logger()<<"Running interpret_as_parent calculations for DecayingDM_photon --> DecayingDM_mixture ..."<<LogTags::info<<EOM;

  targetP.setValue("mass", myP.getValue("mass"));
  targetP.setValue("lifetime", myP.getValue("lifetime"));
  targetP.setValue("fraction", myP.getValue("fraction"));

  // All decays into photons (BR into electrons is 0.0)
  targetP.setValue("BR_el", 0.0);
  targetP.setValue("BR_ph", 1.0);
}
#undef MODEL

#define MODEL DecayingDM_electron
void MODEL_NAMESPACE::DecayingDM_electron_to_DecayingDM_mixture (const ModelParameters &myP, ModelParameters &targetP)
{
  logger()<<"Running interpret_as_parent calculations for DecayingDM_electron --> DecayingDM_mixture ..."<<LogTags::info<<EOM;

  targetP.setValue("mass", myP.getValue("mass"));
  targetP.setValue("lifetime", myP.getValue("lifetime"));
  targetP.setValue("fraction", myP.getValue("fraction"));

  // All decays into electrons (BR into photons is 0.0)
  targetP.setValue("BR_el", 1.0);
  targetP.setValue("BR_ph", 0.0);
}
#undef MODEL
```


-------------------------------

Updated on 2022-09-07 at 14:07:48 +0000
