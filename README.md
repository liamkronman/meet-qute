# MeetQute
> The world's *leading* quantum computing-powered dating platform. A "bad idea".

**Note:** This document is a work in progress (WIP). The current mechanics of MeetQute may change in future iterations.

## Motivations
As we stand at the cusp of a technological renaissance, quantum computing beckons as a game-changer, especially in areas where traditional algorithms have hit their limits. One area that appears to have hit its limit is online (classical) dating. Say goodbye to the days of swiping and liking based on superficial algorithms; quantum computing heralds a new era in matchmaking.

[Recent breakthroughs](https://newsroom.ibm.com/2023-12-04-IBM-Debuts-Next-Generation-Quantum-Processor-IBM-Quantum-System-Two,-Extends-Roadmap-to-Advance-Era-of-Quantum-Utility) in quantum computing, both pioneering and historical, have stirred a whirlwind of emotions in the tech community, from awe to apprehension. These advancements leave people wondering: are we on the verge of a quantum era that will eclipse our current classical computing world, or is this just a transient wave of excitement?

*In short, how practical is quantum computing, today?*

MeetQute was born from these reflections, aiming to harness the unparalleled processing power of quantum computers to create a matchmaking experience that's light-years ahead of today's algorithms. This idea began as an after-lecture thought of clueless Course 6 students in MIT's 18.435 (8.370), envisioning a future where their love lives could finally be catalyzed with quantum tech.

## Why Quantum??
Quantum computing is not just a step up from classical computing; it's a whole new game. Let's break it down:

### A Beginner's Guide to Quantum Computing

#### What is a Qubit?
- **Qubit:** The fundamental unit of quantum computing. Unlike the binary bit in classical computing which represents either 0 or 1, a qubit can exist in a state of 0, 1, or any quantum superposition of these states. Mathematically, a qubit state \(|\psi\rangle\) can be represented as \(|\psi\rangle = \alpha|0\rangle + \beta|1\rangle\), where \(|0\rangle\) and \(|1\rangle\) are the basis states, and \(\alpha\) and \(\beta\) are complex numbers that describe the probability amplitudes of these states.

#### Quantum Superposition and Entanglement
- **Superposition:** This principle allows a qubit to be in a combination of both 0 and 1 states at the same time. For example, a qubit in superposition might be represented as \( \frac{1}{\sqrt{2}}(|0\rangle + |1\rangle) \), indicating equal probabilities of being found in either state upon measurement.
- **Entanglement:** A phenomenon where the states of two or more qubits become interconnected so that the state of one qubit directly correlates with the state of another, regardless of the distance between them. Mathematically, if two qubits are entangled, their combined state cannot be described independently but only as a whole. For example, the Bell state \( \frac{1}{\sqrt{2}}(|00\rangle + |11\rangle) \) is an entangled state of two qubits.

#### Quantum Algorithms: From Factoring to Beyond
- **Shor's Algorithm:** Famous for factoring large numbers exponentially faster than the best-known classical algorithms. Classical algorithms have an exponential runtime of \(O(2^n)\), while Shor's algorithm runs in polynomial time, approximately \(O(n^3)\), for n-bit numbers.
- **Grover's Algorithm:** Improves the efficiency of searching unsorted databases, offering a quadratic speedup compared to classical algorithms. Classical search algorithms have a linear runtime of \(O(N)\), whereas Grover's algorithm brings this down to \(O(\sqrt{N})\), where \(N\) is the number of items.
- **Quantum Simulation:** Quantum computers excel at simulating molecular and quantum systems, tasks that are extremely challenging for classical computers. This capability could lead to breakthroughs in material science and drug discovery.

#### Beyond the Basics: Advanced Quantum Computing
- **Quantum Error Correction:** Due to the sensitivity of quantum systems to external disturbances, error correction is vital for reliable computations. Quantum error correction involves encoding quantum information in such a way that it is protected from errors due to decoherence and other quantum noise.
- **Quantum Networking:** Developing quantum networks could result in exceptionally secure communication methods, leveraging principles like quantum entanglement and no-cloning theorem for unbreakable encryption.


## Implementation

> "Love looks not with the eyes, but with the mind, And therefore is winged Cupid painted blind."

> "The course of true love never did run smooth."

Dating, a complex puzzle of human emotions and connections, often reduces to a mere game of numbers in traditional apps. We will transcend this limitation to transform matchmaking into an advanced science of human compatibility.

**to do...**

## Timeline

**Biggest Deadline:** All quantum scripts must be ready for iQuHACK on February 2nd-4th. Matches will be delivered shortly afterwards.

Working backwards, that means that volunteer data should be fully collected over IAP.

This project will be my first time developing in Qiskit. Pray that it isn't my last.

## Contributions
Started by Liam Kronman (a.k.a. [qupid@mit.edu](mailto:qupid@mit.edu)) and aided by his good friend GPT4.

[Contribution guidelines for this project](docs/CONTRIBUTING.md)

[Help and feedback](mailto:qupid@mit.edu)