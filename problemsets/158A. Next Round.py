#Problem: 158A. Next Round
#Link: https://codeforces.com/problemset/problem/158/A
n,k = map(int,input().split())

l=list(map(int,input().split()))
r=l[k-1]
s=0
for x in l:
    if x>0 and x>=r:
        s+=1
print(s)

