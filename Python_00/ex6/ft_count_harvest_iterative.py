def ft_count_harvest_iterative():
    days = input("Days until harvest: ")
    r = range(1, int(days) + 1)
    for i in r:
        print("Day ", i)
    print("Harvest time!")
