# Synchronized Inventory Merger

### Challenge 2: Synchronized Inventory Merger

**Difficulty:** Intermediate

**Problem Description:**
A retail store needs to synchronize two separate list streams containing inventory records before executing updates.

- Stream 1 contains unique product identification tags (strings).
- Stream 2 contains the respective current stock quantities (integers).

The streams are intended to be mapped 1-to-1 by index position. However, due to systemic transmission lag, the two lists might arrive with mismatching lengths.

Your task is to combine these streams using efficient data structures. You must create an aggregated dictionary matching each tag to its stock quantity.

Rules:

1. If the lists are uneven, processing **must stop** as soon as the shorter stream is exhausted (any trailing elements in the longer stream must be dropped).
2. If duplicate product tags appear consecutively within the valid window of Stream 1, update the dictionary so it only stores the **maximum** stock quantity encountered for that tag.

**Input Format:**

- The first line contains space-separated string tags representing Stream 1.
- The second line contains space-separated integers representing Stream 2.

**Output Format:**

- Print the resulting dictionary sorted alphabetically by its keys.

**Sample Input:**

```
prod_A prod_B prod_A prod_C prod_D
10 45 35 12
```

**Sample Output:**

```
{'prod_A': 35, 'prod_B': 45, 'prod_C': 12}
```

**Notes:**

- Only elements up to the length of the shorter stream should be processed.
- Duplicate tags only matter when they occur inside the processed window; use the maximum quantity seen for that tag.
- The output should be a Python-style dictionary with keys sorted alphabetically.
