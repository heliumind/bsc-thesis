# Gilbert-Elliot Model

Author/Owner: Henry He
Related Draft: [Simulation Code](simulation_code.md), [Background](background.md)
Type: Note

Wireless channels are error-prone and 

Realistic models for impairments and failures during transmission.

Popular model based approach to describe for bit error processes (stochastic process) / patterns in transmission channels and for analysing 

- 2 state homogenous markov chain
    - GOOD
    - BAD
    - each has its own loss probability

markov chain → ergodic & stationary → packet → implementation

1. Perform a random experiment (Bernoulli experiment) according to the present channel state to determine whether the package is lost
2. Perform a random experiment according to the present channel state to determine the next state. In case a state change occur, set the state variable and error probability to the new state

## Average Coherence Time

In the literature often a discrete time Markov chain is used, with state transitions after every packet / time slot. Thus the state sojourn time (duration of being in a state) is geometrically distributed. The mean state sojourn time measuerd in number of steps in this state is given by:

$$T_G = \frac{1}{P(B\mid G)} = 10 \\
T_B = \frac{1}{P(G\mid B)} = 10$$

## Parameters

- Transition probabilities $P(G \mid B) = 0.1$ *recovery rate*
- Transition probabilities $P(B \mid G) = 0.1$ *failure rate*
- Loss probability in *GOOD* state: $p_G = 0.1$
- Loss probability in *BAD* state: $p_B = 0.75$

This is a balanced case

## Formulas

$$w_G = P(G) = \frac{P(G \mid B)}{P(G \mid B) + P(B \mid G)} = \frac{1}{2}$$

$$w_B = P(B) = \frac{P(B \mid G)}{P(G \mid B) + P(B \mid G)} = \frac{1}{2}$$

$$\mathbf{p}^{(t+1)} = \Pi^T \left [\begin{array}{c} P(G)^t \\ P(B)^t \end{array} \right]$$

$$\Pi = \left [\begin{array}{cc} 1 - P(B \mid G) & P(B \mid G) \\ P(G \mid B) & 1-P(G \mid B) \end{array} \right]$$

Average loss probability $w_G \cdot p_G + w_B \cdot p_B = \frac{17}{40} = 0.425$
