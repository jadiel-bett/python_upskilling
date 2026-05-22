if __name__ == '__main__':
    records = []
    scores = set()
    targets = []
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        scores.add(score)
        records.append([name, score])
        
    scorelist = list((scores))
    scorelist.sort()
    secondlowest = scorelist[1]
    
    for record in records:
        if secondlowest in record:
            targets.append(record[0])
            
    targets.sort()
    for target in targets:
        print(target)