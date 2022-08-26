---
title: "Installation for Windows"
description: ""
date: 2022-07-01T22:31:46+01:00
lastmod: 2022-07-01T22:31:46+01:00
draft: false
images: []
menu:
  documentation:
    parent: "installation"
weight: 40
---

Windows is not directly supported by GAMBIT. However, Linux distributions can be installed on Windows machines using WSL or by dual-booting. GAMBIT can then be built within these Linux environments

### Running Linux on a Windows machine

##### Installing Windows Subsystem for Linux (WSL)

WSL is a tool supplied by Microsoft that allows Linux distributions to be installed on Windows. Follow the [installation instructions ⧉](https://docs.microsoft.com/en-us/windows/wsl/install) to install it on your system.

<!--- ROSSTODO: List of supported linux distros? -->

{{< alert icon="ⓘ" context="info">}}

**Info**: WSL 2 is a requirement for installing the Docker engine on Windows. If you have installed WSL and wish to easily install a limited version of GAMBIT rather than building it from source, consult the [Docker Usage](/documentation/installation/docker_usage/) page to download the Docker image.

{{< /alert >}}

##### Dual-booting Linux

Alternatively, you can set up your machine so that part of your hard drive is occupied by a Linux installation. At start-up you can then choose to boot either Windows or Linux. This separates Linux and GAMBIT from your Windows installation but is much more involved to set up. For example, refer to the [Ubuntu dual-booting guide ⧉](https://help.ubuntu.com/community/WindowsDualBoot) for instructions on dual-booting Windows and Ubuntu, a common Linux distribution.

### Building GAMBIT

Once you have a working Linux installation, refer to the [Installation for Linux](/documentation/installation/installation_for_linux/) page for instructions on building GAMBIT from source.