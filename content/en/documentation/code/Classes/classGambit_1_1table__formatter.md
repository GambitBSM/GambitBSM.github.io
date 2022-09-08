---
title: "class Gambit::table_formatter"

description: "[No description available]"

---

# class Gambit::table_formatter



[No description available]

## Public Functions

|                | Name           |
| -------------- | -------------- |
| template <typename... T\> <br>| **[table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/)**(const T &... params) |
| template <typename... T\> <br>void | **[new_titles](/documentation/code/classes/classgambit_1_1table__formatter/)**(const T &... in) |
| template <typename... T\> <br>void | **[default_widths](/documentation/code/classes/classgambit_1_1table__formatter/)**(const T &... in) |
| template <typename... T\> <br>void | **[min_widths](/documentation/code/classes/classgambit_1_1table__formatter/)**(const T &... in) |
| void | **[padding](/documentation/code/classes/classgambit_1_1table__formatter/)**(int p) |
| void | **[wrap_around](/documentation/code/classes/classgambit_1_1table__formatter/)**(bool b) |
| void | **[top_line](/documentation/code/classes/classgambit_1_1table__formatter/)**(bool b) |
| void | **[bottom_line](/documentation/code/classes/classgambit_1_1table__formatter/)**(bool b) |
| void | **[capitalize_title](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i) |
| void | **[capitalize_title](/documentation/code/classes/classgambit_1_1table__formatter/)**() |
| int | **[rows](/documentation/code/classes/classgambit_1_1table__formatter/)**() const |
| int | **[cols](/documentation/code/classes/classgambit_1_1table__formatter/)**() const |
| int | **[row_pos](/documentation/code/classes/classgambit_1_1table__formatter/)**() const |
| int | **[col_pos](/documentation/code/classes/classgambit_1_1table__formatter/)**() const |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[new_row](/documentation/code/classes/classgambit_1_1table__formatter/)**(int n =1) |
| template <typename T \> <br>[table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[operator<<](/documentation/code/classes/classgambit_1_1table__formatter/)**(const T & in) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[reset_pt_flag](/documentation/code/classes/classgambit_1_1table__formatter/)**(const unsigned char flag, int i, int j) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[reset_row_flag](/documentation/code/classes/classgambit_1_1table__formatter/)**(const unsigned char flag, int i) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[reset_col_flag](/documentation/code/classes/classgambit_1_1table__formatter/)**(const unsigned char flag, int i) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[set_pt_flag](/documentation/code/classes/classgambit_1_1table__formatter/)**(const unsigned char flag, int i, int j) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[set_row_flag](/documentation/code/classes/classgambit_1_1table__formatter/)**(const unsigned char flag, int i) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[set_col_flag](/documentation/code/classes/classgambit_1_1table__formatter/)**(const unsigned char flag, int i) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[reset](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i =-1, int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[red](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i =-1, int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[green](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i =-1, int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[yellow](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i =-1, int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[bold](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i =-1, int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[underline](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i =-1, int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[right_justify](/documentation/code/classes/classgambit_1_1table__formatter/)**(int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[center_justify](/documentation/code/classes/classgambit_1_1table__formatter/)**(int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[left_justify](/documentation/code/classes/classgambit_1_1table__formatter/)**(int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[no_newline](/documentation/code/classes/classgambit_1_1table__formatter/)**(int j =-1) |
| [table_formatter](/documentation/code/classes/classgambit_1_1table__formatter/) & | **[newline](/documentation/code/classes/classgambit_1_1table__formatter/)**(int j =-1) |
| std::vector< std::string > & | **[operator[]](/documentation/code/classes/classgambit_1_1table__formatter/)**(int i) |
| std::string | **[str](/documentation/code/classes/classgambit_1_1table__formatter/)**() |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| const unsigned char | **[RESET](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[RED](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[GREEN](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[YELLOW](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[COLOR](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[BOLD](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[JUST_RIGHT](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[JUST_CENTER](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[JUST](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[UNDERLINE](/documentation/code/classes/classgambit_1_1table__formatter/)**  |
| const unsigned char | **[WRAP](/documentation/code/classes/classgambit_1_1table__formatter/)**  |

## Public Functions Documentation

### function table_formatter

```
template <typename... T>
inline table_formatter(
    const T &... params
)
```


### function new_titles

```
template <typename... T>
inline void new_titles(
    const T &... in
)
```


### function default_widths

```
template <typename... T>
inline void default_widths(
    const T &... in
)
```


### function min_widths

```
template <typename... T>
inline void min_widths(
    const T &... in
)
```


### function padding

```
inline void padding(
    int p
)
```


### function wrap_around

```
inline void wrap_around(
    bool b
)
```


### function top_line

```
inline void top_line(
    bool b
)
```


### function bottom_line

```
inline void bottom_line(
    bool b
)
```


### function capitalize_title

```
inline void capitalize_title(
    int i
)
```


### function capitalize_title

```
inline void capitalize_title()
```


### function rows

```
inline int rows() const
```


### function cols

```
inline int cols() const
```


### function row_pos

```
inline int row_pos() const
```


### function col_pos

```
inline int col_pos() const
```


### function new_row

```
inline table_formatter & new_row(
    int n =1
)
```


### function operator<<

```
template <typename T >
inline table_formatter & operator<<(
    const T & in
)
```


### function reset_pt_flag

```
inline table_formatter & reset_pt_flag(
    const unsigned char flag,
    int i,
    int j
)
```


### function reset_row_flag

```
inline table_formatter & reset_row_flag(
    const unsigned char flag,
    int i
)
```


### function reset_col_flag

```
inline table_formatter & reset_col_flag(
    const unsigned char flag,
    int i
)
```


### function set_pt_flag

```
inline table_formatter & set_pt_flag(
    const unsigned char flag,
    int i,
    int j
)
```


### function set_row_flag

```
inline table_formatter & set_row_flag(
    const unsigned char flag,
    int i
)
```


### function set_col_flag

```
inline table_formatter & set_col_flag(
    const unsigned char flag,
    int i
)
```


### function reset

```
inline table_formatter & reset(
    int i =-1,
    int j =-1
)
```


### function red

```
inline table_formatter & red(
    int i =-1,
    int j =-1
)
```


### function green

```
inline table_formatter & green(
    int i =-1,
    int j =-1
)
```


### function yellow

```
inline table_formatter & yellow(
    int i =-1,
    int j =-1
)
```


### function bold

```
inline table_formatter & bold(
    int i =-1,
    int j =-1
)
```


### function underline

```
inline table_formatter & underline(
    int i =-1,
    int j =-1
)
```


### function right_justify

```
inline table_formatter & right_justify(
    int j =-1
)
```


### function center_justify

```
inline table_formatter & center_justify(
    int j =-1
)
```


### function left_justify

```
inline table_formatter & left_justify(
    int j =-1
)
```


### function no_newline

```
inline table_formatter & no_newline(
    int j =-1
)
```


### function newline

```
inline table_formatter & newline(
    int j =-1
)
```


### function operator[]

```
inline std::vector< std::string > & operator[](
    int i
)
```


### function str

```
std::string str()
```


## Public Attributes Documentation

### variable RESET

```
static const unsigned char RESET = 0x00;
```


### variable RED

```
static const unsigned char RED = 0x01;
```


### variable GREEN

```
static const unsigned char GREEN = 0x02;
```


### variable YELLOW

```
static const unsigned char YELLOW = 0x04;
```


### variable COLOR

```
static const unsigned char COLOR = 0x07;
```


### variable BOLD

```
static const unsigned char BOLD = 0x80;
```


### variable JUST_RIGHT

```
static const unsigned char JUST_RIGHT = 0x10;
```


### variable JUST_CENTER

```
static const unsigned char JUST_CENTER = 0x20;
```


### variable JUST

```
static const unsigned char JUST = 0x30;
```


### variable UNDERLINE

```
static const unsigned char UNDERLINE = 0x40;
```


### variable WRAP

```
static const unsigned char WRAP = 0x80;
```


-------------------------------

Updated on 2022-09-08 at 01:05:16 +0000