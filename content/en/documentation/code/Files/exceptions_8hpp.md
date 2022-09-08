---
title: "file Utils/exceptions.hpp"

description: "[No description available]"

---

# file Utils/exceptions.hpp

[No description available] [More...](#detailed-description)

## Namespaces

| Name           |
| -------------- |
| **[Gambit](/documentation/code/namespaces/namespacegambit/)** <br>TODO: see if we can use this one:  |

## Classes

|                | Name           |
| -------------- | -------------- |
| class | **[Gambit::exception](/documentation/code/classes/classgambit_1_1exception/)** <br>GAMBIT exception base class.  |
| class | **[Gambit::error](/documentation/code/classes/classgambit_1_1error/)** <br>GAMBIT error class.  |
| class | **[Gambit::warning](/documentation/code/classes/classgambit_1_1warning/)** <br>GAMBIT warning class.  |
| class | **[Gambit::special_exception](/documentation/code/classes/classgambit_1_1special__exception/)** <br>GAMBIT special exception class. Not logged, meant for always catching.  |
| class | **[Gambit::invalid_point_exception](/documentation/code/classes/classgambit_1_1invalid__point__exception/)** <br>[Gambit](/documentation/code/namespaces/namespacegambit/) invalid point exception class.  |
| class | **[Gambit::halt_loop_exception](/documentation/code/classes/classgambit_1_1halt__loop__exception/)** <br>[Gambit](/documentation/code/namespaces/namespacegambit/) halt loop exception class.  |
| class | **[Gambit::invalid_loop_iteration_exception](/documentation/code/classes/classgambit_1_1invalid__loop__iteration__exception/)** <br>[Gambit](/documentation/code/namespaces/namespacegambit/) invalid loop iteration exception class.  |
| class | **[Gambit::Piped_invalid_point](/documentation/code/classes/classgambit_1_1piped__invalid__point/)** <br>[Gambit](/documentation/code/namespaces/namespacegambit/) piped invalid point exception class.  |
| class | **[Gambit::Piped_exceptions](/documentation/code/classes/classgambit_1_1piped__exceptions/)** <br>[Gambit](/documentation/code/namespaces/namespacegambit/) piped error class.  |
| class | **[Gambit::SilentShutdownException](/documentation/code/classes/classgambit_1_1silentshutdownexception/)** <br>Special exception used during clean exit from diagnostics.  |
| class | **[Gambit::SoftShutdownException](/documentation/code/classes/classgambit_1_1softshutdownexception/)** <br>Special exception used during controlled early shutdown.  |
| class | **[Gambit::HardShutdownException](/documentation/code/classes/classgambit_1_1hardshutdownexception/)** <br>Special exception used during emergency early shutdown.  |
| class | **[Gambit::MPIShutdownException](/documentation/code/classes/classgambit_1_1mpishutdownexception/)** <br>Special exception raised when emergency shutdown triggered via MPI.  |

## Detailed Description


**Author**: Pat Scott ([patscott@physics.mcgill.ca](mailto:patscott@physics.mcgill.ca)) 

**Date**: 2014 Mar

Threadsafe exception class declarations.



------------------

Authors (add name and date if you modify):


Distantly inspired by SUFIT classes of the same name by Johan Lundberg, Aug 2011.



------------------




## Source code

```
//   GAMBIT: Global and Modular BSM Inference Tool
//   *********************************************
///  \file
///
///  Threadsafe exception class declarations.
///
///  *********************************************
///
///  Authors (add name and date if you modify):
///
///  \author Pat Scott
///          (patscott@physics.mcgill.ca)
///  \date 2014 Mar
///
///  Distantly inspired by SUFIT classes of the
///  same name by Johan Lundberg, Aug 2011.
///
///  *********************************************

#ifndef __exceptions_hpp__
#define __exceptions_hpp__

#include <map>
#include <set>
#include <string>
#include <exception>
#include <vector>
#include <utility>

#include "gambit/Utils/util_macros.hpp"
#include "gambit/Logs/log_tags.hpp"

namespace Gambit
{

  // Forward declaration of functor class.
  class functor;

  /// GAMBIT exception base class.
  class EXPORT_SYMBOLS exception : virtual public std::exception
  {
    public:

      /// Constructors
      /// @{
      /// Constructor without log tags
      exception(const char*, const char*, const char*, const char*, bool);
      /// Constructor with 1 log tag
      exception(const char*, const char*, const char*, const char*, bool, LogTag);
      /// Constructor with 2 log tags
      exception(const char*, const char*, const char*, const char*, bool, LogTag, LogTag);
      /// Constructor with 3 log tags
      exception(const char*, const char*, const char*, const char*, bool, LogTag, LogTag, LogTag);
      /// Constructor with 4 log tags
      exception(const char*, const char*, const char*, const char*, bool, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with 5 log tags
      exception(const char*, const char*, const char*, const char*, bool, LogTag, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with 6 log tags
      exception(const char*, const char*, const char*, const char*, bool, LogTag, LogTag, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with 7 log tags
      exception(const char*, const char*, const char*, const char*, bool, LogTag, LogTag, LogTag, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with log tags as a set
      exception(const char*, const char*, const char*, const char*, bool, std::set<LogTag>);
      /// @}

      /// Destructor
      virtual ~exception() throw() {}

      /// Setter for the fatal flag.
      void set_fatal(bool);

      /// Retrieve the identity of the exception.
      virtual const char* what() const throw();

      /// Raise the exception.
      /// Log the exception and, if it is considered fatal, actually throw it.
      /// This is the canonical way to trigger a GAMBIT error or warning.
      void raise(const std::string&, const std::string&);

      /// Force a throw of the exception.
      /// These should only be used inside a try block, i.e. if you plan to catch the exception.
      /// @{
      /// Log the exception and throw it regardless of whether is is fatal or not.
      void forced_throw(const std::string&, const std::string&);
      /// As per forced_throw but without logging.
      void silent_forced_throw();
      /// @}

      /// Get a read-only map of pointers to all instances of this class.
      static const std::map<const char*,exception*>& all_exceptions();

      /// Set the parameter point string to append if a fatal exception is thrown
      static void set_parameters(std::string);

    protected:

      /// The set of tags to be passed to the logger
      std::set<LogTag> myLogTags;

    private:

      /// Get a map of pointers to all instances of this class.
      static std::map<const char*,exception*>& exception_map();

      /// Log the details of the exception
      void log_exception(const std::string&, const std::string&);

      /// Throw the exception onward if running serially, abort if not.
      void throw_iff_outside_parallel();

      /// Cause the code to print the exception and abort.
      void abort_here_and_now();

      /// The kind of exception (error, warning, etc; for logging).
      const char* myKind;

      /// What sort of exception this is (for returning with what method).
      std::string myWhat;

      /// Initial value of myWhat.
      const std::string myShortWhat;

      /// The message to be logged when this exception is raised.
      const char* myMessage;

      /// Flag indicating if this exception should be considered fatal or not.
      bool isFatal;

      /// Shared string indicating the current values of the paramters.
      static std::string parameters;

  };


  /// GAMBIT error class.
  class EXPORT_SYMBOLS error : public exception
  {

    public:

      /// Constructors
      /// @{
      /// Constructor without log tags
      error(const char*, const char*);
      /// Constructor with 1 log tag
      error(const char*, const char*, LogTag);
      /// Constructor with 2 log tags
      error(const char*, const char*, LogTag, LogTag);
      /// Constructor with 3 log tags
      error(const char*, const char*, LogTag, LogTag, LogTag);
      /// Constructor with 4 log tags
      error(const char*, const char*, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with 5 log tags
      error(const char*, const char*, LogTag, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with 6 log tags
      error(const char*, const char*, LogTag, LogTag, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with log tags as a set
      error(const char*, const char*, std::set<LogTag>);
      /// @}

  };


  /// GAMBIT warning class.
  class EXPORT_SYMBOLS warning : public exception
  {

    public:

      /// Constructors
      /// @{
      /// Constructor without log tags
      warning(const char*, const char*);
      /// Constructor with 1 log tag
      warning(const char*, const char*, LogTag);
      /// Constructor with 2 log tags
      warning(const char*, const char*, LogTag, LogTag);
      /// Constructor with 3 log tags
      warning(const char*, const char*, LogTag, LogTag, LogTag);
      /// Constructor with 4 log tags
      warning(const char*, const char*, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with 5 log tags
      warning(const char*, const char*, LogTag, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with 6 log tags
      warning(const char*, const char*, LogTag, LogTag, LogTag, LogTag, LogTag, LogTag);
      /// Constructor with log tags as a set
      warning(const char*, const char*, std::set<LogTag>);
      /// @}

  };


  /// GAMBIT special exception class.  Not logged, meant for always catching.
  class EXPORT_SYMBOLS special_exception : virtual public std::exception
  {
    public:

      /// Constructor
      special_exception(const char*);

      /// Destructor
      virtual ~special_exception() throw() {}

      /// Retrieve the identity of the exception.
      virtual const char* what() const throw();

      /// Retrieve the message that this exception was raised with.
      std::string message();

      /// Raise the exception, i.e. throw it.
      virtual void raise(const std::string&);

      /// Integer code used for exceptions
      int invalidcode;

    private:

      /// What this exception is (for returning with what method).
      const char* myWhat;

    protected:

      /// The message passed when this exception is raised.
      std::string myMessage;

  };

  /// Gambit invalid point exception class.
  class invalid_point_exception : public special_exception
  {

    private:

      /// The functor responsible for throwing this exception.
      functor* myThrower;

      /// Cause the code to print the exception and abort.
      void abort_here_and_now();

    public:

      /// Constructor
      invalid_point_exception();

      /// Set the pointer to the functor that threw the invalid point exception.
      void set_thrower(functor*);

      /// Retrieve pointer to the functor that threw the invalid point exception.
      functor* thrower();

      /// Raise the exception, i.e. throw it. Exact override of base method.
      virtual void raise(const std::string&);

      /// Raise the exception, i.e. throw it with a message and code.
      virtual void raise(const std::string&, int code);

  };

  /// Gambit halt loop exception class.
  class halt_loop_exception : public special_exception
  {

    public:

      /// Constructor
      halt_loop_exception();

  };

  /// Gambit invalid loop iteration exception class.
  class invalid_loop_iteration_exception : public special_exception
  {

    public:

      /// Constructor
      invalid_loop_iteration_exception();

  };

  /// Gambit piped invalid point exception class.
  class Piped_invalid_point
  {
    public:
      /// Constructor
      Piped_invalid_point() : flag(false), message("") {};

      /// Request an exception.
      void request(std::string message);

      /// Check whether an exception was requested, and throw it if necessary.
      void check();

    private:
      bool flag;
      std::string message;
  };

  /// Global instance of piped invalid point class.
  extern Piped_invalid_point piped_invalid_point;

  /// Gambit piped error class.
  class EXPORT_SYMBOLS Piped_exceptions
  {
    public:
      typedef std::pair<std::string,std::string> description;
      /// Constructor
      Piped_exceptions(size_t maxExceptions) : flag(false), maxExceptions(maxExceptions) {};

      /// Request an exception.
      void request(std::string origin, std::string message);
      void request(description desc);

      /// Check whether any exceptions were requested, and raise them.
      void check(exception &excep);

      /// Check whether any exceptions were requested without handling them.
      bool inquire();

      /// Check whether any exceptions with a specific message were requested, without handling them.
      bool inquire(std::string);

    private:
      bool flag;
      size_t maxExceptions;
      std::vector<description> exceptions;
  };

  /// Global instance of Piped_exceptions class for errors.
  extern Piped_exceptions piped_errors;

  /// Global instance of Piped_exceptions class for warnings.
  extern Piped_exceptions piped_warnings;

  /// Special exception used during clean exit from diagnostics
  class SilentShutdownException : public std::exception
  {
    public:
      SilentShutdownException();
      SilentShutdownException(const std::string& message);
      virtual const char* what() const throw();
    private:
      std::string myWhat;
  };
  /// Special exception used during controlled early shutdown
  class SoftShutdownException : public std::exception
  {
    public:
      SoftShutdownException(const std::string& message);
      virtual const char* what() const throw();
    private:
      std::string myWhat;
  };
  /// Special exception used during emergency early shutdown
  class HardShutdownException : public std::exception
  {
    public:
      HardShutdownException(const std::string& message);
      virtual const char* what() const throw();
    private:
      std::string myWhat;
  };
  /// Special exception raised when emergency shutdown triggered via MPI
  class MPIShutdownException : public std::exception
  {
    public:
      MPIShutdownException(const std::string& message);
      virtual const char* what() const throw();
    private:
      std::string myWhat;
  };

}


#endif
```


-------------------------------

Updated on 2022-09-08 at 03:46:45 +0000
