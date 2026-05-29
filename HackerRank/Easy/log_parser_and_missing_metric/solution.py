import sys
import math
import re

# regex matches numeric literals (integers, decimals, optional exponent), rejects NaN/inf
NUM_RE = re.compile(r'^[+-]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][+-]?\d+)?$')

def get_event_average(logs, target_event):
    # Write your code here
    if not logs:
        return 0.00
    if not target_event:
        return 0.00
        
    scores = []
    
    for log in logs:
        if target_event in log:
            log_parts = log.split()
            if not log_parts:
                continue
            token = log_parts[-1]
            if not NUM_RE.match(token):
                continue
            score = float(token)
            if math.isnan(score):
                continue
            scores.append(score)
            
    if not scores:
        return 0.00
        
    return sum(scores) / len(scores)
            
    

if __name__ == '__main__':
    lines = sys.stdin.read().splitlines()
    if lines:
        n = int(lines[0])
        log_entries = lines[1:n+1]
        target = lines[n+1]
        
        result = get_event_average(log_entries, target)
        print(f"{result:.2f}")

# --- Solution Analysis ---
# 1. Time Complexity: O(N * L)
#    - N is the number of log entries, L is the average length of a log string.
#    - We iterate through each log entry once and perform string operations.
#
# 2. Space Complexity: O(N)
#    - In the worst case, we store all log entries in memory and keep a list of scores.
#
# 3. Critique & Suggestions:
#    - Robustness: Added a check for 'if not scores' to prevent ZeroDivisionError.
#    - Flexibility: Changed int() to float() to handle decimal metrics if they appear.
#    - Filtering: 'target_event in log' is simple but could be improved to check exact field matching if logs were more complex.