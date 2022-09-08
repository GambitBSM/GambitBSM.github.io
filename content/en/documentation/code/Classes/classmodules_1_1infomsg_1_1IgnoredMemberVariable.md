---
title: "class modules::infomsg::IgnoredMemberVariable"

description: "[No description available]"

---

# class modules::infomsg::IgnoredMemberVariable



[No description available]

Inherits from [modules.infomsg.InfoMessage](/documentation/code/classes/classmodules_1_1infomsg_1_1infomessage/), object

## Public Functions

|                | Name           |
| -------------- | -------------- |
| def | **[__init__](/documentation/code/classes/classmodules_1_1infomsg_1_1ignoredmembervariable/)**(self self, tag tag, reason reason ='') |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| string | **[msg](/documentation/code/classes/classmodules_1_1infomsg_1_1ignoredmembervariable/)**  |
| | **[tags_done](/documentation/code/classes/classmodules_1_1infomsg_1_1ignoredmembervariable/)**  |
| | **[tag](/documentation/code/classes/classmodules_1_1infomsg_1_1ignoredmembervariable/)**  |
| | **[msg](/documentation/code/classes/classmodules_1_1infomsg_1_1ignoredmembervariable/)**  |

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
static string msg =  gb.textmods['yellow'] +  "The member variable '%s' is ignored." + gb.textmods['end'];
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