# Open file content
with open("day4.txt", 'r', encoding='utf-8') as f:
    content = f.readlines()

def count_occurrences_in_lines(input_lines):
    """
    Counts occurrences of the strings 'XMAS' and 'SAMX' across all lines in the input.

    Args:
        input_lines (list of str): List of input lines to search in.

    Returns:
        int: Total count of occurrences of 'XMAS' and 'SAMX' across all lines.
    """
    count = 0
    for line in input_lines:
        count += line.count("XMAS")
        count += line.count("SAMX")
    return count

def vertical_to_horizontal(input_lines):
    """
    Converts vertical columns of characters into horizontal lines.

    Args:
        input_lines (list of str): List of input lines (where each line represents a row).

    Returns:
        list of str: List of horizontal lines constructed from the vertical columns.
    """
    num_columns = len(input_lines[0].strip())  # Assuming all rows have the same length.
    horizontal = ['' for _ in range(num_columns)]

    for line in input_lines:
        for j, char in enumerate(line.strip()):
            horizontal[j] += char

    return horizontal

def diagonal_to_horizontal_top_left(input_lines):
    """
    Converts diagonals starting from the top-left of the matrix into horizontal lines.

    Args:
        input_lines (list of str): List of input lines (matrix).

    Returns:
        list of str: List of horizontal lines formed from the diagonals starting from top-left.
    """
    num_rows = len(input_lines)
    num_columns = len(input_lines[0].strip())
    horizontal = ['' for _ in range(num_rows + num_columns - 1)]  # Diagonal lines

    for i in range(num_rows):
        for j in range(num_columns):
            if input_lines[i][j] != '\n':
                horizontal[i + j] += input_lines[i][j]

    return horizontal

def diagonal_to_horizontal_top_right(input_lines):
    """
    Converts diagonals starting from the top-right of the matrix into horizontal lines.

    Args:
        input_lines (list of str): List of input lines (matrix).

    Returns:
        list of str: List of horizontal lines formed from the diagonals starting from top-right.
    """
    num_rows = len(input_lines)
    num_columns = len(input_lines[0].strip())
    horizontal = ['' for _ in range(num_rows + num_columns - 1)]  # Diagonal lines

    for i in range(num_rows):
        for j in range(num_columns):
            if input_lines[i][j] != '\n':
                horizontal[(num_columns - 1) + (i - j)] += input_lines[i][j]

    return horizontal

# Main computation (combining results from horizontal, vertical, and diagonal searches)
total_count = (
    count_occurrences_in_lines(content) +
    count_occurrences_in_lines(vertical_to_horizontal(content)) +
    count_occurrences_in_lines(diagonal_to_horizontal_top_left(content)) +
    count_occurrences_in_lines(diagonal_to_horizontal_top_right(content))
)

print(total_count)
