# Simulation Code

Author/Owner: Onur Ayan
Related Draft: 
Tags: C++, Primary
Type: Code

Simulation code for the **Finite Horizon Scheduler** → See [AoI-based Finite Horizon Scheduling for Heterogeneous Networked Control Systems](ayan2020aoi.md) 

## Dependencies

- QT 5.14.2

## Building

`NCS_framework_cpp.pro` contains information used by `qmake` to generate Makefiles that contain the commands that are needed to build the project.

1. Run `qmake`
2. Run `make`

# Structure

## Folders

- `Control`: contains plant behaviors
- `Network`: contains every Network related sources

### BaseStation

- *Main class*: `basestation.*`
- 2 Scheduler Types as member:
    1. **AOI**
    2. **FINITE_HORIZON_SCHEDULER**
- are implemented in `aoischeduler.*` and `finitehorizonscheduler.*` respectively
- `BaseStation` stores *hosts/MobileTerminals* as pointers in a vector `users`
    - assigns them with an ID (range(0, BS_MAX_USERS)) but doesn't save the combination → `getUsersWithID`
- Schedulers are told which two *rxGw* and *txGw* are a pair / form a loop via `registerLoop` called by `controlloop.h`
- Every slot `BaseStation::update`(number
    - equivalent of its run function
- `NetworkBase` contains common elements both scheduler types share

### MobileTerminal

- `Gateway.h` → `txgateway.h` and `rxgateway.h` which are used by the main control object `controlloop.h`
- Loss probability is defined at initialization

### Controlloop

- **Actual** plant simulation
- Initializes a generalized control loop with *plant, controller, sensor* and as building *blocks* and connects their *links*
- Further network parameters are set e.g. *sampling period, sampling offset are initialized*
- *update*
    - control input is computed by the controller at the beginning of each *sam*p*le period* k
        - Uses only the freshest packet received → during the last sampling period rxBuf is constantly rewritten with the newest packet
    - the calculated input is applied directly after obtaining it within the same *sample period k*
    - also the plant is sampled at the end of *sample period k*
- k is the current sampling period
- packets are timestamped so that the controller is able to calculate AoI

**Scheduler and ControlLoop access the gateways seperately**: The controlLoop sees them as Gateways while the scheduler sees them as ControlApplications

### ControlApplication

Has members *txGw, rxGw, time-invariant system parameters of sub system i, ts_ms and samplingOffset*

How the *scheduler* sees the plant ⇒ another replica of simulation

- has to verify by its own if an sample event occurred in order to properly manage / update network state
- Network state needed to do tree

## FiniteHorizonScheduler

- `costMap` has every possible cost in a tabular form
- are precomputed at `initCostMap` → high computation

|Control Loop / AoI| 1 | 2 | 3 |
|---|---|---|---|
|Loop1| |
|Loop2| |
|Loop3| |

## Tree

tree is saved as vector of nodes

- in building the tree

Question: I think the code doesn't allow the case in a tree where for a given state every admissible action taken (feasible + no schedule). If feasible not equal to 0 . Or 

### Misc

- `Eigen`: Math library
- `Common`: Sources for common elements mostly regarding *graph/tree* structure for the schedulers

## Files to check

- [x]  `mobileterminal.*`
- [x]  `scheduler.*`
- [x]  `application.h`
- [x]  `controlapplication.*`
