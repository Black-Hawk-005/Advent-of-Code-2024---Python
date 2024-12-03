import re

def compute_statement(line):
    commands = re.findall(r"mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", line)
    
    total_sum = 0  
    mul_enabled = True  
    print(commands)
    for command in commands:
        if command[2] == 'do':  
            mul_enabled = True
        elif command[3] == "don't":  
            mul_enabled = False
        elif command[3] == "" and command[2] == "" and mul_enabled:  
            num1 = int(command[0])
            num2 = int(command[1])
            total_sum += num1 * num2

    return total_sum

total = 0
n = int(input("Enter the number of lines: "))  
l= ""
for i in range(n):
    line = input() 
    l+=line
print(compute_statement(l))
