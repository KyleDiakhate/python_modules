import sys
from typing import IO

def transform_file(original_text: str) -> None:
    linhas: list[str] = original_text.splitlines()
    text_transformed : list[str] = [f"{linha}#" for linha in linhas]
    final_text: str = "\n".join(text_transformed) + "\n"

    print("Transform data:")
    print(final_text, end ="")

    file_name: str = input("Enter new file name (or empty):")
    if not file_name.strip():
        print("Not saving data")
        return

    file_text: IO[str] | None = None
    try:
        print(f"Saving data to {file_name}")
        file_text = open(file_name, "w")
        file_text.write(final_text)
    except OSError as erro:
        print(f"Error opening file :{erro}")
    finally:
        if file_text is not None:
            file_text.close()
    
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    path: str = sys.argv[1]

    print("=== Cyber Archives Recovery ===")
    print(f"Accessing file: {path}")
    file_open : IO[str] | None = None
    content: str = ""
    success: bool = False
    try:
        file_open = open(path, "r")
        content = file_open.read()
        print(content, end ="")
        success = True
    except OSError as erro:
        print(f"Erro opening file '{path}': {erro}")
    finally:
        if file_open is not None:
            file_open.close()
            print(f"File '{path}' closed.")
    if success:
        transform_file(content)
    
    
    

