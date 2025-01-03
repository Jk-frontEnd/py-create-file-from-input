import os


def main() -> None:
    file_name = input("Enter name of the file: ")
    check_type(file_name)

    with open(file_name + ".txt", "a") as file:
        while True:
            next_line = input("Enter new line of content: ")
            if next_line.lower() == "stop":
                break
            else:
                file.write(next_line + "\n")

    print(f"File name: {file_name}.txt \n")
    print("File content:\n")
    print(f"{read_lines(file_name + '.txt')}")


def check_type(file_name: str) -> None:
    _, extension = os.path.splitext(file_name)
    if extension and extension != ".txt":
        raise ValueError("Error: The file must be a .txt file")


def read_lines(file_name: str) -> str:
    with open(file_name, "r") as file:
        return file.read()


if __name__ == "__main__":
    main()
