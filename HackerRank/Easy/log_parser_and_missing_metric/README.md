# Log Parser and Missing Metrics

## Challenge 1: Log Parser and Missing Metrics

**Difficulty:** Easy to Intermediate

**Problem Description:**

You are given a stream of log strings from a server network. Each log entry is formatted as a single string containing a timestamp, an alphanumeric event type, and a numeric metric score, separated by single spaces: `"  "`.

Your task is to process these logs to find the average metric score for _only_ a specific target event type. However, some entries might contain corrupt, non-numeric metric values (e.g., `"NaN"` or letters instead of digits). Your program must gracefully handle or ignore these corrupt values without crashing.

**Input Format:**

- The first line contains an integer $N$, representing the number of log lines.
- The next $N$ lines each contain a log entry string.
- The final line contains a string representing the target `event_type` to filter by.

**Output Format:**

- Print a single floating-point value representing the average score of valid metrics matching the target event type, rounded precisely to **2 decimal places**.
- If the target event type does not exist or has no valid numeric metrics, print `0.00`.
