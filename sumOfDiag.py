a=[[1,2,3,4],
[4,5,6,4],
[7,8,9,4],
[4,4,4,4]]
sum=0
add=0
m=len(a)
n=len(a[0])
if m==n:
    for i in range(0,len(a[0])):
        for j in range(0,len(a[3])):
            if i==j:
                sum=sum+a[i][j]
                
            if i+j==m-1:
                add=add+a[i][j]
    print(sum,add)            
    total=sum+add
    print(total)
else:
    print(0)
