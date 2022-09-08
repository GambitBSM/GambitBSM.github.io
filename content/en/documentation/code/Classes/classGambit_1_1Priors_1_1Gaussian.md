---
title: "class Gambit::Priors::Gaussian"
description: "Multi-dimensional [Gaussian]() prior. "

---

# class Gambit::Priors::Gaussian



Multi-dimensional [Gaussian]() prior.  [More...](#detailed-description)


`#include <gaussian.hpp>`

Inherits from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Gaussian](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/#function-gambitpriorsgaussian-gaussian)**(const std::vector< std::string > & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/#function-gambitpriorsgaussian-transform)**(const std::vector< double > & unitpars, std::unordered_map< std::string, double > & outputMap) const override<br>Transformation from unit interval to the [Gaussian](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/).  |
| virtual std::vector< double > | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/#function-gambitpriorsgaussian-inverse-transform)**(const std::unordered_map< std::string, double > & ) const override<br>Transform from parameter back to unit hypercube.  |
| virtual double | **[operator()](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/#function-gambitpriorsgaussian-operator)**(const std::vector< double > & ) const override<br>Log of PDF density.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**() =default |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**() |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**(const int param_size) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**(const std::vector< std::string > & param_names, const int param_size =0) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-baseprior)**(const std::string & param_name, const int param_size =0) |
| virtual std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-getshownparameters)**() const |
| unsigned int | **[size](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-size)**() const |
| void | **[setSize](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-setsize)**(const unsigned int size) |
| unsigned int & | **[sizeRef](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-sizeref)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-getparameters)**() const |

**Protected Attributes inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[param_names](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#variable-gambitpriorsbaseprior-param-names)**  |


## Detailed Description

```
class Gambit::Priors::Gaussian;
```

Multi-dimensional [Gaussian]() prior. 

Defined by a covariance matrix and mean.

If the covariance matrix is diagonal, it may instead be specified by the square-roots of its diagonal entries, denoted \(\sigma\). 

## Public Functions Documentation

### function Gaussian

```
Gaussian(
    const std::vector< std::string > & param,
    const Options & options
)
```


### function transform

```
inline virtual void transform(
    const std::vector< double > & unitpars,
    std::unordered_map< std::string, double > & outputMap
) const override
```

Transformation from unit interval to the [Gaussian](/documentation/code/classes/classgambit_1_1priors_1_1gaussian/). 

**Reimplements**: [Gambit::Priors::BasePrior::transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-transform)


### function inverse_transform

```
inline virtual std::vector< double > inverse_transform(
    const std::unordered_map< std::string, double > & 
) const override
```

Transform from parameter back to unit hypercube. 

**Reimplements**: [Gambit::Priors::BasePrior::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-inverse-transform)


### function operator()

```
inline virtual double operator()(
    const std::vector< double > & 
) const override
```

Log of PDF density. 

**Reimplements**: [Gambit::Priors::BasePrior::operator()](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/#function-gambitpriorsbaseprior-operator)


-------------------------------

Updated on 2022-09-08 at 02:00:49 +0000