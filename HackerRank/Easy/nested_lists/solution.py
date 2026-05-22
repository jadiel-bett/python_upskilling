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
