# Assignment 5 - Q4 - Bayesian Networks

## Aim

To explore the tools used for modelling, problem representation, and inferencing using Bayesian Networks and to implement a sample Bayesian Network application.

---

# Introduction

A Bayesian Network is a probabilistic graphical model that represents relationships among different variables using nodes and directed edges. It is used to model uncertainty and perform reasoning based on available evidence.

Bayesian Networks are widely used in Artificial Intelligence, medical diagnosis, decision support systems, risk analysis, and prediction systems because they can handle uncertain and incomplete information.

---

# Components of a Bayesian Network

### 1. Nodes

Nodes represent random variables in the problem.

Examples:

```text
Flu
Covid
Fever
Cough
Breathing Problem
```

### 2. Directed Edges

Directed edges represent dependencies between variables.

Example:

```text
Flu → Fever
Covid → Fever
Covid → Breathing Problem
```

### 3. Conditional Probability Tables (CPDs)

CPDs store the probability values associated with each variable based on its parent nodes.

---

# Tools Used for Bayesian Networks

### 1. pgmpy

pgmpy is a Python library used for creating Bayesian Networks, defining probability distributions, and performing inference.

### 2. GeNIe

GeNIe is a graphical tool used for designing and analyzing Bayesian Networks and decision models.

### 3. Netica

Netica is a software tool used for building and evaluating Bayesian Networks.

### 4. Bayes Server

Bayes Server is a platform for probabilistic modelling and machine learning applications.

### 5. bnlearn

bnlearn is a package used for learning and analyzing Bayesian Networks from data.

---

# Problem Representation

In this assignment, a medical diagnosis problem is considered.

The Bayesian Network contains the following variables:

```text
Flu
Covid
Fever
Cough
Breathing Problem
```

Relationships used:

```text
Flu → Fever
Flu → Cough

Covid → Fever
Covid → Cough
Covid → Breathing Problem
```

The network models how diseases influence different symptoms.

---

# Inferencing

Inferencing is the process of calculating probabilities based on observed evidence.

The implementation uses Variable Elimination to perform inference.

Examples:

```text
Probability of Flu given Fever and Cough

Probability of Covid given Fever, Cough, and Breathing Problem

Probability of Covid given Breathing Problem
```

The calculated probabilities help in determining the likelihood of diseases based on symptoms.

---

# Example Implementation

A Bayesian Network was implemented using the pgmpy library.

The network contains:

- Flu
- Covid
- Fever
- Cough
- Breathing Problem

Conditional Probability Distribution (CPD) tables were defined for all variables, and inference was performed using Variable Elimination.

---

# Sample Output

```text
Bayesian Network model created successfully.

Nodes in the network:
['Flu', 'Fever', 'Cough', 'Covid', 'BreathingProblem']

Edges in the network:
[('Flu', 'Fever'),
 ('Flu', 'Cough'),
 ('Covid', 'Fever'),
 ('Covid', 'Cough'),
 ('Covid', 'BreathingProblem')]

Probability of Flu given Fever and Cough
No : 0.2369
Yes: 0.7631

Probability of Covid given Breathing Problem
No : 0.4474
Yes: 0.5526
```

---

# Conclusion

Bayesian Networks provide an effective way to represent uncertain knowledge and perform probabilistic reasoning. Various tools such as pgmpy, GeNIe, Netica, Bayes Server, and bnlearn can be used for modelling and inferencing.

The medical diagnosis example was implemented successfully, and inference queries were tested using multiple evidence conditions.
