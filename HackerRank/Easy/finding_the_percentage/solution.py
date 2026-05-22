if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        
    query_name = input()
    query_scores = student_marks[query_name]
    totalscore = 0
    
    for score in query_scores:
        totalscore += score
        
    average = totalscore / len(query_scores)
    print(f"{average:.2f}")

# --- Solution Analysis ---
# 1. Time Complexity: O(N * M)
#    - Reading input takes O(N * M), where N is the number of students and M is the number of marks (M=3).
#    - Accessing the dictionary and calculating the average takes O(M).
#
# 2. Space Complexity: O(N * M)
#    - We store marks for all N students in a dictionary.
#
# 3. Critique & Suggestions:
#    - Conciseness: The score summation can be replaced with the built-in sum() function:
#      average = sum(query_scores) / len(query_scores)
#    - Formatting: The f-string "{average:.2f}" correctly handles the requirement of showing 2 decimal places.
#    - Robustness: Added error handling for missing keys would make it more robust for real-world applications.
