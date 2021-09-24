# Enter your code here. Read input from STDIN. Print output to STDOUT
a=int(input())
l1=list(map(int,input().split()))
b=int(input())
l2=list(map(int,input().split()))

s1=set(l1)
s2=set(l2)
s=s1.union(s2)
print(s)
print(len(list(s)))
