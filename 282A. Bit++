#Problem: 282A. Bit++
#Link: https://codeforces.com/problemset/problem/282/A

n = int(input())

s = 0    
for i in range(n):
    seq = input()
    if len(seq)==3:            
        if (seq.count('+')==2)and(seq.count('-')==0):
            s+=1
        if(seq.count('-')==2)and(seq.count('+')==0):
            s-=1
print(s)
