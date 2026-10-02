def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    x = seed_type.capitalize()
    if unit == "packets":
        print(f"{x} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{x} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{x} seeds: {quantity} square meters")
    else:
        print("Unknown unit type")
