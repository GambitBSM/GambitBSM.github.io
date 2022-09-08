---
title: "class Gambit::ModelParameters"

description: "[No description available]"

---

# class Gambit::ModelParameters



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-modelparameters)**()<br>Default constructor.  |
| | **[ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-modelparameters)**(const std::vector< std::string > & paramlist)<br>Constructor using vector of strings.  |
| | **[ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-modelparameters)**(const char ** paramlist)<br>Constructor using array of char arrays.  |
| double | **[getValue](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-getvalue)**(std::string const & inkey) const<br>Get value of named parameter.  |
| bool | **[has](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-has)**(const std::string & inkey) const<br>Check if a parameter exists in this object.  |
| const std::map< std::string, double > & | **[getValues](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-getvalues)**() const<br>Get values of all parameters.  |
| std::map< std::string, double >::const_iterator | **[begin](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-begin)**() const<br>Get a const iterator to the first parameter map entry.  |
| std::map< std::string, double >::const_iterator | **[end](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-end)**() const<br>Get a const iterator to the last parameter map entry.  |
| int | **[getNumberOfPars](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-getnumberofpars)**() const<br>Get number of parameters stored in this object.  |
| const double & | **[operator[]](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-operator)**(std::string const & inkey) const<br>Get parameter value using bracket operator.  |
| const double & | **[at](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-at)**(std::string const & inkey) const<br>Get parameter value using 'at' syntax.  |
| void | **[setValue](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-setvalue)**(std::string const & inkey, double const & value)<br>Set single parameter value.  |
| void | **[setValues](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-setvalues)**(std::map< std::string, double > const & params_map, bool missing_is_error =true)<br>Set many parameter values using a map.  |
| void | **[setValues](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-setvalues)**([ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) const & donor, bool missing_is_error =true)<br>Set many parameter values using another [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) object.  |
| std::vector< std::string > | **[getKeys](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-getkeys)**() const<br>Get parameter keys (names), probably for external iteration.  |
| void | **[print](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-print)**() const<br>Dump parameter names and values to stdout (should be for debugging only)  |
| void | **[_definePar](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-definepar)**(const std::string & newkey)<br>Define a parameter with name, value (i.e. add to internal map). Value is initialised to zero.  |
| void | **[_definePars](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-definepars)**(const std::vector< std::string > & v)<br>Define many new parameters at once via a vector of names.  |
| void | **[_definePars](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-definepars)**(const char ** array)<br>Define many new parameters at once via an array of char arrays.  |
| std::string | **[getModelName](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-getmodelname)**() const<br>Getters/setters for model and output names.  |
| std::string | **[getOutputName](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-getoutputname)**() const |
| void | **[setModelName](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-setmodelname)**(const std::string & in) |
| void | **[setOutputName](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-setoutputname)**(const std::string & in) |

## Protected Functions

|                | Name           |
| -------------- | -------------- |
| void | **[assert_contains](/documentation/code/classes/classgambit_1_1modelparameters/#function-gambitmodelparameters-assert-contains)**(std::string inkey) const<br>Checks if this model container holds a parameter match the supplied name.  |

## Friends

|                | Name           |
| -------------- | -------------- |
| std::ostream & | **[operator<<](/documentation/code/classes/classgambit_1_1modelparameters/#friend-gambitmodelparameters-operator)**(std::ostream & strm, const [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) & me) <br>Dump parameter names and values to stream (again for debugging only I think)  |

## Public Functions Documentation

### function ModelParameters

```
ModelParameters()
```

Default constructor. 

### function ModelParameters

```
ModelParameters(
    const std::vector< std::string > & paramlist
)
```

Constructor using vector of strings. 

### function ModelParameters

```
ModelParameters(
    const char ** paramlist
)
```

Constructor using array of char arrays. 

### function getValue

```
double getValue(
    std::string const & inkey
) const
```

Get value of named parameter. 

### function has

```
bool has(
    const std::string & inkey
) const
```

Check if a parameter exists in this object. 

### function getValues

```
const std::map< std::string, double > & getValues() const
```

Get values of all parameters. 

### function begin

```
std::map< std::string, double >::const_iterator begin() const
```

Get a const iterator to the first parameter map entry. 

### function end

```
std::map< std::string, double >::const_iterator end() const
```

Get a const iterator to the last parameter map entry. 

### function getNumberOfPars

```
int getNumberOfPars() const
```

Get number of parameters stored in this object. 

### function operator[]

```
const double & operator[](
    std::string const & inkey
) const
```

Get parameter value using bracket operator. 

### function at

```
const double & at(
    std::string const & inkey
) const
```

Get parameter value using 'at' syntax. 

Get parameter value using 'at' operator This is no different to the bracket operator method, since keys cannot be added with the bracket method anyhow, but for people who are used to maps it is nice to have. 


### function setValue

```
void setValue(
    std::string const & inkey,
    double const & value
)
```

Set single parameter value. 

### function setValues

```
void setValues(
    std::map< std::string, double > const & params_map,
    bool missing_is_error =true
)
```

Set many parameter values using a map. 

### function setValues

```
void setValues(
    ModelParameters const & donor,
    bool missing_is_error =true
)
```

Set many parameter values using another [ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) object. 

### function getKeys

```
std::vector< std::string > getKeys() const
```

Get parameter keys (names), probably for external iteration. 

### function print

```
void print() const
```

Dump parameter names and values to stdout (should be for debugging only) 

### function _definePar

```
void _definePar(
    const std::string & newkey
)
```

Define a parameter with name, value (i.e. add to internal map). Value is initialised to zero. 

### function _definePars

```
void _definePars(
    const std::vector< std::string > & v
)
```

Define many new parameters at once via a vector of names. 

### function _definePars

```
void _definePars(
    const char ** array
)
```

Define many new parameters at once via an array of char arrays. 

### function getModelName

```
std::string getModelName() const
```

Getters/setters for model and output names. 

### function getOutputName

```
std::string getOutputName() const
```


### function setModelName

```
void setModelName(
    const std::string & in
)
```


### function setOutputName

```
void setOutputName(
    const std::string & in
)
```


## Protected Functions Documentation

### function assert_contains

```
void assert_contains(
    std::string inkey
) const
```

Checks if this model container holds a parameter match the supplied name. 

[ModelParameters](/documentation/code/classes/classgambit_1_1modelparameters/) class member function definitions.

Checks if this model container holds a parameter matching the supplied name 


## Friends

### friend operator<<

```
friend std::ostream & operator<<(
    std::ostream & strm,

    const ModelParameters & me
);
```

Dump parameter names and values to stream (again for debugging only I think) 

-------------------------------

Updated on 2022-09-08 at 02:00:46 +0000