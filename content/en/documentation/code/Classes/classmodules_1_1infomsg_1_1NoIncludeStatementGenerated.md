---
title: "class modules::infomsg::NoIncludeStatementGenerated"

description: "[No description available]"

---

# class modules::infomsg::NoIncludeStatementGenerated



[No description available]

Inherits from [modules.infomsg.InfoMessage](/documentation/code/classes/classmodules_1_1infomsg_1_1infomessage/), object

## Public Functions

|                | Name           |
| -------------- | -------------- |
| def | **[__init__](/documentation/code/classes/classmodules_1_1infomsg_1_1noincludestatementgenerated/)**(self self, tag tag, reason reason ='') |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| string | **[msg](/documentation/code/classes/classmodules_1_1infomsg_1_1noincludestatementgenerated/)**  |
| | **[tags_done](/documentation/code/classes/classmodules_1_1infomsg_1_1noincludestatementgenerated/)**  |
| | **[tag](/documentation/code/classes/classmodules_1_1infomsg_1_1noincludestatementgenerated/)**  |
| | **[msg](/documentation/code/classes/classmodules_1_1infomsg_1_1noincludestatementgenerated/)**  |

## Additional inherited members

**Public Functions inherited from [modules.infomsg.InfoMessage](/documentation/code/classes/classmodules_1_1infomsg_1_1infomessage/)**

|                | Name           |
| -------------- | -------------- |
| def | **[printMessage](/documentation/code/classes/classmodules_1_1infomsg_1_1infomessage/)**(self self) |


## Public Functions Documentation

### function __init__

```
def __init__(
    self self,
    tag tag,
    reason reason =''
)
```


**Reimplements**: [modules::infomsg::InfoMessage::__init__](/documentation/code/classes/classmodules_1_1infomsg_1_1infomessage/)


## Public Attributes Documentation

### variable msg

```
static string msg =  gb.textmods['yellow'] +  "No header file include statement generated for the type '%s'." + gb.textmods['end'];
```


### variable tags_done

```
static tags_done =  set();
```


### variable tag

```
tag;
```


### variable msg

```
msg;
```


-------------------------------

Updated on 2022-09-08 at 01:05:15 +0000