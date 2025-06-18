AoI-based Scheduling for Networked Control Systems over Gilbert-Elliot Channels
===
[![Download
PDF](https://img.shields.io/badge/Download-PDF-green)](https://github.com/heliumind/bsc-thesis/releases/download/final/BA_He.pdf)
[![CC BY 4.0][cc-by-shield]][cc-by]

## TUM EI Bachelor's thesis
Supervised by [Onur Ayan](https://github.com/oayan)
at Chair for Communication Systems (Prof. Wolfgang Kellerer)

## Directories
### LaTeX
Includes the actual thesis work
### code
Includes any code samples needed for evaluating and plotting simulation results
### notes
Includes the various content collection and notes made during the creation
### presentation
Includes the kickoff and final presentations
### results
Includes logs from simulations performed on a NCS testing framework available
from [here](https://github.com/oayan/finite_horizon_scheduling)

## Citation
```
@mastersthesis{BA_He,
  author = {He, Henry},
  title = {AoI-based Scheduling for Networked Control Systems over Gilbert-Elliot Channels},
  year = {2020},
  school = {Technische Universität München},
  pages = {44},
  language = {en},
  abstract = {Many emerging applications to be supported by upcoming 5G networks can be seen as Networked Control Systems (NCS), i.e., feedback control loops closed over a communication network. Delay, limited network resources, time-varying channel conditions are common network-induced challenges which can be tackled by a scheduler granting medium access efficiently. Age-of-Information (AoI) is a recently introduced network metric quantifying information freshness at a receiving network node and is meant to serve as an interface between communication network and application. AoI has generalized joint design in NCS, where networking policies have to consider the underlying system dynamics of its users. It has found successful use-cases in control-aware data scheduling. In this work, we employ AoI to calculate penalty functions used to derive an optimal control-aware scheduling strategy. We consider multiple, heterogeneous NCS sharing a single wireless link with time-varying channel conditions governed by the Gilbert-Elliot model. We have implemented a channel state dependent scheduling algorithm and obtained its complexity. However, simulations have shown that it is not scalable due to high computational costs. Furthermore, we have investigated possible reasons behind inconsistent behavior of our scheduling algorithm when simulated on different operating systems. The effect occurs on Linux, Mac and Windows and results in the scheduler distributing network resources differently, which leads to varying performance.},
}
```
---
This work is licensed under a
[Creative Commons Attribution 4.0 International License][cc-by].

[![CC BY 4.0][cc-by-image]][cc-by]

[cc-by]: http://creativecommons.org/licenses/by/4.0/
[cc-by-image]: https://i.creativecommons.org/l/by/4.0/88x31.png
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg
