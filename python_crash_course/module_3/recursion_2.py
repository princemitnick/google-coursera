def test():
    name = input("Enter your fullname : ")
    if name != "Prince":
        print("Should be Prince")
        return 1
    test()
    print("It's a good one")


test()