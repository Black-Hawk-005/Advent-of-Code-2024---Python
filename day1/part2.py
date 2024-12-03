def similar(l, number):
    count = 0
    for i in l:
        if i == number:
            count += 1
    return count

# Read input and populate l1 and l2
l1 = []
l2 = []

for _ in range(1000):
    line = input().split()  # Handle multiple spaces correctly
    l1.append(int(line[0]))
    l2.append(int(line[1]))

# Calculate the score
score = 0
for i in l1:
    score += i * similar(l2, i)

print(score)
