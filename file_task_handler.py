
def handle_file_task():
    file_path = input("Enter a file path: ")
    task = input("Enter a task: ").strip()

    with open(file_path, 'r') as file:
        lines = file.readlines()

    if task == "sort":
        words = set()
        for line in lines:
            words.update(line.strip().split())
        print(sorted(words))

    elif task == "rev":
        for line in lines:
            print(line.strip()[::-1])

    elif task == "last":
        n = int(input("Enter a number: "))
        for line in lines[-n:]:
            print(line.strip())

    else:
        print("Invalid task name.")

if __name__ == "__main__":
    handle_file_task()
