import re 

def compute_statement(line):
    list = re.findall(r"mul\((\d+),(\d+)\)",line)
    sum = 0
    print(list)
    for i in list:
        sum+=(int(i[0])*int(i[1]))     
    return sum

total = 0
for i in range(6):
    str = input()
    total+=compute_statement(str)
    
print(total)
