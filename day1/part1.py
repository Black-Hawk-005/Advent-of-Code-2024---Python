def find_min(l):
    # Returns the minimum value in the list (without using the built-in min)
    return min(l)

l1 = []
l2 = []

# Read input and store values in l1 and l2
for i in range(1000):
    line = input().split()
    l1.append(int(line[0]))
    l2.append(int(line[1]))

# Sort both lists for efficient access to the minimum values
l1.sort()
l2.sort()

total_sum = 0

# Iterate over the lists and calculate the sum of differences
while l1 and l2:  # While both lists are not empty
    m1 = l1.pop(0)  # Get the smallest value from l1
    m2 = l2.pop(0)  # Get the smallest value from l2
    
    # Add the absolute difference to total_sum
    total_sum += abs(m1 - m2)

print(total_sum)
