def Show(func):
    def Your_Name(Name):
        Name = Name.upper()

        for Char in Name:
            if Char == "A":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if ((column == 1 or column == 8) and row != 0) or (
                                (row == 0 or row == 4) and (column > 1 and column < 8)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "B":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if ((column == 1 or column == 8) and (row != 0 and row != 4 and row != 8)) \
                                or ((row == 0 or row == 4 or row == 8) and (column < 8 and column > 0)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "C":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if ((column == 1) and (row != 0 and row != 8) or (column == 8) and (row == 1 or row == 7) \
                                or (row == 0 or row == 8) and (column > 1 and column < 8)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "D":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if ((column == 1 or column == 8) and (row != 0 and row != 8) \
                                or ((row == 0 or row == 8) and (column > 0 and column < 8))):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "E":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if ((column == 1) or (row == 0 or row == 4 or row == 8) and (column > 1)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "F":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if (column == 1 or (row == 0 and column > 1) or (row == 4) and (column > 1 and column < 7)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "G":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if ((column == 1 and row != 0 and row != 8) or (
                                (row == 0 or row == 8) and column > 1 and column < 8) \
                                or (row == 4 and column > 4) or (column == 8 and row == 1) or (
                                        column == 8 and row > 4 and row < 8)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "H":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if (column == 1 or column == 8 or (row == 4 and column > 1)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "I":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if (column == 4 and row > 1 or (row == 1 or row == 8)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "J":
                for row in range(0, 9):
                    for column in range(0, 9):
                        if (row == 0 or (column == 4 and row < 8) \
                                or (row == 8 and column == 3) or (row == 7 and column == 1)):
                            print(end="*")
                        else:
                            print(end=" ")
                    print()
                print()


            elif Char == "K":
                i = 0
                j = 8
                for row in range(0, 9):
                    for column in range(0, 9):
                        if (column == 1 or (row == column) and row >= 4):
                            print(end="*")
                        elif row == i and column == j:
                            print(end="*")
                            i = i + 1
                            j = j - 1
                        else:
                            print(end=" ")
                    print()
                print()




        func(Name)
    return Your_Name

@Show
def vahid(Name):
    return Name

vahid(input("Please enter your name: "))
