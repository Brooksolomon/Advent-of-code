myarr = []
f = open("input.txt",'r')
md = {}
sym = []
count = 0
for i in f:
    i =i.rstrip('\n')
    print(i)
    n = len(i)
    j = 0
    while j  < n :
        if i[j].isdigit():
            start = j
            num = ""
            while j < n  and i[j].isdigit():
                num+=i[j]
                j+=1
            end = j-1
            j-=1
            md[num+','+str(count)+str(start)+str(end)] = [count , start,end]
        elif i[j]=='*':
            sym.append([count,j])

        j+=1
    count+=1


print(md)
print(sym)
print(count)
total = 0
alreadyfound = []
for i in sym:
    row, col = map(int,i)
    found = []

    for j in md:
        x,y,z = map(int,md[j])
        if md[j] in alreadyfound:
            continue
        if row-1 == x and (col-1>=y and col-1<=z):
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
        elif row-1==x and col>=y and col <=z:
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
            
        elif row-1 ==x and col+1>=y and col+1 <=z:
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
            
        elif row == x and (col-1>=y and col-1<=z):
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
            
        elif row == x and col+1>=y and col+1 <=z:
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
            
        elif row+1==x and (col-1>=y and col-1<=z):
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
            
        elif row+1 == x and col>=y and col <=z:
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
            
        elif row+1==x and col+1>=y and col+1 <=z:
            # print(j)
            alreadyfound.append(md[j])
            found.append(int(j.split(',')[0]))
            
    if len(found) ==2:
        total += found[0] * found[1]

print(total)


