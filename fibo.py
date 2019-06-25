def fibo(n):
    mylist=[]
    mylist.append(0)
    mylist.append(1)
    for i in range(2,n):
        mylist.append(mylist[i-1]+mylist[i-2])
    return mylist
