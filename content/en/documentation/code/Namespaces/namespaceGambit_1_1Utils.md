---
title: "namespace Gambit::Utils"

description: "[No description available]"

---

# namespace Gambit::Utils

[No description available]

## Classes

|                | Name           |
| -------------- | -------------- |
| struct | **[Gambit::Utils::ci_less](/documentation/code/classes/structgambit_1_1utils_1_1ci__less/)** <br>Comparator for case-insensitive comparison in STL assos. containers */.  |
| class | **[Gambit::Utils::FileLock](/documentation/code/classes/classgambit_1_1utils_1_1filelock/)**  |
| class | **[Gambit::Utils::interp1d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__collection/)**  |
| class | **[Gambit::Utils::interp1d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp1d__gsl__collection/)**  |
| class | **[Gambit::Utils::interp2d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__collection/)**  |
| class | **[Gambit::Utils::interp2d_gsl_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp2d__gsl__collection/)**  |
| class | **[Gambit::Utils::interp4d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp4d__collection/)**  |
| class | **[Gambit::Utils::interp5d_collection](/documentation/code/classes/classgambit_1_1utils_1_1interp5d__collection/)**  |
| class | **[Gambit::Utils::ProcessLock](/documentation/code/classes/classgambit_1_1utils_1_1processlock/)** <br>Class to manage a process lock, using a file.  |
| class | **[Gambit::Utils::python_interpreter_guard](/documentation/code/classes/classgambit_1_1utils_1_1python__interpreter__guard/)** <br>Dummy guard class for python interpreters when python support is turned off.  |
| class | **[Gambit::Utils::specialised_threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1specialised__threadsafe__rng/)** <br>Derived thread-safe random number generator class, templated on the RNG engine type.  |
| class | **[Gambit::Utils::threadsafe_rng](/documentation/code/classes/classgambit_1_1utils_1_1threadsafe__rng/)**  |
| class | **[Gambit::Utils::translator](/documentation/code/classes/classgambit_1_1utils_1_1translator/)**  |
| struct | **[Gambit::Utils::type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/)** <br>Structure providing type equivalency classes to the dep resolver.  |

## Types

