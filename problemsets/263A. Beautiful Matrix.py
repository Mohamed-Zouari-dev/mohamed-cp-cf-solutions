#Problem: Beautiful Matrix
#Link: https://codeforces.com/problemset/problem/263/A

l=[]
for i in range(5):
    a = list(map(int,input().split()))
    l.append(a)
    if (1 in a):
        x=i
        j=a.index(1)
s=abs(x-2)+abs(j-2)
print(s)
