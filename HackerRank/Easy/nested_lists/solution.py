if __name__ == '__main__':
    # Use a list to maintain the order of input and a set to track unique scores
    records = []
    scores = set()
    targets = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score) # Set ensures only unique grades are stored
        records.append([name, score])
        
    # Convert unique scores to a sorted list to easily find the second lowest value
    scorelist = list((scores))
    scorelist.sort()
    secondlowest = scorelist[1] # Index 1 represents the second smallest unique grade
    
    # Filter names of all students who have the second lowest grade
    for record in records:
        if secondlowest in record:
            targets.append(record[0])
            
    # Requirement: Order names alphabetically if multiple students have the same grade
    targets.sort()
    for target in targets:
        print(target)

# --- Solution Analysis ---
# 1. Time Complexity: O(N log N). 
#    - Sorting the unique scores takes O(U log U), where U is the number of unique scores (U <= N).
#    - Filtering students takes O(N).
#    - Sorting the final list of names takes O(K log K), where K is the number of students with the second lowest grade.
#    - Overall, the complexity is dominated by sorting, making it efficient for the given constraints.
#
# 2. Space Complexity: O(N).
#    - We store all students in the 'records' list and unique scores in a set, both taking linear space.
#
# 3. Critique & Suggestions:
#    - Correctness: The use of a 'set' is a great way to handle duplicate scores, ensuring the 'second lowest' is actually the second unique value.
#    - Conciseness: The filtering loop could be replaced with a list comprehension:
#      targets = sorted([record[0] for record in records if record[1] == secondlowest])
#    - Robustness: The code assumes index [1] always exists in scorelist. While the problem constraints guarantee a second lowest grade, in a real-world scenario, adding a check for len(scorelist) > 1 would be safer.
#    - Naming: 'targets' is a bit generic; 'second_lowest_students' would be more descriptive.
