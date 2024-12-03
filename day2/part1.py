def is_safe_sequence(seq):   
    # Assume the sequence is increasing or decreasing based on first two elements
    is_increasing = False
    if seq[1] > seq[0]:
        is_increasing = True
    
    # Iterate through the sequence to check if differences are valid
    for i in range(len(seq) - 1):
        diff = seq[i + 1] - seq[i]
        
        if is_increasing:
            if diff not in [1, 2, 3]:
                return False
        else:
            if diff not in [-1, -2, -3]:
                return False
                
    return True

# Main logic
safe_count = 0
for _ in range(1000):  # Loop 1000 times for input
    line = input().split()  # Read and split input
    seq = [int(x) for x in line]  # Convert the sequence elements to integers
    
    if is_safe_sequence(seq):
        safe_count += 1

print(safe_count)
