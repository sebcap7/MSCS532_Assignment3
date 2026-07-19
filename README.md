# MSCS532_Assignment3

# Assignment 3: Understanding Algorithm Efficiency and Scalability


## Overview

This project includes the implementation and analysis of:

1. Randomized Quicksort
2. Hash Table with Chaining

The assignment contains theoretical analysis, empirical testing, and performance comparisons.

---

## Files

- `quicksort.py` – Deterministic and Randomized Quicksort implementations
- `comparison.py` – Performance comparison of both Quicksort algorithms
- `hashtable.py` – Hash Table using chaining for collision resolution
- `report.pdf` – Analysis, results, and discussion
- `README.md` – Project documentation

---

## How to Run

### Quicksort Implementation

```bash
python3 quicksort.py
```

Tests Deterministic and Randomized Quicksort on several edge cases.

### Performance Comparison

```bash
python3 comparison.py
```

Compares both algorithms using:

- Random arrays
- Sorted arrays
- Reverse-sorted arrays
- Arrays with repeated elements

### Hash Table with Chaining

```bash
python3 hashtable.py
```

Demonstrates:

- Insert
- Search
- Delete
- Collision handling through chaining

---

## Summary of Results

Randomized Quicksort performed consistently across all input types and avoided the recursion errors seen in Deterministic Quicksort on sorted and reverse-sorted arrays. The theoretical analysis showed an expected running time of **O(n log n)**, which matched the experimental results.

The Hash Table successfully supported insert, search, and delete operations using chaining. Under normal conditions, these operations run in expected **O(1)** time, while performance is affected by collisions and the load factor.

---

## Repository Structure

```text
Assignment3-Algorithm-Efficiency/
│
├── quicksort.py
├── comparison.py
├── hashtable.py
├── report.pdf
└── README.md
```
