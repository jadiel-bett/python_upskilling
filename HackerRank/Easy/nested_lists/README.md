# Nested Lists

## 📝 Problem Description

Given the names and grades for each student in a class of students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.

**Constraints:**

- 2 <= N <= 5
- There will always be one or more students having the second lowest grade.

## 💡 Approach

The solution follows these steps:

1. Collect student names and scores into a nested list `records` and store unique scores in a `set` named `scores`.
2. Convert the set of scores to a list and sort it to identify the second lowest score at index 1.
3. Iterate through the `records` list and collect the names of all students whose score matches the second lowest grade.
4. Sort the resulting list of names alphabetically.
5. Print each name on a new line.

## 🚀 Complexity Analysis

- **Time Complexity**: O(N log N) where N is the number of students, primarily due to sorting the unique scores and the final list of names.
- **Space Complexity**: O(N) to store the records and unique scores.

## 🧪 Test Cases

- **Sample Input**:
  5
  Harry
  37.21
  Berry
  37.21
  Tina
  37.2
  Akriti
  41
  Harsh
  39
- **Expected Output**:
  Berry
  Harry
