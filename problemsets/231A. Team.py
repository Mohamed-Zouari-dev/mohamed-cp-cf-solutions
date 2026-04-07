#Problem: 231A. Team
#Link: https://codeforces.com/problemset/problem/231/A

n=int(input())
s=0
for i in range(n):
    p,v,t = map(int,input().split())
    if p+v+t>=2:
        s+=1

print(s)
