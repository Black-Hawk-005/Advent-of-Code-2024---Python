def is_valid_sequence(seq, rules):
    """
    Validate if the sequence follows the specified rules.

    Args:
    - seq (list): A list of page numbers in the sequence.
    - rules (dict): A dictionary containing the rules, where keys are page numbers
                    and values are lists of pages that must appear after the key page.

    Returns:
    - bool: True if the sequence follows all the rules, False otherwise.
    """
    for i in seq:
        if i in rules:  # Check if there are rules for this page
            for j in rules[i]:  # Get the pages that must come after `i`
                if j in seq:  # Both pages must exist in the sequence
                    if seq.index(i) >= seq.index(j):  # `i` must appear before `j`
                        return False
    return True

def validate_invalid(seq, rules):
    """
    Attempt to rearrange a sequence so it follows the rules by swapping pages.

    Args:
    - seq (list): A list of page numbers in the sequence.
    - rules (dict): A dictionary containing the rules for page order.

    Returns:
    - list: The modified sequence that adheres to the rules.
    """
    while not is_valid_sequence(seq, rules):
        for i in seq:
            if i in rules:  # Check if there are rules for this page
                for j in rules[i]:  # Get the pages that must come after `i`
                    if j in seq:  # Both pages must exist in the sequence
                        if seq.index(i) >= seq.index(j):  # `i` must appear before `j`
                            # Swap `i` and `j` to try to fix the order
                            seq[seq.index(i)], seq[seq.index(j)] = seq[seq.index(j)], seq[seq.index(i)]
    return seq

# Initialize variables
rules = []  # Store the rule definitions
sequences = []  # Store the sequences of pages
rule_hash = {}  # Dictionary for rules, with pages as keys
sum_middle = 0  # Accumulate the sum of middle page numbers from valid sequences
valid = []  # List of valid sequences

# Parse rules from file
with open(r"5-rules.txt") as f:
    line = f.readline().strip("\n")
    while line:
        line = line.split("|")
        rules.append(line)  # Add each rule to the rules list
        line = f.readline().strip("\n")

# Parse sequences from file
with open(r"5-sequence.txt") as f:
    line = f.readline().strip("\n")
    while line:
        sequences.append(line.split(","))  # Convert sequence line into a list of pages
        line = f.readline().strip("\n")

# Build the rule dictionary from the rules list
for i in rules:
    if i[0] not in rule_hash:
        rule_hash[i[0]] = []
    rule_hash[i[0]].append(i[1])  # Map each page to its subsequent pages

invalid = []  # List for sequences that don't follow the rules

# Separate valid and invalid sequences
for seq in sequences:
    if is_valid_sequence(seq, rule_hash):
        # valid.append(seq)
        pass  # Ignore valid sequences for now
    else:
        invalid.append(seq)

# Try to rearrange invalid sequences to make them valid
for i in invalid:
    i = validate_invalid(i, rule_hash)
    valid.append(i)  # Add rearranged sequence to valid list

# Calculate the sum of the middle page numbers from valid sequences
for seq in valid:
    middle_index = len(seq) // 2  # Calculation of middle index
    sum_middle += int(seq[middle_index])  # Add middle page number to the sum

# Output the sum of the middle page numbers
print(sum_middle)
