---
title: "class Gambit::Priors::Cauchy"
description: "Multi-dimensional [Cauchy]() prior. "

---

# class Gambit::Priors::Cauchy



Multi-dimensional [Cauchy]() prior.  [More...](#detailed-description)


`#include <cauchy.hpp>`

Inherits from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/)**(const std::vector< std::string > & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & options) |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/)**(const std::vector< double > & unitpars, std::unordered_map< std::string, double > & outputMap) const override<br>Transformation from unit interval to the [Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/).  |
| virtual std::vector< double > | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/)**(const std::unordered_map< std::string, double > & ) const override<br>Transform from parameter back to unit hypercube.  |
| virtual double | **[operator()](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/)**(const std::vector< double > & ) const override<br>Log of PDF density.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() =default |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const int param_size) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const std::vector< std::string > & param_names, const int param_size =0) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const std::string & param_name, const int param_size =0) |
| virtual std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() const |
| unsigned int | **[size](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() const |
| void | **[setSize](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const unsigned int size) |
| unsigned int & | **[sizeRef](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() const |

**Protected Attributes inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[param_names](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**  |


## Detailed Description

```
class Gambit::Priors::Cauchy;
```

Multi-dimensional [Cauchy]() prior. 

This is a [multivariate \(t\)-distribution](https://en.wikipedia.org/wiki/Multivariate_t-distribution) with \(\nu = 1\) degree of freedom.

Defined by a scale matrix, \(\Sigma\), and a location vector.

If the scale matrix is diagonal,it may instead be specified by the square-roots of its diagonal entries, denoted \(\gamma\). 

## Public Functions Documentation

### function Cauchy

```
Cauchy(
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

Transformation from unit interval to the [Cauchy](/documentation/code/classes/classgambit_1_1priors_1_1cauchy/). 

**Reimplements**: [Gambit::Priors::BasePrior::transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)


### function inverse_transform

```
inline virtual std::vector< double > inverse_transform(
    const std::unordered_map< std::string, double > & 
) const override
```

Transform from parameter back to unit hypercube. 

**Reimplements**: [Gambit::Priors::BasePrior::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)


### function operator()

```
inline virtual double operator()(
    const std::vector< double > & 
) const override
```

Log of PDF density. 

**Reimplements**: [Gambit::Priors::BasePrior::operator()](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000