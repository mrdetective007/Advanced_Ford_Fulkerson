# Advanced Ford Fulkerson Algorithm

This repository contains C++ code files that implement the Advanced Ford Fulkerson Algorithm for solving network flow problems.

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Code Files](#code-files)
- [Usage](#usage)
- [Explanation of q1.cpp](#explanation-of-q1cpp)
- [Explanation of q1_Bipartite_matching.cpp](#explanation-of-q1_bipartite_matchingcpp)
- [Conclusion](#conclusion)

## Introduction

The Advanced Ford Fulkerson Algorithm is a graph algorithm used to find the maximum flow in a flow network. It is an extension of the classical Ford Fulkerson Algorithm, with additional optimizations and techniques for efficient flow computation.

## Prerequisites

To compile and run the C++ code files, you'll need:

- C++ compiler (e.g., g++)
- Basic knowledge of graph theory and network flows

## Code Files

This repository contains the following C++ code files:

- [q1.cpp](Ford_Fulkerson/q1.cpp): Implementation of the Advanced Ford Fulkerson Algorithm for maximum flow computation.
- [q1_Bipartite_matching.cpp](Ford_Fulkerson/q1_Bipartite_matching.cpp): Implementation of Bipartite Matching using the Ford Fulkerson Algorithm.

## Usage

1. Clone the repository:

```bash
git clone https://github.com/mrdetective007/Advanced_Ford_Fulkerson.git
```

2. Navigate to the `Ford_Fulkerson` directory:

```bash
cd Advanced_Ford_Fulkerson/Ford_Fulkerson
```

3. Compile and run the C++ code:

```bash
g++ q1.cpp -o advanced_ford_fulkerson
./advanced_ford_fulkerson

g++ q1_Bipartite_matching.cpp -o bipartite_matching
./bipartite_matching
```

4. Follow the instructions in each code file to input the graph and required parameters. The code will output the maximum flow or the results of the bipartite matching.

## Explanation of q1.cpp

The `q1.cpp` file implements the Advanced Ford Fulkerson Algorithm for maximum flow computation in a flow network. It incorporates techniques like scaling and layered BFS to optimize flow augmentation. The code reads the graph's structure and capacities, calculates the maximum flow, and outputs the result.

## Explanation of q1_Bipartite_matching.cpp

The `q1_Bipartite_matching.cpp` file implements Bipartite Matching using the Ford Fulkerson Algorithm. It takes an input graph that represents a bipartite graph and computes the maximum matching by finding the maximum flow in an equivalent flow network.

## Conclusion

The Advanced Ford Fulkerson Algorithm and its extensions provide efficient solutions for network flow problems. The provided code files demonstrate the implementation of the algorithm and its application in finding maximum flows and bipartite matchings.
