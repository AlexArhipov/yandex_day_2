def ex01():
    fail = 0
    data = raw_input().split(' ')
    mi = data[0]
    for i in range(1, len(data)):
        if int(mi) >= int(data[i]):
            fail = 1
        mi = data[i]
    if fail == 1:
        print "NO"
    else:
        print "YES"

def ex02():
    CONSTANT = 0
    ASCENDING = 0
    DESCENDING = 0
    caunt = -1
    ex = -2000000000
    mi = int(raw_input())
    ch = 0
    while mi != ex:
        ch = int(raw_input())
        if (mi < ch) and (ch != ex):
            ASCENDING += 1
        if (mi > ch) and (ch != ex):
            DESCENDING += 1
        if (mi == ch) and (ch != ex):
            CONSTANT += 1
        mi = ch
        caunt += 1
    if caunt == 0:
        print "RANDOM"
    elif caunt == ASCENDING + CONSTANT and ASCENDING != 0 and CONSTANT != 0:
        print "WEAKLY ASCENDING"
    elif caunt == ASCENDING:
        print "ASCENDING"
    elif caunt == DESCENDING:
        print "DESCENDING"
    elif caunt == DESCENDING + CONSTANT and DESCENDING != 0 and CONSTANT != 0:
        print "WEAKLY DESCENDING"
    elif caunt == CONSTANT:
        print "CONSTANT"
    else:
        print "RANDOM"

def ex03():
    caunt = int(raw_input())
    data = raw_input().split(' ')
    find = int(raw_input())
    bliz = abs(int(data[0]) - find)
    j = 0
    for i in range(1, caunt):
        if abs(int(data[i]) - find) < bliz:
            bliz = abs(int(data[i]) - find)
            j = i
    print data[j]

def ex04():
    data = raw_input().split(' ')
    caunt = 0
    for i in range(1, len(data) - 1):
        if (int(data[i - 1]) < int(data[i])) and (int(data[i]) > int(data[i + 1])):
            caunt += 1
    print caunt

def ex05():
    def pos(a, n, jst):
        while (n < jst):
            n += 1
            jst -= 1
            if a[n] != a[jst]:
                return 1
        return 0

    dl = int(raw_input())
    data = raw_input().split(' ')
    a = [0] * dl * 2

    for i in range(dl):
        a[i] = int(data[i])
    jen = 0
    for i in range(dl):
        if a[dl - 1] == a[i]:
            if pos(a, i, dl - 1) == 0:
                jen = i
                break
    print jen
    for i in range(jen):
        print a[jen - i - 1],

def ex06():
    a = raw_input().split(' ')
    dl = len(a)
    m1 = max(int(a[0]), int(a[1]))
    temp1 = m1
    m2 = min(int(a[0]), int(a[1]))
    temp2 = m2
    if a[dl - 1] == '':
        dl -= 1
    for i in range(2, dl):
        if int(a[i]) >= m1:
            temp1 = m1
            m1 = int(a[i])
        elif int(a[i]) > temp1:
            temp1 = int(a[i])
        if int(a[i]) <= m2:
            temp2 = m2
            m2 = int(a[i])
        elif int(a[i]) < temp2:
            temp2 = int(a[i])
    if (m1 > 0 and m2 > 0 and (m1 * temp1 < m1 * m2)) or (m1 < 0 and m2 < 0 and (m2 * temp2 < m1 * m2)) or dl == 2:
        print min(m1, m2), max(m1, m2)
    elif (temp1 * m1) > (temp2 * m2):
        print min(temp1, m1), max(temp1, m1)
    else:
        print min(temp2, m2), max(temp2, m2)

def ex07():
    a = raw_input().split(' ')
    dl = len(a)
    m1 = int(a[0])
    temp1 = - 10 ** 9
    temp11 = - 10 ** 9
    m2 = int(a[0])
    temp2 = 10 ** 9
    temp22 = 10 ** 9
    if a[dl - 1] == '':
        dl -= 1
    for i in range(1, dl):
        if int(a[i]) >= m1:
            temp11 = temp1
            temp1 = m1
            m1 = int(a[i])
        elif int(a[i]) > temp1:
            temp11 = temp1
            temp1 = int(a[i])
        elif int(a[i]) > temp11:
            temp11 = int(a[i])
        if int(a[i]) <= m2:
            temp22 = temp2
            temp2 = m2
            m2 = int(a[i])
        elif int(a[i]) < temp2:
            temp22 = temp2
            temp2 = int(a[i])
        elif int(a[i]) < temp22:
            temp22 = int(a[i])
    if dl == 3:
        for i in range(dl):
            print a[i],
    elif (m1 * m2) > 0 and (temp1 > 0 or temp2 > 0) and (m1 * temp1 * temp11 < m1 * m2 * max(temp1, temp2)) and (
            m2 * temp2 * temp22 < m1 * m2 * max(temp1, temp2)):
        print m1, m2, max(temp1, temp2)
    elif (m1 * m2) < 0 and (temp1 < 0 or temp2 < 0) and (m2 * temp2 * temp22 < m1 * m2 * min(temp1, temp2)) and (
            m1 * temp1 * temp11 < m1 * m2 * min(temp1, temp2)):
        print m1, m2, min(temp1, temp2)
    elif (temp1 * m1 * temp11) > (temp2 * m2 * temp22):
        print temp1, m1, temp11
    else:
        print temp2, m2, temp22