---
title: 'class modules::infomsg::TypeNotAccepted'

description: "[No description available]"

---








[No description available]

Inherits from [modules.infomsg.InfoMessage](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1infomessage/), object

## Public Functions

|                | Name           |
| -------------- | -------------- |
| def | **[__init__](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1typenotaccepted/#function---init--)**(self self, tag tag, reason reason ='') |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| string | **[msg](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1typenotaccepted/#variable-msg)**  |
| | **[tags_done](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1typenotaccepted/#variable-tags-done)**  |
| | **[tag](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1typenotaccepted/#variable-tag)**  |
| | **[msg](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1typenotaccepted/#variable-msg)**  |

## Additional inherited members

**Public Functions inherited from [modules.infomsg.InfoMessage](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1infomessage/)**

|                | Name           |
| -------------- | -------------- |
| def | **[printMessage](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1infomessage/#function-printmessage)**(self self) |


## Public Functions Documentation

### function __init__

```
def __init__(
    self self,
    tag tag,
    reason reason =''
)
```


**Reimplements**: [modules::infomsg::InfoMessage::__init__](/documentation/code/gambit_2-2/classes/classmodules_1_1infomsg_1_1infomessage/#function---init--)


## Public Attributes Documentation

### variable msg

```
static string msg =  gb.textmods['yellow'] +  "The type '%s' is not accepted." + gb.textmods['end'];
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

Updated on 2022-08-10 at 17:51:33 +0000