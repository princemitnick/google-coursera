def x_figure(salary):

    tally = 0

    if salary == 0:
        tally += 1

    while salary >=1:
        salary = salary / 10
        print(salary)

        tally += 1
    return tally


print(x_figure(23000400))


def x_figure_2(salary):

    return len(str(salary))

print(x_figure_2(23000320))