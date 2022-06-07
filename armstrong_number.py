n = input("Enter the number:") #number
p = len(n)                     #length
x=0                            #range
t=0                            #total
while x < p:
    t += ((int(n[x]))**p)
    x += 1
print(t)