import time

x = 0
while x < 5:
    print("Not there yet, x=" + str(x))
    x = x + 1
print("x=" + str(x))

name = None
while name != "Prince":
    name = input("Enter name : ")
    print(name)


def attempts(n):
    x = 1
    while x <= n:
        print("Attempt : " + str(x))
        x += 1
        time.sleep(1)
    print("Done")


attempts(5)
