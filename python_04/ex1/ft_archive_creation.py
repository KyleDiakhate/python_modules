import sys
from typing import IO
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    path: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file: {path}")
    file_open : IO[str] | None = None
    try:
        file_open = open(path, "r")
        content : str = file_open.read()
        print(content, end ="")
    except OSError as erro:
        print(f"Erro opening file '{path}': {erro}")
    finally:
        if file_open is not None:
            file_open.close()
            print(f"File '{sys.argv[1]}' closed.")


