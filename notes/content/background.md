# Background

Development of the upcoming generation of communication networks are largely
driven by changing application demands. Instead of solely focusing on data rate
increase, these networks are envisioned to support machine-type-communications
(MTC) or machine-to-machine communications (M2M), transforming the current
"Internet of Information" to a "Internet of Things and Services". Prominent
applications include vehicular networks, industrial automation, tele-robotics,
smart grids and cyber-physical systems. \cite{murray2003future} From a system
theoretical view, most of these emerging applications fall into the category of
_Networked Control Systems_ (NCS), i.e., feedback control loops closed
over a communication network. Each loop consists of a plant, a sensor, measuring
the plant's output, and the respective controller, reacting to the sensor's
data. 

In a typical NCS scenario, multiple heterogenous NCSs share a wireless
communication medium and compete for network resource to transmit their latest
sensor measurements to the controllers. Medium access is granted by a
centralized scheduler that determines which subset of control loops are allowed
to send their up-to-date state information. In such a setting, the communication
system needs to satisfy different time-critical-requirements of the underlying
control loops, while dealing with problems inherent to the network, such as
random delays, packet losses and time varying channel conditions. These
shortcomings motivate _control-aware_ communication protocol design
incorporating prioritization and efficient scheduling of NCSs. Such schedulers
aim to mitigate these network induced challenges, otherwise resulting in reduced
precision of control actions and degraded control quality. Thus, networking
policies need to be designed in a joint fashion by using _cross-layer_
metrics and considering detailed models of feedback control loops. 

Clearly, the control performance of NCS, i.e., quality of control (QoC), is
tightly coupled with the service provided by the communication network. While
traditionally, performance of network systems are measured by means of delay,
jitter and throughput, these human-oriented metrics do not sufficiently capture
the QoC requirements of heterogeneous NCS applications. Hence, new cross-layer
metrics are needed in control-aware communication protocol design.
Age-of-Information (AoI) is such a relatively new metric that measures the
information freshness at the receiver monitoring a remote process and used as
cross-layer metric in wireless medium access protocol design. It is defined as
the time elapsed since the generation of the latest received information. As the
name implies, AoI increases linearly in time for all types of applications and
drops upon receiving a new update. AoI combines packet generation frequency,
end-to-end delay, and packet loss in a single metric. For instance, the absence
of information increases AoI on the controller side regardless of its cause:
high delay, packet loss, or a low information update frequency. As an interface
between control application and communication network, AoI has been widely
adopted as an intermediate metric to calculate control system metrics. 

While such a setting allows control over large distances, wireless networks
inevitably introduce random delays, packet losses and time varying channel
conditions, degrading the control quality. As modern control theory is based on
the assumption that information are transmitted along perfect communication
channels, imperfections of the wireless channel or time-critical requirements of
the underlying control loops impose challenges for both communication and
control. 

## Contributions and Outline
In this work, we aim to develop a scheduling policy addressing a centralized
wireless resource scheduling problem for NCS with time varying Gilbert-Elliot
channel. To achieve this, we utilize an AoI-based, control dependent age-penalty
and form scheduling decisions by means of expected cost minimization. Further,
we consider the feedback control loops sharing a wireless communication link
with time-varying packet loss probabilities. Time varying conditions in the
network prevent the calculation of infinite horizon optimal scheduling policies.
Nevertheless, by applying stochastic optimization and dynamic programming has
proposed an online, centralized scheduling policy that is age-penalty optimal
for a finite horizon H. However, this solution assumes a Bernoulli, i.e.,
identically and independently distributed (i.i.d.), loss process for packet
transmission, while in reality packet losses tend to be correlated. One simple
model for correlated losses is the Gilbert-Elliot model. We aim to extend the
state-of-the-art by combining our findings of the Gilbert-Elliot channel model
with the said AoI-based Finite Horizon scheduler.
