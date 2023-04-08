my_string = "The quick brown fox jumps over the lazy dog"

l1=my_string.split()
d1={}

for i in l1:
    d1[i]=len(i)

print(d1.values())

for k