---
title: "class Gambit::Utils::FileLock"

description: "[No description available]"

---

# class Gambit::Utils::FileLock



[No description available] [More...](#detailed-description)


`#include <file_lock.hpp>`

Inherited by [Gambit::Utils::ProcessLock](/documentation/code/classes/classgambit_1_1utils_1_1processlock/)

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[FileLock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-filelock)**(const std::string & fname, const bool harderrs =false)<br>Constructor.  |
| | **[~FileLock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-filelock)**() |
| void | **[get_lock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-get-lock)**()<br>Obtain lock (or wait if lock cannot be obtained, and then obtain lock)  |
| void | **[release_lock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-release-lock)**()<br>Release a lock (error if no lock held)  |
| const std::string & | **[get_filename](/documentation/code/classes/classgambit_1_1utils_1_1filelock/#function-get-filename)**() const<br>Getter for lockfile name.  |

## Detailed Description

```
class Gambit::Utils::FileLock;
```


Class to manage a file lock Lock will be automatically released if this object is destructed 

## Public Functions Documentation

### function FileLock

```
FileLock(
    const std::string & fname,
    const bool harderrs =false
)
```

Constructor. 

Should check for errors opening the file. List of error codes is kind of long though, let people look it up themselves for now...

Error opening file!


### function ~FileLock

```
~FileLock()
```


Destructor Closing the file descriptor will automatically release any lock we might have 


Error closing file!


### function get_lock

```
void get_lock()
```

Obtain lock (or wait if lock cannot be obtained, and then obtain lock) 

Already have the lock!

Ok it seems there are some errors that we should handle, and then just try again to obtain the lock.


### function release_lock

```
void release_lock()
```

Release a lock (error if no lock held) 

Don't have the lock!

Release the lock


### function get_filename

```
const std::string & get_filename() const
```

Getter for lockfile name. 

-------------------------------

Updated on 2022-09-07 at 23:22:07 +0000