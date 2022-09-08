---
title: "namespace Gambit::NodeUtility"

description: "[No description available]"

---

# namespace Gambit::NodeUtility

[No description available]

## Functions

|                | Name           |
| -------------- | -------------- |
| template <class TYPE \> <br>TYPE | **[safeIntegerTypeCast](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-safeintegertypecast)**(const std::string & s) |
| void | **[autoExpandEnvironmentVariables](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-autoexpandenvironmentvariables)**(std::string & text)<br>Expand environment variables in the given string.  |
| void | **[removeCharsFromString](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-removecharsfromstring)**(std::string & text, const char * charsToRemove)<br>Remove characters in the given string.  |
| std::string | **[expandEnvironmentVariables](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-expandenvironmentvariables)**(const std::string & input) |
| template <class TYPE \> <br>TYPE | **[getNode](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode)**(const YAML::Node node) |
| int | **[getNode< int >](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode-int)**(const YAML::Node node) |
| unsigned int | **[getNode< unsigned int >](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode-unsigned-int)**(const YAML::Node node)<br>See int specialization.  |
| long | **[getNode< long >](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode-long)**(const YAML::Node node)<br>See int specialization.  |
| unsigned long | **[getNode< unsigned long >](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode-unsigned-long)**(const YAML::Node node)<br>See int specialization.  |
| long long | **[getNode< long long >](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode-long-long)**(const YAML::Node node)<br>See int specialization.  |
| unsigned long long | **[getNode< unsigned long long >](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode-unsigned-long-long)**(const YAML::Node node)<br>See int specialization.  |
| std::string | **[getNode< std::string >](/documentation/code/namespaces/namespacegambit_1_1nodeutility/#function-getnode-std-string)**(const YAML::Node node) |


## Functions Documentation

### function safeIntegerTypeCast

```
template <class TYPE >
TYPE safeIntegerTypeCast(
    const std::string & s
)
```


Wrapper for integer type casts from a double in string representation. It does first try to safely convert the string to a double and then performs checks before casting to an integer type. 


### function autoExpandEnvironmentVariables

```
void autoExpandEnvironmentVariables(
    std::string & text
)
```

Expand environment variables in the given string. 

### function removeCharsFromString

```
void removeCharsFromString(
    std::string & text,
    const char * charsToRemove
)
```

Remove characters in the given string. 

### function expandEnvironmentVariables

```
std::string expandEnvironmentVariables(
    const std::string & input
)
```


Leave input alone and return new string, which has environment variables substituted and escpae characters removed. 


### function getNode

```
template <class TYPE >
TYPE getNode(
    const YAML::Node node
)
```


Wrapper for reading the node for a given type. Default case does nothing. However in some instances we want to catch the yamlcpp exception and try to interpret it, e.g. scientific notation numbers as integers. 


### function getNode< int >

```
inline int getNode< int >(
    const YAML::Node node
)
```


Allows to read scientific notation integer numbers. If the number does not fit into the given type (here int) or is not an integer, this function will raise. This exception is then caught by getValue and handled. 


### function getNode< unsigned int >

```
inline unsigned int getNode< unsigned int >(
    const YAML::Node node
)
```

See int specialization. 

### function getNode< long >

```
inline long getNode< long >(
    const YAML::Node node
)
```

See int specialization. 

### function getNode< unsigned long >

```
inline unsigned long getNode< unsigned long >(
    const YAML::Node node
)
```

See int specialization. 

### function getNode< long long >

```
inline long long getNode< long long >(
    const YAML::Node node
)
```

See int specialization. 

### function getNode< unsigned long long >

```
inline unsigned long long getNode< unsigned long long >(
    const YAML::Node node
)
```

See int specialization. 

### function getNode< std::string >

```
inline std::string getNode< std::string >(
    const YAML::Node node
)
```


Read string and expand environment variables of the type ${MYVAR}. Expansion of environment variables is not performed if given as $MYVAR and ${MYVAR}. 






-------------------------------

Updated on 2022-09-08 at 03:41:59 +0000