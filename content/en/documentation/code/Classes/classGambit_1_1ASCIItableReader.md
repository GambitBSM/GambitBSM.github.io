---
title: "class Gambit::ASCIItableReader"

description: "[No description available]"

---

# class Gambit::ASCIItableReader



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ASCIItableReader](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-asciitablereader)**(std::string filename) |
| | **[ASCIItableReader](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-asciitablereader)**() |
| | **[~ASCIItableReader](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-asciitablereader)**() |
| int | **[read](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-read)**(std::string filename) |
| void | **[setcolnames](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-setcolnames)**(std::vector< std::string > names) |
| template <typename... Args\> <br>void | **[setcolnames](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-setcolnames)**(std::string name, Args... args) |
| template <typename... Args\> <br>void | **[setcolnames](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-setcolnames)**(std::vector< std::string > vec, std::string name, Args... args) |
| const std::vector< double > & | **[operator[]](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-operator)**(int i) |
| const std::vector< double > & | **[operator[]](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-operator)**(std::string name) |
| int | **[getncol](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-getncol)**() |
| int | **[getnrow](/documentation/code/classes/classgambit_1_1asciitablereader/#function-gambitasciitablereader-getnrow)**() |

## Public Functions Documentation

### function ASCIItableReader

```
inline ASCIItableReader(
    std::string filename
)
```


### function ASCIItableReader

```
inline ASCIItableReader()
```


### function ~ASCIItableReader

```
inline ~ASCIItableReader()
```


### function read

```
int read(
    std::string filename
)
```


### function setcolnames

```
void setcolnames(
    std::vector< std::string > names
)
```


### function setcolnames

```
template <typename... Args>
inline void setcolnames(
    std::string name,
    Args... args
)
```


### function setcolnames

```
template <typename... Args>
inline void setcolnames(
    std::vector< std::string > vec,
    std::string name,
    Args... args
)
```


### function operator[]

```
inline const std::vector< double > & operator[](
    int i
)
```


### function operator[]

```
inline const std::vector< double > & operator[](
    std::string name
)
```


### function getncol

```
inline int getncol()
```


### function getnrow

```
inline int getnrow()
```


-------------------------------

Updated on 2022-09-08 at 01:48:53 +0000