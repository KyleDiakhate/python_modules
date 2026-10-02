def ft_count_harvest_recursive(x=None, day=1):
    if x is None:
        x = int(input("Days until harvest: "))
    if day <= x:
        print(f"Day {day}")
        ft_count_harvest_recursive(x, day + 1)
    else:
        print("Harvest time!")
