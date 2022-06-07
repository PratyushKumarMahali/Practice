nlist = list(range(31))
print(nlist)
elist = []
olist = []
for i in nlist:    
    if (i % 2 == 0):
        elist.append(i)
    else:
        olist.append(i)
print(elist)
print(olist)
slist = elist, olist
print(slist)

alist = ["abc", "xyz", "djk", "jsl", "nsa", "pts", "orc"]
print(alist)
alist.reverse()
print(alist)
rlist =[]
for i in alist:
    rlist.append(i[::-1])
print(rlist)

def list_Counter(l):
    count=0
    for i in l:
        if type(i)== list:
            count+=1
    return count
list1=[1,2,3,[1,2],[3,4],[6,8]]
print(list_Counter(list1))