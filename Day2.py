with open('day2.txt') as f:
    input=f.readlines()
s_tot=0
r_tot=0
for gift in input:
    a,b,c=gift.split('x')
    s1=2*(int(a)*int(b)+int(b)*int(c)+int(a)*int(c))
    s2=min(int(a)*int(b),int(b)*int(c),int(a)*int(c))
    s_tot+=s1+s2
    ribbon=2*(int(a)+int(b)+int(c)-max(int(a),int(b),int(c)))
    bow=int(a)*int(b)*int(c)
    r_tot+=(ribbon+bow)
print(f"total surface is {s_tot}")
print(f"total ribbon is {r_tot}")