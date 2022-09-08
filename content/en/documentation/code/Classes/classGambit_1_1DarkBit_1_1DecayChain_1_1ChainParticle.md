---
title: "class Gambit::DarkBit::DecayChain::ChainParticle"

description: "[No description available]"

---

# class Gambit::DarkBit::DecayChain::ChainParticle



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ChainParticle](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-chainparticle)**([vec3](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1vec3/) ipLab, const [DecayTable](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1decaytable/) * dc, string pID) |
| void | **[generateDecayChainMC](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-generatedecaychainmc)**(int maxSteps, double Emin) |
| void | **[reDrawAngles](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-redrawangles)**() |
| void | **[cutChain](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-cutchain)**() |
| [vec4](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1vec4/) | **[p_to_Lab](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-p-to-lab)**(const [vec4](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1vec4/) & p) const |
| [vec4](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1vec4/) | **[p_Lab](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-p-lab)**() const |
| double | **[E_Lab](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-e-lab)**() const |
| void | **[collectEndpointStates](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-collectendpointstates)**(vector< const [ChainParticle](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/) * > & endpointStates, bool includeAborted, string ipID ="") const |
| int | **[getnChildren](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-getnchildren)**() const |
| const [ChainParticle](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/) * | **[operator[]](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-operator)**(int i) const |
| const [ChainParticle](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/) * | **[getParent](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-getparent)**() const |
| double | **[E_parentFrame](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-e-parentframe)**() const |
| string | **[getpID](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-getpid)**() const |
| void | **[printChain](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-printchain)**() const |
| double | **[getWeight](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-getweight)**() const |
| void | **[getBoost](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-getboost)**(double & gamma, double & beta) const |
| const [DecayTable](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1decaytable/) * | **[getDecayTable](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-getdecaytable)**() const |
| | **[~ChainParticle](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#function-gambitdarkbitdecaychainchainparticle-chainparticle)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const double | **[m](/documentation/code/classes/classgambit_1_1darkbit_1_1decaychain_1_1chainparticle/#variable-gambitdarkbitdecaychainchainparticle-m)**  |

## Public Functions Documentation

### function ChainParticle

```
ChainParticle(
    vec3 ipLab,
    const DecayTable * dc,
    string pID
)
```


### function generateDecayChainMC

```
void generateDecayChainMC(
    int maxSteps,
    double Emin
)
```


### function reDrawAngles

```
void reDrawAngles()
```


### function cutChain

```
void cutChain()
```


### function p_to_Lab

```
vec4 p_to_Lab(
    const vec4 & p
) const
```


### function p_Lab

```
vec4 p_Lab() const
```


### function E_Lab

```
double E_Lab() const
```


### function collectEndpointStates

```
void collectEndpointStates(
    vector< const ChainParticle * > & endpointStates,
    bool includeAborted,
    string ipID =""
) const
```


### function getnChildren

```
inline int getnChildren() const
```


### function operator[]

```
const ChainParticle * operator[](
    int i
) const
```


### function getParent

```
const ChainParticle * getParent() const
```


### function E_parentFrame

```
double E_parentFrame() const
```


### function getpID

```
inline string getpID() const
```


### function printChain

```
void printChain() const
```


### function getWeight

```
inline double getWeight() const
```


### function getBoost

```
void getBoost(
    double & gamma,
    double & beta
) const
```


### function getDecayTable

```
inline const DecayTable * getDecayTable() const
```


### function ~ChainParticle

```
~ChainParticle()
```


## Public Attributes Documentation

### variable m

```
const double m;
```


-------------------------------

Updated on 2022-09-08 at 02:00:48 +0000