def magic_square(n):
    
    magicSquare=[]
    for i in range(n):
        l=[]
        for j in range(n):
            l.append(0)
        magicSquare.append(l)    
    i=n//2
    j=n-1
    num=n*n
    count=1
    while(count<=num):
        if(i==-1 and j==n):  #condition 4
            j=n-2
            i=0        
        else:
            if(j==n):  #column value is exceeding
                j=0
            if(i<0):  #row is becoming -1
                 i=n-1             
        if(magicSquare[i][j]!=0):
            j=j-2
            i=i+1
            continue   
        else:
            magicSquare[i][j]=count
            count+=1
        i=i-1
        j=j+1   #condition 1
    for i in range(n):
          for j in range(n):
                print(magicSquare[i][j], end=" ")
          print()
    print("The Sum of each Row/Column/Diagonal is: "+str(n*(n**2+1)/2))  

magic_square(5)          