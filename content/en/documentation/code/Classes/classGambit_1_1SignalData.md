---
title: 'class Gambit::SignalData'
description: 'Variables for use in signal handlers. '

---

# Gambit::SignalData





Variables for use in signal handlers. 


`#include <signal_handling.hpp>`

## Public Types

|                | Name           |
| -------------- | -------------- |
| typedef void(*)() | **[void_func](/documentation/code/classes/classgambit_1_1signaldata/#typedef-void-func)** <br>Set cleanup function to run during emergency shutdown.  |

## Public Functions

|                | Name           |
| -------------- | -------------- |
| | **[SignalData](/documentation/code/classes/classgambit_1_1signaldata/#function-signaldata)**()<br>[SignalData](/documentation/code/classes/classgambit_1_1signaldata/) member functions.  |
| std::string | **[myrank](/documentation/code/classes/classgambit_1_1signaldata/#function-myrank)**()<br>Retrieve MPI rank as a string (for log messages etc.)  |
| void | **[setjump](/documentation/code/classes/classgambit_1_1signaldata/#function-setjump)**()<br>Set jump point;.  |
| void | **[set_cleanup](/documentation/code/classes/classgambit_1_1signaldata/#function-set-cleanup)**([void_func](/documentation/code/classes/classgambit_1_1signaldata/#typedef-void-func) f)<br>Set cleanup function.  |
| void | **[call_cleanup](/documentation/code/classes/classgambit_1_1signaldata/#function-call-cleanup)**()<br>Call cleanup function.  |
| void | **[set_shutdown_begun](/documentation/code/classes/classgambit_1_1signaldata/#function-set-shutdown-begun)**(const sig_atomic_t emergnc =0)<br>Register that shutdown has begun.  |
| bool | **[shutdown_begun](/documentation/code/classes/classgambit_1_1signaldata/#function-shutdown-begun)**()<br>Check if (any kind of) shutdown is in progress.  |
| EXPORT_SYMBOLS bool | **[check_if_shutdown_begun](/documentation/code/classes/classgambit_1_1signaldata/#function-check-if-shutdown-begun)**() |
| void | **[add_signal](/documentation/code/classes/classgambit_1_1signaldata/#function-add-signal)**(int sig)<br>Check if emergency shutdown is in progress.  |
| std::string | **[display_received_signals](/documentation/code/classes/classgambit_1_1signaldata/#function-display-received-signals)**()<br>Print to string a list of the signals received so far by this process.  |
| void | **[entering_multithreaded_region](/documentation/code/classes/classgambit_1_1signaldata/#function-entering-multithreaded-region)**()<br>Only check for emergency shutdown signals (i.e. do not attempt synchronisation)  |
| void | **[leaving_multithreaded_region](/documentation/code/classes/classgambit_1_1signaldata/#function-leaving-multithreaded-region)**()<br>Exit threadsafe signal handling mode.  |
| bool | **[inside_multithreaded_region](/documentation/code/classes/classgambit_1_1signaldata/#function-inside-multithreaded-region)**()<br>Report 'true' if inside a multithreaded region (according to our own flag)  |
| void | **[update_looptime](/documentation/code/classes/classgambit_1_1signaldata/#function-update-looptime)**(double newtime)<br>Extra functions needed in MPI mode.  |
| void | **[attempt_soft_shutdown](/documentation/code/classes/classgambit_1_1signaldata/#function-attempt-soft-shutdown)**()<br>Perform soft shutdown if processes can be synchronised.  |

## Public Attributes

|                | Name           |
| -------------- | -------------- |
| jmp_buf | **[env](/documentation/code/classes/classgambit_1_1signaldata/#variable-env)** <br>Saved information on calling environment for longjmp.  |
| bool | **[jumppoint_set](/documentation/code/classes/classgambit_1_1signaldata/#variable-jumppoint-set)**  |
| int | **[havejumped](/documentation/code/classes/classgambit_1_1signaldata/#variable-havejumped)**  |
| [void_func](/documentation/code/classes/classgambit_1_1signaldata/#typedef-void-func) | **[cleanup](/documentation/code/classes/classgambit_1_1signaldata/#variable-cleanup)**  |
| bool | **[cleanup_function_set](/documentation/code/classes/classgambit_1_1signaldata/#variable-cleanup-function-set)**  |

## Public Types Documentation

### typedef void_func

```
typedef void(* Gambit::SignalData::void_func) ();
```

Set cleanup function to run during emergency shutdown. 

## Public Functions Documentation

### function SignalData

```
SignalData()
```

[SignalData](/documentation/code/classes/classgambit_1_1signaldata/) member functions. 

Constructor (initialise member variables) 


### function myrank

```
std::string myrank()
```

Retrieve MPI rank as a string (for log messages etc.) 

### function setjump

```
void setjump()
```

Set jump point;. 

### function set_cleanup

```
void set_cleanup(
    void_func f
)
```

Set cleanup function. 

### function call_cleanup

```
void call_cleanup()
```

Call cleanup function. 

### function set_shutdown_begun

```
void set_shutdown_begun(
    const sig_atomic_t emergnc =0
)
```

Register that shutdown has begun. 

### function shutdown_begun

```
bool shutdown_begun()
```

Check if (any kind of) shutdown is in progress. 

Check if shutdown is in progress. 


### function check_if_shutdown_begun

```
EXPORT_SYMBOLS bool check_if_shutdown_begun()
```


Check for signals that early shutdown is required If an MPI message telling us to perform an emergency shutdown is received (which should only happen in the case of an error on some other process) then a shutdown exception is raised. Otherwise, we just return a bool indicating the shutdown status 


### function add_signal

```
void add_signal(
    int sig
)
```

Check if emergency shutdown is in progress. 

Add signal to record.

Add signal to record 


### function display_received_signals

```
std::string display_received_signals()
```

Print to string a list of the signals received so far by this process. 

### function entering_multithreaded_region

```
void entering_multithreaded_region()
```

Only check for emergency shutdown signals (i.e. do not attempt synchronisation) 

TODO: Thread checking routines are no longer needed due to simplified shutdown method. Can be deleted when functors are updated to no longer call these routines.

Check if shutdown is in progress and raise appropriate termination exception if so. (to be called by [Gambit](/documentation/code/namespaces/namespacegambit/) once it is safe to trigger termination) Switch to threadsafe signal handling mode

Absorb any extra shutdown messages that may be unreceived (since every process broadcasts to every other process that it should shut down, so with lots of processess there will be lots of unreceived messages floating around) Switch to threadsafe signal handling mode 


### function leaving_multithreaded_region

```
void leaving_multithreaded_region()
```

Exit threadsafe signal handling mode. 

### function inside_multithreaded_region

```
bool inside_multithreaded_region()
```

Report 'true' if inside a multithreaded region (according to our own flag) 

### function update_looptime

```
void update_looptime(
    double newtime
)
```

Extra functions needed in MPI mode. 

Add a new loop time to internal array used to decide barrier timeout.

Add a new loop time to internal array used to decide barrier timeout 


### function attempt_soft_shutdown

```
void attempt_soft_shutdown()
```

Perform soft shutdown if processes can be synchronised. 

Start counting...

First time we see the shutdown signal, we will allow control to return to the scanner at least once, so that it can get its own affairs in order.


## Public Attributes Documentation

### variable env

```
jmp_buf env;
```

Saved information on calling environment for longjmp. 

### variable jumppoint_set

```
bool jumppoint_set;
```


### variable havejumped

```
int havejumped;
```


### variable cleanup

```
void_func cleanup;
```


### variable cleanup_function_set

```
bool cleanup_function_set;
```


-------------------------------

Updated on 2022-09-07 at 13:49:49 +0000