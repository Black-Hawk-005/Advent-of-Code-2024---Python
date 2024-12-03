def is_valid_sequence(seq):
    """Checks if a sequence follows the valid difference rules."""
    # Determine if the sequence is increasing or decreasing
    is_increasing = seq[1] > seq[0] if len(seq) > 1 else False
    
    # Check the differences between adjacent elements
    for i in range(len(seq) - 1):
        diff = seq[i + 1] - seq[i]
        if is_increasing:
            if diff not in [1, 2, 3]:
                return False
        else:
            if diff not in [-1, -2, -3]:
                return False
    return True

def is_safe_with_one_removal(seq):
    """Checks if the sequence becomes valid by removing one element."""
    for i in range(len(seq)):
        modified_seq = seq[:i] + seq[i+1:]  # Remove the i-th element
        if is_valid_sequence(modified_seq):  # Check if the modified sequence is valid
            return True
    return False

def is_safe_sequence(seq):
    """Main check for the sequence: if it's valid or becomes valid by removing one element."""
    if is_valid_sequence(seq):
        return True
    return is_safe_with_one_removal(seq)

# Main logic for processing input
safe_count = 0
for _ in range(1000):
    line = input().split()  # Read input and split by space
    seq = [int(x) for x in line]  # Convert each part to an integer
    
    if is_safe_sequence(seq):  # Check if the sequence is safe
        safe_count += 1

print(safe_count)
