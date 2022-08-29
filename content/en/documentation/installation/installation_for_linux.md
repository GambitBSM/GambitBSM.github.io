---
title: "Installation for Linux"
description: ""
date: 2022-07-01T22:31:46+01:00
lastmod: 2022-07-01T22:31:46+01:00
draft: false
images: []
menu:
  documentation:
    parent: "installation"
weight: 30
---

{{< alert icon="ⓘ" context="info">}}

**Info**: If you intend to build the entirety of GAMBIT without optimisation, at least 10GB of RAM is required. Building with optimisation (for performance-critical applications) may require more than 20GB of RAM. If your system does not meet these requirements then consider [only partially building GAMBIT](/documentation/help/common_problems_and_questions#gambit-builds-extremely-slowly), or using the [Docker image](/documentation/installation/docker_usage).

{{< /alert >}}

### Installing dependencies

GAMBIT is built using Cmake, and has a number of compulsory dependencies. Before installing a dependency, make sure to check if it is already present on your system. Multiple different installs of dependencies can cause issues during the build process.

{{< alert icon="⚠" context="danger">}}

**Common Problem**: For users on a shared cluster, it may not be possible (or desirable) to install dependencies system-wide. Instead, dependencies should be installed in a folder specified by the user. See [here](/documentation/help/common_problems_and_questions#i-don-t-want-to-install-dependencies-system-wide) for more information.

{{< /alert >}}

##### C++ compiler

GAMBIT requires one of `gcc` (GNU Compiler Collection) `>= 5.1`, `llvm clang >= 10`, or `icc` (Intel C/C++ Compiler) `>= 15.0.2`. It is likely that one of these is already present on your system. To check which versions of each are installed, you can use the following commands:

```
gcc --version
clang --version
icc -v
```

In the event that none are installed, `gcc` and `clang` are available via the package managers of all major Linux distributions (`apt` for Debian, `dnf` for RHEL/Fedora etc). `icc` can be downloaded as part of the [Intel oneAPI Base Toolkit ⧉](https://www.intel.com/content/www/us/en/developer/tools/oneapi/base-toolkit.html#gs.a3697a), which also includes the `ifort` Fortran compiler (see next section).

Alternatively, to build from source refer to the installation guides for [GCC ⧉](https://gcc.gnu.org/install/index.html), [Clang ⧉](https://clang.llvm.org/get_started.html) or [ICC ⧉](http://registrationcenter-download.intel.com/akdlm/irc_nas/1855/l_cc_p_10.1.026_INSTALL.htm).

{{< alert icon="⚠" context="danger">}}

**Common Problem**: If you have installed a package but `$PACKAGE_NAME --version` or similar cannot detect any installed versions, then you may need to take extra steps so that your system can find the package. See [here](/documentation/help/common_problems_and_questions#my-system-cannot-find-an-installed-package) for more information.

{{< /alert >}}

##### Fortran compiler

GAMBIT requires either `gfortran` (GNU Fortran Compiler) `>= 5.1` or `ifort` (Intel Fortran Compiler) `>= 15.0.2`. `gfortran` is associated with `gcc` and `ifort` is associated with `icc`, so depending on your C++ compiler you may already have a Fortran compiler installed. You can check the versions using:

```
gfortran --version
ifort --version
```

`gfortran` is available via all major Linux package managers, see the [GFortran installation page ⧉](https://fortran-lang.org/learn/os_setup/install_gfortran#linux) for more information. `ifort` has been superceded by Intel oneAPI (see previous section), however it can still be downloaded from [Intel's standalone component page ⧉](https://www.intel.com/content/www/us/en/developer/articles/tool/oneapi-standalone-components.html#fortran).

##### Cmake

GAMBIT requires `cmake >= 2.8.12`. The installed version can be checked using `cmake --version`. If it is not installed, Cmake source code or pre-built binaries can be downloaded from the [Cmake installation page ⧉](https://cmake.org/install/).