def input_temperature(temp_str : str) -> int:
    nbr = int(temp_str)
    return nbr


def test_temperature() -> None:
    print("Sucessefull print.")
    try:
        nbr = input_temperature("12")
        print(f"Temperature is now {nbr}ºC")
    except ValueError as v:
        print(f"Caught input_temperature error: {v}")
    print()
    print("Not sucessfull print.")
    try:
        nbr = input_temperature("adc")
        print(f"Temperature is now {nbr}ºC")
    except ValueError as v:
        print(f"Caught input_temperature error: {v}")


test_temperature()