# a=int(input("enter the number:"))
# s=[]
# i=len(str(a))
# for n in (str(a)):
#     if n!="0":
#         s.append(n*i)
#         s.append("+")
#     i-=1
# print(s)
# i=0
# n=str(a)
# while i<len(n):
#     if n!="0":
#         v=n*n[i]
#         s.append(v)
#     i+=1
# print(s)

a=[34,56,21,87,13,23,19]
i=0
sum=0
# v=str(a[i])
b=[]
while i<len(a):

    
    j=0
    while j<len(a):
        sum+=a[i]+a[j]
        b.append(sum)
    i=i+1
print(b)
