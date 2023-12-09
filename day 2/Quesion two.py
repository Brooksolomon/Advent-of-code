
file = open("input.txt",'r')
myd = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
total = 0
digitf = -1
digitl = -1
for s in file:
    f = 0
    lv = 0
    check = False
    for i in range(len(s)):
        if s[i].isdigit():
            if not check:
                f = s[i]
                digitf = i
                check = True
            lv = s[i]
            digitl = i
    demo = [0] * 6
    demoind = [-1] * 6
    temp = 0
    for win in range(3, 6):
        l = 0
        r = win
        check = False
        while r <= len(s):
            if s[l:r] in myd:
                if not check:
                    demo[temp] = myd[s[l:r]]
                    demoind[temp] = l
                    check = True
                demo[temp + 1] = myd[s[l:r]]
                demoind[temp + 1] = l
            l += 1
            r += 1
        temp += 2
    finalx = 0
    fianlxind = float('inf')
    finaly = 0
    finalyind = -1
    for I in range(6):
        if demoind[I] < fianlxind and demoind[I] != -1:
            fianlxind = demoind[I]
            finalx = demo[I]
        if demoind[I] > finalyind:
            finaly = demo[I]
            finalyind = demoind[I]

    if fianlxind > digitf and digitf != -1:
        finalx = f
    if finalyind < digitl:
        finaly = lv

    ans = int(finalx) * 10 + int(finaly)
    total += ans
print(total)
file.close()