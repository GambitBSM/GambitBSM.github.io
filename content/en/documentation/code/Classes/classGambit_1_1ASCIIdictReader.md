---
title: "class Gambit::ASCIIdictReader"

description: "[No description available]"

---

# class Gambit::ASCIIdictReader



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ASCIIdictReader](/documentation/code/classes/classgambit_1_1asciidictreader/#function-asciidictreader)**(std::string filename) |
| | **[ASCIIdictReader](/documentation/code/classes/classgambit_1_1asciidictreader/#function-asciidictreader)**() |
| | **[~ASCIIdictReader](/documentation/code/classes/classgambit_1_1asciidictreader/#function-asciidictreader)**() |
| int | **[read](/documentation/code/classes/classgambit_1_1asciidictreader/#function-read)**(std::string filename) |
| const std::vector< std::string > & | **[get_keys](/documentation/code/classes/classgambit_1_1asciidictreader/#function-get-keys)**() const |
| const std::map< std::string, std::vector< double > > & | **[get_dict](/documentation/code/classes/classgambit_1_1asciidictreader/#function-get-dict)**() const |
| bool | **[duplicated_keys](/documentation/code/classes/classgambit_1_1asciidictreader/#function-duplicated-keys)**() const |
| int | **[nrow](/documentation/code/classes/classgambit_1_1asciidictreader/#function-nrow)**() const |

## Public Functions Documentation

### function ASCIIdictReader

```
inline ASCIIdictReader(
    std::string filename
)
```


### function ASCIIdictReader

```
inline ASCIIdictReader()
```


### function ~ASCIIdictReader

```
inline ~ASCIIdictReader()
```


### function read

```
int read(
    std::string filename
)
```


### function get_keys

```
inline const std::vector< std::string > & get_keys() const
```


### function get_dict

```
inline const std::map< std::string, std::vector< double > > & get_dict() const
```


### function duplicated_keys

```
inline bool duplicated_keys() const
```


### function nrow

```
inline int nrow() const
```


-------------------------------

Updated on 2022-09-08 at 02:22:59 +0000