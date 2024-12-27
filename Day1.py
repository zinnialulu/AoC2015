with open('day1.txt') as f:
    input=f.read()
up=input.count("(")
down=input.count(")")
part1=up-down
print(f"part 1 answer is {part1}")

l=len(input)
i=0
floor=0
while floor>=0 and i <=l:
    if input[i]=="(":
        floor+=1
    else:
        floor-=1
    i+=1
    print(f"character number: {i}, instruction is {input[i]} and floor at {floor}")
print(f"the character is {i}")