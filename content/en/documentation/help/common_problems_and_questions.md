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

### Installation

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

More information can be found on the [Docker Linux post-install page ⧉](https://docs.docker.com/engine/install/linux-postinstall/).

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
./configure -prefix=$INSTALL_DIRECTORY
```

When installing Python packages using `pip`, it is good practice to use a virtual environment 

<!--- ROSSTODO: instructions on building to specific folders and python venv -->

##### My system cannot find an installed package

If you have installed a package but `$PACKAGE_NAME --version` or similar cannot detect any installed versions, then you may need to take extra steps so that your system can find the package. 

<!--- ROSSTODO: Instructions on adding to path, using full executable paths, and aliases, whereis list -->

##### GAMBIT builds extremely slowly

<!--- ROSSTODO: Instructions on ditching parts of gambit -->

### Running GAMBIT

### Miscellaneous Questions

| Question | Answer |
| --- | --- |
| I get `undefined symbol: run` or `undefined symbol: cdiver` or similar when I try to run a scan.  What gives? | You probably forgot to re-run cmake (followed by make) after building the scanner you're trying to run with. |
| Is the detector parameterisation BuckFast in ColliderBit named after Andy Buckley? | [No ⧉](http://www.theguardian.com/lifeandstyle/2015/feb/27/buckfast-drink-with-supernatural-powers-destruction). |
| Is Are Raklev's first name really Åre? | No, that's a ski resort. |
