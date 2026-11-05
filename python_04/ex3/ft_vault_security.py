def secure_archive(
    file_name: str, action: str = "read", content: str = ""
) -> tuple[bool, str]:
    try:
        if action == "read":
            with open(file_name, "r") as f:
                result: str = f.read()
            return True, result
        elif action == "write":
            with open(file_name, "w") as f:
                f.write(content)
            return True, "Content successfully written to file"
        else:
            return False, f"Invalid action: {action}"
    except OSError as err:
        return False, str(err)


if __name__ == "__main__":
    print("=== Cyber Archives Security ===")

    print("\nUsing 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", "read"))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", "read"))

    print("\nUsing 'secure_archive' to read from a regular file:")
    print(secure_archive("ancient_fragment.txt", "read"))

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("new_file.txt", "write", "Exemplo de conteudo"))