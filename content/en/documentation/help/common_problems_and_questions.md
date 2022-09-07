---
title: "Common Problems and Questions"
description: "List of frequently encountered problems and questions."
date: 2022-07-01T22:31:46+01:00
lastmod: 2022-07-01T22:31:46+01:00
draft: false
images: []
menu:
  documentation:
    parent: "help"
weight: 10
---

### Docker

##### I cannot start or run Docker on Linux

On Linux, non-`sudo` users may encounter `permission denied` or `Cannot connect to the Docker daemon. Is the docker daemon running on this host?` errors. By default, only `sudo` users may run Docker commands on Linux (by adding `sudo` to the start of the command). To allow other users to run commands, a `sudo` user must created a new group called `docker` and add users to it: 

```
sudo groupadd docker             # Create new group
sudo usermod -aG docker $USER    # Add USER to group
```

Exercise caution with the `usermod` command; incorrect use may result in privileges being removed from users. Users may need to log out and then log back in for changes to take effect. Users belonging to the `docker` group should now be able to run Docker without the `sudo` command.

In addition, `sudo` users can control the Docker daemon using the following commands:

```
sudo systemctl start docker      # Start daemon
sudo systemctl stop docker       # Stop daemon
sudo systemctl restart docker    # Restart daemon
sudo systemctl status docker     # Check status of daemon
```

{{< alert icon="ⓘ" context="info">}}

