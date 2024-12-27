input="yzbqklnj"

input0="abcdef609043"
inputex="abcdef"
import hashlib
h=hashlib.md5(input0.encode())
print(h.hexdigest())
print(hashlib.md5(input0.encode()).hexdigest())

i=0
cond=True
while cond==True:
    i+=1
    new=input+str(i)
    s=hashlib.md5(new.encode()).hexdigest()
    if s.startswith("000000"):
        print(s)
        cond=False
    else:
        cond=True


print(i)
