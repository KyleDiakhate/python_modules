import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    print(f"Program Name: {sys.argv[0]}")

    len_list = len(sys.argv) - 1
    i = 1

    if len_list == 0:
        print("No Arguments Provide")
    else:
        print(f"Arguments received: {len_list}")
        while i <= len_list:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print (f"Total arguments: {len(sys.argv)}")
