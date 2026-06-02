def ft_count_harvest_recursive():
    days = input("Days until harvest: ")

    def ft_recursion(x):
        if x > 0:
            ft_recursion(x - 1)
            print("Day", x)
    ft_recursion(int(days))
    print("Harvest time!")