|                | Name           |
| -------------- | -------------- |
| typedef std::chrono::time_point< std::chrono::system_clock > | **[time_point](/documentation/code/namespaces/namespacegambit_1_1utils/#typedef-time-point)**  |

## Functions

|                | Name           |
| -------------- | -------------- |
| const std::string | **[hardmsg](/documentation/code/namespaces/namespacegambit_1_1utils/#function-hardmsg)**("Now calling abort (will produce a core file for analysis [if](/documentation/code/files/darksusy__mssm__6__4__0_8cpp/#function-if) this is enabled on your system; [if](/documentation/code/files/darksusy__mssm__6__4__0_8cpp/#function-if) so please include this with the bug report)" )<br>Members of [FileLock]() class.  |
| [type_equivalency](/documentation/code/classes/structgambit_1_1utils_1_1type__equivalency/) & | **[typeEquivalencies](/documentation/code/namespaces/namespacegambit_1_1utils/#function-typeequivalencies)**()<br>Backend info accessor function.  |
| [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[fix_type](/documentation/code/namespaces/namespacegambit_1_1utils/#function-fix-type)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) s)<br>Clean out whitespace and strip [Gambit](/documentation/code/namespaces/namespacegambit/) and default BOSSed class namespaces.  |
| time_point | **[get_clock_now](/documentation/code/namespaces/namespacegambit_1_1utils/#function-get-clock-now)**()<br>Get clock time.  |
| double | **[unwrap](/documentation/code/namespaces/namespacegambit_1_1utils/#function-unwrap)**(double x, void * p) |
| double | **[integrate_cquad](/documentation/code/namespaces/namespacegambit_1_1utils/#function-integrate-cquad)**(std::function< double(double)> ftor, double a, double b, double abseps, double releps)<br>Integrate a std::function using GSL cquad.  |
| double | **[run_lnlike_modifier](/documentation/code/namespaces/namespacegambit_1_1utils/#function-run-lnlike-modifier)**(double lnlike, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & lnlike_modifier_name, const [Options](/documentation/code/classes/classgambit_1_1options/) & lnlike_modifier_options)<br>Interface function that calls the correct modifier function based on the name in lnlike_modifier_name.  |
| double | **[lnlike_modifier_gaussian](/documentation/code/namespaces/namespacegambit_1_1utils/#function-lnlike-modifier-gaussian)**(double lnlike, const [Options](/documentation/code/classes/classgambit_1_1options/) & lnlike_modifier_options)<br>lnlike modifier: gaussian  |
| double | **[lnlike_modifier_gaussian_plateau](/documentation/code/namespaces/namespacegambit_1_1utils/#function-lnlike-modifier-gaussian-plateau)**(double lnlike, const [Options](/documentation/code/classes/classgambit_1_1options/) & lnlike_modifier_options)<br>lnlike modifier: gaussian_plateau  |
| EXPORT_SYMBOLS const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & | **[runtime_scratch](/documentation/code/namespaces/namespacegambit_1_1utils/#function-runtime-scratch)**() |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[p2dot](/documentation/code/namespaces/namespacegambit_1_1utils/#function-p2dot)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) s)<br>Convert all instances of "p" in a string to ".".  |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[construct_runtime_scratch](/documentation/code/namespaces/namespacegambit_1_1utils/#function-construct-runtime-scratch)**(bool fail_on_mpi_uninitialised =true) |
| EXPORT_SYMBOLS std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[delimiterSplit](/documentation/code/namespaces/namespacegambit_1_1utils/#function-delimitersplit)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) s, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) delim) |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[strip_leading_namespace](/documentation/code/namespaces/namespacegambit_1_1utils/#function-strip-leading-namespace)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) s, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ns)<br>Strips namespace from the start of a string, or after "const".  |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[replace_leading_namespace](/documentation/code/namespaces/namespacegambit_1_1utils/#function-replace-leading-namespace)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) s, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ns, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) ns_new)<br>Replaces a namespace at the start of a string, or after "const".  |
| EXPORT_SYMBOLS void | **[strip_whitespace_except_after_const](/documentation/code/namespaces/namespacegambit_1_1utils/#function-strip-whitespace-except-after-const)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s)<br>Strips all whitespaces from a string, but re-inserts a single regular space after "const".  |
| EXPORT_SYMBOLS void | **[strip_parentheses](/documentation/code/namespaces/namespacegambit_1_1utils/#function-strip-parentheses)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s)<br>Strips leading and/or trailing parentheses from a string.  |
| EXPORT_SYMBOLS bool | **[sspairset_contains](/documentation/code/namespaces/namespacegambit_1_1utils/#function-sspairset-contains)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > & )<br>Test if a set of str,str pairs contains any entry with first element matching a given string.  |
| EXPORT_SYMBOLS bool | **[sspairset_contains](/documentation/code/namespaces/namespacegambit_1_1utils/#function-sspairset-contains)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & , const std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > & )<br>Tests if a set of str,str pairs contains an entry matching two given strings.  |
| EXPORT_SYMBOLS bool | **[sspairset_contains](/documentation/code/namespaces/namespacegambit_1_1utils/#function-sspairset-contains)**(const [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) & quantity, const std::set< [sspair](/documentation/code/namespaces/namespacegambit/#typedef-sspair) > & set)<br>Tests if a set of str,str pairs contains an entry matching a given pair.  |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[str_fixed_len](/documentation/code/namespaces/namespacegambit_1_1utils/#function-str-fixed-len)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) s, int len)<br>Created a str of a specified length.  |
| EXPORT_SYMBOLS void | **[strcpy2f](/documentation/code/namespaces/namespacegambit_1_1utils/#function-strcpy2f)**(char * arr, int len, [str](/documentation/code/namespaces/namespacegambit/#typedef-str) s)<br>Copy a str to a character array, stripping the null termination character.  |
| EXPORT_SYMBOLS bool | **[endsWith](/documentation/code/namespaces/namespacegambit_1_1utils/#function-endswith)**(const std::string & str, const std::string & suffix)<br>Checks whether "str ends with "suffix.  |
| EXPORT_SYMBOLS bool | **[startsWith](/documentation/code/namespaces/namespacegambit_1_1utils/#function-startswith)**(const std::string & str, const std::string & prefix, bool case_sensitive =true)<br>Checks whether "str begins with "prefix.  |
| EXPORT_SYMBOLS bool | **[iequals](/documentation/code/namespaces/namespacegambit_1_1utils/#function-iequals)**(const std::string & a, const std::string & b, bool case_sensitive =false)<br>Perform a (possibly) case-insensitive string comparison.  |
| EXPORT_SYMBOLS std::vector< std::string > | **[split](/documentation/code/namespaces/namespacegambit_1_1utils/#function-split)**(const std::string & input, const std::string & delimiter)<br>Split string into vector of strings, using a delimiter string.  |
| EXPORT_SYMBOLS std::string | **[strtolower](/documentation/code/namespaces/namespacegambit_1_1utils/#function-strtolower)**(const std::string & a)<br>Convert a whole string to lowercase.  |
| EXPORT_SYMBOLS std::string | **[quote_if_contains_commas](/documentation/code/namespaces/namespacegambit_1_1utils/#function-quote-if-contains-commas)**([str](/documentation/code/namespaces/namespacegambit/#typedef-str) in)<br>Enclose a string in quotation marks if it contains commas.  |
| template <typename T ,size_t N\> <br>T * | **[beginA](/documentation/code/namespaces/namespacegambit_1_1utils/#function-begina)**(T(&) arr[N])<br>Get pointers to beginning and end of array.  |
| template <typename T ,size_t N\> <br>T * | **[endA](/documentation/code/namespaces/namespacegambit_1_1utils/#function-enda)**(T(&) arr[N]) |
| template <class Set1 ,class Set2 \> <br>bool | **[is_disjoint](/documentation/code/namespaces/namespacegambit_1_1utils/#function-is-disjoint)**(const Set1 & set1, const Set2 & set2)<br>Test if two sets are disjoint (works on any sorted std container I think)  |
| EXPORT_SYMBOLS const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & | **[ensure_path_exists](/documentation/code/namespaces/namespacegambit_1_1utils/#function-ensure-path-exists)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & path)<br>Ensure that a path exists (and then return the path, for chaining purposes)  |
| EXPORT_SYMBOLS bool | **[file_exists](/documentation/code/namespaces/namespacegambit_1_1utils/#function-file-exists)**(const std::string & filename)<br>Check if a file exists.  |
| EXPORT_SYMBOLS std::vector< [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > | **[ls_dir](/documentation/code/namespaces/namespacegambit_1_1utils/#function-ls-dir)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & dir)<br>Return a vector of strings listing the contents of a directory (POSIX)  |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[dir_name](/documentation/code/namespaces/namespacegambit_1_1utils/#function-dir-name)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & path)<br>Get directory name from full path+filename (POSIX)  |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[base_name](/documentation/code/namespaces/namespacegambit_1_1utils/#function-base-name)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & path)<br>Get file name from full path+filename (POSIX)  |
| EXPORT_SYMBOLS int | **[remove_all_files_in](/documentation/code/namespaces/namespacegambit_1_1utils/#function-remove-all-files-in)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & dirname, bool error_if_absent =true)<br>Delete all files in a directory (does not act recursively)  |
| EXPORT_SYMBOLS [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[return_time_and_date](/documentation/code/namespaces/namespacegambit_1_1utils/#function-return-time-and-date)**(const time_point & in)<br>Get date and time.  |
| EXPORT_SYMBOLS bool | **[are_similar](/documentation/code/namespaces/namespacegambit_1_1utils/#function-are-similar)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s1, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s2) |
| bool | **[check1](/documentation/code/namespaces/namespacegambit_1_1utils/#function-check1)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s1, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s2)<br>true if s1 can be obtained by deleting one character from s2  |
| bool | **[check2](/documentation/code/namespaces/namespacegambit_1_1utils/#function-check2)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s1, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & s2)<br>true if s1 can be obtained from s2 by changing no more than X characters (X=2 for now)  |
| EXPORT_SYMBOLS double | **[sqr](/documentation/code/namespaces/namespacegambit_1_1utils/#function-sqr)**(double a)<br>returns square of double - saves tedious repetition  |
| EXPORT_SYMBOLS bool | **[isInteger](/documentation/code/namespaces/namespacegambit_1_1utils/#function-isinteger)**(const std::string & s) |
| template <typename... T\> <br>void | **[dummy_function](/documentation/code/namespaces/namespacegambit_1_1utils/#function-dummy-function)**() |
| template <typename T \> <br>void | **[dummy_function](/documentation/code/namespaces/namespacegambit_1_1utils/#function-dummy-function)**(T one) |
| template <typename T1 ,typename... T\> <br>void | **[dummy_function](/documentation/code/namespaces/namespacegambit_1_1utils/#function-dummy-function)**(T1 first, T... args) |
| template <template< class, class > class Container,class T \> <br>void | **[masked_erase](/documentation/code/namespaces/namespacegambit_1_1utils/#function-masked-erase)**(Container< std::pair< T, bool >, std::allocator< std::pair< T, bool > > > & c) |
| void | **[InterpIter](/documentation/code/namespaces/namespacegambit_1_1utils/#function-interpiter)**(int Ntemp, double xi_1, double xi_2, std::vector< double > & fi, double test) |
| double | **[linearinterp1D](/documentation/code/namespaces/namespacegambit_1_1utils/#function-linearinterp1d)**(double x1, double x2, double y1, double y2, double xtest) |
| bool | **[sspairset_contains](/documentation/code/namespaces/namespacegambit_1_1utils/#function-sspairset-contains)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & el, const std::set< std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > & set)<br>Test if a set of str,str pairs contains any entry with first element matching a given string.  |
| bool | **[sspairset_contains](/documentation/code/namespaces/namespacegambit_1_1utils/#function-sspairset-contains)**(const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & el1, const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) & el2, const std::set< std::pair< [str](/documentation/code/namespaces/namespacegambit/#typedef-str), [str](/documentation/code/namespaces/namespacegambit/#typedef-str) > > & set)<br>Tests if a set of str,str pairs contains an entry matching two given strings.  |

## Attributes

|                | Name           |
| -------------- | -------------- |
| const [str](/documentation/code/namespaces/namespacegambit/#typedef-str) | **[buildtime_scratch](/documentation/code/namespaces/namespacegambit_1_1utils/#variable-buildtime-scratch)** <br>Return the path to the build-time scratch directory.  |
| const char *[] | **[whitespaces](/documentation/code/namespaces/namespacegambit_1_1utils/#variable-whitespaces)**  |

## Types Documentation

### typedef time_point

```
typedef std::chrono::time_point< std::chrono::system_clock > Gambit::Utils::time_point;
```



## Functions Documentation

### function hardmsg

```
const std::string hardmsg(
    "Now calling abort (will produce a core file for analysis if this is enabled on your system; if so please include this with the bug report)" 
)
```

Members of [FileLock]() class. 

### function typeEquivalencies

```
type_equivalency & typeEquivalencies()
```

Backend info accessor function. 

Type equivalency accessor function. 


### function fix_type

```
str fix_type(
    str s
)
```

Clean out whitespace and strip [Gambit](/documentation/code/namespaces/namespacegambit/) and default BOSSed class namespaces. 

### function get_clock_now

```
time_point get_clock_now()
```

Get clock time. 

Get current system clock time. 


### function unwrap

```
double unwrap(
    double x,
    void * p
)
```


Unwrapper for passing std::function to GSL integrator Based on example from [https://martin-ueding.de/articles/cpp-lambda-into-gsl/index.html](https://martin-ueding.de/articles/cpp-lambda-into-gsl/index.html)


### function integrate_cquad

```
double integrate_cquad(
    std::function< double(double)> ftor,
    double a,
    double b,
    double abseps,
    double releps
)
```

Integrate a std::function using GSL cquad. 

### function run_lnlike_modifier

```
double run_lnlike_modifier(
    double lnlike,
    const str & lnlike_modifier_name,
    const Options & lnlike_modifier_options
)
```

Interface function that calls the correct modifier function based on the name in lnlike_modifier_name. 

### function lnlike_modifier_gaussian

```
double lnlike_modifier_gaussian(
    double lnlike,
    const Options & lnlike_modifier_options
)
```

lnlike modifier: gaussian 

### function lnlike_modifier_gaussian_plateau

```
double lnlike_modifier_gaussian_plateau(
    double lnlike,
    const Options & lnlike_modifier_options
)
```

lnlike modifier: gaussian_plateau 

### function runtime_scratch

```
EXPORT_SYMBOLS const str & runtime_scratch()
```


Return the path to the run-specific scratch directory Don't call this from a destructor, as the internal static str may have already been destroyed. 


### function p2dot

```
EXPORT_SYMBOLS str p2dot(
    str s
)
```

Convert all instances of "p" in a string to ".". 

### function construct_runtime_scratch

```
EXPORT_SYMBOLS str construct_runtime_scratch(
    bool fail_on_mpi_uninitialised =true
)
```


Construct the path to the run-specific scratch directory This version is safe to call from a destructor. 


### function delimiterSplit

```
EXPORT_SYMBOLS std::vector< str > delimiterSplit(
    str s,
    str delim
)
```


Split a string into a vector of strings, using a delimiter, and removing any whitespace around the delimiter.

Split a string into a vector of strings using a delimiter, and remove any whitespace around the delimiters. 


### function strip_leading_namespace

```
EXPORT_SYMBOLS str strip_leading_namespace(
    str s,
    str ns
)
```

Strips namespace from the start of a string, or after "const". 

### function replace_leading_namespace

```
EXPORT_SYMBOLS str replace_leading_namespace(
    str s,
    str ns,
    str ns_new
)
```

Replaces a namespace at the start of a string, or after "const". 

### function strip_whitespace_except_after_const

```
EXPORT_SYMBOLS void strip_whitespace_except_after_const(
    str & s
)
```

Strips all whitespaces from a string, but re-inserts a single regular space after "const". 

Strip all whitespace except that following "const", in which case the whitespace is replaced by a single space. 


### function strip_parentheses

```
EXPORT_SYMBOLS void strip_parentheses(
    str & s
)
```

Strips leading and/or trailing parentheses from a string. 

### function sspairset_contains

```
EXPORT_SYMBOLS bool sspairset_contains(
    const str & ,
    const std::set< sspair > & 
)
```

Test if a set of str,str pairs contains any entry with first element matching a given string. 

### function sspairset_contains

```
EXPORT_SYMBOLS bool sspairset_contains(
    const str & ,
    const str & ,
    const std::set< sspair > & 
)
```

Tests if a set of str,str pairs contains an entry matching two given strings. 

### function sspairset_contains

```
EXPORT_SYMBOLS bool sspairset_contains(
    const sspair & quantity,
    const std::set< sspair > & set
)
```

Tests if a set of str,str pairs contains an entry matching a given pair. 

### function str_fixed_len

```
EXPORT_SYMBOLS str str_fixed_len(
    str s,
    int len
)
```

Created a str of a specified length. 

Created a std::string of a specified length. 


### function strcpy2f

```
EXPORT_SYMBOLS void strcpy2f(
    char * arr,
    int len,
    str s
)
```

Copy a str to a character array, stripping the null termination character. 

Copy a std::string to a character array, stripping the null termination character. Good for sending to Fortran. 


### function endsWith

```
EXPORT_SYMBOLS bool endsWith(
    const std::string & str,
    const std::string & suffix
)
```

Checks whether "str ends with "suffix. 

### function startsWith

```
EXPORT_SYMBOLS bool startsWith(
    const std::string & str,
    const std::string & prefix,
    bool case_sensitive =true
)
```

Checks whether "str begins with "prefix. 

### function iequals

```
EXPORT_SYMBOLS bool iequals(
    const std::string & a,
    const std::string & b,
    bool case_sensitive =false
)
```

Perform a (possibly) case-insensitive string comparison. 

Perform a simple case-insensitive string comparison From: [https://stackoverflow.com/a/4119881/1447953](https://stackoverflow.com/a/4119881/1447953)


### function split

```
EXPORT_SYMBOLS std::vector< std::string > split(
    const std::string & input,
    const std::string & delimiter
)
```

Split string into vector of strings, using a delimiter string. 

### function strtolower

```
EXPORT_SYMBOLS std::string strtolower(
    const std::string & a
)
```

Convert a whole string to lowercase. 

### function quote_if_contains_commas

```
EXPORT_SYMBOLS std::string quote_if_contains_commas(
    str in
)
```

Enclose a string in quotation marks if it contains commas. 

### function beginA

```
template <typename T ,
size_t N>
T * beginA(
    T(&) arr[N]
)
```

Get pointers to beginning and end of array. 

### function endA

```
template <typename T ,
size_t N>
T * endA(
    T(&) arr[N]
)
```


### function is_disjoint

```
template <class Set1 ,
class Set2 >
bool is_disjoint(
    const Set1 & set1,
    const Set2 & set2
)
```

Test if two sets are disjoint (works on any sorted std container I think) 

### function ensure_path_exists

```
EXPORT_SYMBOLS const str & ensure_path_exists(
    const str & path
)
```

Ensure that a path exists (and then return the path, for chaining purposes) 

### function file_exists

```
EXPORT_SYMBOLS bool file_exists(
    const std::string & filename
)
```

Check if a file exists. 

### function ls_dir

```
EXPORT_SYMBOLS std::vector< str > ls_dir(
    const str & dir
)
```

Return a vector of strings listing the contents of a directory (POSIX) 

Return a vector of strings listing the contents of a directory (POSIX) Based on [http://www.gnu.org/software/libtool/manual/libc/Simple-Directory-Lister.html](http://www.gnu.org/software/libtool/manual/libc/Simple-Directory-Lister.html)


### function dir_name

```
EXPORT_SYMBOLS str dir_name(
    const str & path
)
```

Get directory name from full path+filename (POSIX) 

### function base_name

```
EXPORT_SYMBOLS str base_name(
    const str & path
)
```

Get file name from full path+filename (POSIX) 

### function remove_all_files_in

```
EXPORT_SYMBOLS int remove_all_files_in(
    const str & dirname,
    bool error_if_absent =true
)
```

Delete all files in a directory (does not act recursively) 

### function return_time_and_date

```
EXPORT_SYMBOLS str return_time_and_date(
    const time_point & in
)
```

Get date and time. 

Return (locally defined) date and time corresponding to time_point. 


### function are_similar

```
EXPORT_SYMBOLS bool are_similar(
    const str & s1,
    const str & s2
)
```


Check if two strings are a "close" match Used for "did you mean?" type checking during command line argument processing 


### function check1

```
bool check1(
    const str & s1,
    const str & s2
)
```

true if s1 can be obtained by deleting one character from s2 

Sub-check for are_similar. true if s1 can be obtained by deleting one character from s2 


### function check2

```
bool check2(
    const str & s1,
    const str & s2
)
```

true if s1 can be obtained from s2 by changing no more than X characters (X=2 for now) 

Sub-check for are_similar. true if s1 can be obtained from s2 by changing no more than X characters (X=2 for now) 


### function sqr

```
EXPORT_SYMBOLS double sqr(
    double a
)
```

returns square of double - saves tedious repetition 

### function isInteger

```
EXPORT_SYMBOLS bool isInteger(
    const std::string & s
)
```


Check if a string represents an integer From: [http://stackoverflow.com/a/2845275/1447953](http://stackoverflow.com/a/2845275/1447953)


### function dummy_function

```
template <typename... T>
void dummy_function()
```


### function dummy_function

```
template <typename T >
void dummy_function(
    T one
)
```


### function dummy_function

```
template <typename T1 ,
typename... T>
void dummy_function(
    T1 first,
    T... args
)
```


### function masked_erase

```
template <template< class, class > class Container,
class T >
void masked_erase(
    Container< std::pair< T, bool >, std::allocator< std::pair< T, bool > > > & c
)
```


Expunge entries in a container of std::pairs for which the second (boolean) value of the pair is false. Useful for allowing evaluation of a removal criterion over the whole container in parallel. 


### function InterpIter

```
void InterpIter(
    int Ntemp,
    double xi_1,
    double xi_2,
    std::vector< double > & fi,
    double test
)
```


### function linearinterp1D

```
double linearinterp1D(
    double x1,
    double x2,
    double y1,
    double y2,
    double xtest
)
```


### function sspairset_contains

```
bool sspairset_contains(
    const str & el,
    const std::set< std::pair< str, str > > & set
)
```

Test if a set of str,str pairs contains any entry with first element matching a given string. 

### function sspairset_contains

```
bool sspairset_contains(
    const str & el1,
    const str & el2,
    const std::set< std::pair< str, str > > & set
)
```

Tests if a set of str,str pairs contains an entry matching two given strings. 


## Attributes Documentation

### variable buildtime_scratch

```
const str buildtime_scratch = GAMBIT_DIR "/scratch/build_time/";
```

Return the path to the build-time scratch directory. 

### variable whitespaces

```
const char *[] whitespaces = {" ", "\t", "\n", "\f", "\r"};
```





-------------------------------

Updated on 2025-02-12 at 16:10:33 +0000