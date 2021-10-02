t=int(input())
for i in range(t):
    n=int(input())
    count=0
    mac=0
    arr=[]
    for i in range(1,n+1):
        arr.append(i)
    if n==1:
        print(1)
    else:
        for i in range(len(arr)):
            if (arr[i] & arr[i+1])>0:
                count=arr[i] & arr[i+1]
    mac=max(mac,count)
    print(mac)


