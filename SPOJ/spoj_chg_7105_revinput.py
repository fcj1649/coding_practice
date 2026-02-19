i = int(input())
o = []
s = open(0).read().strip("\\n").split(" ")
for k in s:
    for j in range(i):
        o += [k[::-1]]
        o += [" "]
for k in reversed(o):
    print(k)