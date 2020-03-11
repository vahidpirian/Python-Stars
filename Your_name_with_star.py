def Show(func):
    def Your_Name(Name):
        Name = Name.upper()

        func(Name)
    return Your_Name

@Show
def vahid(Name):
    return Name

vahid(input("Please enter your name: "))
