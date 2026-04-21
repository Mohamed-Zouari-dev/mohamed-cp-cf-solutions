#Problem : 112A. Petya and Strings
#Link: https://codeforces.com/problemset/problem/112/A

fss = input()
fs = fss.lower()
sss = input()
ss = sss.lower()
r=0
i=0
while i<len(ss):
    if ord(fs[i])>ord(ss[i]) :
        r= 1
        break
    elif ord(fs[i])<ord(ss[i]):
        r= -1
        break
    else:
        i+=1
        continue
print(r)
