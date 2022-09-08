---
title: "class Gambit::Utils::ProcessLock"
description: "Class to manage a process lock, using a file. "

---

# class Gambit::Utils::ProcessLock



Class to manage a process lock, using a file. 


`#include <file_lock.hpp>`

Inherits from [Gambit::Utils::FileLock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[ProcessLock](/documentation/code/classes/classgambit_1_1utils_1_1processlock/#function-processlock)**(const std::string & fname, const bool harderrs =false)<br>Constructor.  |

## Additional inherited members

**Public Functions inherited from [Gambit::Utils::FileLock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/)**

|                | Name           |
| -------------- | -------------- |
| | **[FileLock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-filelock)**(const std::string & fname, const bool harderrs =false)<br>Constructor.  |
| | **[~FileLock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-filelock)**() |
| void | **[get_lock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-get-lock)**()<br>Obtain lock (or wait if lock cannot be obtained, and then obtain lock)  |
| void | **[release_lock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-release-lock)**()<br>Release a lock (error if no lock held)  |
| const std::string & | **[get_filename](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-get-filename)**() const<br>Getter for lockfile name.  |


## Public Functions Documentation

### function ProcessLock

```
ProcessLock(
    const std::string & fname,
    const bool harderrs =false
)
```

Constructor. 

-------------------------------

Updated on 2022-09-08 at 03:08:04 +0000