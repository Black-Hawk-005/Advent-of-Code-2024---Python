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


# Initialize variables
rules = []  # To store the rule definitions from the file
sequences = []  # To store the sequences of pages
rule_hash = {}  # Dictionary to store rules with the page as the key
sum_middle = 0  # Sum of the middle page numbers of valid sequences
valid = []  # To store sequences that follow the rules

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
    rule_hash[i[0]].append(i[1])  # Add each page's subsequent pages to the rule dictionary

# Validate sequences and add valid sequences to the list
for seq in sequences:
    if is_valid_sequence(seq, rule_hash):
        valid.append(seq)  # Add sequence to valid if it follows the rules

# Calculate the sum of the middle page numbers from valid sequences
for seq in valid:
    middle_index = len(seq) // 2  # Calculation of middle index
    sum_middle += int(seq[middle_index])  # Add middle page to the sum

# Print the sum of the middle page numbers
print(sum_middle)
