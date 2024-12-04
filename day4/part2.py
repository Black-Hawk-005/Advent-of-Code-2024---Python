# Read content from the file
with open("day4.txt", 'r') as f:
    content = f.readlines()

def count_XMAS_patterns(input_grid):
    """
    Counts the occurrences of different "XMAS" patterns in a grid of characters.
    The grid is searched for the following patterns:
    - 'M' at (i, j), 'M' at (i+2, j), 'S' at (i, j+2), 'S' at (i+2, j+2)
    - 'S' at (i, j), 'S' at (i+2, j), 'M' at (i, j+2), 'M' at (i+2, j+2)
    - 'M' at (i, j), 'S' at (i+2, j), 'M' at (i, j+2), 'S' at (i+2, j+2)
    - 'S' at (i, j), 'M' at (i+2, j), 'S' at (i, j+2), 'M' at (i+2, j+2)

    Args:
        input_grid (list of str): A list of strings representing rows of the grid.

    Returns:
        int: The total count of matching patterns.
    """
    count = 0
    num_rows = len(input_grid)
    num_cols = len(input_grid[0])

    # Define the pattern offsets for each possible "XMAS" variant
    patterns = [
        [(0, 0), (2, 0), (0, 2), (2, 2)],  # M M S S
        [(0, 0), (2, 0), (0, 2), (2, 2)],  # S S M M
        [(0, 0), (2, 0), (0, 2), (2, 2)],  # M S M S
        [(0, 0), (2, 0), (0, 2), (2, 2)],  # S M S M
    ]

    # Traverse the grid and check each pattern
    for i in range(num_rows - 2):
        for j in range(num_cols - 2):
            # Check all patterns
            for pattern in patterns:
                # For each pattern, check the characters at the respective offsets
                chars = [input_grid[i + dx][j + dy] for dx, dy in pattern]
                
                # Check if the pattern matches the required 'M' and 'S'
                if sorted(chars) == ['M', 'M', 'S', 'S']:
                    count += 1

    return count

# Call the function and print the result
print(count_XMAS_patterns(content))
