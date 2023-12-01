s = 'a'
file = open("input.txt",'r')
total = 0
for s in file:
    f = 0
    lv = 0
    check = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not check:
                f = s[i]
                check = True
            lv = s[i]
    ans = int(f) * 10 + int(lv)
    total += ans
print(total)
file.close()