
def y():
    stri=""
    for row in range(0,7):
        for col in range(0,7):
            if (((col == 1 or col == 5) and row < 2) or row == col and col > 0 and col < 4 or ( \
                    col == 4 and row == 2) or ((col == 3) and row > 3)):
                stri=stri+"*"
            else:
                stri=stri+" "
        stri=stri+"\n"
    print(stri)


def o():
    stri = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 5) and row != 0 and row != 6) or ( \
                    (row == 0 or row == 6) and column > 1 and column < 5)):
                stri = stri + "*"
            else:
                stri = stri + " "
        stri = stri + "\n"
    print(stri)


def u():
    stri = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (((column == 1 or column == 5) and row != 6) or (row == 6 and column > 1 and column < 5)):
                stri = stri + "*"
            else:
                stri = stri + " "
        stri = stri + "\n"
    print(stri)

def s():
    stri = ""
    for Row in range(0, 7):
        for Col in range(0, 7):
            if (((Row == 0 or Row == 3 or Row == 6) and Col > 1 and Col < 5) or (
                    Col == 1 and (Row == 1 or Row == 2 or Row == 6)) or (
                    Col == 5 and (Row == 0 or Row == 4 or Row == 5))):
                stri = stri + "*"
            else:
                stri = stri + " "
        stri = stri + "\n"
    print(stri)


def e():
    stri = ""
    for row in range(0, 7):
        for column in range(0, 7):
            if (column == 1 or ((row == 0 or row == 6) and (column > 1 and column < 6)) or (
                    row == 3 and column > 1 and column < 5)):
                stri = stri + "*"
            else:
                stri = stri + " "
        stri = stri + "\n"
    print(stri)

def f():
    str = ""
    for Row in range(0, 7):
        for Col in range(0, 7):
            if (Col == 1 or (Row == 0 and Col > 1 and Col < 6) or (Row == 3 and Col > 1 and Col < 5)):
                str = str + "*"
            else:
                str = str + " "
        str = str + "\n"
    print(str)


print(y(), o(), u(), s(), s(), e(), f())


