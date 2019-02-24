n=int(input())
arr=list(input().split())
result=[]
for i, j in  zip(arr, arr[::-1]):
    result.append(int(i)+int(j))
for k in range(n-1):
  print(result[k], end=" ")
print(result[n-1], end="")  