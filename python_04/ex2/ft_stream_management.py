import sys
from typing import IO

def get_file_name() -> str:
    sys.stdout.write("Enter new file name (or empty):")
    sys.stdout.flush()
    line:str = sys.stdin.readline()
    return line.rstrip("\r\n")

def save_archive(path: str, final_text:str) -> None:
    file_text: IO[str] | None = None
    print(f"Saving data to '{path}'")
    try: 
        file_text = open(path, "w")
        file_text.write(final_text)
        print(f"Data saved in file '{path}'.")
    except OSError as error:
        print(f"[STDERR] Error openening file :'{path}' {error}:", file=sys.stderr)
        print("Data not saved.")
    finally:
        if file_text is not None:
             file_text.close()
		
def transform_file(original_text: str) -> None:
    lines: list[str] = original_text.splitlines()
    text_transformed : list[str] = [f"{line}#" for line in lines]
    final_text: str = "\n".join(text_transformed) + "\n"

    print("Transform data:")
    print(final_text, end ="")

    file_name: str = get_file_name()
    if not file_name.strip():
        print("Not saving data.")
        return
    save_archive(file_name, final_text)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <file>")
        sys.exit(1)
    path: str = sys.argv[1]

    print("=== Cyber Archives Recovery & Preservation ===")
    print(f"Accessing file: '{path}'")
    file_open : IO[str] | None = None
    content: str = ""
    success: bool = False
    try:
        file_open = open(path, "r")
        content = file_open.read()
        print(content, end ="")
        success = True
    except OSError as erro:
        print(f"[STDERR] Erro opening file '{path}': {erro}", file=sys.stderr)
    finally:
        if file_open is not None:
            file_open.close()
            print(f"File '{path}' closed.")
    if success:
        transform_file(content)
    
    
    

