# Quicksort Algorithm: Implementation, Analysis and Randomization

## Purpose

This project implements and compares two versions of the Quicksort algorithm:

* Deterministic Quicksort, which uses the last element as the pivot
* Randomized Quicksort, which selects the pivot randomly

The program tests both algorithms on random, sorted, and reverse-sorted datasets and records their average execution times.

## Files

* `quicksort_analysis.py` - Contains both Quicksort implementations and the empirical testing code
* `quicksort_results.csv` - Contains the recorded execution-time results
* `README.md` - Provides instructions and a summary of the project

## Requirements

* Python 3.8 or higher

No additional packages are required because the program only uses Python’s built-in modules.

## How to Run

1. Place `quicksort_analysis.py` in your project folder.
2. Open the folder in VS Code or a terminal.
3. Run the following command:

```bash
python quicksort_analysis.py
```

The program will display the results in the terminal and create `quicksort_results.csv` in the same folder.

## Summary of Findings

The deterministic version performed slightly faster on random data because it did not include the extra work of selecting random pivots. However, it became much slower on sorted and reverse-sorted data because using the last element as the pivot created highly unbalanced partitions.

The randomized version performed more consistently across all input distributions. Random pivot selection reduced the chance of repeatedly creating unbalanced partitions and helped the algorithm avoid worst-case behavior in the tested datasets.

Overall, randomized Quicksort was the more reliable option when the input order was unknown.
::: 
