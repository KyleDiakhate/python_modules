def garden_operations(operation_number) -> None:
    if operation_number == 0:
        total = int("abc")
    elif operation_number == 1:
        nbr = 10
        count = 0
        average = nbr / count
    elif operation_number == 2:
        f = open("existe.txt")
    elif operation_number == 3:
        len(5)
    else:
        pass

def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")

    i = 0
    while i < 5:
        try:
            garden_operations(i)
            print("Operation completed successfully")     
        except ValueError as e:
            print(f"Caught ValueError: {e}")
        except ZeroDivisionError as e:
            print(f"Caught ZeroDivisionError: {e}")
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except TypeError as e:
            print(f"Caught TypeError: {e}")
        i += 1
test_error_types()

    
    
    
