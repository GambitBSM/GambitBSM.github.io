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

On Linux, non-`sudo` users may encounter `permission denied` or `Cannot connect to the Docker daemon. Is the docker daemon running on this host?` errors. By default, only `sudo` users may run `docker` commands on Linux (by adding `sudo` to the start of the command). To allow other users to run commands, a `sudo` user must created a new group called `docker` and add users to it: 

```
sudo groupadd docker             # Create new group
sudo usermod -aG docker $USER    # Add USER to group
```

Exercise caution with the `usermod` command; incorrect use may result in privileges being removed from users. Users may need to log out and then log back in for changes to take effect. Users belonging to the `docker` group should now be able to run `docker` without the `sudo` command.

In addition, `sudo` users can control the Docker daemon using the following commands:

```
sudo systemctl start docker      # Start daemon
sudo systemctl stop docker       # Stop daemon
sudo systemctl restart docker    # Restart daemon
sudo systemctl status docker     # Check status of daemon
```

More information can be found on the [Docker Linux post-install page ⧉](https://docs.docker.com/engine/install/linux-postinstall/).

##### I don't know how to install a package

<!--- ROSSTODO: instructions on building from source, binaries, header only, package managers, un taring etc -->

##### I can't or don't want to install dependencies system-wide

For users on a shared cluster, it may not be possible (or desirable) to install dependencies system-wide. Instead, dependencies should be installed in a folder specified by the user.

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
