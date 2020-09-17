# Scheduler Performance

Author/Owner: Henry He
Type: Note

## Age-of-Information (AoI)

- Average AoI → the lower the better
- connects several communication metrics e.g. delay, update frequency

## Mean Squared Error (MSE) a.k.a NIE

- Quality of control input is dependent on state estimation
- Disturbance and high AoI cause high state estimation error
- discounted age penalty
- the lower the better
- Optimization goal of scheduler

## Control Cost J

- LQG (linear quadratic gaussian) cost → applied to a plant and sensor subject to additive gaussian white noise (AWGN)

$$F_i = \frac{1}{K}\limsup_{K\to\infty}\sum_{k_i=0}^{K-1}(\mathbf{x_i[k_i]})^T\mathbf{Q}_i\mathbf{x_i[k_i]} + (\mathbf{u_i}[k_i])^T\mathbf{R}_i\mathbf{u}_i[k_i]$$

- Linear controller consisting of Kalman filter and LQR optimizes $F_i$
- $Q_i$ is a positive definite matrix: diagonal elements control how fast system state converge to 0 → the bigger the value the faster
- $R_i$ is a positive definite matrix: diagonal elements account for restriction of control variables → the bigger the value the smaller the respective control value

> Existing code uses $Q_i = \mathbb{1}$ and $R_i = 0$
