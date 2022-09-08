---
title: "class Gambit::Priors::None"

description: "[No description available]"

---

# class Gambit::Priors::None



[No description available]

Inherits from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[None](/documentation/code/classes/classgambit_1_1priors_1_1none/)**(const std::vector< std::string > & param, const [Options](/documentation/code/classes/classgambit_1_1options/) & ) |
| virtual void | **[transform](/documentation/code/classes/classgambit_1_1priors_1_1none/)**(const std::vector< double > & , std::unordered_map< std::string, double > & ) const override<br>Transform from unit hypercube to parameter.  |
| virtual std::vector< double > | **[inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1none/)**(const std::unordered_map< std::string, double > & ) const override<br>Transform from parameter back to unit hypercube.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| virtual | **[~BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() =default |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const int param_size) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const std::vector< std::string > & param_names, const int param_size =0) |
| | **[BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const std::string & param_name, const int param_size =0) |
| virtual double | **[operator()](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const std::vector< double > & ) const<br>Log of PDF density.  |
| virtual std::vector< std::string > | **[getShownParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() const |
| unsigned int | **[size](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() const |
| void | **[setSize](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**(const unsigned int size) |
| unsigned int & | **[sizeRef](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() |
| std::vector< std::string > | **[getParameters](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**() const |

**Protected Attributes inherited from [Gambit::Priors::BasePrior](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**

|                | Name           |
| -------------- | -------------- |
| std::vector< std::string > | **[param_names](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)**  |


## Public Functions Documentation

### function None

```
inline None(
    const std::vector< std::string > & param,
    const Options & 
)
```


### function transform

```
inline virtual void transform(
    const std::vector< double > & ,
    std::unordered_map< std::string, double > & 
) const override
```

Transform from unit hypercube to parameter. 

**Reimplements**: [Gambit::Priors::BasePrior::transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)


### function inverse_transform

```
inline virtual std::vector< double > inverse_transform(
    const std::unordered_map< std::string, double > & 
) const override
```

Transform from parameter back to unit hypercube. 

**Reimplements**: [Gambit::Priors::BasePrior::inverse_transform](/documentation/code/classes/classgambit_1_1priors_1_1baseprior/)


-------------------------------

Updated on 2022-09-08 at 01:05:18 +0000