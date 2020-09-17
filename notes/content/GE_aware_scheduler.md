# GE aware FH scheduler

Author/Owner: Henry He
Related Draft: [Simulation code](simulation_code.md) 
Type: Note

The scheduling task a.k.a *H-stage problem* can be modeled as a tree structure, where each node inside the tree represents a network state *s(t*). The root of the tree corresponds to the current network state *s(t)* 

## Tree structure

The node is recursively build through following instructions:

- Given a node with state *s(t)* there exists 2^N possible next states due to channel transitions. These are
    - Every binary combination of N bits: each user can be in a different channel state at any given time. For each of these channel state, the following N + 1 future state due to scheduling policies are possible
        - N Transmission success states
        - 1 failed state → failed states are always added as consequent nodes as it resembles the minimum set of admissible scheduling decisions / actions

### Nodes

There exists 2^N * (2 * N + 1) edges connecting given node to 2^N * (N + 1) next nodes

- 2 * N for either successful or failed transmission
- 1 Edge for no UL allocated → always there

### Complexity

- dominated by the construction of tree / graph
- **Worst case**: every sub-system has a *sampling period* of 1 (admissible action space is not reduced) → Every node will have maximum amount of 2^N * (N+1) child nodes
A perfect *m-ary tree* can be computed by the following formula:

    $$\sum\limits_{i=0}^{h}{m^i} = \frac{m^{h+1}-1}{m-1}$$

    Applied to our case m = 2^N * (N+1) and h = H

    $$\frac{(2^N(N+1))^{H+1}-1}{2^N(N+1)-1} \Rightarrow \mathcal{O}(N^H)$$
