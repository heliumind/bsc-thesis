# AoI-based Finite Horizon Scheduling for Heterogeneous Networked Control Systems

Author/Owner: Onur Ayan
Related Draft: 
Tags: Primary
Type: Paper

## Gist

Introduces an optimal finite horizon scheduler for centralized resource scheduling problem in NCS

## Setting

- Single wireless link
- multiple, heterogenous control systems
- each sub-system has it's own time-varying packet loss probability
- each sub-system is a linear time-invariant (LTI) control system consisting of a plant, a sensor and a controller
- state of the plant is observed by the sensor transmitted in a packet over a wireless link to the controller
- link between sensor and controller has their characteristic packet loss probability
- the controller's state of controller estimates the current remote plant's with it's most recent observation
- using the estimation it calculates its appropriate control input
- thus each sub-system is competing for network resources to improve the accuracy of their remote estimation process

## AoI - Age of Information

- Traditionally metrics used to measure the performance of human-oriented networks (delay, packet loss, throughput etc.) are not sufficient to capture *QoC* (Quality of Control) requirements
- *AoI* is a new *cross-layer* metric combining multiple metrics of communication networks into a single one

## Finite Horizon Scheduler

- AoI is used as an intermediary metric to calculate a cost function / **age penalty** for the scheduling problem (proportional to MSE of state estimation)
- Cost function is the aggregated MSE of state estimation
- Expected Finite Horizon cost
- Each time slot the scheduler can measure the instantaneous link quality → loss probability
- AoI-based *penalty functions* which the scheduler seeds to minimize looking a certain finite horizon into the future
- The scheduler is executed every slot but *only* the action at level 0 is used from the policy

### Complexity

- dominated by the construction of tree / graph
- **Worst case**: every sub-system has a *sampling period* of 1 (admissible action space is not reduced) → Every node will have maximum amount of N+1 child nodes
A perfect *m-ary tree* can be computed by the following formula:

    $$\sum\limits_{i=0}^{h}{m^i} = \frac{m^{h+1}-1}{m-1}$$

    Applied to our case m = N+1 and h = H

    $$\frac{(N+1)^{H+1}-1}{N} \Rightarrow \mathcal{O}(N^H)$$
