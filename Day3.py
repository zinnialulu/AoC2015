with open('day3.txt') as f:
    input=f.read()

pos=[0,0]
house=[[0,0]]
input2="^>v<"
for i in input:
    if i=="^":
        pos[1]+=1
    if i=="v":
        pos[1]-=1
    if i==">":
        pos[0]+=1
    if i=="<":
        pos[0]-=1
    if not (pos in house):
        house.append([pos[0],pos[1]])

nb=len(house)
print(f"visited {nb} houses")

n=len(input)
pos_1=[0,0]
pos_2=[0,0]
house_bis=[[0,0]]
for i in range(0,n,2): ##real santa
    if input[i]=="^":
        pos_1[1]+=1
    if input[i]=="v":
        pos_1[1]-=1
    if input[i]==">":
        pos_1[0]+=1
    if input[i]=="<":
        pos_1[0]-=1
    if not (pos_1 in house_bis):
        house_bis.append([pos_1[0],pos_1[1]])
for j in range(1,n,2): ##robot santa
    if input[j]=="^":
        pos_2[1]+=1
    if input[j]=="v":
        pos_2[1]-=1
    if input[j]==">":
        pos_2[0]+=1
    if input[j]=="<":
        pos_2[0]-=1
    if not (pos_2 in house_bis):
        house_bis.append([pos_2[0],pos_2[1]])

print(f"with help of robot santa, visited house are {len(house_bis)}")