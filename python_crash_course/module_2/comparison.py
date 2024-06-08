print("A" == "a")

print(not "A" == "a")


def is_even(number):
    if number % 2 == 0:
        return True
    return False


print(is_even(4))


def test(number):
    if number > 11:
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)


test(10)


print(10 // 2)