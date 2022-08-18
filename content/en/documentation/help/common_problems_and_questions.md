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

##### Docker not starting

It may be necessary to create `docker` group and add users to it in order to use Docker commands. For example:

```
sudo groupadd docker
sudo usermod -aG docker $USER
```

### Running GAMBIT

### Miscellaneous Questions

| Question | Answer |
| --- | --- |
| I get `undefined symbol: run` or `undefined symbol: cdiver` or similar when I try to run a scan.  What gives? | You probably forgot to re-run cmake (followed by make) after building the scanner you're trying to run with. |
| Is the detector parameterisation BuckFast in ColliderBit named after Andy Buckley? | [No](http://www.theguardian.com/lifeandstyle/2015/feb/27/buckfast-drink-with-supernatural-powers-destruction). |
| Is Are Raklev's first name really Åre? | No, that's a ski resort. |
