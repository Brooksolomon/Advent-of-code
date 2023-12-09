file = open("input.txt",'r')
myd = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
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