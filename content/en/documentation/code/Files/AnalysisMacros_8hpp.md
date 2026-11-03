---
title: "file analyses/AnalysisMacros.hpp"

description: "[No description available]"

---

# file analyses/AnalysisMacros.hpp

[No description available] [More...](#detailed-description)

## Defines

|                | Name           |
| -------------- | -------------- |
|  | **[ETAMIN](/documentation/code/files/analysismacros_8hpp/#define-etamin)** <br>Min and max values of eta and pT.  |
|  | **[PTMIN](/documentation/code/files/analysismacros_8hpp/#define-ptmin)**  |
|  | **[ETAMAX](/documentation/code/files/analysismacros_8hpp/#define-etamax)**  |
|  | **[PTMAX](/documentation/code/files/analysismacros_8hpp/#define-ptmax)**  |
|  | **[BASELINE_OBJECTS_3](/documentation/code/files/analysismacros_8hpp/#define-baseline-objects-3)**(TYPE, OBJECTS, NAME) <br>Define baseline objects without cuts.  |
|  | **[BASELINE_OBJECTS_5](/documentation/code/files/analysismacros_8hpp/#define-baseline-objects-5)**(TYPE, OBJECTS, NAME, MINPT, MINETA) <br>Define baseline objects with min pT and min eta.  |
|  | **[BASELINE_OBJECTS_6](/documentation/code/files/analysismacros_8hpp/#define-baseline-objects-6)**(TYPE, OBJECTS, NAME, MINPT, MINETA, EFF) <br>Define baseline objects with min pT, min eta and selection efficiency.  |
|  | **[BASELINE_OBJECTS_7](/documentation/code/files/analysismacros_8hpp/#define-baseline-objects-7)**(TYPE, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA) <br>Define baseline objects with min pT, min eta, max pT and max eta.  |
|  | **[BASELINE_OBJECTS_8](/documentation/code/files/analysismacros_8hpp/#define-baseline-objects-8)**(TYPE, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF) <br>Define baseline objects with min pT, min eta, max pT, max eta and selection efficiency.  |
|  | **[BASELINE_PARTICLES_2](/documentation/code/files/analysismacros_8hpp/#define-baseline-particles-2)**(OBJECTS, NAME) <br>Define baseline particles without cuts.  |
|  | **[BASELINE_PARTICLES_4](/documentation/code/files/analysismacros_8hpp/#define-baseline-particles-4)**(OBJECTS, NAME, MINPT, MINETA) <br>Define baseline particles with min pT and min et.  |
|  | **[BASELINE_PARTICLES_5](/documentation/code/files/analysismacros_8hpp/#define-baseline-particles-5)**(OBJECTS, NAME, MINPT, MINETA, EFF) <br>Define baseline particles with min pT, min eta and selection efficiency.  |
|  | **[BASELINE_PARTICLES_6](/documentation/code/files/analysismacros_8hpp/#define-baseline-particles-6)**(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA) <br>Define baseline particles with min pT, min eta, max pT and max eta.  |
|  | **[BASELINE_PARTICLES_7](/documentation/code/files/analysismacros_8hpp/#define-baseline-particles-7)**(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF) <br>Define baseline particles with min pT, min eta, max pT, max eta and selection efficiency.  |
|  | **[BASELINE_JETS_2](/documentation/code/files/analysismacros_8hpp/#define-baseline-jets-2)**(OBJECTS, NAME) <br>Define baseline jets without cuts.  |
|  | **[BASELINE_JETS_4](/documentation/code/files/analysismacros_8hpp/#define-baseline-jets-4)**(OBJECTS, NAME, MINPT, MINETA) <br>Define baseline jets with a min pT and a min eta.  |
|  | **[BASELINE_JETS_5](/documentation/code/files/analysismacros_8hpp/#define-baseline-jets-5)**(OBJECTS, NAME, MINPT, MINETA, EFF) <br>Define baseline jets with a min pT, a min eta and selection efficiency.  |
|  | **[BASELINE_JETS_6](/documentation/code/files/analysismacros_8hpp/#define-baseline-jets-6)**(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA) <br>Define baseline jets with a min pT, a min eta, max pT and max eta.  |
|  | **[BASELINE_JETS_7](/documentation/code/files/analysismacros_8hpp/#define-baseline-jets-7)**(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF) <br>Define baseline jets with a min pT, a min eta, max pT, max eta and selection efficiency.  |
|  | **[BASELINE_PARTICLES](/documentation/code/files/analysismacros_8hpp/#define-baseline-particles)**(...) <br>Redirection macro.  |
|  | **[BASELINE_JETS](/documentation/code/files/analysismacros_8hpp/#define-baseline-jets)**(...)  |
|  | **[BASELINE_OBJECTS](/documentation/code/files/analysismacros_8hpp/#define-baseline-objects)**(...)  |
|  | **[BASELINE_BJETS_4](/documentation/code/files/analysismacros_8hpp/#define-baseline-bjets-4)**(OBJECTS, NAME, MINPT, MINETA) <br>Define baseline bjets with a min pT and a min eta.  |
|  | **[BASELINE_BJETS_5](/documentation/code/files/analysismacros_8hpp/#define-baseline-bjets-5)**(OBJECTS, NAME, MINPT, MINETA, EFF) <br>Define baseline bjets with a min pT, a min eta and selection efficiency.  |
|  | **[BASELINE_BJETS_6](/documentation/code/files/analysismacros_8hpp/#define-baseline-bjets-6)**(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA) <br>Define baseline bjets with a min pT, a min eta, a max pT and a max eta.  |
|  | **[BASELINE_BJETS_7](/documentation/code/files/analysismacros_8hpp/#define-baseline-bjets-7)**(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF) <br>Define baseline bjets with a min pT, a min eta, a max pT, a max eta and selection efficiency.  |
|  | **[BASELINE_BJETS_8](/documentation/code/files/analysismacros_8hpp/#define-baseline-bjets-8)**(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF, MISID)  |
|  | **[BASELINE_BJETS](/documentation/code/files/analysismacros_8hpp/#define-baseline-bjets)**(...)  |
|  | **[BASELINE_OBJECT_COMBINATION_8](/documentation/code/files/analysismacros_8hpp/#define-baseline-object-combination-8)**(TYPE, TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA) <br>Define a combination of baseline objects with pT and eta cuts.  |
|  | **[BASELINE_PARTICLE_COMBINATION_7](/documentation/code/files/analysismacros_8hpp/#define-baseline-particle-combination-7)**(TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA) <br>Define a combination of baseline particles with pT and eta cuts.  |
|  | **[BASELINE_JET_COMBINATION_7](/documentation/code/files/analysismacros_8hpp/#define-baseline-jet-combination-7)**(TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA) <br>Define a combination of baseline jets with pT and eta cuts.  |
|  | **[BASELINE_OBJECT_COMBINATION_4](/documentation/code/files/analysismacros_8hpp/#define-baseline-object-combination-4)**(TYPE, TARGET, OBJECT1, OBJECT2) <br>Define a combination of baseline objects.  |
|  | **[BASELINE_PARTICLE_COMBINATION_3](/documentation/code/files/analysismacros_8hpp/#define-baseline-particle-combination-3)**(TARGET, OBJECT1, OBJECT2) <br>Define a combination of baseline particles.  |
|  | **[BASELINE_JET_COMBINATION_3](/documentation/code/files/analysismacros_8hpp/#define-baseline-jet-combination-3)**(TARGET, OBJECT1, OBJECT2) <br>Define a combination of baseline jets.  |
|  | **[BASELINE_PARTICLE_COMBINATION](/documentation/code/files/analysismacros_8hpp/#define-baseline-particle-combination)**(...) <br>Redirection macro.  |
|  | **[BASELINE_JET_COMBINATION](/documentation/code/files/analysismacros_8hpp/#define-baseline-jet-combination)**(...)  |
|  | **[BASELINE_OBJECT_COMBINATION](/documentation/code/files/analysismacros_8hpp/#define-baseline-object-combination)**(...)  |
|  | **[SIGNAL_OBJECTS_8](/documentation/code/files/analysismacros_8hpp/#define-signal-objects-8)**(TYPE, BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA) <br>Define (potentially sorted) signal objects from baseline objects with pT and eta cuts.  |
|  | **[SIGNAL_PARTICLES_7](/documentation/code/files/analysismacros_8hpp/#define-signal-particles-7)**(BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA) <br>Define (potentially sorted) signal particles from baseline particles with pT and eta cuts.  |
|  | **[SIGNAL_JETS_7](/documentation/code/files/analysismacros_8hpp/#define-signal-jets-7)**(BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA) <br>Define (potentially sorted) signal jets from baseline jets with pT and eta cuts.  |
|  | **[SIGNAL_OBJECTS_4](/documentation/code/files/analysismacros_8hpp/#define-signal-objects-4)**(TYPE, BASELINE, SIGNAL, SORTED) <br>Define (potentially sorted) signal objects from baseline objects.  |
|  | **[SIGNAL_PARTICLES_3](/documentation/code/files/analysismacros_8hpp/#define-signal-particles-3)**(BASELINE, SIGNAL, SORTED) <br>Define a (potentially sorted) signal particles from baseline particles.  |
|  | **[SIGNAL_JETS_3](/documentation/code/files/analysismacros_8hpp/#define-signal-jets-3)**(BASELINE, SIGNAL, SORTED) <br>Define a (potentially sorted) signal jets from a baseline jets.  |
|  | **[SIGNAL_OBJECTS_3](/documentation/code/files/analysismacros_8hpp/#define-signal-objects-3)**(TYPE, BASELINE, SIGNAL) <br>Define a sorted signal objects from a baseline objects.  |
|  | **[SIGNAL_PARTICLES_2](/documentation/code/files/analysismacros_8hpp/#define-signal-particles-2)**(BASELINE, SIGNAL) <br>Define sorted signal particles from baseline particles.  |
|  | **[SIGNAL_JETS_2](/documentation/code/files/analysismacros_8hpp/#define-signal-jets-2)**(BASELINE, SIGNAL) <br>Define a signal jets from a baseline jets.  |
|  | **[SIGNAL_PARTICLES](/documentation/code/files/analysismacros_8hpp/#define-signal-particles)**(...) <br>Redirection macros.  |
|  | **[SIGNAL_JETS](/documentation/code/files/analysismacros_8hpp/#define-signal-jets)**(...)  |
|  | **[SIGNAL_OBJECTS](/documentation/code/files/analysismacros_8hpp/#define-signal-objects)**(...)  |
|  | **[SIGNAL_OBJECT_COMBINATION](/documentation/code/files/analysismacros_8hpp/#define-signal-object-combination)**(TYPE, TARGET, OBJECT1, OBJECT2) <br>Define a combination of signal objects.  |
|  | **[SIGNAL_PARTICLE_COMBINATION](/documentation/code/files/analysismacros_8hpp/#define-signal-particle-combination)**(TARGET, OBJECT1, OBJECT2) <br>Define a combination of signal particles.  |
|  | **[SIGNAL_JET_COMBINATION](/documentation/code/files/analysismacros_8hpp/#define-signal-jet-combination)**(TARGET, OBJECT1, OBJECT2) <br>Define a combination of signal jets.  |
|  | **[CREATE_PAIR](/documentation/code/files/analysismacros_8hpp/#define-create-pair)**(TYPE, SOURCE, CONTAINER, UNIQUE) <br>Types of predefined pairs.  |
|  | **[BEGIN_PRESELECTION](/documentation/code/files/analysismacros_8hpp/#define-begin-preselection)** <br>Preselection, at the start initialize cutflows, at the end fill preselection cutflow.  |
|  | **[END_PRESELECTION](/documentation/code/files/analysismacros_8hpp/#define-end-preselection)**  |
|  | **[LOG_CUT_1](/documentation/code/files/analysismacros_8hpp/#define-log-cut-1)**(A) <br>Log current event for one or more signal regions.  |
|  | **[LOG_CUT_2](/documentation/code/files/analysismacros_8hpp/#define-log-cut-2)**(A, B)  |
|  | **[LOG_CUT_3](/documentation/code/files/analysismacros_8hpp/#define-log-cut-3)**(A, B, C)  |
|  | **[LOG_CUT_4](/documentation/code/files/analysismacros_8hpp/#define-log-cut-4)**(A, B, C, D)  |
|  | **[LOG_CUT_5](/documentation/code/files/analysismacros_8hpp/#define-log-cut-5)**(A, B, C, D, E)  |
|  | **[LOG_CUT_6](/documentation/code/files/analysismacros_8hpp/#define-log-cut-6)**(A, B, C, D, E, F)  |
|  | **[LOG_CUT_7](/documentation/code/files/analysismacros_8hpp/#define-log-cut-7)**(A, B, C, D, E, F, G)  |
|  | **[LOG_CUT_8](/documentation/code/files/analysismacros_8hpp/#define-log-cut-8)**(A, B, C, D, E, F, G, H)  |
|  | **[LOG_CUT_9](/documentation/code/files/analysismacros_8hpp/#define-log-cut-9)**(A, B, C, D, E, F, G, H, I)  |
|  | **[LOG_CUT_10](/documentation/code/files/analysismacros_8hpp/#define-log-cut-10)**(A, B, C, D, E, F, G, H, I, J)  |
|  | **[LOG_CUT](/documentation/code/files/analysismacros_8hpp/#define-log-cut)**(...)  |
|  | **[LOG_CUT_N](/documentation/code/files/analysismacros_8hpp/#define-log-cut-n)**(SR, N)  |
|  | **[LOG_CUTS_2](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-2)**(CUTS, A)  |
|  | **[LOG_CUTS_3](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-3)**(CUTS, A, B)  |
|  | **[LOG_CUTS_4](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-4)**(CUTS, A, B, C)  |
|  | **[LOG_CUTS_5](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-5)**(CUTS, A, B, C, D)  |
|  | **[LOG_CUTS_6](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-6)**(CUTS, A, B, C, D, E)  |
|  | **[LOG_CUTS_7](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-7)**(CUTS, A, B, C, D, E, F)  |
|  | **[LOG_CUTS_8](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-8)**(CUTS, A, B, C, D, E, F, G)  |
|  | **[LOG_CUTS_9](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-9)**(CUTS, A, B, C, D, E, F, G, H)  |
|  | **[LOG_CUTS_10](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-10)**(CUTS, A, B, C, D, E, F, G, H, I)  |
|  | **[LOG_CUTS_11](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-11)**(CUTS, A, B, C, D, E, F, G, H, I, J)  |
|  | **[LOG_CUTS](/documentation/code/files/analysismacros_8hpp/#define-log-cuts)**(...)  |
|  | **[LOG_CUTS_N](/documentation/code/files/analysismacros_8hpp/#define-log-cuts-n)**(CUTS, SR, N)  |
|  | **[FILL_SIGNAL_REGION](/documentation/code/files/analysismacros_8hpp/#define-fill-signal-region)**(NAME) <br>Fill signal region and cutflow.  |
|  | **[COMMIT_SIGNAL_REGION](/documentation/code/files/analysismacros_8hpp/#define-commit-signal-region)**(NAME, OBS, BKG_CENTRAL, BKG_ERR) <br>Commit values for the signal region: predictions, observed and backgrounds.  |
|  | **[COMMIT_COVARIANCE_MATRIX](/documentation/code/files/analysismacros_8hpp/#define-commit-covariance-matrix)**(COV) <br>Commit a covariance matrix.  |
|  | **[COMMIT_CUTFLOWS](/documentation/code/files/analysismacros_8hpp/#define-commit-cutflows)** <br>Commit cutflows.  |

## Detailed Description


**Author**: Tomas Gonzalo ([tomas.gonzalo@kit.edu](mailto:tomas.gonzalo@kit.edu)) 

**Date**: 2023 July, Aug

Macros for ColliderBit analyses. These macros define an analysis language that simplify writing analyses and avoid code repetition.



------------------

Authors (add name and date if you modify):



------------------




## Macros Documentation

### define ETAMIN

```
#define ETAMIN 0
```

Min and max values of eta and pT. 

### define PTMIN

```
#define PTMIN 0
```


### define ETAMAX

```
#define ETAMAX DBL_MAX
```


### define PTMAX

```
#define PTMAX DBL_MAX
```


### define BASELINE_OBJECTS_3

```
#define BASELINE_OBJECTS_3(
    TYPE,
    OBJECTS,
    NAME
)
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    NAME.push_back(object);                                                       \
  }
```

Define baseline objects without cuts. 

### define BASELINE_OBJECTS_5

```
#define BASELINE_OBJECTS_5(
    TYPE,
    OBJECTS,
    NAME,
    MINPT,
    MINETA
)
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA)                                             \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline objects with min pT and min eta. 

### define BASELINE_OBJECTS_6

```
#define BASELINE_OBJECTS_6(
    TYPE,
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    EFF
)
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline objects with min pT, min eta and selection efficiency. 

### define BASELINE_OBJECTS_7

```
#define BASELINE_OBJECTS_7(
    TYPE,
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if(object->pT() > MINPT and                                                   \
       object->pT() < MAXPT and                                                   \
       fabs(object->eta()) > MINETA and                                           \
       fabs(object->eta()) < MAXETA)                                              \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline objects with min pT, min eta, max pT and max eta. 

### define BASELINE_OBJECTS_8

```
#define BASELINE_OBJECTS_8(
    TYPE,
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA,
    EFF
)
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline objects with min pT, min eta, max pT, max eta and selection efficiency. 

### define BASELINE_PARTICLES_2

```
#define BASELINE_PARTICLES_2(
    OBJECTS,
    NAME
)
BASELINE_OBJECTS_3(Particle, OBJECTS, NAME)
```

Define baseline particles without cuts. 

### define BASELINE_PARTICLES_4

```
#define BASELINE_PARTICLES_4(
    OBJECTS,
    NAME,
    MINPT,
    MINETA
)
BASELINE_OBJECTS_5(Particle, OBJECTS, NAME, MINPT, MINETA)
```

Define baseline particles with min pT and min et. 

### define BASELINE_PARTICLES_5

```
#define BASELINE_PARTICLES_5(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    EFF
)
BASELINE_OBJECTS_6(Particle, OBJECTS, NAME, MINPT, MINETA, EFF)
```

Define baseline particles with min pT, min eta and selection efficiency. 

### define BASELINE_PARTICLES_6

```
#define BASELINE_PARTICLES_6(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
BASELINE_OBJECTS_7(Particle, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)
```

Define baseline particles with min pT, min eta, max pT and max eta. 

### define BASELINE_PARTICLES_7

```
#define BASELINE_PARTICLES_7(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA,
    EFF
)
BASELINE_OBJECTS_8(Particle, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF)
```

Define baseline particles with min pT, min eta, max pT, max eta and selection efficiency. 

### define BASELINE_JETS_2

```
#define BASELINE_JETS_2(
    OBJECTS,
    NAME
)
BASELINE_OBJECTS_3(Jet, OBJECTS, NAME)
```

Define baseline jets without cuts. 

### define BASELINE_JETS_4

```
#define BASELINE_JETS_4(
    OBJECTS,
    NAME,
    MINPT,
    MINETA
)
BASELINE_OBJECTS_5(Jet, OBJECTS, NAME, MINPT, MINETA)
```

Define baseline jets with a min pT and a min eta. 

### define BASELINE_JETS_5

```
#define BASELINE_JETS_5(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    EFF
)
BASELINE_OBJECTS_6(Jet, OBJECTS, NAME, MINPT, MINETA, EFF)
```

Define baseline jets with a min pT, a min eta and selection efficiency. 

### define BASELINE_JETS_6

```
#define BASELINE_JETS_6(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
BASELINE_OBJECTS_7(Jet, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)
```

Define baseline jets with a min pT, a min eta, max pT and max eta. 

### define BASELINE_JETS_7

```
#define BASELINE_JETS_7(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA,
    EFF
)
BASELINE_OBJECTS_8(Jet, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF)
```

Define baseline jets with a min pT, a min eta, max pT, max eta and selection efficiency. 

### define BASELINE_PARTICLES

```
#define BASELINE_PARTICLES(
    ...
)
VARARG(BASELINE_PARTICLES, __VA_ARGS__)
```

Redirection macro. 

### define BASELINE_JETS

```
#define BASELINE_JETS(
    ...
)
VARARG(BASELINE_JETS, __VA_ARGS__)
```


### define BASELINE_OBJECTS

```
#define BASELINE_OBJECTS(
    ...
)
VARARG(BASELINE_OBJECTS, __VA_ARGS__)
```


### define BASELINE_BJETS_4

```
#define BASELINE_BJETS_4(
    OBJECTS,
    NAME,
    MINPT,
    MINETA
)
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA)                                             \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline bjets with a min pT and a min eta. 

### define BASELINE_BJETS_5

```
#define BASELINE_BJETS_5(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    EFF
)
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline bjets with a min pT, a min eta and selection efficiency. 

### define BASELINE_BJETS_6

```
#define BASELINE_BJETS_6(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA)                                             \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline bjets with a min pT, a min eta, a max pT and a max eta. 

### define BASELINE_BJETS_7

```
#define BASELINE_BJETS_7(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA,
    EFF
)
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```

Define baseline bjets with a min pT, a min eta, a max pT, a max eta and selection efficiency. 

### define BASELINE_BJETS_8

```
#define BASELINE_BJETS_8(
    OBJECTS,
    NAME,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA,
    EFF,
    MISID
)
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if ((object->btag() or has_tag(MISID)) and                                    \
        object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }
```


Define baseline bjets with a min pT, a min eta, a max pT, a max eta, a selection efficiency and a misidentification efficiency 


### define BASELINE_BJETS

```
#define BASELINE_BJETS(
    ...
)
VARARG(BASELINE_BJETS, __VA_ARGS__)
```


### define BASELINE_OBJECT_COMBINATION_8

```
#define BASELINE_OBJECT_COMBINATION_8(
    TYPE,
    TARGET,
    OBJECT1,
    OBJECT2,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
  std::vector<const HEPUtils::TYPE*> TARGET;                                      \
  for(const HEPUtils::TYPE* obj1 : OBJECT1)                                       \
  {                                                                               \
    if(obj1->pT() > MINPT and                                                     \
       obj1->pT() < MAXPT and                                                     \
       fabs(obj1->eta()) > MINETA and                                             \
       fabs(obj1->eta()) < MAXETA)                                                \
    {                                                                             \
      TARGET.push_back(obj1);                                                     \
    }                                                                             \
  }                                                                               \
  for(const HEPUtils::TYPE* obj2 : OBJECT2)                                       \
  {                                                                               \
    if(obj2->pT() > MINPT and                                                     \
       obj2->pT() < MAXPT and                                                     \
       fabs(obj2->eta()) > MINETA and                                             \
       fabs(obj2->eta()) < MAXETA)                                                \
    {                                                                             \
      TARGET.push_back(obj2);                                                     \
    }                                                                             \
  }
```

Define a combination of baseline objects with pT and eta cuts. 

### define BASELINE_PARTICLE_COMBINATION_7

```
#define BASELINE_PARTICLE_COMBINATION_7(
    TARGET,
    OBJECT1,
    OBJECT2,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
BASELINE_OBJECT_COMBINATION_8(Particle, TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA)  \
```

Define a combination of baseline particles with pT and eta cuts. 

### define BASELINE_JET_COMBINATION_7

```
#define BASELINE_JET_COMBINATION_7(
    TARGET,
    OBJECT1,
    OBJECT2,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
BASELINE_OBJECT_COMBINATION_8(Jet, TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA)  \
```

Define a combination of baseline jets with pT and eta cuts. 

### define BASELINE_OBJECT_COMBINATION_4

```
#define BASELINE_OBJECT_COMBINATION_4(
    TYPE,
    TARGET,
    OBJECT1,
    OBJECT2
)
  std::vector<const HEPUtils::TYPE*> TARGET;                                      \
  for(const HEPUtils::TYPE* obj1 : OBJECT1)                                       \
    TARGET.push_back(obj1);                                                       \
  for(const HEPUtils::TYPE* obj2 : OBJECT2)                                       \
    TARGET.push_back(obj2);
```

Define a combination of baseline objects. 

### define BASELINE_PARTICLE_COMBINATION_3

```
#define BASELINE_PARTICLE_COMBINATION_3(
    TARGET,
    OBJECT1,
    OBJECT2
)
BASELINE_OBJECT_COMBINATION_4(Particle, TARGET, OBJECT1, OBJECT2)
```

Define a combination of baseline particles. 

### define BASELINE_JET_COMBINATION_3

```
#define BASELINE_JET_COMBINATION_3(
    TARGET,
    OBJECT1,
    OBJECT2
)
BASELINE_OBJECT_COMBINATION_4(Jet, TARGET, OBJECT1, OBJECT2)
```

Define a combination of baseline jets. 

### define BASELINE_PARTICLE_COMBINATION

```
#define BASELINE_PARTICLE_COMBINATION(
    ...
)
VARARG(BASELINE_PARTICLE_COMBINATION, __VA_ARGS__)
```

Redirection macro. 

### define BASELINE_JET_COMBINATION

```
#define BASELINE_JET_COMBINATION(
    ...
)
VARARG(BASELINE_JET_COMBINATION, __VA_ARGS__)
```


### define BASELINE_OBJECT_COMBINATION

```
#define BASELINE_OBJECT_COMBINATION(
    ...
)
VARARG(BASELINE_OBJECT_COMBINATION, __VA_ARGS__)
```


### define SIGNAL_OBJECTS_8

```
#define SIGNAL_OBJECTS_8(
    TYPE,
    BASELINE,
    SIGNAL,
    SORTED,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
  std::vector<const HEPUtils::TYPE*> SIGNAL;                                      \
  for (const HEPUtils::TYPE* object : BASELINE)                                   \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA)                                             \
    {                                                                             \
      SIGNAL.push_back(object);                                                   \
    }                                                                             \
  }                                                                               \
  if(SORTED) sortByPt(SIGNAL);
```

Define (potentially sorted) signal objects from baseline objects with pT and eta cuts. 

### define SIGNAL_PARTICLES_7

```
#define SIGNAL_PARTICLES_7(
    BASELINE,
    SIGNAL,
    SORTED,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
SIGNAL_OBJECTS_8(Particle, BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA)   \
```

Define (potentially sorted) signal particles from baseline particles with pT and eta cuts. 

### define SIGNAL_JETS_7

```
#define SIGNAL_JETS_7(
    BASELINE,
    SIGNAL,
    SORTED,
    MINPT,
    MINETA,
    MAXPT,
    MAXETA
)
SIGNAL_OBJECTS_8(Jet, BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA)   \
```

Define (potentially sorted) signal jets from baseline jets with pT and eta cuts. 

### define SIGNAL_OBJECTS_4

```
#define SIGNAL_OBJECTS_4(
    TYPE,
    BASELINE,
    SIGNAL,
    SORTED
)
  std::vector<const HEPUtils::TYPE*> SIGNAL(BASELINE);                            \
  if(SORTED) sortByPt(SIGNAL);
```

Define (potentially sorted) signal objects from baseline objects. 

### define SIGNAL_PARTICLES_3

```
#define SIGNAL_PARTICLES_3(
    BASELINE,
    SIGNAL,
    SORTED
)
SIGNAL_OBJECTS_4(Particle, BASELINE, SIGNAL, SORTED)                            \
```

Define a (potentially sorted) signal particles from baseline particles. 

### define SIGNAL_JETS_3

```
#define SIGNAL_JETS_3(
    BASELINE,
    SIGNAL,
    SORTED
)
SIGNAL_OBJECTS_4(Jet, BASELINE, SIGNAL, SORTED)
```

Define a (potentially sorted) signal jets from a baseline jets. 

### define SIGNAL_OBJECTS_3

```
#define SIGNAL_OBJECTS_3(
    TYPE,
    BASELINE,
    SIGNAL
)
SIGNAL_OBJECTS_4(TYPE, BASELINE, SIGNAL, 1)
```

Define a sorted signal objects from a baseline objects. 

### define SIGNAL_PARTICLES_2

```
#define SIGNAL_PARTICLES_2(
    BASELINE,
    SIGNAL
)
SIGNAL_OBJECTS_3(Particle, BASELINE, SIGNAL)
```

Define sorted signal particles from baseline particles. 

### define SIGNAL_JETS_2

```
#define SIGNAL_JETS_2(
    BASELINE,
    SIGNAL
)
SIGNAL_OBJECTS_3(Jet, BASELINE, SIGNAL)
```

Define a signal jets from a baseline jets. 

### define SIGNAL_PARTICLES

```
#define SIGNAL_PARTICLES(
    ...
)
VARARG(SIGNAL_PARTICLES, __VA_ARGS__)
```

Redirection macros. 

### define SIGNAL_JETS

```
#define SIGNAL_JETS(
    ...
)
VARARG(SIGNAL_JETS, __VA_ARGS__)
```


### define SIGNAL_OBJECTS

```
#define SIGNAL_OBJECTS(
    ...
)
VARARG(SIGNAL_OBJECTS, __VA_ARGS__)
```


### define SIGNAL_OBJECT_COMBINATION

```
#define SIGNAL_OBJECT_COMBINATION(
    TYPE,
    TARGET,
    OBJECT1,
    OBJECT2
)
  std::vector<const HEPUtils::TYPE*> TARGET = OBJECT1;                            \
  TARGET.insert(TARGET.end(), OBJECT2.begin(), OBJECT2.end());                    \
  sortByPt(TARGET);
```

Define a combination of signal objects. 

### define SIGNAL_PARTICLE_COMBINATION

```
#define SIGNAL_PARTICLE_COMBINATION(
    TARGET,
    OBJECT1,
    OBJECT2
)
SIGNAL_OBJECT_COMBINATION(Particle, TARGET, OBJECT1, OBJECT2)
```

Define a combination of signal particles. 

### define SIGNAL_JET_COMBINATION

```
#define SIGNAL_JET_COMBINATION(
    TARGET,
    OBJECT1,
    OBJECT2
)
SIGNAL_OBJECT_COMBINATION(Jet, TARGET, OBJECT1, OBJECT2)
```

Define a combination of signal jets. 

### define CREATE_PAIR

```
#define CREATE_PAIR(
    TYPE,
    SOURCE,
    CONTAINER,
    UNIQUE
)
  typedef std::vector<std::vector<const HEPUtils::Particle*>> ParticleContainer;  \
  ParticleContainer CONTAINER = CAT_3(get,TYPE,pairs)(SOURCE);                    \
  if(UNIQUE)                                                                      \
    uniquePairs(CONTAINER);
```

Types of predefined pairs. 

Create a container for pairs 


### define BEGIN_PRESELECTION

```
#define BEGIN_PRESELECTION   _cutflows.fillinit(event->weight());
```

Preselection, at the start initialize cutflows, at the end fill preselection cutflow. 

### define END_PRESELECTION

```
#define END_PRESELECTION   _cutflows.fillnext(event->weight());
```


### define LOG_CUT_1

```
#define LOG_CUT_1(
    A
)
_cutflows[A].fillnext(event->weight());
```

Log current event for one or more signal regions. 

### define LOG_CUT_2

```
#define LOG_CUT_2(
    A,
    B
)
LOG_CUT_1(A) LOG_CUT_1(B)
```


### define LOG_CUT_3

```
#define LOG_CUT_3(
    A,
    B,
    C
)
LOG_CUT_1(A) LOG_CUT_2(B,C)
```


### define LOG_CUT_4

```
#define LOG_CUT_4(
    A,
    B,
    C,
    D
)
LOG_CUT_1(A) LOG_CUT_3(B,C,D)
```


### define LOG_CUT_5

```
#define LOG_CUT_5(
    A,
    B,
    C,
    D,
    E
)
LOG_CUT_1(A) LOG_CUT_4(B,C,D,E)
```


### define LOG_CUT_6

```
#define LOG_CUT_6(
    A,
    B,
    C,
    D,
    E,
    F
)
LOG_CUT_1(A) LOG_CUT_5(B,C,D,E,F)
```


### define LOG_CUT_7

```
#define LOG_CUT_7(
    A,
    B,
    C,
    D,
    E,
    F,
    G
)
LOG_CUT_1(A) LOG_CUT_6(B,C,D,E,F,G)
```


### define LOG_CUT_8

```
#define LOG_CUT_8(
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H
)
LOG_CUT_1(A) LOG_CUT_7(B,C,D,E,F,G,H)
```


### define LOG_CUT_9

```
#define LOG_CUT_9(
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H,
    I
)
LOG_CUT_1(A) LOG_CUT_8(B,C,D,E,F,G,H,I)
```


### define LOG_CUT_10

```
#define LOG_CUT_10(
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H,
    I,
    J
)
LOG_CUT_1(A) LOG_CUT_9(B,C,D,E,F,G,H,I,J)
```


### define LOG_CUT

```
#define LOG_CUT(
    ...
)
VARARG(LOG_CUT, __VA_ARGS__)
```


### define LOG_CUT_N

```
#define LOG_CUT_N(
    SR,
    N
)
  for(size_t i=1; i<=N; ++i)                                                      \
  {                                                                               \
    str basename(SR);                                                             \
    str name = basename + std::to_string(i);                                      \
    _cutflows[name].fillnext(event->weight());                                    \
  }
```


### define LOG_CUTS_2

```
#define LOG_CUTS_2(
    CUTS,
    A
)
_cutflows[A].fillnext(CUTS,event->weight());
```


### define LOG_CUTS_3

```
#define LOG_CUTS_3(
    CUTS,
    A,
    B
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_2(CUTS,B)
```


### define LOG_CUTS_4

```
#define LOG_CUTS_4(
    CUTS,
    A,
    B,
    C
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_3(CUTS,B,C)
```


### define LOG_CUTS_5

```
#define LOG_CUTS_5(
    CUTS,
    A,
    B,
    C,
    D
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_4(CUTS,B,C,D)
```


### define LOG_CUTS_6

```
#define LOG_CUTS_6(
    CUTS,
    A,
    B,
    C,
    D,
    E
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_5(CUTS,B,C,D,E)
```


### define LOG_CUTS_7

```
#define LOG_CUTS_7(
    CUTS,
    A,
    B,
    C,
    D,
    E,
    F
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_6(CUTS,B,C,D,E,F)
```


### define LOG_CUTS_8

```
#define LOG_CUTS_8(
    CUTS,
    A,
    B,
    C,
    D,
    E,
    F,
    G
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_7(CUTS,B,C,D,E,F,G)
```


### define LOG_CUTS_9

```
#define LOG_CUTS_9(
    CUTS,
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_8(CUTS,B,C,D,E,F,G,H)
```


### define LOG_CUTS_10

```
#define LOG_CUTS_10(
    CUTS,
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H,
    I
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_9(CUTS,B,C,D,E,F,G,H,I)
```


### define LOG_CUTS_11

```
#define LOG_CUTS_11(
    CUTS,
    A,
    B,
    C,
    D,
    E,
    F,
    G,
    H,
    I,
    J
)
LOG_CUTS_2(CUTS,A) LOG_CUTS_10(CUTS,B,C,D,E,F,G,H,I,J)
```


### define LOG_CUTS

```
#define LOG_CUTS(
    ...
)
VARARG(LOG_CUTS, __VA_ARGS__)
```


### define LOG_CUTS_N

```
#define LOG_CUTS_N(
    CUTS,
    SR,
    N
)
  for(size_t i=1; i<=N; ++i)                                                      \
  {                                                                               \
    str basename(SR);                                                             \
    str name = basename + std::to_string(i);                                      \
    _cutflows[name].fillnext(CUTS,event->weight());                               \
  }
```


### define FILL_SIGNAL_REGION

```
#define FILL_SIGNAL_REGION(
    NAME
)
  _cutflows[NAME].fillnext(event->weight());                                      \
  _counters.at(NAME).add_event(event);
```

Fill signal region and cutflow. 

### define COMMIT_SIGNAL_REGION

```
#define COMMIT_SIGNAL_REGION(
    NAME,
    OBS,
    BKG_CENTRAL,
    BKG_ERR
)
  add_result(SignalRegionData(_counters.at(NAME), OBS, {BKG_CENTRAL, BKG_ERR}));
```

Commit values for the signal region: predictions, observed and backgrounds. 

### define COMMIT_COVARIANCE_MATRIX

```
#define COMMIT_COVARIANCE_MATRIX(
    COV
)
  set_covariance(COV);
```

Commit a covariance matrix. 

### define COMMIT_CUTFLOWS

```
#define COMMIT_CUTFLOWS   add_cutflows(_cutflows);
```

Commit cutflows. 

## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Macros for ColliderBit analyses.
///  These macros define an analysis language that
///  simplify writing analyses and avoid code
///  repetition.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Tomas Gonzalo
///          (tomas.gonzalo@kit.edu)
///  \date 2023 July, Aug
///
///  *********************************************

#pragma once

/// Min and max values of eta and pT
#define ETAMIN 0
#define PTMIN 0
#define ETAMAX DBL_MAX
#define PTMAX DBL_MAX

/// Define baseline objects without cuts
#define BASELINE_OBJECTS_3(TYPE, OBJECTS, NAME)                                   \
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    NAME.push_back(object);                                                       \
  }

/// Define baseline objects with min pT and min eta
#define BASELINE_OBJECTS_5(TYPE, OBJECTS, NAME, MINPT, MINETA)                    \
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA)                                             \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline objects with min pT, min eta and selection efficiency
#define BASELINE_OBJECTS_6(TYPE, OBJECTS, NAME, MINPT, MINETA, EFF)               \
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline objects with min pT, min eta, max pT and max eta
#define BASELINE_OBJECTS_7(TYPE, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)     \
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if(object->pT() > MINPT and                                                   \
       object->pT() < MAXPT and                                                   \
       fabs(object->eta()) > MINETA and                                           \
       fabs(object->eta()) < MAXETA)                                              \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline objects with min pT, min eta, max pT, max eta and selection efficiency
#define BASELINE_OBJECTS_8(TYPE, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF) \
  std::vector<const HEPUtils::TYPE*> NAME;                                        \
  for (const HEPUtils::TYPE* object : OBJECTS)                                    \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline particles without cuts
#define BASELINE_PARTICLES_2(OBJECTS, NAME)                                       \
  BASELINE_OBJECTS_3(Particle, OBJECTS, NAME)

/// Define baseline particles with min pT and min et
#define BASELINE_PARTICLES_4(OBJECTS, NAME, MINPT, MINETA)                         \
  BASELINE_OBJECTS_5(Particle, OBJECTS, NAME, MINPT, MINETA)

/// Define baseline particles with min pT, min eta and selection efficiency
#define BASELINE_PARTICLES_5(OBJECTS, NAME, MINPT, MINETA, EFF)                    \
  BASELINE_OBJECTS_6(Particle, OBJECTS, NAME, MINPT, MINETA, EFF)

/// Define baseline particles with min pT, min eta, max pT and max eta
#define BASELINE_PARTICLES_6(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)          \
  BASELINE_OBJECTS_7(Particle, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)

/// Define baseline particles with min pT, min eta, max pT, max eta and selection efficiency
#define BASELINE_PARTICLES_7(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF)     \
  BASELINE_OBJECTS_8(Particle, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF)

/// Define baseline jets without cuts
#define BASELINE_JETS_2(OBJECTS, NAME)                                             \
  BASELINE_OBJECTS_3(Jet, OBJECTS, NAME)

/// Define baseline jets with a min pT and a min eta
#define BASELINE_JETS_4(OBJECTS, NAME, MINPT, MINETA)                              \
  BASELINE_OBJECTS_5(Jet, OBJECTS, NAME, MINPT, MINETA)

/// Define baseline jets with a min pT, a min eta and selection efficiency
#define BASELINE_JETS_5(OBJECTS, NAME, MINPT, MINETA, EFF)                         \
  BASELINE_OBJECTS_6(Jet, OBJECTS, NAME, MINPT, MINETA, EFF)

/// Define baseline jets with a min pT, a min eta, max pT and max eta
#define BASELINE_JETS_6(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)               \
  BASELINE_OBJECTS_7(Jet, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)

/// Define baseline jets with a min pT, a min eta, max pT, max eta and selection efficiency
#define BASELINE_JETS_7(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF)          \
  BASELINE_OBJECTS_8(Jet, OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF)

/// Redirection macro
#define BASELINE_PARTICLES(...)      VARARG(BASELINE_PARTICLES, __VA_ARGS__)
#define BASELINE_JETS(...)           VARARG(BASELINE_JETS, __VA_ARGS__)
#define BASELINE_OBJECTS(...)        VARARG(BASELINE_OBJECTS, __VA_ARGS__)

/// Define baseline bjets with a min pT and a min eta
#define BASELINE_BJETS_4(OBJECTS, NAME, MINPT, MINETA)                            \
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA)                                             \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline bjets with a min pT, a min eta and selection efficiency
#define BASELINE_BJETS_5(OBJECTS, NAME, MINPT, MINETA, EFF)                       \
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline bjets with a min pT, a min eta, a max pT and a max eta
#define BASELINE_BJETS_6(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA)             \
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA)                                             \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline bjets with a min pT, a min eta, a max pT, a max eta and selection efficiency
#define BASELINE_BJETS_7(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF)        \
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if (object->btag() and                                                        \
        object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }

/// Define baseline bjets with a min pT, a min eta, a max pT, a max eta,
/// a selection efficiency and a misidentification efficiency
#define BASELINE_BJETS_8(OBJECTS, NAME, MINPT, MINETA, MAXPT, MAXETA, EFF, MISID) \
  std::vector<const HEPUtils::Jet*> NAME;                                         \
  for (const HEPUtils::Jet* object : OBJECTS)                                     \
  {                                                                               \
    if ((object->btag() or has_tag(MISID)) and                                    \
        object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA and                                          \
        has_tag(EFF, fabs(object->eta()), object->pT()))                          \
    {                                                                             \
      NAME.push_back(object);                                                     \
    }                                                                             \
  }


#define BASELINE_BJETS(...)          VARARG(BASELINE_BJETS, __VA_ARGS__)


/// Define a combination of baseline objects with pT and eta cuts
#define BASELINE_OBJECT_COMBINATION_8(TYPE, TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA)  \
  std::vector<const HEPUtils::TYPE*> TARGET;                                      \
  for(const HEPUtils::TYPE* obj1 : OBJECT1)                                       \
  {                                                                               \
    if(obj1->pT() > MINPT and                                                     \
       obj1->pT() < MAXPT and                                                     \
       fabs(obj1->eta()) > MINETA and                                             \
       fabs(obj1->eta()) < MAXETA)                                                \
    {                                                                             \
      TARGET.push_back(obj1);                                                     \
    }                                                                             \
  }                                                                               \
  for(const HEPUtils::TYPE* obj2 : OBJECT2)                                       \
  {                                                                               \
    if(obj2->pT() > MINPT and                                                     \
       obj2->pT() < MAXPT and                                                     \
       fabs(obj2->eta()) > MINETA and                                             \
       fabs(obj2->eta()) < MAXETA)                                                \
    {                                                                             \
      TARGET.push_back(obj2);                                                     \
    }                                                                             \
  }

/// Define a combination of baseline particles with pT and eta cuts
#define BASELINE_PARTICLE_COMBINATION_7(TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA)  \
  BASELINE_OBJECT_COMBINATION_8(Particle, TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA)  \

/// Define a combination of baseline jets with pT and eta cuts
#define BASELINE_JET_COMBINATION_7(TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA)  \
  BASELINE_OBJECT_COMBINATION_8(Jet, TARGET, OBJECT1, OBJECT2, MINPT, MINETA, MAXPT, MAXETA)  \

/// Define a combination of baseline objects
#define BASELINE_OBJECT_COMBINATION_4(TYPE, TARGET, OBJECT1, OBJECT2)             \
  std::vector<const HEPUtils::TYPE*> TARGET;                                      \
  for(const HEPUtils::TYPE* obj1 : OBJECT1)                                       \
    TARGET.push_back(obj1);                                                       \
  for(const HEPUtils::TYPE* obj2 : OBJECT2)                                       \
    TARGET.push_back(obj2);

/// Define a combination of baseline particles
#define BASELINE_PARTICLE_COMBINATION_3(TARGET, OBJECT1, OBJECT2)                   \
  BASELINE_OBJECT_COMBINATION_4(Particle, TARGET, OBJECT1, OBJECT2)

/// Define a combination of baseline jets
#define BASELINE_JET_COMBINATION_3(TARGET, OBJECT1, OBJECT2)                        \
  BASELINE_OBJECT_COMBINATION_4(Jet, TARGET, OBJECT1, OBJECT2)

/// Redirection macro
#define BASELINE_PARTICLE_COMBINATION(...)     VARARG(BASELINE_PARTICLE_COMBINATION, __VA_ARGS__)
#define BASELINE_JET_COMBINATION(...)          VARARG(BASELINE_JET_COMBINATION, __VA_ARGS__)
#define BASELINE_OBJECT_COMBINATION(...)       VARARG(BASELINE_OBJECT_COMBINATION, __VA_ARGS__)

/// Define (potentially sorted) signal objects from baseline objects with pT and eta cuts
#define SIGNAL_OBJECTS_8(TYPE, BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA)   \
  std::vector<const HEPUtils::TYPE*> SIGNAL;                                      \
  for (const HEPUtils::TYPE* object : BASELINE)                                   \
  {                                                                               \
    if (object->pT() > MINPT and                                                  \
        object->pT() < MAXPT and                                                  \
        fabs(object->eta()) > MINETA and                                          \
        fabs(object->eta()) < MAXETA)                                             \
    {                                                                             \
      SIGNAL.push_back(object);                                                   \
    }                                                                             \
  }                                                                               \
  if(SORTED) sortByPt(SIGNAL);

/// Define (potentially sorted) signal particles from baseline particles with pT and eta cuts
#define SIGNAL_PARTICLES_7(BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA)     \
  SIGNAL_OBJECTS_8(Particle, BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA)   \

/// Define (potentially sorted) signal jets from baseline jets with pT and eta cuts
#define SIGNAL_JETS_7(BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA)     \
  SIGNAL_OBJECTS_8(Jet, BASELINE, SIGNAL, SORTED, MINPT, MINETA, MAXPT, MAXETA)   \

/// Define (potentially sorted) signal objects from baseline objects
#define SIGNAL_OBJECTS_4(TYPE, BASELINE, SIGNAL, SORTED)                          \
  std::vector<const HEPUtils::TYPE*> SIGNAL(BASELINE);                            \
  if(SORTED) sortByPt(SIGNAL);

/// Define a (potentially sorted) signal particles from baseline particles
#define SIGNAL_PARTICLES_3(BASELINE, SIGNAL, SORTED)                              \
  SIGNAL_OBJECTS_4(Particle, BASELINE, SIGNAL, SORTED)                            \

/// Define a (potentially sorted) signal jets from a baseline jets
#define SIGNAL_JETS_3(BASELINE, SIGNAL, SORTED)                                   \
  SIGNAL_OBJECTS_4(Jet, BASELINE, SIGNAL, SORTED)

/// Define a sorted signal objects from a baseline objects
#define SIGNAL_OBJECTS_3(TYPE, BASELINE, SIGNAL)                                  \
  SIGNAL_OBJECTS_4(TYPE, BASELINE, SIGNAL, 1)

/// Define sorted signal particles from baseline particles
#define SIGNAL_PARTICLES_2(BASELINE, SIGNAL)                                      \
  SIGNAL_OBJECTS_3(Particle, BASELINE, SIGNAL)

/// Define a signal jets from a baseline jets
#define SIGNAL_JETS_2(BASELINE, SIGNAL)                                           \
  SIGNAL_OBJECTS_3(Jet, BASELINE, SIGNAL)

/// Redirection macros
#define SIGNAL_PARTICLES(...)    VARARG(SIGNAL_PARTICLES, __VA_ARGS__)
#define SIGNAL_JETS(...)         VARARG(SIGNAL_JETS, __VA_ARGS__)
#define SIGNAL_OBJECTS(...)      VARARG(SIGNAL_OBJECTS, __VA_ARGS__)

/// Define a combination of signal objects
#define SIGNAL_OBJECT_COMBINATION(TYPE, TARGET, OBJECT1, OBJECT2)                 \
  std::vector<const HEPUtils::TYPE*> TARGET = OBJECT1;                            \
  TARGET.insert(TARGET.end(), OBJECT2.begin(), OBJECT2.end());                    \
  sortByPt(TARGET);

/// Define a combination of signal particles
#define SIGNAL_PARTICLE_COMBINATION(TARGET, OBJECT1, OBJECT2)                     \
  SIGNAL_OBJECT_COMBINATION(Particle, TARGET, OBJECT1, OBJECT2)

/// Define a combination of signal jets
#define SIGNAL_JET_COMBINATION(TARGET, OBJECT1, OBJECT2)                          \
  SIGNAL_OBJECT_COMBINATION(Jet, TARGET, OBJECT1, OBJECT2)

/// Types of predefined pairs
/*#define OS    1  // opposite sign
#define SS    2  // same sign
#define SF    3  // same flavour
#define OSSF  4  // opposite sign, same flavour
#define SSSF  5  // ssame sign, same flavour
*/
/// Create a container for pairs
#define CREATE_PAIR(TYPE, SOURCE, CONTAINER, UNIQUE)                              \
  typedef std::vector<std::vector<const HEPUtils::Particle*>> ParticleContainer;  \
  ParticleContainer CONTAINER = CAT_3(get,TYPE,pairs)(SOURCE);                    \
  if(UNIQUE)                                                                      \
    uniquePairs(CONTAINER);

/// Preselection, at the start initialize cutflows, at the end fill preselection cutflow
#define BEGIN_PRESELECTION                                                        \
  _cutflows.fillinit(event->weight());

#define END_PRESELECTION                                                          \
  _cutflows.fillnext(event->weight());

/// Log current event for one or more signal regions
#define LOG_CUT_1(A)                      _cutflows[A].fillnext(event->weight());
#define LOG_CUT_2(A,B)                    LOG_CUT_1(A) LOG_CUT_1(B)
#define LOG_CUT_3(A,B,C)                  LOG_CUT_1(A) LOG_CUT_2(B,C)
#define LOG_CUT_4(A,B,C,D)                LOG_CUT_1(A) LOG_CUT_3(B,C,D)
#define LOG_CUT_5(A,B,C,D,E)              LOG_CUT_1(A) LOG_CUT_4(B,C,D,E)
#define LOG_CUT_6(A,B,C,D,E,F)            LOG_CUT_1(A) LOG_CUT_5(B,C,D,E,F)
#define LOG_CUT_7(A,B,C,D,E,F,G)          LOG_CUT_1(A) LOG_CUT_6(B,C,D,E,F,G)
#define LOG_CUT_8(A,B,C,D,E,F,G,H)        LOG_CUT_1(A) LOG_CUT_7(B,C,D,E,F,G,H)
#define LOG_CUT_9(A,B,C,D,E,F,G,H,I)      LOG_CUT_1(A) LOG_CUT_8(B,C,D,E,F,G,H,I)
#define LOG_CUT_10(A,B,C,D,E,F,G,H,I,J)   LOG_CUT_1(A) LOG_CUT_9(B,C,D,E,F,G,H,I,J)
#define LOG_CUT(...)                      VARARG(LOG_CUT, __VA_ARGS__)

// Log specific cuts for a sequential list of signal regions
#define LOG_CUT_N(SR, N)                                                          \
  for(size_t i=1; i<=N; ++i)                                                      \
  {                                                                               \
    str basename(SR);                                                             \
    str name = basename + std::to_string(i);                                      \
    _cutflows[name].fillnext(event->weight());                                    \
  }


// Log specific cuts for one or more signal region
#define LOG_CUTS_2(CUTS,A)                     _cutflows[A].fillnext(CUTS,event->weight());
#define LOG_CUTS_3(CUTS,A,B)                   LOG_CUTS_2(CUTS,A) LOG_CUTS_2(CUTS,B)
#define LOG_CUTS_4(CUTS,A,B,C)                 LOG_CUTS_2(CUTS,A) LOG_CUTS_3(CUTS,B,C)
#define LOG_CUTS_5(CUTS,A,B,C,D)               LOG_CUTS_2(CUTS,A) LOG_CUTS_4(CUTS,B,C,D)
#define LOG_CUTS_6(CUTS,A,B,C,D,E)             LOG_CUTS_2(CUTS,A) LOG_CUTS_5(CUTS,B,C,D,E)
#define LOG_CUTS_7(CUTS,A,B,C,D,E,F)           LOG_CUTS_2(CUTS,A) LOG_CUTS_6(CUTS,B,C,D,E,F)
#define LOG_CUTS_8(CUTS,A,B,C,D,E,F,G)         LOG_CUTS_2(CUTS,A) LOG_CUTS_7(CUTS,B,C,D,E,F,G)
#define LOG_CUTS_9(CUTS,A,B,C,D,E,F,G,H)       LOG_CUTS_2(CUTS,A) LOG_CUTS_8(CUTS,B,C,D,E,F,G,H)
#define LOG_CUTS_10(CUTS,A,B,C,D,E,F,G,H,I)    LOG_CUTS_2(CUTS,A) LOG_CUTS_9(CUTS,B,C,D,E,F,G,H,I)
#define LOG_CUTS_11(CUTS,A,B,C,D,E,F,G,H,I,J)  LOG_CUTS_2(CUTS,A) LOG_CUTS_10(CUTS,B,C,D,E,F,G,H,I,J)
#define LOG_CUTS(...)                          VARARG(LOG_CUTS, __VA_ARGS__)

// Log specific cuts for a sequential list of signal regions
#define LOG_CUTS_N(CUTS, SR, N)                                                   \
  for(size_t i=1; i<=N; ++i)                                                      \
  {                                                                               \
    str basename(SR);                                                             \
    str name = basename + std::to_string(i);                                      \
    _cutflows[name].fillnext(CUTS,event->weight());                               \
  }


/// Fill signal region and cutflow
#define FILL_SIGNAL_REGION(NAME)                                                  \
  _cutflows[NAME].fillnext(event->weight());                                      \
  _counters.at(NAME).add_event(event);

/// Commit values for the signal region: predictions, observed and backgrounds
#define COMMIT_SIGNAL_REGION(NAME, OBS, BKG_CENTRAL, BKG_ERR)                     \
  add_result(SignalRegionData(_counters.at(NAME), OBS, {BKG_CENTRAL, BKG_ERR}));

/// Commit a covariance matrix
#define COMMIT_COVARIANCE_MATRIX(COV)                                             \
  set_covariance(COV);

/// Commit cutflows
#define COMMIT_CUTFLOWS                                                           \
  add_cutflows(_cutflows);
```


-------------------------------

Updated on 2026-11-03 at 14:50:47 +0000
