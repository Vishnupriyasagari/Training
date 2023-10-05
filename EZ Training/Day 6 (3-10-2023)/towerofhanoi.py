def toh(n,source,aux,dest):
    if n>0:
        toh(n-1,source,dest,aux)
        print(n,"from",source," to ",dest)
        toh(n-1,aux,source,dest)
n=int(input())
toh(n,'source','aux','dest')
