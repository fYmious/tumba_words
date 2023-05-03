import random
count = 0


def TumbaWords(A, w, L):
    global count

    if len(w) == L:

        if not "ОО" in w:
            print(w)

            count += 1

        return

    for c in A:
        TumbaWords(A, w + c, L)


TumbaWords("ЫШЧО", "", 3)

print(count)


def words(alph, length):
    otv = []
    otvet = []
    global count
    while len(otv) < len(alph) ** length:
        b = list(alph * length)
        random.shuffle(b)
        c = ''.join(b)[0:length]
        if not (c in otv):
            otv.append(c)
            count += 1
    for i in otv:
        if not('ОО' in i):
            otvet.append(i)
        else:
            pass

    for i in otvet:
        print(i)

    print(len(otvet))


words('ЫШЧО', 3)
