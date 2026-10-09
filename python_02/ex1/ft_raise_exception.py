def input_temperature(temp_str : str) -> int:
    nbr = int(temp_str)
    if nbr < 0:
        raise ValueError(f"{nbr} C is too cold for plants (min 0°C)")
    elif nbr > 40:
        raise ValueError(f"{nbr} C is too hot for plants (max 40°C)")
    return nbr


def test_temperature() -> None:
    print("Sucessefull print.")
    try:
        nbr = input_temperature("12")
        print(f"Temperature is now {nbr}ºC")
    except ValueError as v:
        print(f"Caught input_temperature error:{e}")
    print()
    try:
        nbr = input_temperature("-50")
        print(f"Temperature is now {nbr}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error:{e}")
    print()
    try:
        nbr = input_temperature("100")
        print(f"Temperature is now {nbr}ºC")
    except ValueError as e:
        print(f"Caught input_temperature error:{e}")
    print()
    try:
        nbr = input_temperature("adc")
        print(f"Temperature is now {nbr}ºC")
    except ValueError as v:
        print(f"Caught input_temperature error:{e}")

test_temperature()