**Info**: More information can be found on the [Docker Linux post-install page ⧉](https://docs.docker.com/engine/install/linux-postinstall/).

{{< /alert >}}

### Installing dependencies

##### I don't know how to check if a package is already installed

Before installing a dependency it is important to check if it is already present on your system, as multiple different installs of dependencies can cause issues during the build process. This can be done using the `whereis $PACKAGE_NAME` command which searches your system for the package's binary, source, or manual files. Additionally, the version number of many packages can be checked using `$PACKAGE_NAME --version`. 

##### I don't know how to install packages

In general, on Linux there are three main ways to install software packages:

*Via a package manager*: There are a variety of Linux package managers, for example `apt` is used on Debian systems and `dnf` is used on RHEL/Fedora. Common packages can be installed and managed using these package managers, for example:

```
sudo apt install $PACKAGE_NAME    # On Debian
sudo dnf install $PACKAGE_NAME    # On RHEL/Fedora
```

This can only be carried out by a user with `sudo` privileges, and also installs packages system-wide.

*By downloading a binary*: If a package is not available via a package manager, or if you do not have `sudo` privileges, then pre-built binaries might be available. Binaries are files which have been build from the source code of the package, and are operating-system specific. These can be downloaded to your system and require no further installation. This can be useful for keeping installed packages in one folder and not installing system-wide.

You can download files using a web browser, or if you have a link to the download (which may be a compressed folder) you can use:

```
wget $DOWNLOAD_LINK            # Download folder
tar -xvf $COMPRESSED_FOLDER    # Extract (if folder is tarball)
unzip $COMPRESSED_FOLDER       # Extract (if folder is zip file)
```

*By building from source*: If the package is not available via package managers or as a binary, then you may have to build the package from source. Often there will be detailed instructions on how to do this on the package's website. Alternatively, the source code may include an `INSTALL` file (similar to a `README` file) which provides installation instructions. For example, GSL 2.7.1 can be fully installed from source using the following commands:

```
wget https://mirror.ibcp.fr/pub/gnu/gsl/gsl-latest.tar.gz
tar -xvf gsl-latest.tar.gz
cd gsl-2.7.1
./configure
make
make install
```

Some packages are header-only; this means that the package does not need to be built and consists simply of header files.

##### I can't or don't want to install dependencies system-wide

For users on a shared cluster, it may not be possible (or desirable) to install dependencies system-wide. Instead, dependencies should be installed in a folder specified by the user.

In general, package managers do not support installing packages to arbitrary directories. To install a package in a specific folder, you will need to either download a binary to that folder or build the package from source.

See [I don't know how to install packages](/documentation/help/common_problems_and_questions#i-don-t-know-how-to-install-packages) for an example of building GSL from source. The `make install` command will attempt to install the package system-wide in the `/usr` or `/usr/local` directories, and if you do not have `sudo` privileges this will result in a `permission denied` error. To change the install directory, change the `prefix` flag of the `./configure` command:

```
./configure --prefix=$INSTALL_DIRECTORY
```

When installing Python packages using `pip`, it is good practice to use a virtual environment. Python virtual environments allow Python packages to be installed in a specific folder, separate from the other packages already installed on the system. Provided that you already have Python installed, a folder containing virtual environments can be created like so:

```
python -m venv $FOLDER_PATH    # Create virtual environment
cd $FOLDER_PATH                # Navigate to folder
source bin/activate            # Run activation script
pip install $PACKAGE           # Install package in virtual environment
```

Note that every terminal session you will need to re-run the activation script to work in the virtual environment.

{{< alert icon="ⓘ" context="info">}}

**Info**: A good tutorial on virtual environments can be found [here](https://realpython.com/python-virtual-environments-a-primer/).

{{< /alert >}}


##### My system cannot find an installed package

If you have installed a package but `$PACKAGE_NAME --version` or similar cannot detect any installed versions, then you may need to take extra steps so that your system can find the package. 

The `PATH` variable contains a list of directories which are searched when the system is trying to find a package. This list can be viewed with the command `echo $PATH`. If a package is not in any of these directories then it will not be found by the system; this can be fixed by adding the folder containing the package to the `PATH` variable using:

```
export PATH=$PATH:$FOLDER_PATH
```

This will temporarily add a folder to the `PATH` variable. To make it permanent, you must add this command to your `.bashrc` file located in the `/home` directory.

Alternatively, if you do not want to change the `PATH` variable then you can use full paths. For example, Docker commands can be run by replacing `docker` with the full path `/usr/bin/docker`. If you are using full paths frequently, you may wish to create a shortcut using the `alias` command, for example:

```
alias $SHORT_COMMAND=$LONG_COMMAND
```

This allows long commands (possible including full paths) to be invoked using a short, user-defined command. This effect only lasts until the end of the terminal session; to make it permanent it will also need to be added to the `.bashrc` file.

### Building GAMBIT

##### CMake is finding Python backends in a different place to the interpreter

You may encounter the message:

```
NOTE: You are using different Python versions for the interpreter and the libraries!
```

The best way to make sure that CMake finds the right versions of Python is to specify the following flags:

- `-DPYTHON_EXECUTABLE`: This should point to a Python interpreter. If you are using a virtual environment then this should point towards the interpreter present in the virtual environment (this makes sure that the Python libraries installed in the virtual environment are detected).
- `-DPYTHON_INCLUDE_DIR`: This should point to the `include` directory for the system's Python, not the `include` directory in the virtual environment!
- `-DPYTHON_LIBRARY`: This should point to the system's Python library file, which should be of the form `libpython.so` or `libpython3.so`.

If this still is not working, or if CMake cannot determine the version number of the libraries that it finds, it may be that you need to install the Python Development Package. This can be found on major package managers with the name `python-dev` or `python-devel` or some numbered variation.

##### CMake cannot find the LAPACK libraries

If CMake cannot find LAPACK then you should specify the `-DLAPACK_LIBRARIES` flag. This should point to the shared library file `liblapack.so`. Unfortunately, when built from source, LAPACK by default includes the static library file `liblapack.a` rather than the shared library file `liblapack.so`. This static library file will result in a CMake error.

To fix this, try to find a LAPACK distribution which includes the shared library file. For example, for RHEL/Fedora systems a version of LAPACK can be obtained via `dnf` which contains the shared library file.

##### Changing CMake flags does not change the output

On every run, CMake caches flags and values in the `build` directory. If you do not delete the `build` directory each time you run CMake then the cached values will be used and the new flags will be ignored.

It may also be the case that you have spelled a flag incorrectly, or forgotten to add the `-D` prefix. If you have used a flag that CMake does not recognise then you will receive the message:

```
CMake Warning:
  Manually-specified variables were not used by the project:
  $INCORRECT_FLAGS
```

If you are frequently re-running CMake while trying to debug the output, it may be useful to use a `bash` script. For example:

```
#!/bin/bash

rm -r build          # Delete previous run   
mkdir build          # Make build directory
cd build
cmake $YOUR_FLAGS    # Run cmake
```

##### GAMBIT builds extremely slowly

If the final `make gambit` command takes a long time (or fails), then you may want to consider using the `-Ditch` flag with the first `cmake` command. This flag allows you to specify `Bits` and components of GAMBIT to "ditch" from the build process, allowing GAMBIT to build faster.

For example, if you wish to ditch all `Bits` apart from [`ColliderBit`](example.com), add the flag:

```
-Ditch="CosmoBit;FlavBit;NeutrinoBit;DarkBit;DecayBit;FlavBit;ObjectivesBit;PrecisionBit;ScannerBit;SpecBit"
```

##### Python header files are not found

During the `make gambit` command you may encounter the message:

```
fatal error: Python.h: No such file or directory
```

If these header files cannot be found, it may be because you have not installed the Python Development Package. This package provides extra header files and libraries for Python development. You can find it on major package managers with the name `python-dev` or `python-devel` or some numbered variation.

### Running GAMBIT

### Miscellaneous Questions

| Question | Answer |
| --- | --- |
| I get `undefined symbol: run` or `undefined symbol: cdiver` or similar when I try to run a scan.  What gives? | You probably forgot to re-run cmake (followed by make) after building the scanner you're trying to run with. |
| Is the detector parameterisation BuckFast in ColliderBit named after Andy Buckley? | [No ⧉](http://www.theguardian.com/lifeandstyle/2015/feb/27/buckfast-drink-with-supernatural-powers-destruction). |
| Is Are Raklev's first name really Åre? | No, that's a ski resort. |
