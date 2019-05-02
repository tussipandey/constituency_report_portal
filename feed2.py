x=dict()
f=open("rating2.txt")
for g in f:
    c=g.rstrip().split("$")
   # if c=="\n":
    #    break
    #print(c)
    for h in c:
        if h=='':
            continue
        d=h.rstrip().split("|")
        for i in range(len(d)):
            d[i]=int(d[i])
        if d[0] not in x:
            x[d[0]]=d[1:]
        else:
            v=x[d[0]]
            i=(d[1]+v[0])
            j=(d[2]+v[1])
            k=(d[3]+v[2])
            n=d[4]+v[3]
            x[d[0]]=[i,j,k,n]

#print(x) 
n=open("reports2.txt")
for i in n:
    c=i.split("$")
  #  print(c)
    for q in c:
        if q=='':
            continue
        e=q.rstrip().split("|")
 #       print(e)
    #if c[0]=="\n":
     #   break
        if int(e[0]) in x:
            v=x[int(e[0])]
            n=int(v[3])
            u=(int(v[0]))//n
            j=(int(v[1]))//n
            k=(int(v[2]))//n
            x[int(e[0])]=[u,j,k,n]
print("dic is",x)   
open('reports2.txt', 'w').close()
with open("reports2.txt", "a") as myfile:
    for i in x:
        s=x[i]
        u=str(s[0])
        y=str(s[1])
        z=str(s[2])
        p=str(i)+"|"+u+"|"+y+"|"+z+"|"+str(s[3])+"|"+"$"
        myfile.write(p)