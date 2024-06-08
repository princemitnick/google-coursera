def table(facteur):
    for number in range(1, 10 + 1):
        print(str(facteur) + " x " + str(number) + " = " + str(facteur * number))


table(5)

def matrix(initial_number, end_number):
    for column in range (initial_number, end_number):
        for row in range(initial_number, end_number):
            print(column * row, end=" ")
        print()


matrix(1, 5)
